import functions as FUNCTIONS
import motorbike as MOTORBIKE
import json

def drawMainMenu() -> None:
  """
  This function draws the main menu.
  """
  display = """
  -------------------
  |       Menü      |
  -------------------
  1) Túra bevitel
  2) Helyek
  3) Motorok
  0) Kilépés"""
  print(display)

  choice = int(input(">_ "))
  if choice == 1:
      AddTour()
  elif choice == 2:
      drawPlacesMenu()
  elif choice == 3:
      drawBikesMenu()
  elif choice == 0:
      exit()
  else: 
      print("Nem megfelelőt írtál be. Próbáld újra.")
      drawMainMenu()

def drawPlacesMenu() -> None:
  """
  This function draws the places menu.
  """
  display = """
  -------------------
  |      Helyek     |
  -------------------
  1) Bejárt helyek
  2) Eddig még be nem járt helyek"
  0) Vissza"""
  print(display)

  choice = int(input(">_ "))
  if choice == 1:
    KnownPlaces()
  elif choice == 2:
    UnknownPlaces()
  elif choice == 0:
    drawMainMenu()
  else: 
    print("Nem megfelelőt írtál be. Próbáld újra.") 
    drawPlacesMenu()

def drawBikesMenu() -> None:
  """
  This function draws the motorbikes menu.
  """
  display = """
  -------------------
  |      Motorok    |
  -------------------
  1) Motorok megtekintése
  2) Új motor hozzáadása
  3) Motor törlése
  0) Vissza"""
  print(display)

  choice = int(input(">_ "))
  if choice == 1:
    ShowBikes()
  elif choice == 2:
    NewBike()
  elif choice == 3:
    DeleteBike()
  elif choice == 0:
    drawMainMenu()
  else: 
    print("Nem megfelelőt írtál be. Próbáld újra.") 
    drawBikesMenu()

def AddTour() -> None:
    """
    In this function is the logic of option 1 in main menu. 
    Here you can add new tour, which will be stored in "tours.txt".
    """
    date = FUNCTIONS.getDate()
    places = FUNCTIONS.ReadPlaces()
    data = FUNCTIONS.ReadData()

    print("- Túra bevitel - ")
    if not data:
      print("- Motor felvétele -")
      MOTORBIKE.addNewBike()
    else:
      count = MOTORBIKE.LenOfBikes()
      choice = MOTORBIKE.ChooseBike()
      if count > choice-1:
        bike = data["bikes"][choice-1]
      else: 
        print("Nem megfelelőt írtál be. Próbáld újra.")
        print("\n")
        drawMainMenu()

    start_place = str(input("Elindulási hely: "))
    if FUNCTIONS.IsInSettlements(start_place) == True:
      distances, new_places = FUNCTIONS.Tour(start_place)
    else: 
      print("Nincs ilyen település a listában.")
      drawMainMenu()

    fuel_status = int(bike["fuel"]) - int(MOTORBIKE.consumptionCalc(FUNCTIONS.Traveled_Distance(distances),int(bike["consumption"])))
    tier_status = MOTORBIKE.tireWearCalc(FUNCTIONS.Traveled_Distance(distances))
    distance_status = int(int(bike["distance"]) + FUNCTIONS.Traveled_Distance(distances))

    for p in data['bikes']:
      if p["model"] == bike["model"]:
        p["distance"] = distance_status
        p["fuel"] = fuel_status
        p["tire"] = (int(bike["tire"])+int(FUNCTIONS.Traveled_Distance(distances)))
    with open('data.json', 'w') as outfile:
      json.dump(data, outfile)

    file = open("tours.txt","a",encoding="utf-8")
    file.write('{:.2f}'.format(FUNCTIONS.Traveled_Distance(distances))+" km tettél meg a ("+date+") túrán, ezzel a motorral: "+bike["model"] +" "+bike["year"] +" | Gumik állapota: "+'{:.2f}'.format(tier_status)+" % | Üzemanyag: "+str(fuel_status)+" liter | Kilóméter: "+str(distance_status)+" km"+"\n")
    file.close()
    print('{:.2f}'.format(FUNCTIONS.Traveled_Distance(distances))+" km tettél meg a ("+date+") túrán, ezzel a motorral: "+bike["model"] +" "+bike["year"] +" | Gumik állapota: "+'{:.2f}'.format(tier_status)+" % | Üzemanyag: "+str(fuel_status)+" liter | Kilóméter: "+str(distance_status)+" km")
    
    if len(new_places) > 0:
      file = open("places.txt","a",encoding="utf8")
      print("Új helyek: ",end="")
      for place in new_places:
        file.write(place+"\n")
        print(place,end=" ")
      file.close()
    else: print("Új helyek: nincs")

    drawMainMenu()

def KnownPlaces() -> None:
    """
    This is the logic of submenu of option 2 in main menu. Option 1.
    Here you can see what places are where u were already.
    """
    know_places = []
    file = open("places.txt","r",encoding="utf-8")
    know_places.append(file.read())
    file.close()
    print("Eddig az alábbi helyeken jártál: ")
    for i in know_places:
        print(i)
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": 
        drawPlacesMenu()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál be. Próbáld újra.")
        drawMainMenu()

def UnknownPlaces() -> None:
    """
    This is the logic of submenu of option 2 in main menu. Option 2.
    Here you can see the placese where you weren't.
    """
    known_places = []
    unknown_places = []
    file = open("places.txt","r",encoding="utf-8")
    known_places= file.read()
    file.close()
    data = FUNCTIONS.ReadData()
    for p in data['settlements']:
      if p["name"] not in known_places:
        unknown_places.append(p["name"])
    print("Az alábbi helyeken még nem jártál ("+str(len(unknown_places))+")): ")
    for i in unknown_places:
        print(i,end=", ")
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": drawPlacesMenu()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál be. Próbáld újra.")
        drawMainMenu()
        
def ShowBikes() -> None:
  """
  This is the logic of submenu of option 3 in main menu. Option 1. 
  This will be show the motorbikes which are stored in the "data.json".
  """
  data = FUNCTIONS.ReadData()
  for p in data['bikes']:
    print("Típus: " + p['model'])
    print("Évjárat: " + p['year'])
    print("Km óra: " + str(p['distance']))
    print("Üzemanyag szint: " + str(p['fuel'])+' liter')
    print("Gumi: " + str(p['tire'])+' km')
    print("Fogyasztás (l/100km): " + str(p['consumption']))
    print('')
    
  print("Vissza vagy kilépés? (V/K): ")
  choice = str(input(">_ "))
  if choice == "V": drawBikesMenu()
  elif choice == "K": quit()
  else: 
        print("Nem megfelelőt írtál be. Próbáld újra.")
        drawMainMenu()

def NewBike() -> None:
    """
    This is the logic of submenu of option 3 in main menu. Option 2. 
    Here you can add new motorbike.
    """
    MOTORBIKE.addNewBike()
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": drawBikesMenu()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál be. Próbáld újra.")
        drawMainMenu()

def DeleteBike() -> None:
    """
    This is the logic of submenu of option 3 in main menu. Option 3. 
    Here you can delete motorbike from "data.json" and it will be not stored anymore.
    """
    data = FUNCTIONS.ReadData()
    new_data = {}
    new_data['bikes'] = []
    count = 0
    for p in data['bikes']:
      print(str(count+1)+") " + "Típus: " + str(p['model'])+"| "+"Évjárat: " + str(p['year'])+"| "+"Km óra: " + str(p['distance']))
      print('')
      count += 1
    print("Melyik motort szeretnéd törölni? ")
    choice = int(input(">_ "))
    if choice > count: 
        print("Nem megfelelőt választottál. Próbáld újra.")
        drawBikesMenu()
    else:
      choosed_model = data['bikes'][count-1]["model"]
      for p in data['bikes']:
        if p['model'] == choosed_model:
          continue
        else:
          new_data['bikes'].append({
          'model': p['model'],
          'year': p['year'],
          'distance': p['distance'],
          'fuel': p['fuel'],
          'tire': p['tire'],
          'consumption': p['consumption']
          })

    with open('data.json', 'w') as outfile:
      json.dump(new_data, outfile)
    
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": drawBikesMenu()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál be. Próbáld újra.")
        drawMainMenu()

def main() -> None:
    """
    This function contains all the previous functions in a logically correct order for the program to work.
    """
    drawMainMenu()


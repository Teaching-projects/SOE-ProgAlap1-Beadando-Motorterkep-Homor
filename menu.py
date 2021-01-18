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
      print("Nem megfelelő karaktert írtál.")
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
    print("Nem megfelelő karaktert írtál") 
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
    print("Nem megfelelő karaktert írtál") 
    drawBikesMenu()

def AddTour() -> None:
    """
    In this function is the logic of option 1 in main menu. 
    Here you can add new tour, which will be stored in "tours.txt".
    """
    distances = []
    new_places = []
    date = FUNCTIONS.getDate()

    file = open("places.txt","r",encoding='utf-8')
    places = file.read()
    file.close()

    data = MOTORBIKE.ReadBikes()
    print("- Túra bevitel - ")

    if not data:
      print("- Motor felvétele -")
      MOTORBIKE.addNewBike()
    else:
      count = 0
      print("- Motor kiválasztása -")
      for p in data['bikes']:
        print(str(count+1)+") " + "Típus: " + str(p['model'])+"| "+"Évjárat: " + str(p['year'])+"| "+"Km óra: " + str(p['distance']))
        print('')
        count += 1
      choice = int(input(">_ "))
      if count > choice-1:
        model = data['bikes'][choice-1]["model"]
        year = data['bikes'][choice-1]["year"]
        distance = int(data['bikes'][choice-1]["distance"])
        fuel = int(data['bikes'][choice-1]["fuel"])
        tire = data['bikes'][choice-1]["tire"]
        consumption = int(data['bikes'][choice-1]["consumption"])
      else: 
        print("Nem megfelelőt írtál be.")
        print("\n")
        AddTour()

    start_place = str(input("Elindulási hely: "))
    if FUNCTIONS.IsInSettlements(start_place) == True:
      if start_place not in places: new_places.append(start_place)
      while True:
        next_place = str(input("Következő helyszín (irj 'nincs'-et ha be akarod fejezni): "))
        if next_place == "nincs": break
        else:
          if FUNCTIONS.IsInSettlements(next_place) == True:
            if next_place not in places: new_places.append(next_place)
            start_location = FUNCTIONS.getCordinate(start_place).split(" ")
            next_location = FUNCTIONS.getCordinate(next_place).split(" ")
            distances.append(FUNCTIONS.getDistance(float(start_location[0]),float(start_location[1]),float(next_location[0]),float(next_location[1])))
            start_place = next_place
          else: print("Nincs ilyen település a listában.")
    else: 
      print("Nincs ilyen település a listában.")
      drawMainMenu()

    fuel_status = fuel - int(MOTORBIKE.consumptionCalc(FUNCTIONS.Traveled_Distance(distances),consumption))
    tier_status = MOTORBIKE.tireWearCalc(FUNCTIONS.Traveled_Distance(distances))
    distance_status = int(distance + FUNCTIONS.Traveled_Distance(distances))

    new_data = {}
    new_data['bikes'] = []
    for p in data['bikes']:
      if p["model"] == model:
        new_data['bikes'].append({
        'model': model,
        'year': year,
        'distance': distance_status,
        'fuel': fuel_status,
        'tire': (int(tire)+int(FUNCTIONS.Traveled_Distance(distances))),
        'consumption': consumption
        })
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

    file = open("tours.txt","a",encoding="utf-8")
    file.write('{:.2f}'.format(FUNCTIONS.Traveled_Distance(distances))+" km tettél meg a ("+date+") túrán, ezzel a motorral: "+model +" "+year +" | Gumik állapota: "+'{:.2f}'.format(tier_status)+" % | Üzemanyag: "+str(fuel_status)+" liter | Kilóméter: "+str(distance_status)+" km"+"\n")
    file.close()
    
    print('{:.2f}'.format(FUNCTIONS.Traveled_Distance(distances))+" km tettél meg a ("+date+") túrán, ezzel a motorral: "+model +" "+year +" | Gumik állapota: "+'{:.2f}'.format(tier_status)+" % | Üzemanyag: "+str(fuel_status)+" liter | Kilóméter: "+str(distance_status)+" km")
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
        print("Nem megfelelőt írtál.")
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
    FUNCTIONS.loadSettlements()
    for i in range(len(FUNCTIONS.settlements)):
        if FUNCTIONS.settlements[i][0] not in known_places:
            unknown_places.append(FUNCTIONS.settlements[i][0])
    print("Az alábbi helyeken még nem jártál ("+str(len(unknown_places))+")): ")
    for i in unknown_places:
        print(i,end=", ")
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": drawPlacesMenu()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál.")
        drawMainMenu()
        
def ShowBikes() -> None:
  """
  This is the logic of submenu of option 3 in main menu. Option 1. 
  This will be show the motorbikes which are stored in the "data.json".
  """
  data = MOTORBIKE.ReadBikes()
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
        print("Nem megfelelőt írtál.")
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
        print("Nem megfelelőt írtál.")
        drawMainMenu()

def DeleteBike() -> None:
    """
    This is the logic of submenu of option 3 in main menu. Option 3. 
    Here you can delete motorbike from "data.json" and it will be not stored anymore.
    """
    data = MOTORBIKE.ReadBikes()
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
        print("Nem megfelelőt választottál.")
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
        print("Nem megfelelőt írtál.")
        drawMainMenu()

def main() -> None:
    """
    This function contains all the previous functions in a logically correct order for the program to work.
    """
    FUNCTIONS.loadSettlements()
    drawMainMenu()


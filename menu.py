import functions as FUNCTIONS

def drawMainMenu() -> None:
  """
  This function draws the main menu.
  """
  print("-------------------")
  print("|       Menü      |")
  print("-------------------")
  print("1) Túra bevitel")
  print("2) Helyek")
  print("3) Motorok")
  print("0) Kilépés")

def drawPlacesMenu() -> None:
  """
  This function draws the places menu.
  """
  print("-------------------")
  print("|      Helyek     |")
  print("-------------------")
  print("1) Bejárt helyek")
  print("2) Eddig még be nem járt helyek")
  print("0) Vissza")

def drawBikesMenu() -> None:
  """
  This function draws the motorbikes menu.
  """
  print("-------------------")
  print("|      Motorok    |")
  print("-------------------")
  print("1) Motorok megtekintése")
  print("2) Új motor hozzáadása")
  print("3) Motor törlése")
  print("0) Vissza")

def MainMenuOptions() -> None:
  """
  This will be draw the main menu, and u can here choose from the options.
  """
  print("\n")
  drawMainMenu()
  choice = int(input(">_ "))
  if choice == 1:
      MMOption_1()
  elif choice == 2:
      MMOption_2()
  elif choice == 3:
      MMOption_3()
  elif choice == 0:
      exit()
  else: 
      print("Nem megfelelő karaktert írtál.")
      drawMainMenu()

def PlacesMenuOptions() -> None:
    """
    This will be draw the places menu, and u can here choose from the options.
    """
    print("\n")
    drawPlacesMenu()
    choice = int(input(">_ "))
    if choice == 1:
        PMOpton_1()
    elif choice == 2:
        PMOpton_2()
    elif choice == 0:
        drawMainMenu()
    else: 
        print("Nem megfelelő karaktert írtál") 
        drawPlacesMenu()

def BikesMenuOptions() -> None:
    """
    This will be draw the motorbikes menu, and u can here choose from the options.
    """
    print("\n")
    drawBikesMenu()
    choice = int(input(">_ "))
    if choice == 1:
        BMOpton_1()
    elif choice == 2:
        BMOpton_2()
    elif choice == 3:
        BMOpton_3()
    elif choice == 0:
        drawMainMenu()
    else: 
        print("Nem megfelelő karaktert írtál") 
        drawBikesMenu()

def MMOption_1() -> None:
    """
    In this function is the logic of option 1 in main menu. 
    Here u can add new tour, which will be stored in "tours.txt".
    """
    distances = []
    new_places = []
    date = FUNCTIONS.getDate()

    file = open("places.txt","r",encoding='utf-8')
    places = file.read()
    file.close()

    txt = open("motorbikes.txt","r",encoding='utf-8')
    bikes = txt.read()
    txt.close()   
    line = bikes.split("\n")
    print("- Túra bevitel - ")

    if not bikes:
      print("- Motor felvétele -")
      FUNCTIONS.addNewBike()
    elif len(bikes) > 1:
      print("- Motor kiválasztása -")
      for i in range(len(line)):
        print(str(i+1)+") "+line[i].split()[0])
      choice = int(input(">_ "))
      model = line[choice-1].split()[0]
      year = line[choice-1].split()[1]
      distance = int(line[choice-1].split()[2])
      fuel = int(line[choice-1].split()[3])
      tire = line[choice-1].split()[4]
      consumption = int(line[choice-1].split()[5])
    else:
      model = line[0].split()[0]
      year = line[0].split()[1]
      distance = int(line[0].split()[2])
      fuel = int(line[0].split()[3])
      tire = line[0].split()[4]
      consumption = int(line[0].split()[5])

    start_place = str(input("Elindulási hely: "))
    if start_place not in places: new_places.append(start_place)
    while True:
      next_place = str(input("Következő helyszín (irj 'nincs'-et ha be akarod fejezni): "))
      if next_place == "nincs": break
      if next_place not in places: new_places.append(next_place)
      start_location = FUNCTIONS.getCordinate(start_place).split(" ")
      next_location = FUNCTIONS.getCordinate(next_place).split(" ")
      distances.append(FUNCTIONS.getDistance(float(start_location[0]),float(start_location[1]),float(next_location[0]),float(next_location[1])))
      start_place = next_place
    
    fuel_status = fuel - int(FUNCTIONS.consumptionCalc(FUNCTIONS.Traveled_Distance(distances),consumption))
    tier_status = FUNCTIONS.tireWearCalc(FUNCTIONS.Traveled_Distance(distances))
    distance_status = int(distance + FUNCTIONS.Traveled_Distance(distances))

    file = open("motorbikes.txt","w",encoding="utf-8")
    for i in range(len(line)):
      if line[i].split(" ")[0] == model:
        file.write(model+" "+year+" "+str(distance_status)+" "+str(fuel_status)+" "+str(int(int(tire)-FUNCTIONS.Traveled_Distance(distances)))+" "+str(consumption)+"\n")
      else: 
        if i == len(line)-1: file.write(line[i])
        else: file.write(line[i]+"\n") 
    file.close()
    
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

    MainMenuOptions()

def MMOption_2() -> None:
    """
    In this function is the logic of option 2 in main menu. 
    It will be show the places menu.
    """
    PlacesMenuOptions()

def MMOption_3() -> None:
    """
    In this function is the logic of option 3 in main menu. 
    It will be show the motorbikes menu.
    """
    BikesMenuOptions()

def PMOpton_1() -> None:
    """
    This is the logic of submenu of option 2 in main menu. Option 1.
    Here u can see what places are where u were already.
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
        PlacesMenuOptions()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál.")
        MainMenuOptions()

def PMOpton_2() -> None:
    """
    This is the logic of submenu of option 2 in main menu. Option 2.
    Here u can see the placese where u weren't.
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
    if choice == "V": PlacesMenuOptions()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál.")
        MainMenuOptions()
        
def BMOpton_1() -> None:
    """
    This is the logic of submenu of option 3 in main menu. Option 1. 
    This will be show the motorbikes which are stored in the "motorbikes.txt".
    """
    txt = open("motorbikes.txt","r",encoding='utf-8')
    bike = txt.read()
    txt.close()   
    bikes = bike.split("\n")
    for i in range(len(bikes)):
        print(bikes[i].split(" ")[0]+": "+"Évjárat: "+bikes[i].split(" ")[1]+" | Eddig "+bikes[i].split(" ")[2]+"km-t ment | Üzemanyag: "+bikes[i].split(" ")[3]+" liter"+"| Gumi "+bikes[i].split(" ")[4]+" km-t futott"+"| Fogyasztás: "+bikes[i].split(" ")[5]+" liter/100km")
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": BikesMenuOptions()
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál.")
        MainMenuOptions()

def BMOpton_2() -> None:
    """
    This is the logic of submenu of option 3 in main menu. Option 2. 
    Here u can add new motorbike.
    """
    FUNCTIONS.addNewBike()
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": BikesMenuOptions
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál.")
        MainMenuOptions()

def BMOpton_3() -> None:
    """
    This is the logic of submenu of option 3 in main menu. Option 3. 
    Here u can delete motorbike from "motorbikes.txt" and it will be not stored anymore.
    """
    txt = open("motorbikes.txt","r",encoding='utf-8')
    bike = txt.read()
    txt.close()   
    bikes = bike.split("\n")
    new_bikes = []
    for i in range(len(bikes)):
        print(str(i+1)+") "+bikes[i])

    print("Melyik motort szeretnéd törölni? ")
    choice = int(input(">_ "))
    if choice > len(bikes): 
        print("Nem megfelelőt választottál.")
        drawBikesMenu()
    else:
        for i in range(len(bikes)):
            if i == (choice-1):
                continue
            else: new_bikes.append(bikes[i])

    file = open("motorbikes.txt","w",encoding="utf-8")
    for i in range(len(new_bikes)):
        if i != len(new_bikes)-1: file.write(new_bikes[i]+"\n")
        else: file.write(new_bikes[i])
    
    print("Vissza vagy kilépés? (V/K): ")
    choice = str(input(">_ "))
    if choice == "V": BikesMenuOptions
    elif choice == "K": quit()
    else: 
        print("Nem megfelelőt írtál.")
        MainMenuOptions()


def main() -> None:
    """
    This function contains all the previous functions in a logically correct order for the program to work.
    """
    FUNCTIONS.loadSettlements()
    MainMenuOptions()


from typing import List
import math 
from datetime import datetime

settlements = [] #List of the settlements

def getCordinate(name) ->str:
  """
  This function return with the cordinates of settlements' name.

  Args:
    name (str): The name of the settlement.
  Returns:
    >>>getCordinate("Celldömölk")
    47.25 17.15
    >>>getCordinate("Sárvár")
    47.25 16.9333
  """
  for i in range(len(settlements)):
    if settlements[i][0] == name:
      return settlements[i][1]

def getDistance(lat1,lon1,lat2,lon2) -> float:
  """
  Calculate the great circle distance between two points on the earth (specified in decimal degrees)

  Args:
    lat1,lon1,lat2,lon2 (float): Latitude, longitude. ex. 47.25 16.9333
  Returns:
    >>>getDistance(47.25,17.15,47.25,16.9333)
    16.360958348891938
    >>>getDistance(47.2,17.1833,47.25,16.9333)
    19.68590258255439
  """
  R = 6372.8 # Earth radius in kilometers: 6372.8 km

  dLat = math.radians(lat2 - lat1)
  dLon = math.radians(lon2 - lon1)
  lat1 = math.radians(lat1)
  lat2 = math.radians(lat2)

  a = math.sin(dLat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dLon/2)**2
  c = 2*math.asin(math.sqrt(a))

  return R * c

def loadSettlements() ->List:
    """
    This function load the settlements' name and cordinates to the "settlements" list.
    """
    text = open("settlements.txt","r",encoding="utf-8")
    lines = text.read().split("\n")
    for line in lines:
        settlements.append(line.split(":"))
    return settlements

def Traveled_Distance(distances) ->int:
  """
  This function go through a list, and sum all of the elements in list.
  Args:
    distances (list): In this list, there are the distances between coordinates.
  Returns:
    distances = [1,2,3]
    >>>Traveled_Distance(distances)
    6

    distances = [2,2,3]
    >>>Traveled_Distance(distances)
    7
  """
  all_distance = 0
  for i in range(len(distances)):
    all_distance += distances[i]
  return all_distance

def getDate() ->str:
  """
  This function get the date of today.
  """
  return datetime.today().strftime("%Y-%m-%d")

def consumptionCalc(distance,consumption) -> float:
  """
  This function calculate the fuel consumption on 100km.

  Args:
    distance, consumption (int): The travled distance (km) and the consumption of the motorbike (l/100km).
  Returns:
    >>>consumptionCalc(100,7)
    7.0
    >>>consumptionCalc(20,7))
    1.4000000000000001
  """
  return (distance / 100) * float(consumption)

def tireWearCalc(distance_tire) ->float:
  """
  This function calculate the tires' status (%). The value is only approximate. Abou 40000 is the average lifetime of a tire in km (motorbikes).
  Args:
    distance_tire (int): The current km in the tires.
  Returns:
    >>>tireWearCalc(100)
    99.75
    >>>tireWearCalc(35000)
    12.5
  """
  return ((40000-distance_tire) / 40000) * 100 

def addNewBike()->None:
    """
    This function add new bike to the "motorbikes.txt".
    """
    model= str(input("Motor neve és típusa (formátum: KTM-Exc125): "))
    year = str(input("Évjárat: "))
    distance = int(input("Kilóméter óra: "))
    fuel = int(input("Üzemanyag szint (liter): "))
    tire = int(input("Mennyi kilóméter van a gumikban: "))
    consumption = int(input("Fogyasztás (liter/100km): "))

    file = open("motorbikes.txt","a",encoding="utf-8")
    file.writelines("\n"+model+" "+year+" "+str(distance)+" "+str(fuel)+" "+str(tire)+" "+str(consumption))
    file.close()


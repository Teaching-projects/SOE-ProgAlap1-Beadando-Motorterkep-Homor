from typing import List
import math 
from datetime import datetime
import json
import motorbike as MOTORBIKE

def getCordinate(name) ->str:
  """
  This function return with the cordinates of settlements' name.

  Args:
    name (str): The name of the settlement.
  Returns:
    >>> getCordinate("Celldömölk")
    '47.25 17.15'
    >>> getCordinate("Sárvár")
    '47.25 16.9333'
  """
  data = ReadData()
  for p in data["settlements"]:
    if p["name"] == name:
      return (p["latitude"] + " " + p["longitude"])

def IsInSettlements(name) -> bool:
  """
  This check the settlement is in the list.

  Args:
    name (str): The name of the settlement.
  Returns:
    >>> IsInSettlements("Celldömölk")
    True
    >>> IsInSettlements("Sárvár")
    True
  """
  data = ReadData()
  settlement = []
  for p in data["settlements"]:
    settlement.append(p["name"])
  if name in settlement: return True
  else: return False

def getDistance(lat1,lon1,lat2,lon2) -> float:
  """
  Calculate the great circle distance between two points on the earth (specified in decimal degrees)

  Args:
    lat1,lon1,lat2,lon2 (float): Latitude, longitude. ex. 47.25 16.9333
  Returns:
    >>> getDistance(47.25,17.15,47.25,16.9333)
    16.360958348891938
    >>> getDistance(47.2,17.1833,47.25,16.9333)
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

def ReadData() -> List:
  """
  This will read from "data.json" and return a list.
  """
  with open('data.json') as json_file:
    data = json.load(json_file)
  return data

def Traveled_Distance(distances) ->int:
  """
  This function go through a list, and sum all of the elements in list.
  Args:
    distances (list): In this list, there are the distances between coordinates.
  Returns:
    >>> Traveled_Distance([1,2,3])
    6
    >>> Traveled_Distance([2,2,3])
    7
  """
  all_distance = 0
  for i in range(len(distances)):
    all_distance += distances[i]
  return all_distance

def ReadPlaces()->List:
  """
  This function read the data from "data.json".
  """
  file = open("places.txt","r",encoding='utf-8')
  places = file.read()
  file.close()
  return places

def getDate() ->str:
  """
  This function get the date of today.
  """
  return datetime.today().strftime("%Y-%m-%d")

def Tour(start_place)->List:
  """
  Here you can add the places where u were. It will be return a list with the places.
  """
  distances = []
  places = ReadPlaces()
  new_places = []
  if start_place not in places: new_places.append(start_place)
  while True:
    next_place = str(input("Következő helyszín (irj 'nincs'-et ha be akarod fejezni): "))
    if next_place == "nincs": break
    else:
      if IsInSettlements(next_place) == True:
        if next_place not in places: new_places.append(next_place)
        start_location = getCordinate(start_place).split(" ")
        next_location = getCordinate(next_place).split(" ")
        distances.append(getDistance(float(start_location[0]),float(start_location[1]),float(next_location[0]),float(next_location[1])))
        start_place = next_place
      else: print("Nincs ilyen település a listában.")
  return distances, new_places
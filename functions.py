from typing import List
import math 
from datetime import datetime
import json

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

def IsInSettlements(name) -> bool:
  """
  This check the settlement is in the list.
  """
  settlement = []
  for i in range(len(settlements)):
    settlement.append(settlements[i][0])
  if name not in settlement: return False
  else: return True

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

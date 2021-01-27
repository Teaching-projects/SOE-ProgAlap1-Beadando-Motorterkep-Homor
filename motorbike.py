import json
from typing import List
import functions as FUNCTION

def tireWearCalc(distance_tire) ->float:
  """
  This function calculate the tires' status (%). The value is only approximate. Abou 40000 is the average lifetime of a tire in km (motorbikes).
  Args:
    distance_tire (int): The current km in the tires.
  Returns:
    >>> tireWearCalc(100)
    99.75
    >>> tireWearCalc(35000)
    12.5
  """
  return ((40000-distance_tire) / 40000) * 100 

def consumptionCalc(distance,consumption) -> float:
  """
  This function calculate the fuel consumption on 100km.

  Args:
    distance, consumption (int): The travled distance (km) and the consumption of the motorbike (l/100km).
  Returns:
    >>> consumptionCalc(100,7)
    7.0
  """
  return (distance / 100) * float(consumption)

def addNewBike()->None:
    """
    This function add new bike to the "data.json".
    """
    model= input("Motor neve és típusa (formátum: KTM-Exc125): ")
    year = input("Évjárat: ")
    distance = int(input("Kilóméter óra: "))
    fuel = int(input("Üzemanyag szint (liter): "))
    tire = int(input("Mennyi kilóméter van a gumikban: "))
    consumption = int(input("Fogyasztás (liter/100km): "))

    with open('data.json') as json_file:
      data = json.load(json_file)
    
    data['bikes'].append({
    'model': model,
    'year': year,
    'distance': distance,
    'fuel': fuel,
    'tire': tire,
    'consumption': consumption
    })

    with open('data.json', 'w') as outfile:
      json.dump(data, outfile)

def LenOfBikes()->int:
  """
  This will be give how many bike are stored in the list.
  """
  data = FUNCTION.ReadData()
  count = 0
  for p in data['bikes']:
    count += 1
  return count

def ChooseBike():
  """
  Here you can choose the bike.
  """
  count = 0
  data = FUNCTION.ReadData()
  print("- Motor kiválasztása -")
  for p in data['bikes']:
    print(str(count+1)+") " + "Típus: " + str(p['model'])+"| "+"Évjárat: " + str(p['year'])+"| "+"Km óra: " + str(p['distance']))
    print('')
    count += 1
  return int(input(">_ "))
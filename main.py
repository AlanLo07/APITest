from fastapi import FastAPI
from Conecction import get_database
import json

app = FastAPI()
dbname = get_database()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cars/")
async def cars():
  item_details = dbname['cars'].find({})
  cars = []
  for item in item_details:
    cars.append({
      "_id": str(item['_id']),
      "id": item['id'],
      "name": item['name'],
      "year": item['year'],
      "price": item['price'],
      "dimensions": {
          "unit": item['dimensions']['unit'],
          "large": item['dimensions']['large'],
          "high": item['dimensions']['high'],
          "width": item['dimensions']['width']
      },
      "image": item['image'],
      "color": item['color'],
    })
  return {"result": cars}

@app.get("/cars/{car_id}/")
async def car(car_id: str):
  print(car_id)
  try:
    item_details = dbname['cars'].find_one({"id": int(car_id)})
  except:
    return {"error": "Car not found"}
  if item_details:
    return {
      "car": {
        "_id": str(item_details['_id']),
        "id": item_details['id'],
        "name": item_details['name'],
        "year": item_details['year'],
        "price": item_details['price'],
        "dimensions": {
            "unit": item_details['dimensions']['unit'],
            "large": item_details['dimensions']['large'],
            "high": item_details['dimensions']['high'],
            "width": item_details['dimensions']['width']
        },
        "image": item_details['image'],
        "color": item_details['color'],
      }
    }
  else:
    return {"result": "Car not found"}
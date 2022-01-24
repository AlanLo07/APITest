from fastapi import FastAPI, Request
import json

app = FastAPI()


def get_database():
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://alanlo:<Mafer&Alan7>@cluster0.yd92l.mongodb.net/Cars?retryWrites=true&w=majority"

    # client = MongoClient(CONNECTION_STRING)
    client = pymongo.MongoClient('mongodb://mongo:27017/todos')
    # client = pymongo.MongoClient('mongodb://localhost:27017/Cars')
    

    return client["Cars"]

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

@app.post("/cars/")
async def create_car(car: Request):
  car = await car.json()
  id = dbname['cars'].find({}).sort("id", -1).limit(1)
  car = car["car"]
  try:
    car["id"] = id[0]["id"] + 1
  except:
    car["id"] = 1
  car["dimensions"]["unit"] = "m"
  car_id = dbname['cars'].insert_one(car).inserted_id
  return {"result": "success add car"}

@app.delete("/cars/{car_id}/")
async def delete_car(car_id: int):
  dbname['cars'].delete_one({"id": car_id})
  return {"result": "success delete car"}

@app.put("/cars/{car_id}/")
async def update_car(car_id: int, car: Request):
  car = await car.json()
  car = car["car"]
  car["dimensions"]["unit"] = "m"
  dbname['cars'].update_one({"id": car_id}, {"$set": car})
  return {"result": "success update car"}
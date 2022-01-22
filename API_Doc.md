# API Players

API Cars es una simple API para obtener, guardar y borrar autos de la base de datos MONGO DB

## Cars Collection [/cars]

### List All Cars [GET]

+ Response 200 (application/json)

        {
            "result" : [
                {
                    "id": 1
                    "name": "figo",
                    "year": "2014",
                    "price": 259800,
                    "dimensions": {
                        "unit": "m",
                        "large": 4.249,
                        "high": 1.525,
                        "width": 1.699
                    },
                    "image": "http://image.jpg",
                    "color": "red",
                }
            ]
        }

## Car [/cars/{car_id}]

### Get Car [GET]

+ Response 200 (application/json)

        {
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

    Or

+ Response 200 (application/json)

        {"result": "Car not found"}

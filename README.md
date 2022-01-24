# API Cars

API Cars es una simple API para obtener, guardar y borrar autos de la base de datos MONGO DB

## Run local

install [python](https://www.python.org/)

run command

``` python
    pip install -r requierements.txt or python -m pip install -r requierements.txt
    uvicorn app.main:app --port 8090 --reload
```

## Run Docker container

+ install [docker](https://www.docker.com/products/docker-desktop)
+ install [docker-compose](https://docs.docker.com/compose/install/)

run command

```CMD
    docker-compose build
    docker-compose up -d
```

## Run minikube

+ install [kompose](https://kompose.io/)
+ install [kubectl](https://kubernetes.io/es/docs/tasks/tools/install-kubectl/)
+ install [minikube](https://minikube.sigs.k8s.io/docs/start/)

run command

```CMD
    kompose convert
    kubectl apply -f api-service.yaml,api-deployment.yaml,api-claim0-persistentvolumeclaim.yaml,mongo-deployment.yaml,mongo-claim0-persistentvolumeclaim.yaml
    minikube service api
```

## Cars Collection [/cars]

### List All Cars [GET]

+ Response 200 (application/json)

 ``` JSON
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
```

### Get Car [GET] [/cars/{car_id}]

+ Response 200 (application/json)

```JSON
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
```

Or

+ Response 200 (application/json)

```JSON
    {"result": "Car not found"}
```

### POST Car [POST] [/cars/]

+ Parameters Body (application/json)

```JSON
    {
        "name": \<str>,
        "year": \<int>,
        "price": \<float>,
        "dimensions": {,
            "large": \<float>,
            "high": \<float>,
            "width": \<float>,
        },
        "image": \<str>,
        "color": \<str>,
    }
```

+ Response 200 (application/json)

```JSON
    {
        "result": "succes add car"
    }
```

### Delete Car [DELETE] [/cars/{car_id}]

+ Response 200 (application/json)

```JSON
    {
        "result": "success delete car"
    }
```

### Update Car [DELETE] [/cars/{car_id}]

+ Parameters Body (application/json)
  
```JSON
    {
        "name": \<str>,
        "year": \<int>,
        "price": \<float>,
        "dimensions": {,
            "large": \<float>,
            "high": \<float>,
            "width": \<float>,
        },
        "image": \<str>,
        "color": \<str>,
    }
```

+ Response 200 (application/json)

```JSON
    {
        "result": "success delete car"
    }
```

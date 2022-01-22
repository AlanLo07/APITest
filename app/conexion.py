def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://alanlo:<Mafer&Alan7>@cluster0.yd92l.mongodb.net/Cars?retryWrites=true&w=majority"

    # client = MongoClient(CONNECTION_STRING)
    client = pymongo.MongoClient('mongodb://localhost:27017')

    return client["Cars"]
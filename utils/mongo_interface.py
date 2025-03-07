from pymongo import MongoClient

connection_string = 'mongodb://localhost:27017/'
db_name = 'main_db'
collection_name = 'langs'


def setup_mongo():
    client = MongoClient(connection_string)
    db = client[db_name]
    collection = db[collection_name]
    return collection

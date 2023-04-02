import pymongo
from parser import get_generator
from config import MONGO_URI, MONGO_DB_NAME


def mongo_connect():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    return db["students"]


def mongo_insert():
    coll = mongo_connect()
    gen = get_generator()
    i = 1
    while True:
        try:
            insertion_query = next(gen)
            insertion_query['_id'] = i
            coll.insert_one(insertion_query)
            i += 1
        except AttributeError:
            break


def test():
    coll = mongo_connect()
    coll.delete_many({})
    for el in coll.find({"Student_Group": "ИВБО-07-20"}):
        print(el)

#test()
mongo_insert()

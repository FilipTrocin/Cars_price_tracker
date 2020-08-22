import pymongo
import UI

# Connection to the database
from bson import ObjectId


def establish_connection():
    client = pymongo.MongoClient('localhost', 27017)

    # Accessing database
    db = client.CarDatabase

    # Getting collection
    collection = db.CarDatabase

    # inserting object to database, adding _id automatically
    # new = collection.insert_many(post)


# Temporary function to checking is data from UI.global_list is transfered to Database.py
def print_grabber():
    print('Hello Database!: ', UI.user_search_list)

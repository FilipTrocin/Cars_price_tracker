import pymongo
import pprint

# Connection to the database
from bson import ObjectId

client = pymongo.MongoClient('localhost', 27017)

# Accessing database
db = client.CarDatabase

# Getting collection
collection = db.CarDatabase

# inserting object to database, adding _id automatically
# new = collection.insert_many(post)


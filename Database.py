import pymongo
import pprint

# Connection to the database
from bson import ObjectId

client = pymongo.MongoClient('localhost', 27017)

# Accessing database
db = client.MobileDatabase

# Getting collection
collection = db.MobileDatabase

# inserting object to database, adding _id automatically
# new = collection.insert_one(post).inserted_id



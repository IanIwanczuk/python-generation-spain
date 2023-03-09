from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.Northwind
collection = db.Customers

cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": "USA"}).limit(3)
cursor = collection.find({"Country": "USA"}).skip(5)
cursor = collection.find({"Country": "USA"}).sort("City")       # Ascendente A a W
cursor = collection.find({"Country": "USA"}).sort("City", 1)    # Ascendente A a W
cursor = collection.find({"Country": "USA"}).sort("City", -1)   # Descendente W a A

while (cursor.alive):
    document = cursor.next()
    print(document["CompanyName"], document["Country"], document["City"])
    print("")

exit()


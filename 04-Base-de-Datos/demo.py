from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": "USA"}).limit(3)
cursor = collection.find({"Country": "USA"}).skip(5)
cursor = collection.find({"Country": "USA"}).sort("City")       # Ascendente A a W
cursor = collection.find({"Country": "USA"}).sort("City", 1)    # Ascendente A a W
cursor = collection.find({"Country": "USA"}).sort("City", -1)   # Descendente W a A

"""
===================================================
 Listado de operadores relacionales
===================================================
$eq - equal - igual
$lt - low than - menor que
$lte - low than equal - menor o igual que
$gt - greater than - mayor que
$gte - greater than equal - mayor o igual que
$ne - not equal - distinto
$in - in - dentro de
$nin - not in - no dentro de
"""
# Ambas consultas buscan clientes de USA (las dos son iguales)
cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": {"$eq" : "USA"}})

# Todos los cliientes que no son de USA
cursor = collection.find({"Country": {"$ne": "USA"}})

# Buscamos clientes de USA y Mexico
cursor = collection.find({"Country": {"$in": ["USA", "Mexico"]}}).sort([("Country", 1), ("City", 1)])

# Buscamos clientes de USA y la ciudad de San Francisco
cursor = collection.find({"Country": "USA", "City": "San Francisco"})

# Consultas utilizando los operados
cursor = collection.find({"Country": "USA", "City": "San Francisco"})
cursor = collection.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]})

cursor = collection.find({"$or": [{"Country": "USA"}, {"City": "Berlin"}]})
cursor = collection.find({"$or": [{"Country": "USA"}, {"Country": "Germany"}]})


cursor = collection.find({"Country": "Mexico"})
while (cursor.alive):
    cliente = cursor.next()
    print(f"{cliente['CustomerID']}# {cliente['CompanyName']}")
    
    cursorPedidos = db.Orders.find({"CustomerID": cliente["CustomerID"]})
    while (cursorPedidos.alive):
        pedido = cursorPedidos.next()
        print(f">>> {pedido['OrderID']} {pedido['OrderDate']}")

    print("")


print("==========================================================")
print("")

# Los datos de ANATR y todos sus pedidos

cursor = db.Customers.aggregate([
   {"$match": {"Country": "USA"}},
   {"$sort": {"City": 1}},
   {"$lookup": {
        "from": "Orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Orders"
   }}
])

while(cursor.alive):
    customer = cursor.next()
    print(f"{customer['CustomerID']}# {customer['CompanyName']}")
    for order in customer["Orders"]:
        print(f">>> {order['OrderID']} {order['OrderDate']}")
    print("")


exit()

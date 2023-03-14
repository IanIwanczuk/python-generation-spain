from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient("mongodb://localhost:27017")
db = client.Northwind
collection = db.Products

# Definir la conexión

# Cuanto productos tenemos ???, buscamos en mongoDB
# Mostramos el múmero de productos y un listodo

# Filtrar los productos con UnitsInStock 0, utilizando filter()

# Valor del Stock UnitsInStock x UnitPrice
# con un FOR 
# otra formula es realizarlo con MAP() SUM()
# con una función AGGREGATE de mongoDB y los operadores $sum y $multiply 

query = [
    {"$match": { "UnitsInStock": {"$ne": "0"}}},
    {"$addFields": {
        "Price": {"$toDouble": "$UnitPrice"},
        "Stock": {"$toInt": "$UnitsInStock"}
    }},
    {"$group": { 
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Price", "$Stock"]}},
        "Products": { "$sum": 1}
    }}
]


cursor = collection.aggregate(query)
print(cursor.next())


# Con un identificador de pedido
# Mostramos datos -> ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
# Mostramos el detalle del pedido -> Producto, Cantidad, Precio, Precio Total, Total Pedido

import pymssql, time

# Establecer conexión con la base de datos
connection = pymssql.connect(
    server="host-sqlserver-eoi.database.windows.net", 
    user="Administrador", 
    password="azurePa$$w0rd",
    database="Northwind")

# Creamos un cursor para ejecutar comando en la base de datos
# Retorna Tuplas
cursor = connection.cursor()

# Retorna Diccionarios
cursor = connection.cursor(as_dict=True)


command = "INSERT INTO dbo.Customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
command = "INSERT INTO dbo.Customers(CustomerID, CompanyName, City, Country) VALUES (%d, %d, %d, %d)"

data = []
data.append(('DEA10', 'Empresa Uno SL', 'Madrid', 'Spain'))
data.append(('DEA20', 'Empresa Dos SL', 'Valencia', 'Spain'))
data.append(('DEA30', 'Empresa Tes SL', 'Badajoz', 'Spain'))

cursor.executemany(command, data)
connection.commit()
print(f"Número de filas insertadas: {cursor.rowcount}")

exit()


# Insertamos datos utilizando el comando INSERT
cursor.execute("INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, City, Country) VALUES ('DEM75', 'Empresa Demo, SL', 'Borja Cabeza', 'Madrid', 'Spain')")

# Utilizamos la función commit() para confirmar la transación y las operaciones de inserción
# actualización y borrado
connection.commit()

# Utilizamos la función rollback() para cancelar la transación y anular las operaciones de 
# inserción, actualización y borrado
connection.rollback()


exit()





# Ejemplos de comandos SELECT, para recuperar registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'Spain'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "Spain")

cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'Spain' ORDER BY City")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY City", "Spain")

pais = "Spain"
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY City", pais)

cursor.execute("SELECT * FROM dbo.Customers ORDER BY Country, City")
cursor.execute("SELECT CustomerID, CompanyName, Country, City FROM dbo.Customers WHERE Country = %d", "Spain")

# Mostrar el contenido del cursor mediante un WHILE
row = cursor.fetchone()
while(row):
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']} - {row['City']} ({row['Country']})\n")
    row = cursor.fetchone()

# Mostrar el contenido del cursor mediante un FOR
for row in cursor.fetchall():
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}\n")
    # Si trabajamos con Tuplas
    # print(f"     ID: {row[0]}")
    # print(f"Empresa: {row[1]}\n")






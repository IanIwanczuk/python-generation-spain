#####################################################################
# Colecciones - DICCIONARIOS                                        #
#####################################################################

vacio = {}
frutas = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LM":"líma", "MA":"mandarina"}

# Mostrar el diccionario
print(frutas)

# Mostrar un valor utilizando la clave
# Si la clave no existe se produce una Exception
print(frutas["NA"])

# Mostrar un valot utilizando la función GET
# Si la clave no existe la función GET retorna el valor None
print(frutas.get("NA"))
print(frutas.get("NI"))

# Mostar el número de valores del diccionario
print(len(frutas))

# Modificar el valor del diccionario
frutas["NA"] = "sandia"
frutas.update({"NA": "ciruela"})
print(frutas["NA"])

# Añadir un nuevo valor al diccionario
frutas["ME"] = "melón"
frutas.update({"KW": "kiwi"})

# Eliminar un valor utilizando la clave
frutas.pop("NA")
del frutas["LM"]

# Recorremos y mostramos todos los valores del diccionario utilizando FOR
for key in frutas:
    print(f"Clave: {key} - Valor: {frutas[key]}")
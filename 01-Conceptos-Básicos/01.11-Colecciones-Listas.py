
# Utilizamos [] para crear listas
vacia = []
frutas = ["naranja", "limón", "pomelo", "líma", "mandarina"]

# Mostrar el contenido de una lista
print(frutas)

# Mostrar el valor contenido en una posición (2 = pomelo)
print(frutas[2])

# Mostrar el número de valores que contiene la lista
print(len(frutas))

# Mostrar el número de veces que tenemos un valor (sandia, cero repeticiones)
# Sensible a mayúsculas y acentos
print(frutas.count("sandia"))

# Modificar el valor de una posición (modificar pomelo 2 por fresa)
frutas[2] = "fresa"
print(frutas[2])

# Añadir nuevo valores utilizando la función APPEND
frutas.append("manzana")
frutas.append("melón")

# Añadir un nuevo valor en posición con la función INSERT(index, value) (sandia en la posición 1)
frutas.insert(1, "sandia")

# Añadir si el valor no exite
if("platano" not in frutas):
    frutas.append("platano")

# Añadir varios valores procedentes de una lista con EXTEND(values)
nuevasFrutas = ["maracuya", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas)

# Eliminar un valor en base a la posición utilizando POP(index)
frutas.pop(5)

# Eliminar un valor en base al valor utilizando REMOVE(value)
frutas.remove("naranja")

# Eliminar un valor si existe
if("sandia" in frutas):
    frutas.remove("sandia")

# Invertir el orden de los valores utilizando REVERSE
frutas.reverse()

# Ordernar los valores utilizando SORT
frutas.sort()
frutas.sort(reverse = True)

# Recorremos la lista y mostramos los valores
for fruta in frutas:
    print(fruta)

for index in range(0, len(frutas), 1):
    print(f"{index}: {frutas[index]}")

# Copiar todos los valores de la lista
vacia = frutas.copy()

# Eliminar todos los valores de la lista
frutas.clear()
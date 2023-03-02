#####################################################################
# Sentencias de Control - For                                       #
#####################################################################
#                                                                   #
#   Sintaxis: for [variable] in [variable colección]                #
#             print([variable])                                     #
#                                                                   #
#             for [variable] in range([inicio], [fin], [intervalo]) #
#             print([variable])                                     #
#                                                                   #
#####################################################################

citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]

# Utilizamos FOR para recorrer colecciones.
for fruta in citricos:
    print(f"{fruta}")
print("")

# Utilizamos FOR para recorrer colecciones, con RANGE establecemos un contador
# que nos da las posiciones de la colección de citricos
for i in range(0, len(citricos), 1):
    print(f"{i}: {citricos[i]}")
print("")

for i in range(len(citricos)):
    print(f"{i}: {citricos[i]}")
print("")

# Podemos utiliza FOR combinado con otras funciones como ENUMERATE que
# retorna el indice y el valor de cada elemento de la colección

for index, fruta in enumerate(citricos):
    print(f"{index}: {fruta}")
print("")

# Utilizamos FOR para recorrer colecciones.
# Cuando fruta es igual a pomelo se finaliza el for con break, por lo que no
# muestra el valor de lima ni mandarina.
for fruta in citricos:
  print(fruta)
  if fruta == "pomelo":
      break
print("")

# Utilizamos FOR para recorrer colecciones.
# Cuando fruta es igual a pomelo se cotinua el for con continue, por lo que no
# muestra el valor de líma pero si mandarina.
for fruta in citricos:
  print(fruta)
  if fruta == "pomelo":
      continue
print("")
  

# Utilizamos FOR con RANGE para establecer un contador y ejecutar
# sentencias repetidas veces.

# Ejemplo: de 0 a 99 de 5 en 5
for i in range(0, 100, 5):
    print(f"Número: {i}")
print("")

# Ejemplo: de 5 a 0 de 1 en 1
for i in range(5, 0, -1):
    print(f"Número {i}")
print("")
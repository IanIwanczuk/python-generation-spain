valor = 0

while (valor < 5):
    valor = valor + 1                   # equivalente a valor += 1
    if(valor == 2):
        break
    print(f"El valor es {valor}.")

print("Fin del WHILE")

# Número de elementos/valores: 5
# Posiciones 0 hasta num elementos - 1 (0-4)

citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]
posicion = 0

while (posicion < len(citricos)):    
    print(f"{posicion}: {citricos[posicion]}")
    posicion += 1
else:
    print("Else del While")    

print("Fin del WHILE")

while (true):
   #sentencias
   if (posicion < len(citricos)):
       break
else:
    print("Else del While")

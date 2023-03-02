#####################################################################
# Sentencias de Control - While                                     #
#####################################################################
#                                                                   #
#   Sintaxis: while ([condición]):                                  #
#                                                                   #
#   Con while podemos ejecutar un conjunto de sentencias            #
#   siempre que la condición sea verdadera.                         #
#                                                                   #
#####################################################################

valor = 0
while (valor < 5):
    valor += 1
    if (valor == 3):
        continue
    print(f"Valor: {valor}")

print("Fin del WHILE")
print("")

#####################################################################

citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]
index = 0

while (index < len(citricos)):
    print(citricos[index])
    index += 1

print("Fin del WHILE")
print("")

#####################################################################

index = 0

while (index < 5):
    index = index + 1                   # equivalente a valor += 1
    if (index == 2):
        break                           # también podemos utilizar continue
    print(f"El valor es {valor}.")

print("Fin del WHILE")
print("")

#####################################################################

# Como implementar un DO/WHILE de otros leguajes de programación.
# Nos aseguramos que las sentencias se ejecutan al menos una vez.

index = 0

while (True):
   print(citricos[index])
   index += 1
   if (index >= len(citricos)):
       break
else:
    print("Fin del WHILE")
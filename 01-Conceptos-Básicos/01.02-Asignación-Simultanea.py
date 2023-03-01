######################################################################
# Asignación Simultanea                                              #
######################################################################
#                                                                    #
#   Sintaxis: [var1], [var2] = [var2], [var1]                        #
#                                                                    #
#   Ejemplos:                                                        #
#       a = 10                                                       #
#       b = 5                                                        #
#       a,b = b,a                                                    #
#                                                                    #
######################################################################

# Cambiar los valores de a y b. Intento 1.
a = 5
b = 10

a = b
b = a

print("Intento 1. Forma incorrecta.")
print(a)
print(b)
print("")

# Cambiar los valores de a y b. Intento 2.
a = 5
b = 10

temp = a
a = b
b = temp

print("Intento 2. Funciona utilizando una variable temporal.")
print(a)
print(b)
print("")


# Cambiar los valores de a y b. Intento 3.
a = 5
b = 10

a,b = b,a

print("Intento 3. Funciona, la forma preferida en Python.")
print(a)
print(b)
print("")
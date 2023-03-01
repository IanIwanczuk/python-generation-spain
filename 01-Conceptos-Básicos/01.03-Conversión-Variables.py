#####################################################################
# Conversión de variables                                           #
#####################################################################

# Declarar variables
a = 5.3
b = "25"
c = "25.7"

# Conversión alfanúmerico (STR) valores númericos (INT, FLOAT)
print("Número: " + str(a))
print("")

# Conversión númericos (INT, FLOAT) valores alfanúmericos (STR)
print(f"Número: {b}")
print(type(b))
print(f"Número: {int(b)}")
print(type(int(b)))
print("")
print(f"Suma: {b + c}")
print(type(b + c))
print(f"Suma: {int(b) + float(c)}")
print(type(int(b) + float(c)))
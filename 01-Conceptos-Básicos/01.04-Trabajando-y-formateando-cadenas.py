#####################################################################
# Trabajando con Cadenas de Texto                                   #
#####################################################################

cadena = "  hola mundo !!!  "
print(cadena)

# Mostrar caractéres de posiones o rangos
print(cadena[2])
print(cadena[2:])
print(cadena[:6])
print(cadena[2:6])
print(cadena[-2])

print(f"Número de caractéres: {len(cadena)}")

# Funciones de objetos de tipo STR
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())
print(cadena.replace("o", "0"))
print(cadena.count("o"))
print(cadena.isdigit())
print("57".isdigit())


#####################################################################
# Formateando Cadenas y Número                                      #
#####################################################################

mensaje = "Mundo"

print("Hola " + mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))
print(f"Hola {mensaje} !!!")

numero = 10 / 3
print(numero)
print("Hola {n:1.2f} !!!".format(n=numero))
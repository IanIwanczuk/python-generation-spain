#######################################################################
# Requerimientos funcionales:
#
#   -> Calcular la letra de DNI
#   -> Formular: dni % 23
#######################################################################

letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']

try:
    num = int(input("Escribe tu número de DNI:"))
    indice = num % 23
    letra = letras[indice]

    print(f"Tu letra del DNI es {letra}")
except Exception as err:
    print(f"Error: {err}")
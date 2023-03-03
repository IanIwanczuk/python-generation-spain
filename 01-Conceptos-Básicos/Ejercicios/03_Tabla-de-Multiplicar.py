#######################################################################
# Requerimientos funcionales:
#
#   -> Mostar la tabla de multiplicar del número indicado por el usuario
#   -> Resolver con un FOR y también con un WHILE
#######################################################################

import Color

###########################################################################
## Ejemplo 1. FOR
###########################################################################

try:
    num = int(input("Escribe un número: "))
    print("")
    print(f"**************************************")
    print(f" Tabla de multiplicar del {num}")
    print(f"**************************************")

    for i in range(1, 11, 1):
        print(f" {i} x {num} = {str(i * num)}")

    print(f"**************************************")
except Exception as err:
    print(f"Error: {err}")



###########################################################################
# Ejemplo 2. WHILE
###########################################################################
try:
    num = int(input("Escribe un número: "))
    print("")
    print(f"**************************************")
    print(f" Tabla de multiplicar del {num}")
    print(f"**************************************")

    i = 1
    while(i < 11):
        print(f" {i} x {num} = {str(i * num)}")
        i += 1

    print(f"**************************************")
except Exception as err:
    print(f"{Color.CBOLD}Error: {Color.CRED} {err} {Color.CEND}")



###########################################################################
# Ejemplo 3. FOR con colores y ajustes al presentar
###########################################################################
try:
    num = int(input("Escribe un número: "))
    print("")
    print(f"**************************************")
    print(f"{Color.CYELLOW} Tabla de multiplicar del {num}{Color.CEND}")
    print(f"**************************************")

    for i in range(1, 11, 1):
        print(f" {str(i).rjust(2)} x {num} = {str(i*num).rjust(len(str(num*10)))}")

    print(f"**************************************")
except Exception as err:
    print(f"{Color.CBOLD}Error: {Color.CRED} {err} {Color.CEND}")
#####################################################################
# Declaración de Funciones Lambda                                   #
#####################################################################
#                                                                   #
#   Sintaxis: lambda arguments : expression                         #
#                                                                   #
#   Ejemplos:                                                       #
#       x = lambda a : a + 10                                       #
#       print(x(5))                                                 #
#                                                                   #
#####################################################################

numeros = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

#==============================================================

def MayorDeCien(lista):
    resultado = []

    for item in lista:
        if (item > 100):
            resultado.append(item)

    return resultado

print(MayorDeCien(numeros))

#==============================================================

def Func1(x):
    if (x > 100):
        return True
    else:
        return False
    
def Func2(x):
    if (x % 2 == 0):
        return True
    else:
        return False

print(list(filter(Func1, numeros)))

#==============================================================

func1 = lambda x: x > 100
print(f"Valores mayores de 100: ", list(filter(func1, numeros)))

print(f"Valores mayores de 100: ", list(filter(lambda x: x > 100, numeros)))
print(f"Valores pares: ", list(filter(lambda x: x % 2 == 0, numeros)))
print(f"Valores menores de 50: ", list(filter(lambda x: x < 50, numeros)))


def Filtrado(formula, datos):
    resultado = []

    for item in datos:
        if (formula(item) == True):
            resultado.append(item)

    return resultado


print(">>> ", Filtrado(lambda x: x > 100, numeros))
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
# 
#####################################################################

def Saludo(nombre):
    print(f"Hola, me llamo {nombre}")

minombre = "Borja"
Saludo(minombre)
Saludo("Fco. de Borja")


# La función Lambda tiene la misma funcionalidad que la función Saludo()
demo = lambda nombre : print(f"Hola, me llamo {nombre}")
demo("Ana")


# La función Calcular() recibe como parametro una función lambda con el calulo
# que tiene que realizar

def Sumar(num):
    return lambda a: a + num

def Restar(num):
    return lambda a: a - num

def Multiplicar(num):
    return lambda a : a * num

def Dividir(num):
    return lambda a: a / num

def Calcular(formula):
    for n in range(1, 11, 1):
        print(f"Valor: {n} - Resultado: {formula(n)}")

Calcular(Dividir(25))
Calcular(lambda x: x - 30)
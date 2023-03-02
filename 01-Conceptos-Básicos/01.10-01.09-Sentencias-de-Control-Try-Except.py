import sys

num1 = 0
num2 = 100

try:
    raise ValueError("Mi error", "2", "3", 4)
    num3 = num1 / num2
    print(f"Resultado: {num3}")
    f = open('myfile.txt')
except ZeroDivisionError as err:
    print("Upssss !!! no se puede dividir por cero")
    print(err)
    print(type(err))
except FileNotFoundError as err:
    print("Upssss !!! el fichero no existe")
    print(err)
    print(type(err))
except Exception as err:
    print("Upssss !!! se ha producido un error")
    print(err)
    print(type(err))
finally:
    print("Bloque FINALLY")


print("Fin")

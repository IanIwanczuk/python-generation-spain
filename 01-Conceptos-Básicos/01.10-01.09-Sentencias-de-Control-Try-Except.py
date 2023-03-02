#####################################################################
# Sentencias de Control - Try/Except/Else/Finally                   #
#####################################################################
#                                                                   #
#   try     permite controlar las excepciones producidas en un      #
#           bloque de código.                                       #
#                                                                   #
#   except  bloque de instrucciones que se ejecutan cuando se       #
#           produce una excepción.                                  #
#                                                                   #
#   else    bloque de instrucciones que se ejecutan al finalizar    #
#           el try si no se produce un excepción.                   #
#                                                                   #
#   finally bloque de instrucciones que se ejecutan siempre que     #
#           finaliza el try, except o else.                         #
#                                                                   #
#####################################################################
import sys

numero1 = 0
numero2 = 100

###########################################################################

try:
    numero3 = numero2 / numero1
    print(f"Número 3: {numero3}")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except:
    print("Upsss Error !!!")
else:
    print("Bloque TRY finalizado correctamente")
finally:
    print("Bloque TRY o EXCEPT finalizado correctamente")
print("")

###########################################################################

try:
    numero3 = numero1 / numero2
    print(f"Número 3: {numero3}")
    f = open('myfile.txt')
except ZeroDivisionError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
    print(type(err))
except Exception as err:
    print(err)
finally:
    print("Fin")
print("")


###########################################################################
# Utilizamos RAISE para generar una Error controlable mediante Try/Except #
###########################################################################

numero = "32"

try:
    if (type(numero) is not int):
        raise Exception("La variable no es númerica")
except Exception as ex:
    print(ex)
#######################################################################
# Requerimientos funcionales:
#
#   -> Visualizar la media de opión
#   -> Visualizar el número total de encuentas
#   -> El resultado se muestra al escribit FIN
#   -> El valor de opión es entre 0 y 10
#   -> Visualizar el promedio por edades Menor 18; 18 y 55; mayor 55
#######################################################################
# Utilizando listas de Python
#######################################################################

opinion = []

while (True):
    try:
        valor = input("Satisfación de 1 a 10: ")
        if (valor.lower() == "fin"):
            break

        edad = int(input("Escribe tu edad: "))

        if (valor.isalpha()):
            print(f"El valor {valor} no es valido.")
            print("")
        elif (int(valor) < 1 or int(valor) > 10):
            print(f"El valor {valor} no es valido.")
            print("")
        else:
            opinion.append([int(valor), edad])
    except Exception as err:
        print(f"Error: {err}")
        print("")

print("")
print(f">> Número de Encuestados: {len(opinion)}")

omas55 = list(map(lambda x: x[0], filter(lambda x: x[1] > 55, opinion)))
o18y55 = list(map(lambda x: x[0], filter(lambda x: x[1] <= 55 and x[1] >= 18, opinion)))
omen18 = list(map(lambda x: x[0], filter(lambda x: x[1] < 18, opinion)))
otodas = list(map(lambda x: x[0], opinion))

print(f">> Satisfación Media mayores 55 años: {sum(omas55) / len(omas55)}")
print(f">> Satisfación Media: {sum(otodas) / len(otodas)}")
print("")
print(f">> Satisfación Media entre 18 y 55 años: {sum(o18y55) / len(o18y55)}")
print(f">> Satisfación Media menores de 18 años: {sum(omen18) / len(omen18)}")
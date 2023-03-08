#######################################################################
# Requerimientos funcionales:
#   
#   -> Visualizar la media de opión 
#   -> Visualizar el número total de encuentas
#   -> El resultado se muestra al escribit FIN
#   -> El valor de opión es entre 0 y 10
#######################################################################
# Utilizando listas de Python
#######################################################################

opinion = []

while (True):
    try:
        valor = input("Satisfación de 1 a 10: ")
        
        if (valor.lower() == "fin"): 
            break
        elif(valor.isalpha()):
            print(f"El valor {valor} no es valido.")
            print("")
        elif(int(valor) < 1 or int(valor) > 10):
            print(f"El valor {valor} no es valido.")
            print("")
        else:        
            opinion.append(int(valor))
    except Exception as err:        
        print(f"Error: {err}")
        print("")

print("")
print(f">> Número de Encuestados: {len(opinion)}")
print(f">> Satisfación Media: {sum(opinion) / len(opinion)}")
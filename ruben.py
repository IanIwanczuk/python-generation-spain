def Calcular(lista):
    lista = OrderList(lista)

    try:
        lista[0] = int(lista[0])
        lista[1] = int(lista[1])

        if (lista[2] not in operadores):
            print("Operador no encontrado.")
        else:
            if (lista[2] == "+"):
                return lista[0] + lista[1]
            elif (lista[2] == "-"):
                return lista[0] - lista[1]
            elif (lista[2] == "*"):
                return lista[0] * lista[1]
            elif (lista[2] == "/"):
                return lista[0] / lista[1]
    except:
        print("Exvepcion")


def OrderList(lista):
    listaOrdenada = [0, 0, 0]

    for i, s in enumerate(lista):
        try:
            v = float(s)
            #listaOrdenada[i] == v  -> Error utilizar ==
            listaOrdenada[i] = v
        except:
            listaOrdenada[2] = s

    return listaOrdenada

lista = []

operadores = ["+", "-", "*", "/"]

n1 = input("Introduce primer valor: ")
n2 = input("Introduce segundo valor: ")
op = input("Introduce tercer valor: ")

lista.append(n1)
lista.append(n2)
lista.append(op)

print(Calcular(lista))

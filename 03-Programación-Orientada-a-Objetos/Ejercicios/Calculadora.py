#######################################################################
# Requerimientos funcionales:
#
#   -> Una función retorna el calculo solicitado sobre dos números
#
#      Posición 0: un número
#      Posición 1: un número
#      Posición 2: un texto con la operación a realizar -> sum, res, div, mul
#######################################################################
def Calcular(*arg):
    if len(arg) != 3:
        return ("Argumentos no validos")

    try:
        n1 = int(arg[0])
        n2 = int(arg[1])

        if str(arg[2]).lower() == "sum":
            return (n1 + n2)
        elif str(arg[2]).lower() == "res":
            return (n1 - n2)
        elif str(arg[2]).lower() == "mul":
            return (n1 * n2)
        elif str(arg[2]).lower() == "div":
            return (n1 / n2)
        else:
            return "Operativa no valida"

    except Exception as err:
        return f"Error: {err}"


print(Calcular(10, 25, "sum"))
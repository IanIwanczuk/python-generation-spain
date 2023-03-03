#######################################################################
# Requerimientos funcionales:
#
#   -> Calcular la velocidad en km/h
#   -> La información la tenemos en metros y minutos
#   -> Mostrar la velocidad en km/h y si es alta, baja o moderada
#   -> Alta por encima de 75km/h; Baja por debajo de 30km/h; el resto moderada
#######################################################################

try:
    kms = int(input("Distancia recorrida en metros: ")) / 1000
    hours = int(input("Tiempo empleado en minutos: ")) / 60
    vel = kms / hours
    
    if(vel > 75):
        print(f"Velocidad Alta: {vel} km/h")
    elif (vel < 30):
        print(f"Velocidad Moderada: {vel} km/h")
    else:
        print(f"Velocidad Baja: {vel} km/h")
except Exception as err:
    print(f"Error: {err}")
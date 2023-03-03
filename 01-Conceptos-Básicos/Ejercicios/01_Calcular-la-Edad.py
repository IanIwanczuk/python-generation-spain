#######################################################################
# Requerimientos funcionales:
#
#   -> Calcular la edad
#   -> Mostrar si es mayor de edad
#   -> Si no es mayor de edad, mostrar los años que le faltan
#######################################################################
from datetime import datetime

str = input("Fecha de nacimiento dd-mm-aaaa: ")

try:
    fn = datetime.strptime(str, "%d-%m-%Y").date()
    years = datetime.now().year - fn.year
    print(f"Tienes {years} años.")
    if(years < 18): 
        print(f"Te faltan {18 - years} para ser mayor de edad.")
except Exception as err:
    print(f"Error: {err}")
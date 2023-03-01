#####################################################################
# Trabajando con fechas - Zonas Horarias                            #
#####################################################################
#                                                                   #
#  Requiere instalar el módulo PYZT: pip install pytz               #
#                                                                   #
#####################################################################

from datetime import datetime

import pytz

# Mostrar las zonas horarias disponibles
print(pytz.all_timezones)
print("")

# Mostrar la fecha actual
dt = datetime.now()
print(f"Fecha Local: {dt}")
print(f"Zona Hoararia: {dt.tzinfo}")
print("")

# Mostrar la fecha actual en la zona horario de Asia/Tokyo
dtTokio = dt.now(pytz.timezone("Asia/Tokyo"))
print(f"Fecha Tokyo: {dtTokio}")
print(f"Zona Hoararia: {dtTokio.tzinfo}")
print("")

# Mostrar otras zonas horarias
print("Fecha Ushuaia:", datetime.now(pytz.timezone("America/Argentina/Ushuaia")))
print("Fecha Madrid:", datetime.now(pytz.timezone("Europe/Madrid")))
print("Fecha Alaska:", datetime.now(pytz.timezone("US/Alaska")))
print("Fecha UTC:", datetime.now(pytz.timezone("UTC")))

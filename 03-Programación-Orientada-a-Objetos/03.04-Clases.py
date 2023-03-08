#####################################################################
# Clases                                                            #
#####################################################################
#                                                                   #
#   Sintaxis: class [nombre de la clase]:                           #
#                                                                   #
#   Ejemplos:                                                       #
#       class Alumno:                                               #
#                                                                   #
#####################################################################

from datetime import datetime

class Alumno:
    """Comentarios de uso de la clase"""
    # Variables o propiedades de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    # Función constructura que se ejecuta al crear (instaciar) el objeto
    # self, una variable que representa al mismo objeto
    def __init__(self, nombre, apellido1, apellido2 = "") -> None:
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2

    # Otras funciones del objeto

    def getNombreCompleto(self) -> str:
        return f"{self.Apellido1} {self.Apellido2}, {self.Nombre}"
    
    def setFechaNacimiento(self, fecha) -> bool:
        try:
            if(len(fecha) == 10):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()

            return True
        except:
            return False
        
    def getEdad(self) -> int:
        if (self.FechaNacimiento == None):
            return -1
        else:
            return datetime.now().year - self.FechaNacimiento.year


# Creamos un objeto (instaciamos un objeto) ejecutando la función constructora
alumno = Alumno("Borja", "Cabeza", "Rozas")
alumno2 = Alumno("Ana", "Sánchez")

# Mostramos el contenido de de las variables del objetos
print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")


# Ejecutamos las funciones del objeto

# Ejecutamos las funciones del objeto e ignaramos el valor retornado
alumno.setFechaNacimiento("11-09-95")

# Ejecutamos una función del objeto y mostramos el valor retornado
print(f"Me llamo: {alumno.getNombreCompleto()}")

# Ejecutamos una función del objeto y almacenamos el valor retornado en una variable
resultado = alumno.setFechaNacimiento("11-09-99")
if(resultado == True):
    print("Fecha de nacimiento asignada correctamente.")
else:
    print("Error al asignar la fecha de nacimiento")

# Ejecutamos una función del objeto y utilizamos el valor retornado en una sentencia IF
if (alumno.setFechaNacimiento("11-09-1989") == True):
    print("Fecha de nacimiento asignada correctamente.")
    print(alumno.getEdad())
else:
    print("Error al asignar la fecha de nacimiento")
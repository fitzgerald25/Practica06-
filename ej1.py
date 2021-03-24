#Crear una clase Persona que tenga como atributos el "cedula, nombre, apellido y la edad 
# (definir las propiedades para poder acceder a dichos atributos)". Definir como responsabilidad
# una cuncion para mostrar ó imprimir. Crear una segunda clase Profesor que herede de la clase Persona. 
# Añadir un atributo sueldo ( y su propiedad) y en la función para imprimir su sueldo. Definir un objeto de la clase
# Persona y llamar a sus funciones y propiedades. También crear un objeto de la clase Profesor y llamar a sus funciones y propiedades.

class Persona:
    def inicializar(self):
        self.Cedula = "402-4563452-0"
        self.Nombre = "Gerald"
        self.Apellido = "Bautista"
        self.Ed = "18"
    
    def mostrar(self):
        print(self.Cedula)
        print(self.Nombre)
        print(self.Apellido)
        print(self.Ed)

class Profesor(Persona):
    def sueldo(self):
        self.Sueldo = 25000

    def imprimir(self):
        print("sueldo: ", self.Sueldo)

objpersona = Persona()
objpersona.inicializar()
objpersona.mostrar()
print("---------------------------------")
objprofesor = Profesor()
objprofesor.inicializar()
objprofesor.mostrar()
objprofesor.sueldo()
objprofesor.imprimir()
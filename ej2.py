#Crear una clase Contacto. Esta clase deberá tener los atributos "nombre, apellidos, telefono y direccion". 
#También deberá tener una función "SetContacto"  con los parámetros que permita cambiar el valor de los atributos.
#También tendrá una función "Saludar", que escribirá en pantalla "Hola, soy " seguido de sus datos. Crear también una
#clase llamada ProbarContacto. Esta clase deberá contener sólo la función principal, que creará dos objetos de tipo Contacto, 
#les asignará los datos del contacto y les pedirá que saluden.

class Contacto:
    def __init__(self):
        self.Nombre = ""
        self.Apellido = ""
        self.Telefono = ""
        self.Direccion = ""
        
    def SetContacto(self, Nom, Ape, Tel, Direc):
        self.Nombre = Nom
        self.Apellido = Ape
        self.Telefono = Tel
        self.Direccion = Direc
    def Saludar(self):
        print("Hola, Soy", self.Nombre, self.Apellido)
        print("Mi Telefono es:", self.Telefono, "Y mi direccion", self.Direccion)
        

class ProbarContacto:
    def Main(self):
        self.objcontacto = Contacto()
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.telefono = input("Telefono: ")
        self.direccion = input("Direccion: ")
        self.objcontacto.SetContacto(self.nombre, self.apellido, self.telefono, self.direccion)
        print("-----------------------")
        self.objcontacto2 = self.objcontacto.Saludar()


probar = ProbarContacto()
probar.Main()
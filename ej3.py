#Crear tres clases ClaseA, ClaseB, ClaseC que ClaseB herede de ClaseA 
# y ClaseC herede de ClaseB. Definir un constructor a cada clase que muestre
#  un mensaje. Luego definir un objeto de la clase ClaseC.

class ClaseA:
    def mostrarA(self):
        print("HOLA, SOY LA CLASE A")



class ClaseB(ClaseA):
    def MostrarB(self):
        print("HOLA, SOY LA CLASE B")



class ClaseC(ClaseB):
    def MostrarC(self):
        print("HOLA,, SOY LA CLASE C")


objclasec = ClaseC()
objclasec.mostrarA()
objclasec.MostrarB()
objclasec.MostrarC()
#Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma. Usando funciones.

lista =[]

def CargarLista():
    for x in range(10):
        numero = int(input("ESCRIBA UN NUMERO"))
        lista.append(numero)

def MostrarLista():
    print(lista)


CargarLista()
MostrarLista()
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("La lista esta vacia.")
            return

        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente


        actual.siguiente = nuevo
        

        print("None")



Lista1 = ListaEnlazada()


Lista1.insertar_inicio(10)
Lista1.insertar_inicio(15)
Lista1.insertar_inicio(6)
print(Lista1.cabeza.dato)  # Imprime 10
print(Lista1.cabeza.siguiente.dato)  # Imprime 15
print(Lista1.cabeza.siguiente.siguiente.dato)  # Imprime 6

Lista1.mostrar()





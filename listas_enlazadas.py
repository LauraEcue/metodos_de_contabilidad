class Nodo:
    def __init__ (self,data):
        self.data = data
        self.Next = None

class LE:
    def __init__(self):
        self.head = None


    def Adicionar (self, data):
        Nuevo = Nodo(data)
        Nuevo.Next = self.head
        self.head = None

L = LE ()


L.Adicionar(10)
L.Adicionar(20)

L.Adicionar(30)
print(L.head.data)







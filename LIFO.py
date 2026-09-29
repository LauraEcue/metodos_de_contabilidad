class LIFO:
    def __init__(self):
        self.Items = []


    def Push (self,Dato):
        self.Items.append(Dato)

    def Pop (self):
        if self.Empty ():
            return self.Items.pop()

    def Empty (self) -> bool:
        return len(self.Items) == 0

    def Peek (self):
        return None if self.Empty() else self.Items[-1]

    def Size (self):
        return(len(self.Items))


Historial=LIFO()
Historial.Push("yahoo")
Historial.Peek()
Historial.Pop()
Historial.Empty()
    
        


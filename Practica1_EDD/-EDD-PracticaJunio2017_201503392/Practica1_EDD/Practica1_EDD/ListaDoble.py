import Nodo
N = Nodo

class ListaDoble:
    """description of class"""
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def DameVacio(self):
        if self.primero==None:
            return True
        else:
            return False

    def InsertarPrimero(self,elemento):
        nuevo = N.Nodo(elemento)
        if self.DameVacio()==True:
            self.primero=self.ultimo=nuevo
        else:
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
    def InsertarUltimo(self,elemento):
        nuevo= N.Nodo(elemento)
        if self.DameVacio():
            self.primero=self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            self.ultimo=nuevo
    def EliminarPrimero(self):
        if self.DameVacio()==True:
            print("La lista se encuentra vacia, no se pueden eliminar elementos.")
        elif self.primero==self.ultimo:
            self.primero=None
            self.ultimo=None
            print("Elemento eliminado, la lista se encuentra vacia.")
        else:
            temp=self.primero
            self.primero=self.primero.siguiente
            self.primero.anterior=None
            temp=None
            print("Elemento eliminado.")
    def EliminarUltimo(self):
        if self.DameVacio()==True:
            print("La lista se encuentra vacia, no se pueden eliminar elementos.")
        elif self.primero==self.ultimo:
            self.primero=None
            self.ultimo=None
            print("Elemento eliminado, la lista se encuentra vacia.")
        else:
            temp=self.ultimo
            self.ultimo=self.ultimo.anterior
            self.ultimo.siguiente=None
            temp=None
            print("Elemento eliminado.")
    def MostrarPrimeroUltimo(self):
        if self.DameVacio()==True:
            print("Lista vacia.")
        else:
            recorrer=True
            temp=self.primero
            while (recorrer):
                print(temp.DameValor())
                if temp==self.ultimo:
                    recorrer=False
                else:
                    temp=temp.siguiente
    def MostrarUltimoPrimero(self):
        if self.DameVacio()==True:
            print("Lista vacia.")
        else:
            recorrer=True
            temp= self.ultimo
            while (recorrer):
                print(temp.DameValor())
                if temp==self.primero:
                    recorrer=False
                else:
                    temp=temp.anterior
    
    
    
            

    
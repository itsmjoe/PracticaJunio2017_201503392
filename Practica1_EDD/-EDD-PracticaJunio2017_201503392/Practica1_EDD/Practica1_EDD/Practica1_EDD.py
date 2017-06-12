#import ListaDoble
import os
from xml.etree import ElementTree
#import numpy as np
ArchivoCargado=False
class Principal:
    
   def Menu(self):
        salida=True
        entrada=0
        while(salida==True):
            print("*---------------------*Menu Principal*------------------*")
            print ("1. Crear usuario.\n"+"2. Ingresar al sistema. \n"+"3. Salir del programa.")
            entrada = input("Ingrese una opcion: ")
            if entrada=="3":
                salida=False
                print("Hasta luego!")
                raise SystemExit
            elif entrada=="2":
                F.IngresarSistema()
                #print("22")
            elif entrada=="1":
             F.CrearUsuario()
            else:
                print("Ingrese una opcion valida!")


class Funciones:
       Matriz1=object
       NombreUsuario=""
       def CrearUsuario(self):
         Usuario = input("Ingrese nombre de usuario: ")
         Password = input("Ingrese contrasena: ")
         if self.ExisteUsuario(Usuario)==False:    #------------------ Crear usuario
             usuarios.InsertarPrimero(Usuario,Password)
             #passwords.InsertarPrimero(Password)
             #usuarios.MostrarPrimeroUltimo()
             #usuarios.MostrarUltimoPrimero()
         else:
             print("Ya exite el usuario.")
         #usuarios.MostrarPrimero()
       def IngresarSistema(self):
        Usuario = input("Ingrese usuario: ")
        Password = input("Ingrese contrasena: ") 
        if self.ValidarSesion(Usuario,Password):
            print("Bienvenido "+ Usuario)
            NombreUsuario=Usuario
            #Operaciones=Cola()
            self.MenuUsuairo(Usuario)
        else:
            print("Usuario o contrasena invalida, por favor intente de nuevo.")

       def MenuUsuairo(self,nombre):    #---------------------------- Menu usuario -------------------------------------------------------------
          salida=True
          ArchivoCargado=False 
          #Operaciones=Cola()
          while (salida==True):
              print("*-------------------------------*Menu de Usuario*------------------------------*")
              print(" 1. Leer archivo \n 2. Resolver operaciones \n 3. Operar matriz \n 4. Mostrar usuarios \n 5. Mostrar cola \n 6. Cerrar sesion")
              entrada = input("Ingrese una opcion: ")
             
              if entrada=="6":
                  salida=False
                  #Operaciones=Cola()
                  ArchivoCargado=False
                  print("Hasta luego!")
              elif entrada=="1":
                ruta=input("Ingrese ruta de archivo: ")
                self.LeerArchivo(ruta,nombre)
                #usuarios.InsertarColaDeUsuario(nombre,Operaciones)               
                ArchivoCargado=True
              elif entrada=="3":
                  if ArchivoCargado==True:    
                    self.MenuOperarMatriz()
                  else: 
                      print("Debe cargar un archivo primero.")
              elif entrada=="4":
                  usuarios.MostrarPrimeroUltimo()
                  usuarios.MostrarUltimoPrimero()
              elif entrada=="5":
                  #Operaciones.MostrarCola()
                  temp=usuarios.DameUsuario(nombre)                  
                  if temp.cola!=None:
                    te=temp.DameCola()
                    te.MostrarCola()
                  else:
                      print("La cola no ha sido creada.")
              elif entrada=="2":
                if ArchivoCargado==True: 
                    self.MenuResolverOperaciones(nombre)
                else:
                    print("Debe cargar un archivo primero.")
              else:
                  print("Ingrese una opcion valida!")

       def MenuOperarMatriz(self):
           salir=True
           while (salir==True):
              print("*-------------------------------* Menu de Usuario -> Operar Matriz *------------------------------*")
              print(" 1. Ingresar dato \n 2. Operar transpuesta \n 3. Mostrar matriz original \n 4. Mostrar matriz transpuesta \n 5. Regresar")
              entrada = input("Ingrese una opcion: ")
              if entrada=="5":
                  print("Hasta luego!")
                  salir=False
              elif entrada=="1":
                  posx=input("Ingrese columna: ")
                  posy=input("Ingrese fila: ")
                  valor=input("Ingrese valor: ")
                  self.IngresarValorEnMatriz(posx,posy,valor)
              elif entrada=="2":
                  """operar transpuesta"""
              elif entrada=="3":
                  """mostrar matriz original""" #------------------------------------------- Mostrar matriz original ------------------
                  Matriz.MostrarMatriz()
              elif entrada=="4":
                  """mostrar transpuesta"""

              else:
                  print("Ingrese una opcion valida!")

       def IngresarValorEnMatriz(self,posx,posy,valor): #-------------------- Meter datos a la matriz ---------------------------
           Matriz1=Matriz
           Matriz.MeterValor(int(posx),int(posy),valor)

       def MenuResolverOperaciones(self,nombre):
           salida=True
          
           while (salida==True):
               print("*-------------------------------*Menu de Usuario -> Resolver operaciones *------------------------------*")
               print("1. Operar siguiente \n2. Regresar")
               entrada = input("Ingrese una opcion: ")
               if entrada=="2":
                   salida=False
               elif entrada=="1":
                   "operar"
                   self.OperarSiguiene(nombre)
               else:
                   print("Ingrese una opcion valida!")

       def OperarSiguiene(self,nombre): #------------------------------------- Operaciones -------------------------------------
           #Operaciones.MostrarCola()
           operatemp=usuarios.DameUsuario(nombre)
           op=operatemp.DameCola()
           if op.ColaVacia()==False:
            operacion=op.desencolar().split()
            self.InsertarOperacionAPila(operacion)
           else:
               print("La cola esta vacia")
           #return 


       def InsertarOperacionAPila(self,elemento):
           for e in elemento:
               Pila1.Push(e)
           temp=Pila1.primero
           #Pila1.MostrarPila()
           while(temp!=None):
               PilaOperacion.Push(Pila1.Pop())
               temp=temp.siguiente
           #Pila1.MostrarPila()
           #PilaOperacion.MostrarPila()
           #return self.Operar(PilaOperacion) ------>  Esta sirve
           self.Operando(PilaOperacion)



       def Operando(self, pila): #------------------------------------------------- Operando -------------------------------------
           res=0
           if pila.EstadoPila()==1:
                print("Resultado: " +str(pila.Pop()) )
                #return pila.Pop()
           elif pila.EstadoPila()==2:
               pilaux=Pila()
               temp = pila.primero
               salir=True
               while(salir==True):
                  if str(temp.DameValor()) in "+-*":
                      pila.Pop()
                      simb=temp.DameValor()
                      var2=float(pilaux.Pop())
                      var1=float(pilaux.Pop())
                      salir=False
                  else:
                      pilaux.Push(pila.Pop())
                      temp=temp.siguiente

               print(str(var1) + " " + str(var2) + " "+str(simb))
               if simb=="+":
                   res=var1+var2
                   print(str(var1) + " + " + str(var2) + " = "+str(res))
                   while (pilaux.EstadoPila()!=0):
                       pila.Push(pilaux.Pop())
                   pila.Push(res)
               elif simb=="-":
                   res=var1-var2
                   print(str(var1) + " - " + str(var2) + " = "+str(res))
                   while (pilaux.EstadoPila()!=0):
                       pila.Push(pilaux.Pop())
                   pila.Push(res)
               elif simb=="*":
                   res=var1*var2
                   print(str(var1) + " * " + str(var2) + " = "+str(res))
                   while (pilaux.EstadoPila()!=0):
                       pila.Push(pilaux.Pop())
                   pila.Push(res)
               self.Operando(pila)



       def Operar(self, pila):  #------------------------------------------------- Operar ----------------------------------------
           res=0
           if pila.EstadoPila()==1:
                print("Resultado: " +str(pila.Pop()) )
                #return pila.Pop()
           elif pila.EstadoPila()==2:
           
               temp = pila.primero
               salir=True
               while(salir==True):
                   var1=float(pila.Pop())
                   var2=float(pila.Pop())
                   simb=(pila.Pop())
                   if simb in "+-*":
                       salir=False  
                   else:
                        raise ValueError("Simbolo no valido.")

               print(str(var1) + " " + str(var2) + " "+str(simb))
               if simb=="+":
                   res=var1+var2
                   print(str(var1) + " + " + str(var2) + " = "+str(res))
                   pila.Push(res)
               elif simb=="-":
                   res=var1-var2
                   print(str(var1) + " - " + str(var2) + " = "+str(res))
                   pila.Push(res)
               elif simb=="*":
                   res=var1*var2
                   print(str(var1) + " * " + str(var2) + " = "+str(res))
                   pila.Push(res)
               self.Operar(pila)


       def LeerArchivo(self,ruta,nombreuser):  #--------------------------------- Leer archivo  ------------------------
           print("--------------------------->Leyendo archivo...")
           nombrearchivo=ruta
           nombre=os.path.abspath(os.path.join('',nombrearchivo))
           #Operaciones=Cola()

           dom=ElementTree.parse(nombre)

           matriz= dom.findall('matriz')
           operacion = dom.findall('operaciones')
           ope= dom.findall('operacion')
           for ma in matriz:
              x=ma.find('x')
              y=ma.find('y')             
              print("x: "+x.text +", y: "+y.text)
              self.CrearMatriz(x.text,y.text)
           temporal=usuarios.DameUsuario(nombreuser)
           if temporal.cola==None:
              temporal.cola=Cola()
           #te=temporal.DameCola()
           for op in operacion:
               opera = op.findall('operacion')
               for o in opera:
                temporal.cola.encolar((o.text).strip())
                print("operacion: " +(o.text).strip())
           #temporal.cola=Operaciones
           #Operaciones= Cola()

       def CrearMatriz(self,x,y):  #--------------------------------------Crear matriz -----------------------------------------------
           #Matriz= MatrizOrtogonal()
           Matriz.CrearMatriz(int(x),int(y))
           Matriz1=Matriz
           #Matriz.CrearMatriz()

       def ValidarSesion(self,user,pasw):
           """"""
           if usuarios.primero==None:
               print("No se ha creado ningun usuario.")
           else:
                temp=usuarios.primero
                recorrer=True
                while (recorrer): 
                    if temp.DameValor()==user and temp.DamePassw()==pasw:
                        return True
                    else:
                        if temp!=usuarios.ultimo:
                            temp=temp.siguiente
                        elif temp==usuarios.ultimo:
                            return False
                        else:
                            recorrer=False
    

       def ExisteUsuario(self, usuario):
          if usuarios.primero==None:    
                   return False          
          else:
           temp=usuarios.primero
           recorrer=True
           while (recorrer):         
                   if temp.DameValor()==usuario:
                       return True           
                   else:
                       if temp!=usuarios.ultimo:  
                        temp=temp.siguiente
                       elif temp==usuarios.ultimo:
                           return False
                       else:
                        recorrer=False 



class ListaMatriz: #---------------------------------------------- Lista Matriz ********************************************************
    def __init__(self,ancho):
        self.primero=None
        for x in range(ancho):
            self.Insertar()

    def DamePrimero(self):
        return self.primero
    
    def CrearFilaMatriz(self,ancho):
       pass
        

    def MatrizVacia(self):
        if self.primero!=None:
            return False
        else:
            return True

    def MostrarListaMatriz(self):
        temp=self.primero
        fila="|"
        #print("------------------------ Fila Matriz -----------")
        while(temp!=None):
            fila=fila+ " "+ str(temp.DameValor())
            temp=temp.DameDerecha()

        print(fila+ " |")

    def Insertar(self):
        if self.MatrizVacia()==True:
            self.primero= NodoMatriz(0)
        else:
            nuevo= NodoMatriz(0)
            nuevo.MeterDerecha(self.primero)
            self.primero=nuevo

                        
class MatrizOrtogonal: #--------------------------------------------- Matriz Ortogonal ------------------------------------------------
    
    ultima=ListaMatriz(0)
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.X=0
        self.Y=0

        
                #print(ultima)           
   

    def DameAncho(self):
        return self.X

    def DameAlto(self):
        return self.Y

    def DameValor(self,posx,posy):
        #if (self.X<posx and self.Y)
        cabeza=self.ultima.DamePrimero()
        while(cabeza.DameArriba()!=None):
            cabeza=cabeza.DameArriba()

        for i in range(posy):
            cabeza=cabeza.DameAbajo()

        for j in range(posx):
            cabeza=cabeza.DameDerecha()

        return cabeza.DameValor()

    def MeterValor(self,posx,posy,valor):
        if (posx<self.X  and posy<self.Y):
           cabeza=self.ultima.DamePrimero()
           while(cabeza.DameArriba()!=None):
               cabeza=cabeza.DameArriba()

           for i in range(posy):
               cabeza=cabeza.DameAbajo()
           
           for j in range(posx):
               cabeza=cabeza.DameDerecha()

           cabeza.MeterValor(valor)
    



    def CrearMatriz(self,ancho,alto):
        self.X=ancho
        self.Y=alto
        if (self.X>0 and self.Y>0):
            ultima=ListaMatriz(self.X)

            for i in range(self.Y):
                aux=ListaMatriz(self.X)
                recorre=aux.DamePrimero()
                recorreUlitima=ultima.DamePrimero()

                while(recorreUlitima!=None and recorre!=None):
                    recorre.MeterArriba(recorreUlitima)
                    recorreUlitima.MeterAbajo(recorre)
                    recorreUlitima=recorreUlitima.DameDerecha()
                    recorre = recorre.DameDerecha()

                ultima=aux
                ultima.MostrarListaMatriz()
        ultima.primero=NodoMatriz(0)

    def MostrarMatriz(self):
        if (self.X>0 and self.Y>0):
            text=""
            for i in range(self.Y):
                text+="|"
                for j in range(self.X):
                    print(str(self.DameValor(i+1,j+1)))
                    text+=" "+ str(self.DameValor(i,j))

                text+="|"
            text+="|"

            print(text)
    #ultima= ListaMatriz(0)


class NodoMatriz: #----------------------------------------------------- Nodo Matriz ******************************************------
    def __init__(self,elemento):
        self.arriba=None
        self.abajo=None
        self.izquierda=None
        self.derecha=None
        self.elemento=elemento

    def DameValor(self):
        return self.elemento

    def MeterValor(self,dato):
        self.elemento=dato

    def DameArriba(self):
        return self.arriba

    def DameAbajo(self):
        return self.abajo

    def DameIzquierda(self):
        return self.izquierda

    def DameDerecha(self):
        return self.derecha

    def MeterArriba(self,arriba):
        self.arriba=arriba

    def MeterAbajo(self,abajo):
        self.abajo=abajo

    def MeterDerecha(self,derecha):
        self.derecha=derecha

    def MeterIzquierda(self,izquierda):
        self.izquierda=izquierda


    
class Cola: #---------------------------------------------------- Cola ---------------------------------------------
    def __init__(self):
        self.ultimo=None
        self.primero=None

    def encolar(self, elemento):
        nuevo=Nodo(elemento,0)
        if self.ultimo:
            self.ultimo.siguiente=nuevo
            self.ultimo=nuevo
        else: 
            self.primero=nuevo
            self.ultimo=nuevo

    def ColaVacia(self):
        if self.primero!=None:
            return False
        else:
            return True


    def desencolar(self):
        #if (self.ColaVacia==False):
            if self.primero==self.ultimo:
                tempo=self.primero.DameValor()
                self.primero=self.ultimo=None
                print("Desencolado: "+tempo)
                return tempo
            elif self.primero:
                tempo=self.primero.DameValor()
                self.primero=self.primero.siguiente
        
                print("Desencolado: "+tempo)
                return tempo
            else:
                    print("La cola esta vacia.")
        #else:
           # print("La cola esta vacia.")

    def MostrarCola(self):
        #if self.primero.cola!=None:
            if self.primero==None:
                print("La cola esta vacia.")
            else:
                recorrer=True
                temp=self.primero
                i=0
                print("----------------> Mostrar cola de operaciones")
                while (recorrer):
                    print("indice "+str(i) +": "+temp.DameValor())
                    i+=1
                    if temp==self.ultimo:
                        recorrer=False
                    else:
                        temp=temp.siguiente
        #else:
            #print("La cola esta vacia")

class Pila:  #---------------------------------------------------- Pila ---------------------------------------------
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def Push(self,elemento):
        nuevo=Nodo(elemento,0)
        if self.primero==None:
            self.primero=self.ultimo=nuevo 
            #self.ultimo.siguiente=None
        else:
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo

    def EstadoPila(self):
        if self.primero==None:
            return 0
        elif self.primero==self.ultimo:
            return 1
        else: 
            return 2
    
    def Pop(self):
        """"""
        if self.primero==None:
            print("La pila esta vacia.")
        elif self.primero==self.ultimo:
            temp=self.primero
            self.primero=self.ultimo=None
            return temp.DameValor()
        else:
            temp=self.primero
            self.primero=self.primero.siguiente
            return temp.DameValor()
    def MostrarPila(self):
        if self.primero==None:
            print("Lista vacia.")
        else:
            recorrer=True
            temp=self.primero
            print("----------------> Mostrar pila")
            while (recorrer):
                print(temp.DameValor())
                if temp==self.ultimo:
                    recorrer=False
                else:
                    temp=temp.siguiente
        

class Nodo:  #------------------------------------------------------------ Nodo -------------------------------------------
    """description of class"""
    def __init__(self, elemento,pasw):
        self.elemento=elemento
        self.pasw=pasw
        self.siguiente=None
        self.anterior=None
        self.cola=None

    def DameCola(self):
        return self.cola  
        

    def DamePassw(self):
        return self.pasw
    def DameValor(self):
        return self.elemento

class ListaCircularDoble: # ------------------------------------------- Lista doble ----------------------------------
    
    """description of class"""
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def Vacio(self):
        if self.primero==None:
            return True
        else:
            return False

    def InsertarColaDeUsuario(self,nombre,cola):
        temp=self.primero
        recorrer=True
        while(recorrer):
            if temp.DameValor()==nombre:
                #print("llegue")
                temp.cola=cola
                recorrer=False
            else:
                if temp==self.ultimo:
                    recorrer=False
                else:
                    temp=temp.siguiente
        #print("Cola creada")
       
    def DameUsuario(self,nombre):
        temp=self.primero
        recorrer=True
        while(recorrer):
            if temp.DameValor()==nombre:
                return temp
            else:
                if temp==self.ultimo:
                    recorrer=False
                else:
                    temp=temp.siguiente

        #************************ C:\Users\Mynor Joel Molina\Document\prueba.xml


    def MostrarPrimero(self):
        print(self.primero.DameValor())

    def InsertarPrimero(self,elemento,pasw):
        nuevo = Nodo(elemento,pasw)        
        if self.Vacio()==True:
            self.primero=self.ultimo=nuevo
            self.Enlazar()
        else:
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
            self.Enlazar()

    def InsertarUltimo(self,elemento,pasw):
        nuevo= N.Nodo(elemento,pasw)
        if self.Vacio():
            self.primero=self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            self.ultimo=nuevo
    def EliminarPrimero(self):
        if self.Vacio()==True:
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
        if self.Vacio()==True:
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
        if self.Vacio()==True:
            print("Lista vacia.")
        else:
            texto=""
            recorrer=True
            temp=self.primero
            print("----------------> Ultimo a primero")
            while (recorrer):
                #print(temp.DameValor())
                
                if self.primero==self.ultimo:
                    print(temp.DameValor())
                    recorrer=False
                elif temp==self.ultimo:
                    #print(temp.siguiente.DameValor())
                    texto=texto+" -> " + temp.DameValor() 
                    texto=texto+" -> " + temp.siguiente.DameValor()   
                    recorrer=False
                else:
                    if temp==self.primero:
                        texto=temp.DameValor()
                    else:
                        texto=texto+" -> " + temp.DameValor()
                    temp=temp.siguiente
            print(texto)

    def Enlazar(self):
        if self.primero!=None:
            self.ultimo.siguiente=self.primero
            self.primero.anterior=self.ultimo
    

    def MostrarUltimoPrimero(self):
        if self.Vacio()==True:
            print("Lista vacia.")
        else:
            recorrer=True
            texto=""
            temp= self.ultimo
            print("----------------> Primero a ultimo")
            while (recorrer):
                #print(temp.DameValor())
                if self.primero==self.ultimo:
                    print(temp.DameValor())
                    recorrer=False
                elif temp==self.primero:
                    #print(temp.anterior.DameValor())
                    texto=texto+" -> "+temp.DameValor()
                    texto=texto+" -> "+temp.anterior.DameValor()
                    recorrer=False
                else:
                    if temp==self.ultimo:
                        texto=temp.DameValor()
                    else:
                        texto=texto +" -> "+temp.DameValor()
                    temp=temp.anterior
            print(texto)




F = Funciones()
P = Principal()
usuarios= ListaCircularDoble()
passwords= ListaCircularDoble()
Matriz= MatrizOrtogonal()
Operaciones=Cola()
PilaOperacion=Pila()
Pila1=Pila()
P.Menu()
  


   
    

    



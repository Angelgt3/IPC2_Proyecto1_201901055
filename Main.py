from xml.dom import minidom

class Nodo(object):
    def __init__(self,datos):
        self.datos = datos
        self.siguiente = None

class Lista_Circular(object):
    def __init__(self):
        self.cabeza=None

    def esta_vacia(self):
        if self.cabeza is None:
            return True
        else:
            return False

    def tamaño(self):
        temp=self.cabeza
        cont=0
        while temp is not None:
            cont+=1
            if temp.siguiente == self.cabeza:
                break
            else:
                temp=temp.siguiente
        return cont
    
    def agregar_ultimo(self,datos):
        nodo=Nodo(datos)
        if Lista.esta_vacia():
            self.cabeza = nodo
            nodo.siguiente=self.cabeza
        else:
            temp=self.cabeza
            while temp.siguiente is not self.cabeza:
                temp=temp.siguiente
            temp.siguiente=nodo
            nodo.siguiente =self.cabeza

    def recorrer(self):
        if self.esta_vacia():
            return print("Esta vacia")
        temp=self.cabeza
        Lista.son_iguales(temp.datos)
        while temp.siguiente is not self.cabeza:
            temp=temp.siguiente
            Lista.son_iguales(temp.datos)
            #print(temp.datos)
    
    def eliminar(self, Datos):
        if Datos==self.cabeza.datos:
            temp=self.cabeza
            while temp.siguiente is not self.cabeza:
                temp= temp.siguiente
            temp.siguiente =self.cabeza.siguiente
            self.cabeza=self.cabeza.siguiente
        else:
            temp =self.cabeza
            temp2=None
            while temp.datos is not Datos:
                temp2 =temp
                temp=temp.siguiente
            temp2.siguiente =temp.siguiente

    
    def son_iguales(self,Datos):
        nueva_matriz=list()
        valor=True
        for a in range(int(Datos[1])):
            temp_list=list()
            for b in range(int(Datos[2])):
                if Datos[4][a]==Datos[4][b] and not (Datos[3][a]==Datos[3][b]):
                    for c in range(int(Datos[2])):
                        numero1=int(Datos[3][a][c])
                        numero2=int(Datos[3][b][c])
                        total=numero1+numero2
                        temp_list.append(total)
                    valor2=True
                    valor=False
                    for d in nueva_matriz:
                        if d == temp_list:
                            valor2=False
                    if valor2:
                        nueva_matriz.append(temp_list)
                        break
            if valor:
                nueva_matriz.append(Datos[3][a])
            valor=True


        print(nueva_matriz)

       

Lista=Lista_Circular()
Nueva=Lista_Circular()

class Menu:
    @staticmethod
    def mostrar():
        print("<><><><><><><><><><><><><><><><><><><><><><><><> \nEliga una opcion: \n 1. Cargar Archivo \n 2. Procesar Archivo \n 3. Escribir Archivo de Salida \n 4. Mostrar Datos del Estudiante \n 5. Generar Grafica \n 6. Salida \n<><><><><><><><><><><><><><><><><><><><><><><><>")
        opcion = int(input())
        return opcion

    @staticmethod
    def menu():
        op = Menu.mostrar()
        if op == 1:
           Procesos.cargar_Archivo()
           Menu.menu()
        elif op == 2:
            Procesos.procesar()
        elif op == 3:
            print("escribir")
        elif op == 4:
            print("mostrar datos estudiante") 
        elif op == 5:
            print("generar grafica")
        elif op == 6:
            print("Exit")
        else:
            Menu.menu()

class Procesos:

    @staticmethod
    def procesar():
        print("recorriendo la lista")
        Lista.recorrer()

    @staticmethod
    def cargar_Archivo():
        #try:
        ruta=str(input("Ingrese la ruta del archivo"))
        archivo = minidom.parse(ruta)
        Procesos.Leer_Archivo(archivo)
        #except:
        #    print("No se pudo abrir el documento")
        #    Menu.menu()
        
    @staticmethod
    def Leer_Archivo(archivo):
        Datos=list()
        #name = archivo.getElementsByTagName("dato")[0]
        #print(name.firstChild.data)
        matrices=archivo.getElementsByTagName("matriz")
        p=1
        for matriz in matrices:
            nombre=matriz.getAttribute("nombre")
            n=matriz.getAttribute("n")
            m=matriz.getAttribute("m")
            z=int(m)*int(n)
            Matriz=list()
            print("Creando Matriz no."+str(p))
            for uno in range(int(m)):
                temp=list()
                for dos in range(int(n)):
                    temp.append(0)
                Matriz.append(temp)
            datoss=matriz.getElementsByTagName("dato")
            print("Guardando los datos de la matriz no."+str(p))
            for dato in datoss:
                x = dato.getAttribute("x")
                y = dato.getAttribute("y")
                try: 
                    Matriz[int(y)-1][int(x)-1]=dato.firstChild.data
                except:
                    continue
            Matriz2=list()
            for uno in range(int(m)):
                temp=list()
                for dos in range(int(n)):
                    if int(Matriz[uno][dos]) is not 0:
                        temp.append(1)
                    else:
                        temp.append(0)
                Matriz2.append(temp)
            Datos.append(nombre)
            Datos.append(n)
            Datos.append(m)
            Datos.append(Matriz)
            Datos.append(Matriz2)
            temp=list()
            e=0
            for b in range(len(Datos)):
                temp.append(Datos[e])
                e+=1
            for a in range(len(Datos)):
                Datos.pop()
            print(Datos)
            print(temp)
            Lista.agregar_ultimo(temp)
            #print(Matriz)
            #print(Matriz2)
            #print(Lista.tamaño())

        

    



    
  




Menu().menu()

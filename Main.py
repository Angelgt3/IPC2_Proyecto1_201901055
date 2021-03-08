from xml.dom import minidom
import xml.etree.ElementTree as ET 



class Nodo_lista_matriz(object):
    def __init__(self,datos):
        self.datos=datos
        self.siguiente=None
    
class Lista_matriz():
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
        
        nodo=Nodo_lista_matriz(Nodo_Matriz(datos))
        if self.esta_vacia():
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
        #print(temp.datos.datos)
        #print(temp.datos.datos)
        while temp.siguiente is not self.cabeza:
            temp=temp.siguiente
            print(temp.datos.datos)
            

    def modificar(self,x,dato):
        temp=self.cabeza
        for a in range(int(x)):
            temp=temp.siguiente
        temp.datos.datos=dato      
        print()

class Nodo_Matriz(object):
    def __init__(self,datos):
        self.datos=datos
        self.siguiente=None
        self.anterior=None
        self.arriba=None
        self.abajo=None

class Matriz():
    def __init__(self):
        self.cabeza=None

    def crear(self, n, m):
        nodo=Nodo_Matriz(0)
        for a in range(int(n)):
            for b in range(int(m)):
                nodo.siguiente=None
                nodo.abajo=None
                if b==0:
                    nodo.anterior=None
                    if self.cabeza==None:
                        self.cabeza=nodo
                    temp=nodo
                else:
                    nodo.anterior=temp
                    temp.siguiente=nodo
                    temp=nodo
                if a==0:
                    nodo.arriba=None
                    temp=nodo
                else:
                    nodo.arriba=r
                    r.abajo=nodo.siguiente
            r=self.cabeza
            while r.abajo is not None:
                r=r.abajo

    def recorrer(self):
        #print("entro")
        if self.cabeza is not None:
            nodo=self.cabeza
            while nodo is not None:
                temp=nodo
                while temp is not None:
                    print(temp.datos)
                    temp=temp.siguiente
                nodo=nodo.siguiente
        else:
            print("lista vacia")


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
        if self.esta_vacia():
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
        self.son_iguales(temp.datos)
        while temp.siguiente is not self.cabeza:
            temp=temp.siguiente
            self.son_iguales(temp.datos)
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

    def buscar(self,posicion):
        if self.esta_vacia():
            return("la lista esta vacia")
        if posicion==0:
            return self.cabeza.datos
        elif posicion >0:
            temp=self.cabeza
            for a in range(int(posicion)):
                temp=temp.siguiente
            return temp.datos

    def son_iguales(self,Datos):
        matriz_temp=[]
        matriz_temp=Datos
        nueva_matriz=[]
        valor=False
        ñ=0
        a=0
        while len(matriz_temp[4])>0:
            coordenadas=[]
            temp_list=[]
            valor=True
            for b in range(int(matriz_temp[1])):
                try:
                    dato_evaluando=matriz_temp[4][a]
                    if matriz_temp[4][a]==matriz_temp[4][b]:
                        coordenadas.append(b)
                        valor=False
                except:
                    pass
            if valor:
                coordenadas.append(a)
            nueva_matriz2=[]
            for c in range(int(matriz_temp[2])):
                total=0
                for d in range(len(coordenadas)):
                    try:
                        total+=int(matriz_temp[3][coordenadas[d]][c])
                    except:
                        pass
                temp_list.append(total)
            
            for t in range(len(coordenadas)):
                try:
                    num=matriz_temp[4].index(dato_evaluando)
                    matriz_temp[4].pop(num)
                    matriz_temp[3].pop(num)
                    ñ+=1
                except:
                    pass
            
            valor=False
            nueva_matriz.append(temp_list)
        m=0
        n=0
        for i in nueva_matriz:
            m+=1
            n=0
            for j in i:
                n+=1
               
        nueva_matriz2.append(nueva_matriz)
        nueva_matriz2.append(n)
        nueva_matriz2.append(m)
        Nueva.agregar_ultimo(nueva_matriz2)




class Procesos:
    
    @staticmethod
    def hacer_matriz(n,m):
        Matriz1.crear(n,m)
        Matriz2.crear(n,m)
        Matriz1.recorrer()
        
        n=input("numero 1: ")
        m=input("numero 2: ")
        x= input("x: ")
        posicion=input("donde we : ")
        for a in range(int(n)):
            for b in range(int(m)):
                lis_matriz1.agregar_ultimo("02")
                lis_matriz2.agregar_ultimo("10")
        lis_matriz1.modificar(int(posicion),int(x))
        lis_matriz2.recorrer()
        
    @staticmethod
    def procesar():
        print("recorriendo la lista")
        Lista.recorrer()

    @staticmethod
    def cargar_Archivo():
        try:
            ruta=str(input("Ingrese la ruta del archivo"))
            archivo = minidom.parse(ruta)
            Procesos.Leer_Archivo(archivo)
        except:
            print("No se pudo abrir el documento")
            Menu.menu()
        
    @staticmethod
    def Leer_Archivo(archivo):
        matrices=archivo.getElementsByTagName("matriz")
        Datos=[]
        p=1
        for matriz in matrices:
            nombre=matriz.getAttribute("nombre")
            n=matriz.getAttribute("n")
            m=matriz.getAttribute("m")
            z=int(m)*int(n)
            Matriz=[]
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
                    Matriz[int(x)-1][int(y)-1]=dato.firstChild.data
                except:
                    continue
            Matriz2=[]
            for uno in range(int(m)):
                temp=[]
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
            temp=[]
            e=0
            for b in range(len(Datos)):
                temp.append(Datos[e])
                e+=1
            for a in range(len(Datos)):
                Datos.pop()
            Lista.agregar_ultimo(temp)
            p+=1
         

    @staticmethod
    def escribir():
        print("estoy escribiendo")
        matrices=ET.Element("Matrices")
        matrices.text="\n\t"
        for a in range(int(Nueva.tamaño())):
            matriz =ET.SubElement(matrices,"Matriz", nombre=f"{Lista.buscar(a)[0]}", n=f"{Nueva.buscar(a)[1]}", m=f"{Nueva.buscar(a)[2]}" ,g="")
            matriz.text="\n\t\t"
            if a==int(Nueva.tamaño()-1):
                matriz.tail="\n"
            else: 
                matriz.tail="\n\t"
            for b in range(int(Nueva.buscar(a)[2])):
                for c in range(int(Nueva.buscar(a)[1])):
                    dato=ET.SubElement(matriz,"dato",x=f"{b}",y=f"{c}")
                    dato.text=str(Nueva.buscar(a)[0][b][c])
                    if b==int(Nueva.buscar(a)[2]-1) and c==int(Nueva.buscar(a)[1]-1):
                        dato.tail="\n\t"
                    else: 
                        dato.tail="\n\t\t"
        arbol = ET.ElementTree(matrices)
        arbol.write("Salida.xml")
    
    @staticmethod   
    def graficar(posicion):
    
        archivo=open('grafica.dot', 'w')
        contenido="digraph mapa{"
        x=f"""
matrices->{Lista.buscar(int(posicion))[0]}
{Lista.buscar(int(posicion))[0]}->"n={Lista.buscar(int(posicion))[1]}"
{Lista.buscar(int(posicion))[0]}->"m={Lista.buscar(int(posicion))[2]}"

            """
        contenido+=x
        x=""
        c=0
        abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','VV','WW','XX','YY','ZZ']
        for a in range(int(Lista.buscar(int(posicion))[1])):
            for b in range(int(Lista.buscar(int(posicion))[2])):
                x+=f"""
                {abc[c]}[label="{Lista.buscar(int(posicion))[3][a][b]}" style="filled" fillcolor="#92E192" shape="box"]
                """
                c+=1

        c=0
        for a in range(int(Lista.buscar(int(posicion))[1])):
            for b in range(int(Lista.buscar(int(posicion))[2])):
                if a==0:
                    x+=f"""
                    {Lista.buscar(int(posicion))[0]}->{abc[c]}
                    """
                else:
                    x+=f"""
                    {abc[c-int(Lista.buscar(int(posicion))[2])]}->{abc[c]}
                    """
                c+=1

        contenido+=x+"}"
        archivo.write(contenido)
        archivo.close()

    @staticmethod   
    def yo():
       print("<><><><><><><><><><><><><><><><><><><><><><><><> \nNombre: Angel Geovany Aragón Pérez\nCarnet: 201901055\nIntroduccion a la programacion y computacion 2 seccion 'A'\nIngenieria en Ciencias y Sistemas\n4to Semestre \n<><><><><><><><><><><><><><><><><><><><><><><><>")

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
            Menu.menu()
        elif op == 3:
            Procesos.escribir()
            Menu.menu()
        elif op == 4:
            Procesos.yo()
            input("Enter para continuar")
            Menu.menu()
        elif op == 5:
            try:
                a=input("ingrese la matriz que desea seleccionar")
                Procesos.graficar(int(a)-1)    
            except:
                print("Error:La matriz es muy grande")
            
        elif op == 6:
            print("Exit")
        else:
            Menu.menu()



Lista=Lista_Circular()
Nueva=Lista_Circular()
lis_matriz1=Lista_matriz()
lis_matriz2=Lista_matriz()
Matriz1=Matriz()
Matriz2=Matriz()

Menu().menu()

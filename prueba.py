#------NO CAMBIAR ---------
from autoHerramientas import *
#---------------------------
#puede cargar cualquier archivo cambiando este parametro
nombre_archivo = "Autos1"

#puede cambiar la forma de la lista entre:
#lista de diccionario -> tipo_lista = "diccionario"
#lista de listas -> tipo_lista = "lista"
tipo_lista = "diccionario"

lista_autos = obtenerAutos(nombre_archivo,tipo_lista)

#------------

#ejemplo Menu
#Puede copiar esto si estima conveniente

#ejemplo Menu
#Puede copiar esto si estima conveniente

from autoHerramientas import *

#Con esto puede llamar a cualquier funcion creada en prueba.py
from prueba import *

#lista de autos

def buscarpalabra():
    for n in lista_autos:
        if str(marca) in str(n["marca"]) or str(marca) in str(n["modelo"]):
            print (n["marca"], n["modelo"],  n["año"], n["patente"], n["color"])
            return(marca)
        
def filtro():
    if fil == "1":
        marca=str(input("Ingrese la marca del vehículo: "))
        for auto in lista_autos:
            if marca == auto["marca"]:
                print (auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
                     
    elif fil== "2":
        modelo=str(input("Ingrese el modelo del vehículo: "))
        for auto in lista_autos:
            if modelo == auto["modelo"]:
                print (auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
                
    elif fil == "3":
        año=str(input("Ingrese el año del vehículo a buscar: "))
        for auto in lista_autos:
            if año == auto["año"]:
                print(auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
                    
    elif fil == "4":
        patente=str(input("Ingrese la patente del vehículo a buscar: "))
        for auto in lista_autos:
            if patente == auto["patente"]:
                print(auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
    elif fil == "5":
        color=str(input("Ingrese el color vehículo a buscar: "))
        for auto in lista_autos:
            if color ==auto["color"]:
                print(auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])


lista_autos = obtenerAutos("Autos1")

def certificado():
    i=1
    for auto in lista_autos:
        print(i, auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
        i+=1

    i=1
    seleccion=int(input("Seleccione el numero del vehiculo que desea: \n"))
    for auto in lista_autos:
        if seleccion == i:
            print(f"{nombre_usuario} emite certificado que:")
            print(f"El vehiculo {auto['marca']}, modelo {auto['modelo']} con patente {auto['patente']}")
            print(f"De color {auto['color']}")
            print(f"Queda registrado oficialmente a la fecha de: {fecha_actual}")
            return(auto)
        i+=1
    

def buscar_rango_año():

    print("Escriba el rango de años que esta buscando")
    primer_año=int(input("Ingrese el año"))  
    segundo_año=int(input("Ingrese el año")) 
    for auto in lista_autos:
        if auto["año"]>=primer_año and auto["año"]<=segundo_año:
            print(auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"]) 
def escoger_auto():
    i=1
    for auto in lista_autos:
        print(i, auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
        i+=1

    i=1
    seleccion=int(input("Seleccione el numero del vehiculo que desea: \n"))
    for auto in lista_autos:
        if seleccion == i:
            
            return(auto)
        i+=1
def propietario():
    
    auto_escogido = escoger_auto()
    auto_escogido["propietario"] = nombre_usuario   
    print(auto_escogido["marca"], auto_escogido["modelo"],  auto_escogido["año"], auto_escogido["patente"], auto_escogido["color"], auto_escogido["propietario"])


nombre_usuario=str(input("Bienvenido a nuestro filtro de vehículos, Para iniciar, Ingrese su usuario: "))
fecha_actual=str(input("Ingrese la fecha en formato DD/MM/AA: "))
color_favorito = str(input("Ingrese su color favorito: "))
opciones_menu = [
    "Buscar por Marca/Menú",
    "Filtrar por otro parametro",
    "Emitir Certificado",
    "Buscar por patente",
    "Buscar por rango de años",
    "Buscar por color favorito",
    "Añadir propietario"
#agregar más opciones de forma similar
]
opciones_menu.append("Salir")


while (True):
    #Mostrar Menu
    for i, opcion in enumerate(opciones_menu):
        print(i+1,". ",opcion, sep="")

    #Seleccionar
    while (True):
        seleccion = input(">> ")
        if (validar_seleccion(seleccion,opciones_menu)):
            seleccion = int(seleccion)-1
            break
    
    #MOSTRAR OPCION --------------------
    print(opciones_menu[seleccion])

    #HACER ACCIONES ---------------------
    if (seleccion == 0):
        marca=str(input("Ingrese la Marca/Modelo del vehículo a buscar: "))
        buscarpalabra()
        pass

    if (seleccion == 1):
        #opcion 2
        fil=str(input("1.Marca \n2.Modelo \n3.Año \n4.Patente \n5.Color \n"))
        filtro()
        pass

    if (seleccion == 2):
        #opcion 3
        certificado()
        pass

    if (seleccion == 3):
        patente=str(input("Ingrese la patente del vehículo a buscar: "))
        for auto in lista_autos:
            if patente == auto["patente"]:
                print(auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
        #opcion 4
        pass

    if (seleccion == 4):
        buscar_rango_año()

    if (seleccion == 5):
        for auto in lista_autos:
            if color_favorito in auto["color"]:
                print(auto["marca"], auto["modelo"],  auto["año"], auto["patente"], auto["color"])
        
    if (seleccion == 6):
        
        propietario()
    if (seleccion == 7):
        exit()


        
        
        
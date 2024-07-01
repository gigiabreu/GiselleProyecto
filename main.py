from urllib.request import urlopen
import json
import random
from Equipo import Equipos
from Estadio import Estadios, Restaurante, Products
from Partido import Partidos
from Persona import Persona

#Borra los datos de los docs txt
def reinicio():
    open("equipos.txt", "w")
    open("estadios.txt", "w")
    open("partidos.txt", "w") 
    open("personas.txt", "w") 

#guarda los datos de las listas en los documentos txt
def guardar(equipos, estadios, partidos, personas):
    with open("equipos.txt", "w") as z:
        z.write(str([z.para_guardar() for z in equipos]))
    with open("estadios.txt", "w") as z:
        z.write(str([z.para_guardar() for z in estadios]))
    with open("partidos.txt", "w") as z:
        z.write(str([z.para_guardar() for z in partidos]))
    with open("personas.txt", "w") as z:
        z.write(str([z.para_guardar() for z in personas]))

#toma los datos de los archivos.txt o de la api y los coloca como objetos en listas
def cargar_data(equipos, estadios, partidos, personas):
    try:
       
        with open("equipos.txt", "r") as z: #encodig permite leer los acentos y evita que aparezcan simbolos raros
            datos = z.read()
        
        if 0==len(datos):     
            url = urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")

            data = json.loads(url.read())
            for dato in  data:
                equipo = Equipos(dato["id"], dato["code"], dato["name"], dato["group"])
                equipos.append(equipo)
            guardar_equipos=[z.para_guardar() for z in equipos]
            with open("equipos.txt", "w") as w:
                w.write(str(guardar_equipos))
        else:
            Q = eval(datos)
            for x in Q:
                new_equipo = Equipos(x["id"], x["code"], x["name"], x["group"])
                equipos.append(new_equipo)

    except FileNotFoundError:
            print("\nHubo un error.")
            print("\nNo se encontro el archivo.txt.\nequipos.txt no esta\n")
    


    try:
       
        with open("personas.txt", "r") as z: #encodig permite leer los acentos y evita que aparezcan simbolos raros
            datos = z.read()
        
        if len(datos) != 0:     
            
            Q = eval(datos)
            for x in Q:
                new_persona = Persona(x["nombre"], x["cedula"], x["edad"], x["partido_id"], x["entrada_tipo"], x["puesto"], x["codigo"], x["confirmacion"], x["compras"])
                personas.append(new_persona)

    except FileNotFoundError:
            print("\nHubo un error.")
            print("\nNo se encontro el archivo.txt.\nequipos.txt no esta\n")



    try:

        with open("estadios.txt", "r") as z: #encodig permite leer los acentos y evita que aparezcan simbolos raros
            datos = z.read()

        if 0==len(datos):      
            url = urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")

            data = json.loads(url.read())
            for dato in  data:
                rest = []
                for x in dato["restaurants"]:
                    productos =[]
                    for y in x["products"]:
                        prod = Products(y["name"], y["quantity"], y["price"], y["stock"], y["adicional"])
                        productos.append(prod)
                    rest.append(Restaurante(x["name"], productos))
                estadio = Estadios(dato["id"], dato["name"], dato["city"], dato["capacity"], rest, None)
                estadios.append(estadio)
            guardar_estadios=[z.para_guardar() for z in estadios]
            with open("estadios.txt", "w") as w:
                w.write(str(guardar_estadios))
        else:
            Q = eval(datos)
            for x in Q:
                rest = []
                for y in x["restaurantes"]:
                    productos =[]
                    for z in y["products"]:
                        prod = Products(z["name"], z["quantity"], z["price"], z["stock"], z["adicional"])
                        productos.append(prod)
                    rest.append(Restaurante(y["name"], productos))
                new_estadio = Estadios(x["id"], x["name"], x["city"], x["capacity"], rest, x["mapa"])
                estadios.append(new_estadio)
    except FileNotFoundError:
        print("\nHubo un error.")
        print("\nNo se encontro el archivo.txt.\nestadios.txt no esta\n")

    try:

        with open("partidos.txt", "r") as z: #encodig permite leer los acentos y evita que aparezcan simbolos raros
            datos = z.read()

        if 0==len(datos):      
            url = urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")

            data = json.loads(url.read())
            for dato in  data:
                for x in equipos:
                    if x.id == dato["home"]["id"]:
                        home = x
                    if x.id == dato["away"]["id"]:
                        away = x
                for x in estadios:
                    if x.id == dato["stadium_id"]:
                        entradas = x.mapa
                partido = Partidos(dato["id"], dato["number"], home, away, dato["date"], dato["group"], dato["stadium_id"],entradas)
                partidos.append(partido)
            guardar_partidos=[z.para_guardar() for z in partidos]
            with open("partidos.txt", "w") as w:
                w.write(str(guardar_partidos))
        else:
            Q = eval(datos)
            for x in Q:
                for y in equipos:
                    if y.id == x["home"]["id"]:
                        home = y
                    if y.id == x["away"]["id"]:
                        away = y
                new_partido = Partidos(x["id"], x["number"], home, away, x["date"], x["group"], x["stadium_id"], x["entradas"])
                partidos.append(new_partido)


    except FileNotFoundError:
        print("\nHubo un error.")
        print("\nNo se encontro el archivo.txt.\npartidos.txt no esta\n")

#busca los partidos dependiendo de lo indicado
def buscar_partido(equipos, partidos, buscar_pais=None, buscar_estadio=None, buscar_fecha=None):
    res = []
    for partido in partidos:
        if buscar_pais and partido.home.name != buscar_pais and partido.away.name != buscar_pais:
            
            continue
        if buscar_estadio and partido.stadium_id != buscar_estadio:
            continue
        if buscar_fecha and partido.date != buscar_fecha:
            continue
        res.append(partido)
        print(partido.mostrar())
    return res

#busca partidos por pais del equipo
def buscar_partidos_por_pais(equipos, partidos, pais):
    return buscar_partido(equipos, partidos, pais)
#busca partidos por estadio
def buscar_partidos_por_estadio(equipos, partidos, estadio_id):
    return buscar_partido(equipos, partidos, buscar_estadio=estadio_id)
#busca partidos por fecha
def buscar_partidos_por_fecha(equipos, partidos, fecha):
    return buscar_partido(equipos, partidos, buscar_fecha=fecha)

#menu de busqueda de partidos
def partidos_b(equipos, partidos):
     while True:
        print("1. Buscar partidos por pais")
        print("2. Buscar partidos por estadio")
        print("3. Buscar partidos por fecha")
        opa = int(input("Opcion: "))
        if opa == 1:
            for x in equipos:
                print(x.show())
            pais = input("Equipo pais: ")
            print()
            return buscar_partidos_por_pais(equipos, partidos, pais)
        elif opa == 2:
            for x in estadios:
                print(x.show())
            id = input("Estadio id: ")
            return buscar_partidos_por_estadio(equipos, partidos, id)
        elif opa == 3:
            for x in partidos:
                print(x.show())
            fecha = input("Fecha (yyyy-mm-dd): ")
            print()
            return buscar_partidos_por_fecha(equipos, partidos, fecha)
        else:
            print("Opcion invalida")
        print("")

#gestiona la compra de entradas
def Compra(equipos,estadios, partidos, personas):
    print("Comprar entradas")
    nom = input("Nombre: ")
    ced = input("Cedula: ")
    ed = int(input("Edad: "))
    list=[]
    for x in partidos:
        print(x.mostrar())
        print(x.puestos_disponibles())
        list.append(x.id)
    part = input("Partido id: ")
    while not part in list:
        part = input("Error, Partido id: ")
    for x in partidos:
        if x.id == part:
            seleccion = x
            for y in estadios:
                if y.id == x.stadium_id:
                    stad = y
    print("El estadio: ",stad.name, " tiene capacidad de: ",stad.capacity)  
    fila = input("seleccione la fila: ")
    while not int(fila) in range(1,stad.capacity[0]+1):
        fila = input("Error, seleccione la fila: ")
    columna = input("seleccione la columna: ")    
    while not int(columna) in range(1,stad.capacity[1]+1):
        columna = input("Error, seleccione la columna: ")
            
    puesto = [int(fila), int(columna)]
    #comprueba si el puesto ya esta ocupado
    while seleccion.comprobar_puesto(puesto):
        fila = input("seleccione la fila: ")
        while not int(fila) in range(1,stad.capacity[0]+1):
            fila = input("Error, seleccione la fila: ")
        columna = input("seleccione la columna: ")    
        while not int(columna) in range(1,stad.capacity[1]+1):
            columna = input("Error, seleccione la columna: ")
            
        puesto = [int(fila), int(columna)]
            
    tipo = input("Tipo de entrada que desea comprar\n1. General\n2. VIP\n>>: ")
    while tipo != "1" and tipo != "2":
        tipo = input("Opcion invalida\n1. General\n2. VIP\n>>: ")
    codigo = random.randint(100000, 999999)
    while codigo in [x.codigo for x in personas]:
        codigo = random.randint(100000, 999999)
    
    #crea el objeto persona para despues ser guardado al concretar la compra
    if tipo == "1":
        new = Persona(nom, ced, ed, part, puesto, "General", codigo, False)

    else:
        new = Persona(nom, ced, ed, part, puesto, "VIP", codigo, False)
    new.factura()

    if input("Confirmar (s/n): ") == "s": 
        seleccion.comprar_puesto(puesto)
        personas.append(new)
        print("Entrada comprada con exito")
        print("Su codigo es: ",new.codigo)
        print()
        guardar(equipos, estadios, partidos, personas)
    else:
        print("Entrada cancelada")

#confima la asistencia de la persona al partido
def asistencia(equipos, estadios, partidos, personas):
    codigo = int(input("Introduzca el Codigo: "))
    for x in personas:
        if x.codigo == codigo:
            if x.confirmacion == True:
                print("El boleto ya fue utilizado")
                break
            else:
                x.confirmar_asistencia()
                print("Asistencia confirmada")
                guardar(equipos, estadios, partidos, personas)
            break

#filtra los productos dependiendo de el usuario y su edad
def busqueda_productos(estadios, edad, partido):
    rest =[]
    productos = []
    #verifica si es menor de edad
    if edad >= 18:
        alcohol = True
    else:
        alcohol = False
    if partido == None:

        for x in estadios:
            for y in x.restaurantes:
                print(y.name)
                rest.append(y.name)
    
    else:
        for x in estadios:
            if partido.stadium_id == x.id:
                for y in x.restaurantes:
                    print(y.name)
                    rest.append(y.name)
    if len(rest) == 0:
        print("No hay restaurantes en el estadio")
        return
    nombreR = input("Introduce el nombre del restaurante: ")
    while not nombreR in rest:
        nombreR = input("Error, Introduce el nombre del restaurante: ")
    for x in estadios:
        for y in x.restaurantes:
            if y.name == nombreR:
                restaurante = y
    print("Seleccione una opcion de busqueda")
    print("1. Buscar por nombre")
    print("2. Buscar por tipo")
    print("3. Buscar por rango de precio")
    op = input(">> ")
    #si es menor de edad no apareceran bebidas alcoholicas
    if op == "1":
        nombre = input("Introduce el nombre del producto: ")
        for x in restaurante.products:
            if x.name == nombre:
                if alcohol == True or x.adicional != "alcoholic":
                    print(x.to_dict())
                    productos.append(x)
    elif op == "2":
        tip = input("Introduce el tipo de producto:\n1. Bebidas\n2. Comida\n>> ")
        if tip == "1":
            if alcohol == True:
                tipo = input("Introduce el tipo de Bebida:\n1. Bebidas alcoholicas\n2. Bebidas no alcoholicas\n>> ")
                if tipo == "1":
                    tipo = "alcoholic"
                else:
                    tipo = "non-alcoholic"
            else:
                tipo = "non-alcoholic"
        else:
            tipo = input("Introduce el tipo de comida:\n1. Comida de paquete\n2. Comida de plato\n>> ")
            if tipo == "1":
                tipo = "package"
            else:
                tipo = "plate"

        for x in restaurante.products:
            if x.adicional == tipo:
                print(x.to_dict())
                productos.append(x)


    elif op == "3":
        min = float(input("Introduce el minimo: "))
        max = float(input("Introduce el maximo: "))
        for x in restaurante.products:
            if float(x.price) >= min and float(x.price) <= max:
                if alcohol == True or x.adicional != "alcoholic":
                    print(x.to_dict())
                    productos.append(x)
                
    print("los precios no incluyen iva")
    return productos

#verifica si es un numero perfecto
def is_perfect_number(num):
	suma = 0
	for i in range(1,num):
		if (num % (i) == 0):
			suma += (i)
	if num == suma:
		return True
	else:
		return False
 
#menu de estadisticas
def mostrar_estadisticas(equipos, estadios, partidos, personas):
    print("1. promedio gasto en un partido")
    print("2. Mostrar tabla con la asistencia a los partidos de mejor a peor")
    print("3. partido con mayor asistencia")
    print("4. partido con mayor boletos vendidos")
    print("5. Top 3 productos más vendidos en el restaurante")
    print("6. Top 3 de clientes (clientes que más compraron boletos)")
    op = input(">> ")
    #muestra el promedio de gasto en un partido seleccionado
    if op == "1":
        part = buscar_partido(equipos, partidos)
        idPar = input("Introduce el id del partido: ")
        for x in part:
            if x.id == idPar:
                part = x
        promedio = []
        for x in personas:
            if x.id_partido == part.id:
                promedio.append(x.precio_final)
        if len(promedio) == 0:
            print("No hay asistentes")
        else:
            print("el promedio de gasto en el partido es de ", sum(promedio) / len(promedio))
    #muestra los datos de la asistencia de los partidos del mejor al peor
    elif op == "2":
        people = []
        for x in partidos:
            partidos = {"partido": x, "personas": [], "ventas": 0, "asistencias": 0}
            people.append(partidos)

        for x in people:
            for y in personas:
                if y.partido_id == x["partido"].id:
                    x["personas"].append(y)
                    x["ventas"] += 1
                    if y.confirmacion == True:
                        x["asistencias"] += 1
        
        people.sort(key=lambda x: x["asistencias"], reverse=True)

        for x in people:
            print(x["partido"].to_dict())
            if x["asistencias"] != 0:
                print(f"asistencias: {x['asistencias']}, ventas: {x['ventas']}, porcentaje de asistencias: {x['asistencias']/x['ventas']*100}%")
            else:
                print("asistencias: 0, ventas: 0, porcentaje de asistencias: 0%")
    #muestra el partido con mas asistencia
    elif op == "3":
        lista = []
        for x in partidos:
            part ={"partido": x.to_dict(), "asistencias": 0}
            for y in personas:
                if y.id_partido == x.id:
                    if y.confirmacion == True:
                        part["asistencias"] += 1
            lista.append(part)
        print(max(lista, key=lambda x: x["asistencias"]))
    #muestra el partido con mas boletos vendidos
    elif op == "4":
        lista = []
        for x in partidos:
            lista.append({"partido": x.to_dict(), "boletos": x.boletos_vendidos()})
        print(max(lista, key=lambda x: x["boletos"]))
    #muestra el top 3 productos mas vendidos
    elif op == "5":
        prod = []
        for y in estadios:
            for z in y.restaurantes:
                for w in z.products:
                    prod.append({"nombre": w.name, "vendidos": 0})
        for x in personas:
            if x.compra != None:
                for y in x.compras:
                    for z in prod:
                        if y == z["nombre"]:
                            z["vendidos"] += 1
        print(sorted(prod, key=lambda x: x["vendidos"], reverse=True)[:3])
    #muestra el top 3 de clientes que mas compraron boletos
    elif op == "6":
        lista = []
        for x in personas:
            existe =False
            for y in lista:
                if x.cedula == y["cedula"]:
                    y["boletos"] += 1
                    existe =True
            if existe == False:
                lista.append({"cedula": x.cedula, "boletos": 1})
        print(sorted(lista, key=lambda x: x["boletos"], reverse=True)[:3])





            



#inicia el menu principal
def menu(equipos, estadios, partidos, personas):
    while True:
        print()
        print("1. Buscar partidos")
        print("2. comprar entradas")
        print("3. Confirmar asistencia")
        print("4. Restaurantes y productos")
        print("5. Compra en restaurante")
        print("6. Ver estadisticas")
        print("7. reiniciar datos")
        print("8. Salir")
        op = input("Opcion: ")
        print()
        if op == "1":
            partidos_b(equipos, partidos)
        elif op == "2":
            Compra(equipos, estadios, partidos, personas)
        elif op == "3":
            asistencia(equipos, estadios, partidos, personas)
        elif op == "4":
            busqueda_productos(estadios, 18, None)
        #gestiona la compra de productos
        elif op == "5":
            codigo = int(input("Introduzca el Codigo: "))
            exciste = False
            for x in personas:
                if x.codigo == codigo:
                    pers = x
                    exciste =True
            
            if exciste == True:
                print(f"bienvenido, {pers.nombre}")
                for x in partidos:
                    if pers.partido_id == x.id:
                        partido = x
                products = busqueda_productos(estadios, pers.edad, partido)
                prodlist = []
                for x in products:
                    prodlist.append(x.name)
                    compra = []
                while True:
                    for x in products:
                        print(x.to_dict())
                    nomP = input("Introduce el nombre del producto: ")
                    while not nomP in prodlist:
                        nomP = input("Error, Introduce el nombre del producto: ")
                    
                    for x in products:
                        if x.name == nomP:
                            compra.append(x)

                    cont = input("Desea comprar otro?\n1. Si\n2. No\n>> ")  
                    if cont == "2":
                        descuento = 0
                        monto_total = 0
                        if is_perfect_number(int(pers.cedula)):
                            descuento = 0.15
                        for x in compra:
                            print(f"{x.name}: {x.price}")
                            monto_total += float(x.price) - (float(x.price) * descuento)
                        print(f"Descuento: {descuento}")
                        print(f"Total a pagar: {monto_total}")
                        pasar = input("Desea confirmar?\n1. Si\n2. No\n>> ")
                        if pasar == "1":
                            for x in compra:
                                x.stock -= 1
                                pers.compras.append(x.name)
                        guardar(equipos, estadios, partidos, personas)
                        break

        elif op == "6":
            mostrar_estadisticas(equipos, estadios, partidos, personas)
        elif op == "7":
            reinicio()
            print("Se reinicio la base de datos")
        elif op == "8":
            break
        else:
            print("Opcion invalida")


equipos = []
estadios = []
partidos = []
personas = []

#inicia el programa
cargar_data(equipos, estadios, partidos, personas)
#inicia el menu
menu(equipos, estadios, partidos, personas)
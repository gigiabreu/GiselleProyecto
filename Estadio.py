
class Products:
    def __init__(self, name, quantity, price, stock,adicional):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional
    #muestra todo como string
    def show(self):
        return (self.name, self.quantity, self.price, self.stock, self.adicional)
    #muestra todo como diccionario
    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "stock": self.stock,
            "adicional": self.adicional
        }
class Restaurante():
    def __init__(self, name, products):
        self.name = name
        self.products = products
    #muestra todo como string
    def show(self):
        productos = []
        for x in self.products:
            productos.append(x.show())
        return (self.name, productos)
    #muestra todo como diccionario
    def to_dict(self):
        productos = []
        for x in self.products:
            productos.append(x.to_dict())

        return {
            "name": self.name,
            "products": productos
        }

class Estadios:
    def __init__(self, id, name, city, capacity, restaurantes, mapa):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurantes = restaurantes
        if mapa == None:
            self.mapa = self.crear_mapa()
        else:
            self.mapa = mapa

    #muestra todo como string     
    def show(self):
        return (self.id, self.name, self.capacity)
    #muestra todo como diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "capacity": self.capacity,
            "restaurantes": self.restaurantes
        }
    
    #crea el mapa del estadio
    def crear_mapa(self):
        #crea el mapa de los puestos
        filas=self.capacity[0]
        columnas=self.capacity[1]
        mapa = []
        for y in range(filas):
            aux = []
            for x in range(columnas):
                aux.append(False)
            mapa.append(aux)
        return mapa

    #imprime el mapa
    def imprimir_mapa(self):
        #muestra el mapa con los puestos ocupados con una "x"

        print("* "*len(self.mapa[0])+ " ESTADIO "+"* "*len(self.mapa[0]))
        print("\n")

        nums = "    "
        for i,x in enumerate(self.mapa[0]):
            if i >8:
                nums+=str(i+1)+"| "
            else:
                nums+=str(i+1)+" | "

        print(nums)

        for i,x in enumerate(self.mapa):
        
            if i>8:

                auxiliar= str(i+1)
            else:
                auxiliar= str(i+1)+" "
            for y in x:
                if y ==True: #detecta que puestos estan ocupados y lo muestra
                    auxiliar+="| X "
                else:
                    auxiliar+="|   "

            print("   "+"-"*len(self.mapa[0]*4))
            print(auxiliar)
            
    #pasa los datos correctamente para guardar
    def para_guardar(self):
        rest = []
        for x in self.restaurantes:
            rest.append(x.to_dict())
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "capacity": self.capacity,
            "restaurantes": rest,
            "mapa": self.mapa
        }
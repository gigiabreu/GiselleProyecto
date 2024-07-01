from Equipo import Equipos


class Partidos(Equipos):
    def __init__(self, id, number, home, away, date, group, stadium_id, entradas):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium_id = stadium_id
        self.entradas = entradas
    
    #muestra todo como string
    def show(self):
        return self.id, self.number, self.home.show(), self.away.show(), self.date, self.group, self.stadium_id
    
    #muestra todo como diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "home": self.home.to_dict(),
            "away": self.away.to_dict(),
            "date": self.date,
            "group": self.group,
            "stadium_id": self.stadium_id
        }
    #muestra los datos ordenados
    def mostrar(self):
        return f"Partido: id: {self.id}\n Equipo local: {self.home.show()}\n Equipo visitante: {self.away.show()}\n Fecha: {self.date}\n Grupo: {self.group}\n Estadio: {self.stadium_id}\n"
    #muestra el numero de entradas disponibles
    def puestos_disponibles(self):
        i=0
        for x in self.entradas:
            for y in x:
                if y == False:
                    i+=1
        print(f"Entradas disponibles: {i}")

    #muestra el numero de boletos vendidos
    def boletos_vendidos(self):
        i=0
        for x in self.entradas:
            for y in x:
                if y == True:
                    i+=1
        return i
    
    #comprueba si los puestos estan ocupados
    def comprobar_puesto(self, puesto):
        return self.entradas[puesto[0]-1][puesto[1]-1]
    

    #marca puesto como true
    def comprar_puesto(self, puesto):
        self.entradas[puesto[0]-1][puesto[1]-1] = True

    #pasa los datos correctamente para guardar
    def para_guardar(self):
        return {
            "id": self.id,
            "number": self.number,
            "home": self.home.to_dict(),
            "away": self.away.to_dict(),
            "date": self.date,
            "group": self.group,
            "stadium_id": self.stadium_id,
            "entradas": self.entradas
        }
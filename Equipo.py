
class Equipos:
    def __init__(self, id, code, name, group):
        self.id = id
        self.code = code
        self.name = name
        self.group = group
    #muestra todo como string
    def show(self):
        return (self.id, self.code, self.name, self.group)
    
    #muestra todo como diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "group": self.group
        }
    
    #pasa los datos correctamente para guardar
    def para_guardar(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "group": self.group
        }
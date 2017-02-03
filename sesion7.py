#Clases, Herencia
class Animal():
    ruido = "ladra"
    size = "grande"
    color = "cafe"
    ojos = "azules"
    raza = "husky"

    def get_color(self):
        return self.color

    def has_ruido(self):
        return self.ruido

# perro = Animal()
# print perro.has_ruido()
# print perro.raza

class Perro(Animal):
    nombre = "Kyo"
    # color = "gris"
    #
    # def get_color(self):
    #     return self.color
perro = Perro()
print perro.nombre
print perro.get_color()
print perro.ojos

d = Perro() # Se convierte en una instancia de la clase (un objeto)
print type(d)
print d.name
print d.get_color()
d.color = 'blanco'
print d.get_color()

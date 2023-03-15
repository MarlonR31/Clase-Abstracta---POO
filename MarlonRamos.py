# Programa
from abc import ABC, abstractmethod
#Clase padre abstracta
class Bebidas(ABC):

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def salud(self):
        pass
Alumno = "Marlon Stiven Ramos Vasquez"

#Clase 1 (Hija)
class Gaseosas(Bebidas):
    def __init__(self, nombre, tipoBebida, saludBebida):
        self.nombre = nombre
        self.tipoBebida = tipoBebida
        self.saludBebida = saludBebida
        pass

    def tipo(self):
        return "- La {} es tipo de bebida {}".format(self.nombre, self.tipoBebida)
    
    def salud(self):
        print("\nVamos a verificar las bebidas...")
        return "- La bebida de {} es {} para la salud de las personas".format(self.nombre, self.saludBebida)

#Clase 2 (Hija)
class Alcoholicas(Bebidas):
    def __init__(self, nombre, tipoBebida, saludBebida):
        self.nombre = nombre
        self.tipoBebida = tipoBebida
        self.saludBebida = saludBebida
        pass

    def tipo(self):
        return "- La {} es tipo de bebida {}".format(self.nombre, self.tipoBebida)
    
    def salud(self):
        return "- La bebida de {} es {} para la salud de las personas".format(self.nombre, self.saludBebida)
#Clase 3 (Hija)
class Naturales(Bebidas):
    def __init__(self, nombre, tipoBebida, saludBebida):
        self.nombre = nombre
        self.tipoBebida = tipoBebida
        self.saludBebida = saludBebida
        pass

    def tipo(self):
        return "- La {} es tipo de bebida {}".format(self.nombre, self.tipoBebida)
    
    def salud(self):
        return "- La bebida de {} es {} para la salud de las personas".format(self.nombre, self.saludBebida)

#Creacion de los Objetos
bebida1 = Gaseosas("Coca Cola", "Gaseosa", "Mala")
bebida2 = Alcoholicas("Vodka", "Alcoholica", "Mala")
bebida3 = Naturales("Agua", "Natural", "Buena")

print("\nClasificacion de Bedidas segun su tipo...")
print(bebida1.tipo())
print(bebida2.tipo())
print(bebida3.tipo())

print(bebida1.salud())
print(bebida2.salud())
print(bebida3.salud())

print("Alumno: " + Alumno)
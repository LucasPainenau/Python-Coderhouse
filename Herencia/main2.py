

class Clase1:

    def imprimir(self):
        print("Imprimiendo de la clase 1")

class Clase2:

    def imprimir(self):
        print("Imprimiendo de la clase 2")

    def guardar(self):
        print("Guardando")


class Clase3(Clase2, Clase1):
    pass



clase = Clase3()

# clase.imprimir()
# clase.guardar()


help(Clase1)

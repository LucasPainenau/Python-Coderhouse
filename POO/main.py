# Definicion de la clase
class Perro:

    #Atributos de clase
    nacionalidad = "Argentina"
    numero_de_patas = 4


    # Constructor de clase
    def __init__(self, nombre, raza, edad=1):
        

        #Atributos de instancia
        # Decorar objeto
        self.nombre = nombre
        self.edad = edad
        self.raza = raza


    # Metodos propios
    def ladrar(self):
        print("guau"*5+"!")

    def avanzar(self, cant_pasos):
        print(f"soy {self.nombre} y he avanzado {cant_pasos} pasos")


# Instanciar un objeto (crear)
perrito = Perro("Roco", "Labrador")
perrito2 = Perro("Theo", "Caniche", 3)


# print("ID de perrito: ", id(perrito) )
# print("Type de perrito: ", type(perrito) )

print( perrito.nombre, perrito.raza, perrito.edad )
print( perrito2.nombre, perrito2.raza, perrito2.edad )

perrito.avanzar(3)
perrito2.avanzar(50)
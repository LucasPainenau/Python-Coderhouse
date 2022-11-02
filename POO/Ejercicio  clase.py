class Persona:

    # Atributos de clase
    nacionalidad = "Argentina"
    idioma = "Español"

    # Contructor
    def __init__(self, nombre, apellido, edad):

        # Atributos de instancia
        self.nombre = nombre
        self.apeliido = apellido
        self.edad = edad


    # Metodos
    def saludar(self, destinatario):
        print(f"Hola! Como estas {destinatario}? Soy {self.nombre}")

    def dormir(self):
        print("zZ"*4)

    def __str__(self):
        #Debe retornar SI O SI un string
        return f"Persona: Nombre: {self.nombre}; Apellido: {self.apeliido}"


# Instanciar objetos
persona1 = Persona("Leonel", "Gareis", 24)
persona2 = Persona("Pepe", "Barrionuevo", 32)


# Ejecutar los metodos de instancia
persona1.dormir()
persona2.saludar("Leonel")


# Acceder y actualizar atributo
persona2.nombre = "Pedro"
persona2.saludar("Leonel")

print(persona1)

class Pais:

    def capital(self):
        pass

    def lenguaje(self):
        pass

class Argentina(Pais):

    def capital(self):
        print("Mendoza")

    def lenguaje(self):
        print("Español")

class Uruguay(Pais):

    def capital(self):
        print("Montevideo")

    def lenguaje(self):
        print("Español")

class Brasil(Pais):

    def lenguaje(self):
        print("Portugues")



arg = Argentina()
urg = Uruguay()
br = Brasil()

for pais in [arg, urg, br]:
    print("Clase: ", type(pais).__name__ )
    pais.capital()
    print("\n")

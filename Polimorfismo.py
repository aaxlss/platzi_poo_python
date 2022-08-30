class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("Perona caminando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Ciclista avanza en su bici")


def main():
    persona = Persona('persona 1')
    persona.avanza()

    ciclista = Ciclista('persona 2')
    ciclista.avanza() 

if __name__ == '__main__':
    main()
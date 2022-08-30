from lib2to3.pytree import Node


class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self._estado = 'en_reposo'#attribute privado inicialisado con valir en default
        self._motor = Motor(cilindros=4)#attribute privado iniciando la instancia de un objecto Motor

    def acelerar(self, tipo='despacio'):
        
        if tipo=='rapida':
            self._motor.inyecta_gasolina(10)#llamando el metodo de la clase motor
        else:
            self._motor.inyecta_gasolina(3)

        self._estado='en_movimiento'#cambiando el valor de la variable privada

    

class Motor:
    
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantida):
        pass
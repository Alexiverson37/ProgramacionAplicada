from Camara import Camara
class Dispositivo:
    def __init__(self, id, nombre, resolucion, marca, modelo):
        super().__init__(id, nombre, resolucion)
        self.marca = marca
        self.modelo = modelo

    def transmitir(self):
        print(f"Transmitiendo desde el dispositivo {self.modelo} de la marca {self.marca} con resolución")


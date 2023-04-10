from Dispositivo import Dispositivo
from Sesion import Sesion
class Main:
    def __init__(self):
        self.sesion = None

def crear_sesion(self):
        id_sesion = input("Ingrese el ID de la sesión: ")
        nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
        nombre_profesor = input("Ingrese el nombre del profesor: ")
        sala = input("Ingrese el número de la sala: ")
        fecha = input("Ingrese la fecha de la sesión: ")
        hora_inicio = input("Ingrese la hora de inicio de la sesión: ")
        hora_fin = input("Ingrese la hora de fin de la sesión: ")
        
        # Crear lista de cámaras
        camaras = []
        while True:
            opcion = input("¿Desea agregar una cámara? (s/n): ")
            if opcion.lower() == 'n':
                break
            else:
                id_camara = input("Ingrese el ID de la cámara: ")
                nombre_camara = input("Ingrese el nombre de la cámara: ")
                resolucion = input("Ingrese la resolución de la cámara: ")
                marca = input("Ingrese la marca de la cámara: ")
                modelo = input("Ingrese el modelo de la cámara: ")
                tipo_camara = input("Ingrese el tipo de cámara (webcam, cámara de videoconferencias, etc.): ")
                camara = Dispositivo(id_camara, nombre_camara, resolucion, marca, modelo, tipo_camara)
                camaras.append(camara)

        # Crear sesión
        self.sesion = Sesion(id_sesion, nombre_asignatura, nombre_profesor, sala, fecha, hora_inicio, hora_fin, camaras)
        
def cambiar_camara(self):
        if not self.sesion:
            print("No hay una sesión creada")
            return

        self.sesion.cambiar_camara()
        print(f"Se ha cambiado a la cámara: {self.sesion.camara_en_uso.nombre}")
    
def menu(self):
        while True:
            print("------ MENÚ PRINCIPAL ------")
            print("1. Crear sesión de clase")
            print("2. Cambiar cámara")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.crear_sesion()
            elif opcion == '2':
                self.cambiar_camara()
            elif opcion == '3':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida, intente nuevamente")
                
                # Nicolas Almuna, Alex Hernandez

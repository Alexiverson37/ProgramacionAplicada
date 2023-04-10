class Sesion:
    def __init__(self, id, nombre_asignatura, nombre_profesor, sala, fecha_clase, hora_inicio, hora_fin, camara_en_uso, lista_camaras):
        self.id = id
        self.nombre_asignatura = nombre_asignatura
        self.nombre_profesor = nombre_profesor
        self.sala = sala
        self.fecha_clase = fecha_clase
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.camara_en_uso = None
        self.lista_camaras = []

    def CamaraEnUso (self,camara):
        self.lista_camaras.append(camara)

    def CambiarCamara (self):
        if self.camara_en_uso is None:
            self.camara_en_uso = self.lista_camaras[0]
        else:
            index = self.lista_camaras.index(self.camara_en_uso)
            next_index = (index + 1) % len (self.lista_camaras)
            self.camara_en_uso = self.lista_camaras[next_index]
import sys
from PyQt6 import QtWidgets

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso: float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} años de la mascota {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QWidget):
    def __init__(self, mascota: Mascota):
        super().__init__()
        self.mascota = mascota
        self.initUI()

    def initUI(self):
        
        layout = QtWidgets.QVBoxLayout(self)
        self.nombre_lineedit = QtWidgets.QLineEdit(self.mascota.nombre)
        self.especie_lineedit = QtWidgets.QLineEdit(self.mascota.especie)
        self.edad_spinbox = QtWidgets.QSpinBox()
        self.edad_spinbox.setValue(self.mascota.edad)
        self.peso_spinbox = QtWidgets.QDoubleSpinBox()
        self.peso_spinbox.setValue(self.mascota.peso)
        guardar_button = QtWidgets.QPushButton("Guardar")

       
        layout.addWidget(QtWidgets.QLabel("Nombre:"))
        layout.addWidget(self.nombre_lineedit)
        layout.addWidget(QtWidgets.QLabel("Especie:"))
        layout.addWidget(self.especie_lineedit)
        layout.addWidget(QtWidgets.QLabel("Edad:"))
        layout.addWidget(self.edad_spinbox)
        layout.addWidget(QtWidgets.QLabel("Peso:"))
        layout.addWidget(self.peso_spinbox)
        layout.addWidget(guardar_button)

        
        guardar_button.clicked.connect(self.guardar_mascota)

    def guardar_mascota(self)
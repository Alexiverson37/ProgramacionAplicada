import sys
from PyQt6 import QtWidgets, QtGui

class MiVentana(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #titulo de la ventana
        self.setWindowTitle("Mi Ventana")
        layout = QtWidgets.QHBoxLayout(self)

        # Crea un layout para la imagen de usuario y la descripcion
        layout_izquierda= QtWidgets.QVBoxLayout()
        imagen_usuario = QtWidgets.QLabel()
        imagen_usuario.setFixedSize(100, 100)
        imagen_usuario.setStyleSheet("border: 1px solid black")#esta parte la saque de biblioteca externa nose lo que puede hacer(border: 1px solid black)
        layout_izquierda.addWidget(imagen_usuario)

        # Crea una casilla de texto ,es lo unico funcional
        descripcion = QtWidgets.QPlainTextEdit()
        descripcion.setPlainText("")
        layout_izquierda.addWidget(descripcion)
        layout.addLayout(layout_izquierda)

        # Crea una lista para mostrar los atributos,(como no pedia la funcionalidad solamente le coloque atributo estatico)
        lista_atributos = QtWidgets.QListWidget()
        lista_atributos.addItems(["Atributo 1", "Atributo 2", "Atributo 3"])
        layout.addWidget(lista_atributos)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
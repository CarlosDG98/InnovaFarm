import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

# Función para gestionar las granjas
def gestionar_granjas():
    # Aquí puedes agregar la lógica para gestionar las granjas
    pass

app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QMainWindow()
ventana.setWindowTitle("Mis Granjas")
ventana.setGeometry(100, 100, 800, 600)  # Establecer un tamaño más grande

# Establecer un fondo de degradado
palette = QPalette()
palette.setColor(QPalette.Window, QColor(51, 102, 204))  # Azul degradado
palette.setColor(QPalette.WindowText, Qt.white)  # Texto blanco
ventana.setPalette(palette)

# Crear un widget central
central_widget = QWidget()
ventana.setCentralWidget(central_widget)

# Crear un diseño vertical para organizar los elementos
layout = QVBoxLayout()

# Crear un título formal
titulo = QPushButton("Mis Granjas")  # Cambiamos el título a un botón
titulo.setStyleSheet("font-size: 36px; font-weight: bold; background-color: transparent; color: white; border: none;")  # Estilo de botón

# Botón para gestionar las granjas
boton_gestionar = QPushButton("Gestionar mis granjas")
boton_gestionar.clicked.connect(gestionar_granjas)
boton_gestionar.setStyleSheet("font-size: 24px; background-color: #ff9900; color: white;")

# Botón "Nueva granja" en lugar de etiqueta
boton_nueva_granja = QPushButton("Nueva granja")
boton_nueva_granja.setStyleSheet("font-size: 24px; background-color: #ff9900; color: white;")

# Agregar los elementos al diseño con espaciado uniforme
layout.addWidget(titulo, alignment=Qt.AlignCenter)
layout.addStretch(1)  # Espaciado uniforme
layout.addWidget(boton_gestionar, alignment=Qt.AlignCenter)
layout.addWidget(boton_nueva_granja, alignment=Qt.AlignCenter)
layout.addStretch(1)  # Espaciado uniforme

# Establecer el diseño en el widget central
central_widget.setLayout(layout)

ventana.show()
sys.exit(app.exec_())

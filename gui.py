from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from main import convertir_fila_en_uno, restar_filas, calcular_ultima_fila, calcular_respuestas
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout
import sys

variables = ['x +', 'y +', 'z', '=']
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # se inician los inputs
        self.inputs = []
        # titulo
        self.setWindowTitle("Calculadora Gauss")
        self.resize(QSize(600, 400))
        # coso principal
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignHCenter)
        main_layout.setContentsMargins(0, 45, 0, 0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        # titulo
        heading = QLabel("Gauss Calculator")
        heading.setFont(QFont('Segoe UI', 24, QFont.Weight.Bold))

        button = QPushButton("Calcular")
        button.clicked.connect(self.calculate)

        clear_button = QPushButton("Resetear")
        clear_button.clicked.connect(self.clear)

        # Mensajes con la respuesta. Se esconde hasta que se haya calculado todo
        self.message_heading = QLabel("Respuesta: ")
        self.message_heading.setFont(QFont('Segoe UI', 14, QFont.Weight.Bold))
        self.message_heading.setContentsMargins(0, 20, 0, 0)
        self.message_heading.hide()
        self.message = QLabel("")
        self.message.setFont(QFont('Segoe UI', 10.5))
        # elemento que contiene los inputs
        container_element = QVBoxLayout()
        # en un rango de 3, crear tres filas, cada una de las cuales contiene 4 inputs
        for i in range(3):
            row = self.create_matrix_row()
            container_element.addLayout(row)
        # contenedor
        container = QWidget()
        container.setLayout(container_element)
        container.setMaximumWidth(300)

        main_layout.addWidget(heading)
        main_layout.addWidget(container)
        main_layout.addWidget(button)
        main_layout.addWidget(clear_button)
        main_layout.addWidget(self.message_heading)
        main_layout.addWidget(self.message)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_matrix_row(self):
        layout = QHBoxLayout()
        for i in range(4):
            # se crean 4 inputs: x + y + z = respuesta
            input = QLineEdit()
            input.setMaximumWidth(30)
            label = QLabel(variables[i])
            # de acuerdo a las variables posibles, agregarlas a la ecuacion
            if variables[i] == '=':
                layout.addWidget(label)
                layout.addWidget(input)
            else:
                layout.addWidget(input)
                layout.addWidget(label)
            self.inputs.append(input)
        return layout

    def clear(self):
        # borrar todo el contenido y sacar los mensajes de respuesta
        for number in self.inputs:
            number.setText('')
        self.message_heading.hide()
        self.message.hide()

    def calculate(self):    
        # se consigue los valores de todos los inputs y se los pone en un array
        values = [input.text() for input in self.inputs]
        matrix_numbers = []
        matrix = []
        # si alguno de los inputs no es un numero, retornar error
        try:
            matrix_numbers = [float(value) for value in values]
        except ValueError:
            self.message.setText("Todos los valores tienen que ser números")
            return
        # popular el array `matrix` con valores. El loop toma de a cuatro. O sea, de los 12 numeros va a tomar 0, 4, 8, 12
        for i in range(0, len(matrix_numbers), 4):
            matrix.append(matrix_numbers[i:i+4])
        # convertir la primera fila en 1
        matrix[0] = convertir_fila_en_uno(matrix)
        matrix[1] = restar_filas(matrix, 1)
        matrix[2] = restar_filas(matrix, 2)
        matrix[1], matrix[2] = calcular_ultima_fila(matrix)
        matrix[2] = restar_filas(matrix, 2, 1)

        self.message_heading.show()
        self.message.show()
        self.message.setText(calcular_respuestas(matrix))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
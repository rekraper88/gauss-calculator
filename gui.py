from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from main import convertir_fila_en_uno, restar_filas, calcular_segunda_fila, calcular_respuestas
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout
import sys

variables = ['x +', 'y +', 'z', '=']
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inputs = []

        self.setWindowTitle("Calculadora Gauss")
        self.resize(QSize(600, 400))

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignHCenter)
        main_layout.setContentsMargins(0, 45, 0, 0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        heading = QLabel("Gauss Calculator")
        heading.setFont(QFont('Segoe UI', 24, QFont.Weight.Bold))

        button = QPushButton("Calcular")
        button.clicked.connect(self.calculate)

        clear_button = QPushButton("Resetear")
        clear_button.clicked.connect(self.clear)

        self.message_heading = QLabel("Respuesta: ")
        self.message_heading.setFont(QFont('Segoe UI', 14, QFont.Weight.Bold))
        self.message_heading.setContentsMargins(0, 20, 0, 0)
        self.message_heading.hide()

        self.message = QLabel("")
        self.message.setFont(QFont('Segoe UI', 10.5))

        container_element = QVBoxLayout()
        for i in range(3):
            row = self.create_matrix_row()
            container_element.addLayout(row)

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
            input = QLineEdit()
            input.setMaximumWidth(30)
            label = QLabel(variables[i])

            if variables[i] == '=':
                layout.addWidget(label)
                layout.addWidget(input)
            else:
                layout.addWidget(input)
                layout.addWidget(label)
            self.inputs.append(input)
        return layout

    def clear(self):
        for number in self.inputs:
            number.setText('')
        self.message_heading.hide()
        self.message.hide()

    def print_matrix(self, matrix):
        for fila in matrix:
            print(fila)
        print('\n\n')

    def calculate(self):    
        values = [input.text() for input in self.inputs]
        matrix_numbers = []
        try:
            matrix_numbers = [float(value) for value in values]
        except ValueError:
            self.message.setText("Todos los valores tienen que ser números")
            return

        matrix = [matrix_numbers[i:i + 4] for i in range(0, len(matrix_numbers), 4)]
        matrix[0] = convertir_fila_en_uno(matrix)
        matrix[1] = restar_filas(matrix, 1)
        matrix[2] = restar_filas(matrix, 2)
        self.print_matrix(matrix)
        matrix[1], matrix[2] = calcular_segunda_fila(matrix)
        self.print_matrix(matrix)
        matrix[2] = restar_filas(matrix, 2, 1)

        self.message_heading.show()
        self.message.show()
        self.message.setText(calcular_respuestas(matrix))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
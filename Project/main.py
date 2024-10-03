import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, QFrame, QProgressDialog
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import Soyarslan_no_cubico

from PyQt6.QtCore import QThread, pyqtSignal
import Soyarslan_no_cubico

class MyThread(QThread):
    resultado_signal = pyqtSignal(tuple)

    def __init__(self, archivo1, archivo2, epsilon1, simbolo, epsilon2, valor_permutaciones, nombre_resultante,nombre_variables):
        super().__init__()
        self.archivo1 = archivo1
        self.archivo2 = archivo2
        self.epsilon1 = epsilon1
        self.simbolo = simbolo
        self.epsilon2 = epsilon2
        self.valor_permutaciones = valor_permutaciones
        self.nombre_resultante = nombre_resultante
        self.nombre_variables = nombre_variables

    def run(self):
        resultado = Soyarslan_no_cubico.funcion_app(self.archivo1, self.archivo2, self.epsilon1, self.simbolo, self.epsilon2, self.valor_permutaciones, self.nombre_resultante, self.nombre_variables)
        self.resultado_signal.emit(resultado)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nanopore Structure')
        self.layout = QVBoxLayout()
        self.setStyleSheet("background-color: #D8E4FD;")

        # Fuentes de la letra
        titulo = "font-family: Arial; font-size: 24pt; font-weight: bold;color: black;"
        sub_titulo = "font-family: Arial; font-size: 18pt;color: black;"
        letra = "font-family: Arial; font-size: 14pt;color: black;"
        letra_confirmar = "font-family: Arial; font-size: 14pt; font-weight: bold;color: black;"

        # Configuración Bordes
        borde_entry = "border: 2px solid #C0C3CC; background-color: #F1F3F9; padding: 5px; border-radius: 7.5px;font-family: Arial; font-size: 14pt;color: black;"
        botones = "QPushButton {color: white; background-color: #2759BE; padding: 5px; border-radius: 7.5px;font-family: Arial; font-size: 14pt;} QPushButton:hover {background-color: #263576; color: white;}"
        botones_confirmar = "QPushButton {color: white; background-color: #263576; padding: 5px; border-radius: 7.5px;font-family: Arial; font-size: 14pt;} QPushButton:hover {background-color: #2759BE; color: white;}"

        # Crear el layout principal
        layout_principal = QVBoxLayout(self)
        
        # Frames
        def crear_frame_contenido(layout):
            frame = QFrame()
            frame.setStyleSheet("background-color: white; padding: 10px; border-radius: 10px;")
            layout_frame = QVBoxLayout(frame)
            layout_frame.addLayout(layout)
            return frame

        # Función para agregar un frame al layout principal con el contenido y espaciado
        def agregar_seccion(layout):
            frame = crear_frame_contenido(layout)
            layout_principal.addWidget(frame)
            layout_principal.addSpacing(10)

        # Layout titulo
        layout_titulo = QHBoxLayout()
        label_Titulo = QLabel("Nanopore Structure")
        label_Titulo.setStyleSheet(titulo)
        label_Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_titulo.addWidget(label_Titulo)

        # Layout sub_titulo
        layout_sub_titulo = QHBoxLayout()
        label_sub_titulo = QLabel("Core-Shell Type")
        label_sub_titulo.setStyleSheet(sub_titulo)
        label_sub_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_sub_titulo.addWidget(label_sub_titulo)

        # Sección 1: Archivo 1 y Epsilon 1
        layout_seccion1 = QVBoxLayout()
        
        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_archivo1 = QLabel("Core File:")
        label_archivo1.setStyleSheet(letra)
        label_archivo1.setFixedSize(106,36)
        archivo1_entry = QLineEdit()
        archivo1_entry.setStyleSheet(borde_entry)
        boton_explorar1 = QPushButton("Explore")
        boton_explorar1.clicked.connect(lambda: self.seleccionar_archivo(archivo1_entry))
        boton_explorar1.setStyleSheet(botones)
        boton_explorar1.setFixedSize(80,36)
        layout1.addWidget(label_archivo1)
        layout1.addWidget(archivo1_entry)
        layout1.addWidget(boton_explorar1)

        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_epsilon1 = QLabel("E1:")
        label_epsilon1.setStyleSheet(letra)
        label_epsilon1.setFixedSize(52,36)
        epsilon1_entry = QLineEdit()
        epsilon1_entry.setStyleSheet(borde_entry)
        epsilon1_entry.setFixedSize(100,36)
        boton_simbolo = QPushButton("<")
        boton_simbolo.clicked.connect(lambda: self.alternar_simbolo(boton_simbolo, label_simbolo1, label_simbolo2))
        boton_simbolo.setStyleSheet(botones)
        boton_simbolo.setFixedSize(36,36)
        label_valores1 = QLabel("Values")
        label_valores1.setStyleSheet(letra)
        label_valores1.setFixedSize(81,36)
        layout2.addWidget(label_epsilon1)
        layout2.addWidget(epsilon1_entry)
        layout2.addWidget(boton_simbolo)
        layout2.addWidget(label_valores1)

        layout_seccion1.addLayout(layout1)
        layout_seccion1.addLayout(layout2)

        # Sección 2: Archivo 2 y Epsilon 2
        layout_seccion2 = QVBoxLayout()

        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_archivo2 = QLabel("Shell File:")
        label_archivo2.setStyleSheet(letra)
        label_archivo2.setFixedSize(106,36)
        archivo2_entry = QLineEdit()
        archivo2_entry.setStyleSheet(borde_entry)
        boton_explorar2 = QPushButton("Explore")
        boton_explorar2.clicked.connect(lambda: self.seleccionar_archivo(archivo2_entry))
        boton_explorar2.setStyleSheet(botones)
        boton_explorar2.setFixedSize(80,36)
        layout3.addWidget(label_archivo2)
        layout3.addWidget(archivo2_entry)
        layout3.addWidget(boton_explorar2)

        layout4 = QHBoxLayout()
        layout4.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_epsilon2 = QLabel("E2:")
        label_epsilon2.setStyleSheet(letra)
        label_epsilon2.setFixedSize(52,36)
        epsilon2_entry = QLineEdit()
        epsilon2_entry.setStyleSheet(borde_entry)
        epsilon2_entry.setFixedSize(100,36)
        label_simbolo1 = QLabel("<")
        label_simbolo1.setStyleSheet(letra)
        label_simbolo1.setFixedSize(36,36)
        label_valores2 = QLabel("Values")
        label_valores2.setStyleSheet(letra)
        label_valores2.setFixedSize(81,36)
        label_simbolo2 = QLabel("<")
        label_simbolo2.setStyleSheet(letra)
        label_simbolo2.setFixedSize(36,36)
        label_valor_epsilon1 = QLabel("E1")
        epsilon1_entry.textChanged.connect(lambda: self.actualizar_valor_epsilon1(epsilon1_entry, label_valor_epsilon1))
        label_valor_epsilon1.setStyleSheet(letra)
        label_valor_epsilon1.setFixedSize(105,36)
        layout4.addWidget(label_epsilon2)
        layout4.addWidget(epsilon2_entry)
        layout4.addWidget(label_simbolo1)
        layout4.addWidget(label_valores2)
        layout4.addWidget(label_simbolo2)
        layout4.addWidget(label_valor_epsilon1)

        layout_seccion2.addLayout(layout3)
        layout_seccion2.addLayout(layout4)

        # Sección 3: Permutaciones y Nombre Resultado
        layout_seccion3 = QVBoxLayout()

        layout5 = QHBoxLayout()
        layout5.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_permutaciones = QLabel("Permutations:")
        label_permutaciones.setStyleSheet(letra)
        label_permutaciones.setFixedSize(141,36)
        permutaciones_entry = QLineEdit()
        permutaciones_entry.setStyleSheet(borde_entry)
        permutaciones_entry.setFixedSize(100,36)
        layout5.addWidget(label_permutaciones)
        layout5.addWidget(permutaciones_entry)

        layout6 = QHBoxLayout()
        layout6.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_nombre_archivo = QLabel("Output File Name:")
        label_nombre_archivo.setStyleSheet(letra)
        label_nombre_archivo.setFixedSize(178,36)
        nombre_archivo_entry = QLineEdit("Result")
        nombre_archivo_entry.setStyleSheet(borde_entry)
        nombre_archivo_entry.setFixedSize(160,36)
        layout6.addWidget(label_nombre_archivo)
        layout6.addWidget(nombre_archivo_entry)

        layout7 = QHBoxLayout()
        boton_confirmar = QPushButton("Confirm")
        boton_confirmar.clicked.connect(lambda: self.confirmar(archivo1_entry, archivo2_entry, epsilon1_entry, boton_simbolo, epsilon2_entry, permutaciones_entry, nombre_archivo_entry))
        boton_confirmar.setStyleSheet(botones_confirmar)
        boton_confirmar.setFixedSize(98,36)
        layout7.addWidget(boton_confirmar)

        layout_seccion3.addLayout(layout5)
        layout_seccion3.addLayout(layout6)
        layout_seccion3.addLayout(layout7)

        layout_principal.addLayout(layout_titulo)
        layout_principal.addLayout(layout_sub_titulo)
        agregar_seccion(layout_seccion1)
        agregar_seccion(layout_seccion2)
        agregar_seccion(layout_seccion3)

    def seleccionar_archivo(self, entry):
        filename, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Todos los archivos (*);;Archivos de texto (*.txt)")
        if filename:
            entry.setText(filename)
    
    def alternar_simbolo(self, boton_simbolo, label_simbolo1, label_simbolo2):
        simbolo = boton_simbolo.text()
        nuevo_simbolo = '>' if simbolo == '<' else '<'
        boton_simbolo.setText(nuevo_simbolo)
        label_simbolo1.setText(nuevo_simbolo)
        label_simbolo2.setText(nuevo_simbolo)
    
    def actualizar_valor_epsilon1(self,epsilon1_entry, label_valor_epsilon1):
        text = epsilon1_entry.text()
        if text:
            label_valor_epsilon1.setText(text)
        else:
            label_valor_epsilon1.setText("E1")

    def confirmar(self,archivo1_entry, archivo2_entry, epsilon1_entry, boton_simbolo, epsilon2_entry, permutaciones_entry, nombre_archivo_entry):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Confirmation")
        mensaje.setText("The data is correct?")
        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        mensaje.button(QMessageBox.StandardButton.Yes)
        mensaje.button(QMessageBox.StandardButton.No)

        reply = mensaje.exec()
        if reply == QMessageBox.StandardButton.Yes:
            print("The operation was confirmed")
            self.confirmar_operacion(archivo1_entry, archivo2_entry, epsilon1_entry, boton_simbolo, epsilon2_entry, permutaciones_entry, nombre_archivo_entry)
        else:
            print("The operation was canceled")

    def confirmar_operacion(self,archivo1_var, archivo2_var, epsilon1_var, simbolo_var, epsilon2_var, permutaciones_var, nombre_archivo):
        if not os.path.exists("results"):
            os.makedirs("results")
        try:
            archivo1 = str(archivo1_var.text())
            if archivo1 == "":
                QMessageBox.information(None, "File 1", "Incorrect File 1 Format")
                return
        except:
            QMessageBox.information(None, "File 1", "Incorrect File 1 Format")
            return
        try:
            archivo2 = str(archivo2_var.text())
            if archivo2 == "":
                QMessageBox.information(None, "File 2", "Incorrect File 2 Format")
                return
        except:
            QMessageBox.information(None, "File 2", "Incorrect File 2 Format")
            return
        try:
            epsilon1 = float(epsilon1_var.text())
        except:
            QMessageBox.information(None, "Epsilon 1", "Incorrect Epsilon 1 Format")
            return
        try:
            epsilon2 = float(epsilon2_var.text())
        except:
            QMessageBox.information(None, "Epsilon 2", "Incorrect Epsilon 2 Format")
            return
        try:
            valor_permutaciones = int(permutaciones_var.text())
        except:
            QMessageBox.information(None, "Permutations", "Incorrect Permutations Format")
            return

        simbolo = str(simbolo_var.text())
        nombre_variables = str(nombre_archivo.text())
        nombre_resultante = str(nombre_archivo.text() + ".dump")
        if simbolo == ">":
            if epsilon2 > epsilon1:
                variables = open("results/"+nombre_variables+".log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables.write(("Permutations: " + str(valor_permutaciones)) + "\n")
                variables.write("File 1: E1 " + str(simbolo) + " Values \n")
                variables.write("File 2: E2 " + str(simbolo) + " Values " + str(simbolo) + " E1 \n")
                variables.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, archivo2, epsilon1, simbolo, epsilon2, valor_permutaciones, nombre_resultante,nombre_variables)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()

            else:
                QMessageBox.information(None, "", "Epsilon 2 must be greater than Epsilon 1")
        elif simbolo == "<":
            if epsilon2 < epsilon1:
                variables = open("results/variables.txt", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables.write(("Permutations: " + str(valor_permutaciones)) + "\n")
                variables.write("File 1: E1 " + str(simbolo) + " Values \n")
                variables.write("File 2: E2 " + str(simbolo) + " Values " + str(simbolo) + " E1 \n")
                variables.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, archivo2, epsilon1, simbolo, epsilon2, valor_permutaciones, nombre_resultante, nombre_variables)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
                
            else:
                QMessageBox.information(None, "", "Epsilon 2 must be less than Epsilon 1")

    def show_result(self, resultado):
        self.ventana_procesando.setWindowTitle(resultado[0])
        self.ventana_procesando.setText(resultado[1])
        self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.ventana_procesando.adjustSize()
        
        
        # Cerrar el hilo
        self.thread.quit()
        self.thread.wait()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

from translate import Translator
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle("PTranslate")
        
        self.button = QtWidgets.QPushButton("RU")
        self.button2 = QtWidgets.QPushButton("LV")
        self.edit = QLineEdit("Write words to translate")
        self.text = QtWidgets.QLabel("",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        self.button.clicked.connect(self.magic)
        self.button2.clicked.connect(self.magic2)

    @QtCore.Slot()
    def magic(self, translation):
        translator= Translator(to_lang=f"ru")
        translation = translator.translate(self.edit.text())
        self.text.setText(translation)
    def magic2(self, translation):
        translator= Translator(to_lang=f"lv")
        translation = translator.translate(self.edit.text())
        self.text.setText(translation)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(270, 480)
    widget.show()

    sys.exit(app.exec())

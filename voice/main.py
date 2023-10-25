import speech_recognition
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
        self.setWindowTitle("PVTranslate")
        
        self.button = QtWidgets.QPushButton("RU to LV")
        self.button2 = QtWidgets.QPushButton("LV to RU")
        self.text = QtWidgets.QLabel("",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.edit)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        self.button.clicked.connect(self.magic)
        self.button2.clicked.connect(self.magic2)

    @QtCore.Slot()
    def magic(self):
        mic = speech_recognition.Microphone()
        recog = speech_recognition.Recognizer()

        with mic as audio_file:
            recog.adjust_for_ambient_noise(audio_file)
            audio = recog.listen(audio_file)
            
            rec = recog.recognize_google(audio, language="ru-RU")
            translator = Translator(from_lang=f"ru", to_lang=f"lv")
            translation = translator.translate(f"{rec}")
            self.text.setText(translation)            
            
    def magic2(self):
        mic = speech_recognition.Microphone()
        recog = speech_recognition.Recognizer()

        with mic as audio_file:
            # print("Speak ples")
            recog.adjust_for_ambient_noise(audio_file)
            audio = recog.listen(audio_file)
    
            # print("Converting Speech to Text...")
            
            rec = recog.recognize_google(audio, language="lv-LV")
            translator = Translator(from_lang=f"lv", to_lang=f"ru")
            translation = translator.translate(f"{rec}")
            self.text.setText(translation)      
            
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(270, 480)
    widget.show()

    sys.exit(app.exec())

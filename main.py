#!/usr/bin/python3
import sys
#import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap


app = QApplication(sys.argv)

# Пишем что будет делать кнопки
def actinon_button_next():
    ui.label_1.setText("Нажата кнопка дальше")
    #label = QLabel(self)
    pixmap = QPixmap('5.svg')
    pixmap1 = QPixmap('6.svg')

    ui.label_3.setPixmap(pixmap)
    ui.label_4.setPixmap(pixmap1)

    ui.label_8.setText("Подпись ярлыка")
    ui.label_9.setText("Подпись ярлыка2")

def actinon_button_back():
    ui.label_1.setText("Нажата кнопка назад")
    #label = QLabel(self)
    pixmap = QPixmap('7.svg')
    pixmap1 = QPixmap('9.svg')

    ui.label_3.setPixmap(pixmap)
    ui.label_4.setPixmap(pixmap1)

    ui.label_8.setText("Другая подпись ярлыка")
    ui.label_9.setText("Другая подпись ярлыка2")

def actinon_button_exit():
    sys.exit()

# If you saved the template in `templates/main_window.ui`
ui = uic.loadUi("dialog.ui")
ui.show()

# Then you can access the objects from the UI
# For example, if you had a label named label1
ui.label_1.setText('new text')
ui.pushButton_next.clicked.connect(actinon_button_next)
ui.pushButton_back.clicked.connect(actinon_button_back)
ui.pushButton_exit.clicked.connect(actinon_button_exit)


#label = QLabel(self)
pixmap = QPixmap('1.svg')
pixmap1 = QPixmap('2.svg')

ui.label_1.setPixmap(pixmap)
ui.label_2.setPixmap(pixmap1)
sys.exit(app.exec_())

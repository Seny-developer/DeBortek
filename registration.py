#!/usr/bin/env python 3.10
# -*- coding: utf-8 -*-

import main_page # опять импорт других файлов
import DataBase
import log_account

import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *
from PyQt5 import *                           ## всё тоже самое
from PyQt5.QtWinExtras import QtWin 
from PyQt5.QtCore import pyqtSlot 


def start():                                  # Как раз метод который я вызываю в log_account.py
	class Register(QWidget):
		def __init__(self, **kwargs):
			super().__init__()

			self.register()                                                          # на главную страницу

		def register(self):                                                # Как раз основной метод, в котором прописаны все виджеты
			label_register = QLabel("𝓓𝓮𝓑𝓸𝓻𝓽𝓮𝓴") # Работа с лейблом
			label_register.setStyleSheet('font-size: 50px; color: white;')
			layout_main_register.addWidget(label_register, alignment=Qt.AlignCenter)


			self.login_register = QLineEdit() # Первая строка для ввода
			self.login_register.setStyleSheet('font-size: 40px; background-color: #333333; border: 3px solid black;' 
			'border-radius: 25px; padding: 10px; color: #6c7076;')
			self.login_register.setPlaceholderText("     Create login")
			layout_main_register.addWidget(self.login_register, alignment=Qt.AlignCenter)

			self.password_register = QLineEdit() # Вторая строка для ввода
			self.password_register.setStyleSheet('font-size: 40px; background-color: #333333; border: 3px solid black;' 
			'border-radius: 25px; padding: 10px; color: #6c7076;')
			self.password_register.setPlaceholderText("  Create password")
			layout_main_register.addWidget(self.password_register, alignment=Qt.AlignCenter)

			btn_register = QPushButton('register') # Кнопочка, при нажатии на которую идёт переход на главную страницу
			btn_register.setStyleSheet('font-size: 50px; background-color: #4ab34c; border: 2px solid black;'
			'border-radius: 40px; padding: 20px; color: white;')
			btn_register.clicked.connect(self.after_press_register_registration)    # говорим ей про функцию выше
			layout_main_register.addWidget(btn_register, alignment=Qt.AlignCenter)


		def after_press_register_registration(self, **kwargs):             # В дальнейшем будет отвечать за переход
			pass 

	def xy():
		desktop = QtWidgets.QApplication.desktop()                # Узнаём центр экрана и позиционируем ПЕРВОЕ окно по центру.
		x = (desktop.width() - win_register.width()) // 2      # В файле registration.py есть такой же кусочек кода
		y = (desktop.height() - win_register.height()) // 2 

		win_register.move(x, y) 

	if __name__ == '__main__':                           # опять запуск
		app_register = QApplication([])
		win_register = QWidget()
		win_register.showMinimized()
		win_register.resize(641, 480)
		win_register.setWindowTitle("𝓓𝓮𝓑𝓸𝓻𝓽𝓮𝓴")
		win_register.setObjectName("SecondWindow")
		win_register.setStyleSheet("#SecondWindow{background-color: #141414; max-width: 641; max-height: 480; min-width: 641; min-height: 480;}") # - цвет заднего фона
		app_register.setWindowIcon(QtGui.QIcon('img/logo_black.png'))
		win_register.setWindowIcon(QtGui.QIcon('img/logo_black.png'))

		layout_main_register = QVBoxLayout() # лайаут 
		win_register.setLayout(layout_main_register)

		ex = Register()
		sys.exit(app_register.exec_())

start() # Запуск кода ОТДЕЛЬНО. УБРАТЬ ПРИ ЗАПУСКЕ В СВЯЗКЕ С ДРУГИМИ ФАЙЛАМИ !!!!!!!!!!!!!!!!!!!!!!!!!!!

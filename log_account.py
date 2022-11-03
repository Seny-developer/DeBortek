#!/usr/bin/env python 3.10
# -*- coding: utf-8 -*-

import main_page
import registration  #Другие файлы .py(лежат в папке)
import DataBase

import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *  
from PyQt5 import *                                # Импорт файлов PyQt5 и их состовляющие
from PyQt5.QtWinExtras import QtWin 
from PyQt5.QtCore import pyqtSlot 

from colorama import init, Fore, Style, Back    #модуль для окрашивания текста в консоли(необязательный
init()                                          #                                       для работы кода)


print(Fore.GREEN) # <-- colorama
# Created on 2022.11.02
# author: Seny
# email: ay.zhiliaev@outlook.com
# file: MVP
print("__Author__:", "Seny")
print("__Email__:", "ay.zhiliaev@outlook.com")                 # текст, который выводится в консоль
print("__Copyright__:",  "(c) Seny MIT Licence")
print("__Version__:", "MVP 1.0")
print(Fore.WHITE) # <-- colorama


try: # отвечает за иконку приложения на панели задач                                        
    myappid = 'mycompany.myproduct.subproduct.version'                         
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)                       
except ImportError:
    pass


class Log_account(QWidget):         # Класс всего окна (можно без него, но с ним проще читать мне код)
    def __init__(self, **kwargs):
        super().__init__()

        self.log_account() # Вызов функции из класса


    def log_account(self):         # Функция, где прописаны все виджеты
        layout_main_log_account = QVBoxLayout() # Направляющая линия


        label_log_account = QLabel("𝓓𝓮𝓑𝓸𝓻𝓽𝓮𝓴")  # Работа с заголовком
        label_log_account.setStyleSheet('font-size: 50px; color: white;')                
        layout_main_log_account.addWidget(label_log_account, alignment=Qt.AlignCenter)  #добавляем на линию  


        self.login_log_in = QLineEdit() # Первое окно ввода
        self.login_log_in.setStyleSheet('font-size: 40px; background-color: #333333; border: 3px solid black;' 
        'border-radius: 25px; padding: 10px; color: #6c7076;')
        self.login_log_in.setPlaceholderText("      Your login")
        layout_main_log_account.addWidget(self.login_log_in, alignment=Qt.AlignCenter)


        self.password_log_in = QLineEdit() # Второе окно ввода
        self.password_log_in.setStyleSheet('font-size: 40px; background-color: #333333; border: 3px solid black;' 
        'border-radius: 25px; padding: 10px; color: #6c7076;')
        self.password_log_in.setPlaceholderText("   Your password")
        self.password_log_in.setEchoMode( QLineEdit.Password ) #Какая-то штука, которая вместо символов ставит 
        layout_main_log_account.addWidget(self.password_log_in, alignment=Qt.AlignCenter) # кружки, типо ****


        btn_log_in = QPushButton('log in') # Кнопка "войти" 
        btn_log_in.setStyleSheet('font-size: 50px; background-color: #333333; border: 3px solid black;'
        'border-radius: 40px; padding: 20px; color: #6c7076;')
        btn_log_in.clicked.connect(self.after_press_log_in) # Функция after_press_log_in - переход на страницу main_page.py
        layout_main_log_account.addWidget(btn_log_in, alignment=Qt.AlignCenter)


        btn_register = QPushButton('register') # Кнопка "зарегестрироваться" 
        btn_register.setStyleSheet('font-size: 50px; background-color: #4ab34c; border: 2px solid black;'
        'border-radius: 40px; padding: 15px; color: white;')                                # Проблема сейчас с этим куском кода !!!!!!!!
        btn_register.clicked.connect(self.after_press_register_in_log_in)   # Функция ниже
        layout_main_log_account.addWidget(btn_register, alignment=Qt.AlignCenter)


        win_log_account.setLayout(layout_main_log_account)


    @pyqtSlot() # переход на main_page !!! Это нафиг пока не нужно
    def after_press_log_in(self, **kwargs):
        if self.login_log_in.text() in DataBase.database and DataBase.database[self.login_log_in.text()] == self.password_log_in.text():
            pass
        else:
            pass


    @pyqtSlot() # Функция, которая отвечает за переход на registration.py
    def after_press_register_in_log_in(self, **kwargs):
        print("Click!")                    
        win_log_account.close()      # Закрываю старое окно и запускаю новое, но оно не остаётся на экране
        registration.start()
        """ 
        А вот тут поподробнее. Я поперебробывал всё, что можно. Метод .show() вообще тут не причём, как может
        показаться на первый взгяд. Второе окно просто читается и не хочет запускаться. Не знаю что делать!!!
        """


if __name__ == '__main__': # Запуск программы
    app_log_account = QApplication([])                        # Создал приложение
    win_log_account = QWidget()                               # Создал само окно
    win_log_account.showMinimized()                           # Сказал, что открыть в минимальном размере
    win_log_account.resize(641, 480)                          # Указал сами размеры

    desktop = QtWidgets.QApplication.desktop()                # Узнаём центр экрана и позиционируем ПЕРВОЕ окно по центру.
    x = (desktop.width() - win_log_account.width()) // 2      # В файле registration.py есть такой же кусочек кода
    y = (desktop.height() - win_log_account.height()) // 2    
    win_log_account.move(x, y)                                

    win_log_account.setWindowTitle("𝓓𝓮𝓑𝓸𝓻𝓽𝓮𝓴")               # Название окна
    win_log_account.setObjectName("MainWindow")               # Поменял имя, чтобы прописать внешний вид через css. Название переменной не меняется
    win_log_account.setStyleSheet("#MainWindow{background-color: #141414; max-width: 641; max-height: 480; min-width: 641; min_height: 480;}") # - цвет заднего фона
    app_log_account.setWindowIcon(QtGui.QIcon('img/logo_black.png')) #А это просто картинка - лого
    win_log_account.setWindowIcon(QtGui.QIcon('img/logo_black.png'))

    ex1 = Log_account()                                        # Запустил класс
    sys.exit(app_log_account.exec_())                          # Теперь не закроется

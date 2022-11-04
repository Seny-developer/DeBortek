#!/usr/bin/env python 3.10
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *
from PyQt5 import *                         
from PyQt5.QtWinExtras import QtWin 
from PyQt5.QtCore import pyqtSlot 



class mainpage(QWidget):
	def __init__(self, **kwargs):
			super().__init__()

		self.page()

	def page(self):
		layout_mainpage = QVBoxLayout()

		win_mainpage.setLayout(layout_mainpage)


if __name__ == '__main__':
	app_mainpage = QApplication([])
	win_mainpage = QWidget()
	win_mainpage.showMaximized()
	win_mainpage.showMinimized()
	win_mainpage.resize(641, 480)
	win_mainpage.move(x, y)
	win_mainpage.setWindowTitle("𝓓𝓮𝓑𝓸𝓻𝓽𝓮𝓴")
	win_mainpage.setObjectName("SecondWindow")
	win_mainpage.setStyleSheet("#SecondWindow{background-color: #141414; max-width: 641; max-height: 480; min-width: 641; min_height: 480;}") # - цвет заднего фона
	app_mainpage.setWindowIcon(QtGui.QIcon('img/logo_black.png'))
	win_mainpage.setWindowIcon(QtGui.QIcon('img/logo_black.png'))

	sys.exit(app_mainpage.exec_())
	win_mainpage.show()

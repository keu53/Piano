# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.A2 = QtWidgets.QPushButton(self.centralwidget)
        self.A2.setGeometry(QtCore.QRect(280, 50, 41, 141))
        self.A2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.A2.setText("")
        self.A2.setObjectName("A2")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(180, 300, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.C2 = QtWidgets.QPushButton(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(30, 50, 41, 141))
        self.C2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.C2.setText("")
        self.C2.setObjectName("C2")
        self.F2 = QtWidgets.QPushButton(self.centralwidget)
        self.F2.setGeometry(QtCore.QRect(180, 50, 41, 141))
        self.F2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.F2.setText("")
        self.F2.setObjectName("F2")
        self.D6 = QtWidgets.QPushButton(self.centralwidget)
        self.D6.setGeometry(QtCore.QRect(780, 50, 41, 141))
        self.D6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.D6.setText("")
        self.D6.setObjectName("D6")
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(650, 50, 51, 211))
        self.B3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B3.setText("")
        self.B3.setObjectName("B3")
        self.F4 = QtWidgets.QPushButton(self.centralwidget)
        self.F4.setGeometry(QtCore.QRect(530, 50, 41, 141))
        self.F4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.F4.setText("")
        self.F4.setObjectName("F4")
        self.F1 = QtWidgets.QPushButton(self.centralwidget)
        self.F1.setGeometry(QtCore.QRect(150, 50, 51, 211))
        self.F1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.F1.setText("")
        self.F1.setObjectName("F1")
        self.F3 = QtWidgets.QPushButton(self.centralwidget)
        self.F3.setGeometry(QtCore.QRect(500, 50, 51, 211))
        self.F3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.F3.setText("")
        self.F3.setObjectName("F3")
        self.A3 = QtWidgets.QPushButton(self.centralwidget)
        self.A3.setGeometry(QtCore.QRect(600, 50, 51, 211))
        self.A3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A3.setText("")
        self.A3.setObjectName("A3")
        self.A4 = QtWidgets.QPushButton(self.centralwidget)
        self.A4.setGeometry(QtCore.QRect(630, 50, 41, 141))
        self.A4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.A4.setText("")
        self.A4.setObjectName("A4")
        self.G1 = QtWidgets.QPushButton(self.centralwidget)
        self.G1.setGeometry(QtCore.QRect(200, 50, 51, 211))
        self.G1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G1.setText("")
        self.G1.setObjectName("G1")
        self.C6 = QtWidgets.QPushButton(self.centralwidget)
        self.C6.setGeometry(QtCore.QRect(730, 50, 41, 141))
        self.C6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.C6.setText("")
        self.C6.setObjectName("C6")
        self.E3 = QtWidgets.QPushButton(self.centralwidget)
        self.E3.setGeometry(QtCore.QRect(450, 50, 51, 211))
        self.E3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.E3.setText("")
        self.E3.setObjectName("E3")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(10, 300, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.delme = QtWidgets.QPushButton(self.centralwidget)
        self.delme.setGeometry(QtCore.QRect(710, 300, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delme.setFont(font)
        self.delme.setObjectName("delme")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(750, 0, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.C1 = QtWidgets.QPushButton(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(0, 50, 51, 211))
        self.C1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C1.setText("")
        self.C1.setObjectName("C1")
        self.C5 = QtWidgets.QPushButton(self.centralwidget)
        self.C5.setGeometry(QtCore.QRect(700, 50, 51, 211))
        self.C5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C5.setText("")
        self.C5.setObjectName("C5")
        self.D4 = QtWidgets.QPushButton(self.centralwidget)
        self.D4.setGeometry(QtCore.QRect(430, 50, 41, 141))
        self.D4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.D4.setText("")
        self.D4.setObjectName("D4")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(300, 50, 51, 211))
        self.B1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B1.setText("")
        self.B1.setObjectName("B1")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 300, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.D1 = QtWidgets.QPushButton(self.centralwidget)
        self.D1.setGeometry(QtCore.QRect(50, 50, 51, 211))
        self.D1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.D1.setText("")
        self.D1.setObjectName("D1")
        self.G4 = QtWidgets.QPushButton(self.centralwidget)
        self.G4.setGeometry(QtCore.QRect(580, 50, 41, 141))
        self.G4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.G4.setText("")
        self.G4.setObjectName("G4")
        self.D3 = QtWidgets.QPushButton(self.centralwidget)
        self.D3.setGeometry(QtCore.QRect(400, 50, 51, 211))
        self.D3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.D3.setText("")
        self.D3.setObjectName("D3")
        self.D5 = QtWidgets.QPushButton(self.centralwidget)
        self.D5.setGeometry(QtCore.QRect(750, 50, 51, 211))
        self.D5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.D5.setText("")
        self.D5.setObjectName("D5")
        self.D2 = QtWidgets.QPushButton(self.centralwidget)
        self.D2.setGeometry(QtCore.QRect(80, 50, 41, 141))
        self.D2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.D2.setText("")
        self.D2.setObjectName("D2")
        self.E1 = QtWidgets.QPushButton(self.centralwidget)
        self.E1.setGeometry(QtCore.QRect(100, 50, 51, 211))
        self.E1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.E1.setText("")
        self.E1.setObjectName("E1")
        self.G2 = QtWidgets.QPushButton(self.centralwidget)
        self.G2.setGeometry(QtCore.QRect(230, 50, 41, 141))
        self.G2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.G2.setText("")
        self.G2.setObjectName("G2")
        self.vospr = QtWidgets.QPushButton(self.centralwidget)
        self.vospr.setGeometry(QtCore.QRect(500, 300, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vospr.setFont(font)
        self.vospr.setObjectName("vospr")
        self.G3 = QtWidgets.QPushButton(self.centralwidget)
        self.G3.setGeometry(QtCore.QRect(550, 50, 51, 211))
        self.G3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G3.setText("")
        self.G3.setObjectName("G3")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(590, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.A1 = QtWidgets.QPushButton(self.centralwidget)
        self.A1.setGeometry(QtCore.QRect(250, 50, 51, 211))
        self.A1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A1.setText("")
        self.A1.setObjectName("A1")
        self.E5 = QtWidgets.QPushButton(self.centralwidget)
        self.E5.setGeometry(QtCore.QRect(800, 50, 51, 211))
        self.E5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.E5.setText("")
        self.E5.setObjectName("E5")
        self.C4 = QtWidgets.QPushButton(self.centralwidget)
        self.C4.setGeometry(QtCore.QRect(380, 50, 41, 141))
        self.C4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.C4.setText("")
        self.C4.setObjectName("C4")
        self.C3 = QtWidgets.QPushButton(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(350, 50, 51, 211))
        self.C3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C3.setText("")
        self.C3.setObjectName("C3")
        self.G1.raise_()
        self.F1.raise_()
        self.E5.raise_()
        self.D5.raise_()
        self.C5.raise_()
        self.G3.raise_()
        self.F3.raise_()
        self.D3.raise_()
        self.C3.raise_()
        self.B1.raise_()
        self.A1.raise_()
        self.C1.raise_()
        self.D1.raise_()
        self.E1.raise_()
        self.A2.raise_()
        self.stop.raise_()
        self.C2.raise_()
        self.F2.raise_()
        self.D6.raise_()
        self.B3.raise_()
        self.F4.raise_()
        self.A3.raise_()
        self.A4.raise_()
        self.C6.raise_()
        self.E3.raise_()
        self.start.raise_()
        self.delme.raise_()
        self.exit.raise_()
        self.D4.raise_()
        self.comboBox.raise_()
        self.G4.raise_()
        self.D2.raise_()
        self.vospr.raise_()
        self.info.raise_()
        self.C4.raise_()
        self.G2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIANO"))
        self.stop.setText(_translate("MainWindow", "Закончить запись"))
        self.start.setText(_translate("MainWindow", "Начать запись"))
        self.delme.setText(_translate("MainWindow", "Удалить запись"))
        self.exit.setText(_translate("MainWindow", "Закрыть"))
        self.vospr.setText(_translate("MainWindow", "Воспроизвести запись"))
        self.info.setText(_translate("MainWindow", "О программе"))
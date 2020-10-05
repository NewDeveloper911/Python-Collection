# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype_app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def delayAction(self, MainWindow):
        triggered = False
        if triggered == False:
            import mymodule as pepper
            pepper.smallest(2,2,4,10)
            triggered = True
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pepperbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pepperbutton.setGeometry(QtCore.QRect(70, 160, 341, 51))
        self.pepperbutton.setObjectName("pepperbutton")
        self.pepperbutton.clicked.connect(self.delayAction)
        
        self.cabbutton = QtWidgets.QPushButton(self.centralwidget)
        self.cabbutton.setGeometry(QtCore.QRect(70, 260, 341, 51))
        self.cabbutton.setObjectName("cabbutton")
        self.mugbutton = QtWidgets.QPushButton(self.centralwidget)
        self.mugbutton.setGeometry(QtCore.QRect(70, 360, 341, 51))
        self.mugbutton.setObjectName("mugbutton")
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(70, 30, 341, 51))
        self.titlelabel.setAutoFillBackground(False)
        self.titlelabel.setObjectName("titlelabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_recipe = QtWidgets.QAction(MainWindow)
        self.actionNew_recipe.setObjectName("actionNew_recipe")
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prototype app"))
        self.pepperbutton.setText(_translate("MainWindow", "Red chili pepper sauce "))
        self.cabbutton.setText(_translate("MainWindow", "Vegetable medley pot stew"))
        self.mugbutton.setText(_translate("MainWindow", "Strawberries and cream mug cake"))
        self.titlelabel.setText(_translate("MainWindow", "Welcome to my prototype for my Python-based cookbook application"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_recipe.setText(_translate("MainWindow", "New recipe..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

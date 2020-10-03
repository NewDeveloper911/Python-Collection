# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusbar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow): #MainWindow is the main window that shows
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 567)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 480, 391, 61))

        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.PictureMap = QtWidgets.QLabel(self.centralwidget)
        self.PictureMap.setGeometry(QtCore.QRect(6, 2, 581, 311))

        font = QtGui.QFont()
        font.setPointSize(72)

        self.PictureMap.setFont(font)
        self.PictureMap.setText("")
        self.PictureMap.setPixmap(QtGui.QPixmap("../Desktop/kfc secret spice blend#1.PNG"))
        self.PictureMap.setScaledContents(True)
        self.PictureMap.setObjectName("PictureMap")

        self.kfcsecret = QtWidgets.QPushButton(self.centralwidget)
        self.kfcsecret.setGeometry(QtCore.QRect(60, 350, 181, 81))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kfcsecret.setFont(font)
        self.kfcsecret.setObjectName("kfcsecret")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 350, 191, 81))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionPopup = QtWidgets.QAction(MainWindow)
        self.actionPopup.setObjectName("actionPopup")
		
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionSelect_All)
   		
        self.menuEdit.addAction(self.actionPopup)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "This label is used to display button and shortcut changes"))
        self.kfcsecret.setText(_translate("MainWindow", "KFC secret recipe"))
        self.pushButton_2.setText(_translate("MainWindow", "Mountain image"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New.."))
        self.actionNew.setStatusTip(_translate("MainWindow", "Creates a new recipe"))
        self.actionNew.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open an existing recipe file on file explorer"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves a new recipe"))
        self.actionSave.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Saves the name of a recipe"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Alt+Shift+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copies selected text"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Alt+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Pastes previously copied text"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Alt+P"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setStatusTip(_translate("MainWindow", "Cuts out selected text"))
        self.actionCut.setShortcut(_translate("MainWindow", "Alt+X"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setStatusTip(_translate("MainWindow", "Selects all of the text visible by the user"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Alt+Shift+A"))
		
        self.actionPopup.setText(_translate("MainWindow", "Popup"))
        self.actionPopup.setShortcut(_translate("MainWindow", "Alt+Shift+P"))
        self.actionPopup.triggered.connect(self.show_popup)
        self.kfcsecret.clicked.connect(self.show_chicken)
        self.pushButton_2.clicked.connect(self.show_mountain)
        
    def show_mountain(self):
          self.PictureMap.setPixmap(QtGui.QPixmap("../Desktop/mountain.jpg"))

    def show_chicken(self):
          self.PictureMap.setPixmap(QtGui.QPixmap("../Desktop/kfc secret spice blend#1.PNG"))  
    
    
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Welcome to KFC")
        msg.setText("Hello, madamsir, what can I get you?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ignore|QMessageBox.Cancel|QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("At Kentucky Fried Chicken, humble employees such as I in this humble institution, would love to offer you some of the finest fast food in the world")
        msg.setDetailedText("Are you a breasts or thigh guy, because at this exquisite high-speed restaurant, we specialise in both")
        
        msg.buttonClicked.connect(self.popup_button)
        
        x = msg.exec_()
        
    def popup_button(self,i): #i is the widget that we clicked
        print(i.text())
        if i.text() != "OK":
            print("May I please inform you of our 90% quarantine discount, madamsir? Please stay and order something! Millions of underpaid staff depend on this interaction, madamsir")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

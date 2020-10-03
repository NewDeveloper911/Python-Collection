from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(0,0,600,700)
		self.setWindowTitle("Nano Dirty Dungeon")
		self.initUI()
	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Good afternoon, folks")
		self.label.move(50, 50)

		self.button = QtWidgets.QPushButton(self)
		self.button.setText("place that dirty rodent on me and press")
		self.button.clicked.connect(self.click)
	def click(self):
		self.label.setText("Congratulations. You are now unofficially a simp")
		self.update()	

	def update(self):
		self.label.adjustSize()
		self.button.adjustSize()

	
	
def click():
	print("clicked a button")

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()

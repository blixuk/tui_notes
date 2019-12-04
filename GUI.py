
import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize

class ExampleWindow(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)

		self.windowX = 480
		self.windowY = 600

		self.textAreaX = 20
		self.textAreaY = 10

		self.textAreaWidth = self.windowX - (self.textAreaX * 2)
		self.textAreaHeight = self.windowY - (self.textAreaY * 2)

		self.setMinimumSize(QSize(self.windowX, self.windowY))
		self.setWindowTitle("---")

		# Add text field
		self.b = QPlainTextEdit(self)
		self.b.insertPlainText("You can write text here.\n")
		self.b.move(self.textAreaX,self.textAreaY)
		self.b.resize(self.textAreaWidth,self.textAreaHeight)

		self.vbox = QVBoxLayout()
		self.vbox.addWidget(self.b)
		self.vbox.addStretch()

		self.setLayout(self.vbox)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = ExampleWindow()
	mainWin.show()
	sys.exit( app.exec_() )
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtCore,QtGui,QtWidgets
import sys




ui,_ = loadUiType('Claculator.ui')
class Calculator(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,800,450)
        # self.setWindowIcon(QIcon,("salon.jpg"))
        self.setupUi(self)
        self.handlebutton()
        self.actions()
        self.show()


    def handlebutton(self):
        self.pushButton_10.clicked.connect(self.calculation)
        pass



    def calculation(self):
        result = self.lineEdit_2.text()
        final = eval(result)
        self.lineEdit_7.setText(str(final))

    def actions(self):
        self.pushButton_21.clicked.connect(self.sum)
        self.pushButton_33.clicked.connect(self.minus)
        self.pushButton_47.clicked.connect(self.multi)
        self.pushButton_48.clicked.connect(self.div)
        self.pushButton_c.clicked.connect(self.clear)
        self.pushButton_64.clicked.connect(self.exit)




        self.pushButton_1.clicked.connect(self.perform1)
        self.pushButton_2.clicked.connect(self.perform2)
        self.pushButton_3.clicked.connect(self.perform3)
        self.pushButton_4.clicked.connect(self.perform4)
        self.pushButton_5.clicked.connect(self.perform5)
        self.pushButton_6.clicked.connect(self.perform6)
        self.pushButton_7.clicked.connect(self.perform7)
        self.pushButton_8.clicked.connect(self.perform8)
        self.pushButton_9.clicked.connect(self.perform9)
        self.pushButton_0.clicked.connect(self.perform0)
        self.pushButton_c_3.clicked.connect(self.perform10)



    def sum(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "+")
    def minus(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "-")
    def multi(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "*")
    def div(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "/")
    def clear(self):
        self.lineEdit_2.setText("")
        self.lineEdit_7.setText("")
    def exit(self):
        sys.exit(Calculator)





    def perform1(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "1")
    def perform2(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "2")
    def perform3(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "3")
    def perform4(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "4")
    def perform5(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "5")
    def perform6(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "6")
    def perform7(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "7")
    def perform8(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "8")
    def perform9(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "9")
    def perform0(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + "0")
    def perform10(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.setText(text + ".")





def main():
    app= QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


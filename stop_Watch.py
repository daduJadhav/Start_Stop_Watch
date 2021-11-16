from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

se = 0; mn = 0; hr = 0; stp = 0


class windows(QMainWindow):
    def __init__(self):

        super().__init__()              #   This is a consctor for QMainWindows class
        self.setWindowTitle('Stop Watch')
        self.setGeometry(500,200,800,800)
        self.uiComponents()
        self.show()

    def uiComponents(self):
        self.count = 0
        self.flag = False

        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,500)
        self.label.setStyleSheet("border : 10px solid rgb(0, 255, 242)")
        self.setStyleSheet("color : hsl(0, 94%, 54%)")
        self.label.setText(str(self.count))
        self.label.setFont(QFont('Poppin',125)) 
        self.label.setAlignment(Qt.AlignCenter)

        # Start Button

        start = QPushButton("Start",self)
        start.setFont(QFont('Poppin',20)) 
        start.setGeometry(0,500,800,100)
        # start.setStyleSheet("margin-top : 5px")   
        start.pressed.connect(self.start)



        # stop Button

        stop = QPushButton("Stop",self)
        stop.setFont(QFont('Poppin',20)) 
        stop.setGeometry(0,600,800,100)
        # stop.setStyleSheet("margin-top : 5px")
        stop.pressed.connect(self.stop)

        # stop Button

        restart = QPushButton("Restart",self)
        restart.setFont(QFont('Poppin',20)) 
        restart.setGeometry(0,700,800,100)
        restart.setStyleSheet("backgroud-color : Yellow")
        # restart.setStyleSheet("margin-top : 5px")
        restart.pressed.connect(self.restart)


        # for timer : 
        timer = QTimer(self)    #now pyQt5 comes with its own timer 
        timer.timeout.connect(self.show_Timer)
        timer.start(100)

    def show_Timer(self):
        if self.flag:
            self.count = self.count+1
        
        text = str(self.count/10)
        self.label.setText(text)
    
    def start(self):
        self.flag = True

    def stop(self):
        self.flag = False

    def restart(self):
        self.flag = False
        self.count = 0
        self.label.setText(str(self.count))



App = QApplication(sys.argv)
window = windows()
sys.exit(App.exec())
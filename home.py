import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from MenuBarre import Barre
from menu import Menu
from Message import Message


class Title(QWidget) :
    def __init__(self) :
        super().__init__()
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 0)
        
        frame = QFrame()
        frame.setGraphicsEffect(shadow)
        frame.setObjectName("fram")
        self.central , centr= QHBoxLayout(self), QHBoxLayout()
        
        font = QFont("ubuntu", 20)
        font.setBold(True)
        
        self.title = QLabel("ChatApp")
        self.title.setStyleSheet("color : #2C48A1;")
        self.title.setFont(font)
        
        self.menu_barr = QPushButton(icon= QIcon("Style/menu.png"))
        self.menu_barr.setIconSize(self.menu_barr.sizeHint())
        self.menu_barr.setObjectName("rond")
        
        centr.addWidget(self.title), centr.addStretch(), centr.addWidget(self.menu_barr)
        self.title.setContentsMargins(100, 0, 0, 0)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        frame.setLayout(centr)
        self.central.addWidget(frame)
        
        
class Corps(QWidget) :
    def __init__(self) :
        super().__init__()
        self.central_lay = QVBoxLayout(self) 
        frame, box = QFrame(), QVBoxLayout()
        frame.setObjectName("fram")
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 0)
        frame.setGraphicsEffect(shadow)
        
        self.mess = Message()
        self.stack = QStackedWidget()
        
        self.stack.addWidget(self.mess)
        
        box.addWidget(self.stack)
        
        frame.setLayout(box)
        
        self.setFixedWidth(700)
        
        self.central_lay.addWidget(frame)
        
        

class Home(QWidget) :
    def __init__(self) :
        super().__init__()
        self.central_lay = QVBoxLayout(self) 
        box = QVBoxLayout()
    
        self.menu = Menu()
        self.title = Title()
        self.barre = Barre()
        self.corps = Corps()
        centr = QVBoxLayout()
        
        self.hbox =  QHBoxLayout()
        
        
        self.hbox.addWidget(self.menu)
        self.hbox.addWidget(self.corps)
        self.hbox.addWidget(self.barre)
        
        self.barre.setHidden(True)
        
        centr.addWidget(self.title)
        centr.addLayout(self.hbox)

        self.central_lay.addLayout(centr)  
        self.setWindowTitle("Chat Application")
        self.setFixedSize(1000, 650)      
        
        
        #self.setStyleSheet(open("Style/style.qss", 'r').read())
        
        self.title.menu_barr.clicked.connect(self.slotss)
    
    def slotss(self) :
        if self.barre.isVisible() :
            self.barre.setHidden(True)
        else :
            self.barre.setHidden(False)
        
if __name__== '__main__':
    app =QApplication(sys.argv)
    hom = Home()
    hom.show()
    app.exec()


        

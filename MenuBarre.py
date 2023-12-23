from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class Barre(QWidget) :
    def __init__(self) :
        super().__init__()
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 0)
        
        self.central_lay = QVBoxLayout(self) 
        frame, box = QFrame(), QVBoxLayout()
        frame.setObjectName("fram")
        frame.setGraphicsEffect(shadow)
        
        font = QFont("ubuntu", 12)
        font.setBold(True)
        
        self.dict = {
            "font"  : QPushButton(icon=QIcon("Style/font.png"), text= "     Font"),
            "background" : QPushButton(icon=QIcon("Style/background.png"), text = "     Background"),
            "paint" : QPushButton(icon= QIcon("Style/paint.png"), text="      Paint")    
        }
        
        [box.addWidget(widg) for widg in list(self.dict.values())]
        [[self.dict[name].setIconSize(self.dict[name].sizeHint()), self.dict[name].setStyleSheet("color: #2C48A1;"), self.dict[name].setFont(font)] for name in ["font", "background", "paint"]]
        frame.setLayout(box)
        self.central_lay.addWidget(frame)
        
        self.setFixedWidth(250)
        


        
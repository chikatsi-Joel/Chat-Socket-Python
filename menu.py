from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class Menu(QWidget) :
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
            "home"  : QPushButton(icon=QIcon("Style/home.png"), text= "     Home"),
            "mess" : QPushButton(icon=QIcon("Style/chat.png"), text = "     Message"),
            "amis" : QPushButton(icon= QIcon("Style/add.png"), text="      Amis"),
            "notification" : QPushButton(icon=QIcon("Style/notification.png"), text= "   Notification"),
            "params" : QPushButton(icon=QIcon("Style/settings.png"), text= "  Paramètre")         
        }
        
        [box.addWidget(widg) for widg in list(self.dict.values())[:-1]]
        box.addStretch(), box.addWidget(self.dict["params"]), box.addSpacing(100)
        [[self.dict[name].setIconSize(self.dict[name].sizeHint()), self.dict[name].setStyleSheet("color: #2C48A1;"), self.dict[name].setFont(font)] for name in ["home", "mess", "amis", "notification", "params"]]
        frame.setLayout(box)
        self.central_lay.addWidget(frame)
        
        self.setFixedWidth(200)


        
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from datetime import date


class ClavEntete(QWidget) :
    
    def __init__(self) -> None:
        super().__init__()
        self.vbox=QVBoxLayout(self)

class Clavier(QWidget) :
    
    def __init__(self) -> None:
        super().__init__()
        self.vbox=QVBoxLayout(self)
        self.frame, self.group=QGroupBox(), QGroupBox()
        self.hbox=QHBoxLayout()
        self.edit = QTextEdit()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.clav = QGridLayout(scroll_content)
        self.edit.setFont(QFont("Segoe UI Emoji", 12))
        self.edit.setMaximumHeight(40)
        self.send = QPushButton()
        self.emoji = QPushButton()
        box = QVBoxLayout()
        
        scroll_area.setWidget(scroll_content)
        
        [self.hbox.addWidget(value) for value in [self.emoji, self.edit, self.send]]
        [value.setObjectName("bh") for value in [self.emoji, self.send]]
        
        self.group.setLayout(self.hbox)
        self.group.setObjectName("group")
        self.group.setFixedHeight(90)
        
        box.addWidget(scroll_area)
        self.frame.setLayout(box)
        self.frame.setHidden(True)
        
        self.list_lab=[QPushButton(i) for i in ["\U0001F60A", "\U0001F609", "\u2764\ufe0f", "\U0001F602", "\U0001F618", "\U0001F61B", "\U0001F61E", "\U0001F622", "\U0001F621", "\U0001F631", "\U0001F494", "\U0001F60A", "\U0001F917", "\U0001F60D"]]
        [button.setFont(QFont("Segoe UI Emoji", 14)) for button in self.list_lab]
        [button.setObjectName("prod")  for button in self.list_lab]
        for i in range(len(self.list_lab)) :
            self.clav.addWidget(self.list_lab[i], i//4, i%4)
        
        self.vbox.addWidget(self.group)
        self.vbox.addWidget(self.frame)
        
        self.emoji.clicked.connect(self.emojis_slot)
        self.emoji.setIcon(QIcon("Style/stick.png"))
        self.emoji.setIconSize(self.emoji.sizeHint())
        
        
        self.send.setIcon(QIcon("Style/send.png"))
        self.send.setIconSize(self.emoji.sizeHint())
        
        self.frame.setFixedHeight(100)
        
        [val.clicked.connect(self.writeEmojie) for val in self.list_lab]
        
        
    def emojis_slot(self) :
        if self.frame.isVisible() :
            self.frame.setHidden(True) 
            
        else :
            self.frame.setHidden(False)
    @pyqtSlot()
    def writeEmojie(self) :
        sender = self.sender()

        for val in self.list_lab :
            if val == sender :
                self.edit.setText(self.edit.toPlainText()+val.text())
                break



class Head(QWidget) :
    def __init__(self) :
        super().__init__()
        self.back = QPushButton(icon=QIcon("Style/back.png"))
        self.profil = QPushButton(icon=QIcon("Style/contact.png"))
        self.infos = QLabel()
        self.bloq = QPushButton(icon=QIcon("Style/block.png"))

        v, self.central  = QVBoxLayout(), QHBoxLayout(self)
        v.addWidget(self.profil), v.addWidget(self.infos)
        
        
        self.central.addWidget(self.back), self.central.addLayout(v), self.central.addWidget(self.bloq)

        [[value.setObjectName("bh"), value.setFixedSize(80, 80)] for value in [self.back]]
        #self.profil.setObjectName("prof")
        self.profil.setFixedSize(60, 60)
        self.bloq.setFixedSize(60, 60)
        self.bloq.setStyleSheet("border: none;")
        self.infos.setText("connecté à 18 h 00.")
        self.profil.setIconSize(self.profil.size())
        
        self.bloq.setIconSize(self.bloq.size())
        
        
        self.profil.setStyleSheet("border: none;")
        self.back.setIconSize(self.back.sizeHint())
        self.bloq.setIconSize(self.bloq.sizeHint())
        self.profil.setIconSize(self.profil.sizeHint())
        
        self.bloq.clicked.connect(lambda: print("Bonjour.."))
        
class BoxMessage(QWidget) :
    def __init__(self) :
        super().__init__()
        
        self.central_lay, self.centr = QVBoxLayout(self), QVBoxLayout() 
        frame = QFrame()      
        font = QFont("ubuntu", 12)
        font.setBold(True)
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setObjectName("frameMess")
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.vbox = QVBoxLayout(self.scroll_content)
        
        self.scroll_area.setWidget(self.scroll_content)
        
        self.centr.addWidget(self.scroll_area)
        frame.setLayout(self.centr)
        self.central_lay.addWidget(frame)
        
        
    
    def sendMess(self, mess : str) :
        if mess.strip() != "" :
            label = QLabel(mess)
            label.setObjectName("mess")
            font=QFont("Segoe UI Emoji", 9)
            font.setBold(True)
            label.setFont(font), label.setWordWrap(True)
            frame = QFrame()
            frame.setObjectName("mess")
            box = QHBoxLayout()
            box.addStretch()
            bx = QVBoxLayout()
            bx.addWidget(label)
            frame.setLayout(bx)
            label.setFixedWidth(150)
            box.addWidget(frame)
            self.vbox.addLayout(box)
            
            
    def receiveMess(self, mess : str) :
        if mess.strip() != "" :
            label = QLabel(mess)
            label.setObjectName("mess")
            font=QFont("Segoe UI Emoji", 9)
            font.setBold(True)
            label.setFont(font), label.setWordWrap(True)
            frame = QFrame()
            frame.setObjectName("mess")
            box = QHBoxLayout()
            bx = QVBoxLayout()
            bx.addWidget(label)
            frame.setLayout(bx)
            label.setFixedWidth(150)
            box.addWidget(frame)
            box.addStretch()
            self.vbox.addLayout(box)
        
class Message(QWidget) :
    index = 0
    def __init__(self) :
        super().__init__()
        
        
        self.central_lay = QVBoxLayout(self) 
        box = QVBoxLayout()
        frame = QFrame()      
        font = QFont("ubuntu", 12)
        font.setBold(True)
        
        self.dict = {
            "head"  : Head(),
            "corps" : BoxMessage(),
            "clav" : Clavier()   
        }
        b = QVBoxLayout()
        b.addWidget(self.dict["head"])
        frame.setLayout(b)
        self.central_lay.addWidget(frame)
        frame.setStyleSheet("background-color: rgb(166, 192, 230);")
        for value in list(self.dict.values())[1:]:
            self.central_lay.addWidget(value)
        
        
        self.dict["clav"].send.clicked.connect(self.sendMess)
        
    def sendMess(self) :
        mess = self.dict["clav"].edit.toPlainText()
        self.dict["corps"].sendMess(mess)
        self.dict["clav"].edit.setText("")
        self.dict["clav"].frame.setHidden(True)
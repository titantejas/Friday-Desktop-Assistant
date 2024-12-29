from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(3264, 1834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1930, 1045))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.terminal = QtWidgets.QTextBrowser(self.centralwidget)
        self.terminal.setGeometry(QtCore.QRect(0, 740, 600, 300))
        self.terminal.setStyleSheet("""
            background:transparent;                        
            color: white;
            font-size: 18px;
            font-family: Courier;
            border-radius: 10px;
            border: none;
            padding: 10px;
        """)
        self.terminal.setObjectName("terminal")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 150, 480, 480))
        self.label_7.setText("")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

     
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1184, 560, 250, 250))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 560, 250, 250))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_2")

 
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 600, 701, 241))
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 0, 701, 241))
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1380, 1, 211, 61))
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1380, 40, 211, 61))
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1380, 81, 211, 61))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1430, 15, 181, 41))
        self.textBrowser.setStyleSheet("background:transparent;\n"
                                       "border:none;\n"
                                       "color:white;\n"
                                       "font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1440, 56, 181, 41))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
                                       "border:none;\n"
                                       "color:white;\n"
                                       "font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1460, 97, 181, 41))
        self.textBrowser_3.setStyleSheet("background:transparent;\n"
                                       "border:none;\n"
                                       "color:white;\n"
                                       "font-size:20px;")
        self.textBrowser_3.setObjectName("textBrowser_3")
     
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(1650, 970, 120, 60))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStart.setStyleSheet(    """
    QPushButton {
        background:darkgreen;
        border: none;
        color: white;
        font-size: 40px;
        font-weight: bold;
        border-radius: 10px;
    }
    QPushButton:hover {
        background:green; 
    }
    """
)
        self.pushButtonStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonStart.setText("RUN")


        opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.8)  
        self.pushButtonStart.setGraphicsEffect(opacity_effect)


        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(1780, 970, 120, 60))
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.pushButtonExit.setStyleSheet(    """
    QPushButton {
        background:darkred;
        border: none;
        color: white;
        font-size: 40px;
        font-weight: bold;
        border-radius: 10px;
    }
    QPushButton:hover {
        background: red; 
    }
    """
)
        self.pushButtonStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonExit.setText("EXIT")



        opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.8)  
        self.pushButtonExit.setGraphicsEffect(opacity_effect)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Friday"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

   
    ui.label.setMovie(QtGui.QMovie("C:/Users/Sansk/OneDrive/Documents/1111.gif"))
    ui.label.movie().start()


    
    ui.label_5.setPixmap(QtGui.QPixmap("C:/Users/Sansk/OneDrive/Documents/Picsart_24-12-09_18-12-53-545.png"))
    ui.label_6.setPixmap(QtGui.QPixmap("C:/Users/Sansk/OneDrive/Documents/Picsart_24-12-09_18-12-53-545.png"))
    ui.label_9.setPixmap(QtGui.QPixmap("C:/Users/Sansk/OneDrive/Documents/Picsart_24-12-09_18-12-53-545.png"))

    MainWindow.show()
    sys.exit(app.exec_())
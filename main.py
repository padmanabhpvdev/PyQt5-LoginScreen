import sys,login
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class LoginScreen(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint|Qt.SplashScreen)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = login.Ui_Form()
        self.ui.setupUi(self)

if __name__=="__main__":

    app = QApplication(sys.argv)
    ls = LoginScreen()
    ls.show()
    sys.exit(app.exec_())

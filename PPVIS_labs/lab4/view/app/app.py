# pyqt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QStackedWidget

# MVP
from view.app.windows.pin_window import PinWindow
from view.app.windows.atm_window import AtmWindow
from presenter.presenter import Presenter
from model.model import Model

# system
import sys



class App(QApplication):
    ''' class of ui app has all parts of MVP '''
    
    def __init__(self, *args):
        super().__init__(list(args))
        # view
        self.widget = QStackedWidget()
        self.pin_view = PinWindow()
        self.atm_view = AtmWindow()
        # model
        self.model = Model()
        # presenter
        self.presenter = Presenter(view=self, model=self.model)
        self.init_app()
        

    def init_app(self):
        # add widgets
        self.widget.addWidget(self.pin_view)
        self.widget.addWidget(self.atm_view)
        # sizes
        self.widget.setFixedHeight(600)
        self.widget.setFixedWidth(800)
        # show
        self.widget.setCurrentWidget(self.pin_view)
        self.widget.show()



def application():
    app = App(sys.argv)
    app.setApplicationName('ATM')
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    application()
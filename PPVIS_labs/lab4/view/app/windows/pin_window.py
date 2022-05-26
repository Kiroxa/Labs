from PyQt5.QtWidgets import QMainWindow, QMessageBox
from view.app.ui.pin_menu import PinUI


class PinWindow(QMainWindow):
    def __init__(self):
        super(PinWindow, self).__init__()
        self.ui = PinUI(self)
        self.init_UI()
                
    def init_UI(self):
        ''' hide interface while card not choosen '''
        self.hide_interface()

    def hide_interface(self):
        ''' Hide a pin interface while card not chose or session not loaded ''' 
        
        self.ui.confirm_button.hide()
        self.ui.pin_label.hide()
        self.ui.pin_edit.hide()
        self.ui._enter_text_label.hide()
        
    def show_interface(self):
        self.ui.confirm_button.show()
        self.ui.pin_label.show()
        self.ui.pin_edit.show()
        self.ui._enter_text_label.show()
        # hide enter buttons
        self.ui.enter_card_button.hide()
        self.ui.load_session_button.hide()
        
    @staticmethod
    def error_message(window_title: str, text: str):
        ''' raise an error window when some problem '''
        
        error = QMessageBox()
        error.setWindowTitle(window_title)
        error.setText(text)
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        error.exec_()

        

  
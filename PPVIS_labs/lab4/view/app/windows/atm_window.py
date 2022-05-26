from PyQt5.QtWidgets import QMainWindow
from view.app.ui.atm_menu import AtmUI


class AtmWindow(QMainWindow):
    def __init__(self):
        super(AtmWindow, self).__init__()
        self.ui = AtmUI(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
        
    def info_about_user(self, user):
        self.ui.about_user_label.setText(user.__str__())
        
    def payment_screen(self, from_card, to_phone, total_cash, result):
        ''' show payment result '''
        
        self.ui.atm_screen_label.setText('\n'.join(
            [result,
            "From card: "+from_card,
            "To phone: "+to_phone,
            "Total cash: "+total_cash]
        ))
        
    def withdraw_screen(self, from_card, total_cash, result):
        ''' show withdraw result '''
        
        self.ui.atm_screen_label.setText('\n'.join(
            [result,
            "From card: "+from_card,
            "Cash to withdraw: "+total_cash]
        ))
        
    def hide_interface(self):
        pass
        # self.ui.cash_edit.hide()
        # self.ui.phone_edit.hide() 
        
        # self.ui.balance_button
        # self.ui.exit_button
        # self.ui.payment_button
        # self.ui.save_session_button
        # self.ui.withdraw_button
        
from PyQt5.QtWidgets import QFileDialog

import json


class Presenter:
    ''' it is glue between view and model '''
    
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.init_view()

    def init_view(self):
        ''' set all view buttons and action True '''
        
        # pin init
        self.view.pin_view.ui.enter_card_button.clicked.connect(self.enter_card)
        self.view.pin_view.ui.load_session_button.clicked.connect(self.load_session)
        self.view.pin_view.ui.confirm_button.clicked.connect(self.succesful_enter)
        # atm init
        self.view.atm_view.ui.balance_button.clicked.connect(self.show_balance)
        self.view.atm_view.ui.exit_button.clicked.connect(self.exit_session)
        self.view.atm_view.ui.payment_button.clicked.connect(self.transfer_payment)
        self.view.atm_view.ui.withdraw_button.clicked.connect(self.withdraw_cash)
        self.view.atm_view.ui.save_session_button.clicked.connect(self.save_session)

    def open_file_dialog(self):
        ''' while you want to load card '''
        fname = QFileDialog.getOpenFileName(self.view.pin_view)[0]
        try:
            with open(fname, 'r') as f:
                data = json.load(f)
                return data 
        except Exception as e:
            print(e.__str__())
            print("Couldn't open a file!")
        
    def enter_card(self):
        card_data = self.open_file_dialog()
        if self.model.get_card_data(card_data):
            self.view.pin_view.show_interface()
        
    def load_session(self):
        old_sessoin_data = self.open_file_dialog()
        if self.model.get_old_session_data(old_sessoin_data):
            self.view.pin_view.show_interface()

    def update_user_info(self):
        self.view.atm_view.info_about_user(user=self.model.user)

    def succesful_enter(self):
        ''' this is GUI security card PIN to start session '''
        
        enter_pin = self.view.pin_view.ui.pin_edit.toPlainText()
        answer, attempts = self.model.pin_is_valid(pin=enter_pin)
        if answer:
            self.view.widget.setCurrentWidget(self.view.atm_view)
            self.update_user_info()
        else:
            if attempts == 0:
                self.view.pin_view.error_message(window_title=f"Blocked", text=f"Card is blocked!")
                exit()
            else:
                self.view.pin_view.error_message(window_title=f"Invalid PIN", text=f"PIN isn't true\nattemts: {attempts}")
                self.view.pin_view.ui.pin_edit.setPlainText("")
                
    def show_balance(self):
        ''' create balance check '''
        
        balance = self.model.client.get_balance()
        self.view.atm_view.ui.atm_screen_label.setText(f"Balance: {balance}")
        
    def transfer_payment(self):
        ''' From card -> to phone '''
        phone_number = self.view.atm_view.ui.phone_edit.toPlainText()
        cash = self.view.atm_view.ui.cash_edit.toPlainText()
        result = self.model.pay_for_phone(phone=phone_number, cash=cash)
        if self.check_payment_result(result):
            self.view.atm_view.payment_screen(from_card=self.model.user.card.number, to_phone=phone_number, total_cash=cash, result=result)
            self.update_user_info() 
            
    def withdraw_cash(self):
        ''' From card -> to wallet '''
        
        cash = self.view.atm_view.ui.cash_edit.toPlainText()
        result = self.model.withdraw_cash(cash=cash)
        if self.check_withdraw(result):
            self.view.atm_view.withdraw_screen(from_card=self.model.user.card.number, total_cash=cash, result=result)
            self.update_user_info()     
            
    def check_withdraw(self, result):
        ''' Compare money in card and requested money '''
        
        if result == "not money":
            self.view.pin_view.error_message(window_title="No money", text="Not enought money or incorrect cash!")
            return False
        elif result == "incorrect withdraw":
            self.view.pin_view.error_message(window_title="Incorrect withdraw", text="Check withdraw cash!")
            return False        
        return True 
        
        
    def check_payment_result(self, result):
        ''' Check if operation success or error '''
        
        if result == "incorrect phone":
            self.view.pin_view.error_message(window_title="Incorrect phone number", text="You should print +375(xx)xxx-xx-xx !")
            return False
        elif result == "not money":
            self.view.pin_view.error_message(window_title="No money", text="Not enought money or incorrect cash!")
            return False
        return True 
                
    def save_session(self):
        ''' when press save session '''
        
        session_data = self.model.get_session_data()
        
        fname = QFileDialog.getSaveFileName(self.view.atm_view)[0]
        try:
            with open(fname, 'w') as f:
                json.dump(session_data, f, indent=4)
        except Exception as e:
            print(e.__str__())
            print("couldn't save file!")

    @staticmethod
    def exit_session():
        exit()
    

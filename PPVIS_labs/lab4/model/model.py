from model.customer.atm_client import ATMClient
from model.bank.bank import Bank
from model.customer.user import User
from db.db_and_files import Server


class Model:
    def __init__(self):
        # bank
        self.belbank = Bank()
        
    def get_card_data(self, data):
        if data:
            self.card_data = data
            # continue init
            self.fill_bank_storage(data)
            self.create_bank_user(data)
            self.init_bank_client()
            # print(self.card_data)
            return True
        return False 
    
    def get_old_session_data(self, data):
        if data:
            self.old_session_data = data
            # continue init
            self.fill_bank_storage(data)
            self.create_bank_user(data)
            self.init_bank_client()
            return True
        return False 
    
    def fill_bank_storage(self, data):
        self.belbank.atm.storage.fund = data["fund"]
        
    def create_bank_user(self, data):
        # user 
        self.user = User(card_number=data["user_card_number"], phone_number=data["user_phone_number"])
        self.user.wallet.store = data["user_wallet"]
        
    def init_bank_client(self):
        # client
        self.client = ATMClient(self.user, self.belbank.atm)
        # self.client.insert_card(mode="app")

    def draft(self):
        # DRAFT
        msg = ""
        msg += "\nDraft: \n"
        msg += self.user.__str__()
        msg += "\nbank storage: \n"
        msg += self.belbank.atm.storage.__str__()
        return msg 

    def pay_for_phone(self, phone, cash):
        return self.client.phone_payment(app={
            "phone": phone,
            "cash": cash,
        })
        
    def withdraw_cash(self, cash):
        return self.client.withdraw_cash(app_cash=cash)
        
    def get_session_data(self):
        return self.client.save_process(app=True)
        
    def pin_is_valid(self, pin):
         return_pin, attempts = self.client.insert_card(
             app={
                 "pin": pin,
             }
         )
        #  print(return_pin)
         if return_pin:
             return return_pin, attempts
         return False, attempts 
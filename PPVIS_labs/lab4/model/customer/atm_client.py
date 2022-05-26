from model.bank.bank import ATM, Bank
from model.customer.user import User, Phone
from db.db_and_files import Server


class ATMClient:
    __attempts = 3

    def __init__(self, user: User, atm: ATM) -> None:
        self.__atm = atm 
        self.__user = user
        self.__session_phone_number = ""
        self.__session_phone_balance = 0
        # update phone balance
        self.__user.phone.balance = Bank.get_phone_balance(self.user.phone.number)

    @property
    def atm(self) -> ATM:
        return self.__atm
    
    @property
    def attempts(self):
        return self.__attempts

    @property
    def session_phone_number(self) -> str:
        return self.__session_phone_number

    @session_phone_number.setter
    def session_phone_number(self, number) -> None:
        self.__session_phone_number = number

    @property
    def session_phone_balance(self) -> int:
        return self.__session_phone_balance

    @session_phone_balance.setter
    def session_phone_balance(self, cash: int) -> None:
        try:
            self.__session_phone_balance += cash
        except TypeError as te:
            cash = 0
            self.__session_phone_balance += cash
    
    @property
    def user(self) -> User:
        return self.__user 

    @property
    def true_pin(self) -> str:
        return self.__true_pin

    @classmethod
    def check_attempts(cls, app: bool = False) -> None: 
        if cls.__attempts == 0 and not app:
            print("Card is blocked!")
            raise SystemExit

    def insert_card(self, app: dict = {}) -> bool:
        for card_data in Bank.get_cards_data().keys():
            if self.user.card.number == card_data[0]:
                # print("pass card data")
                self.__true_pin = card_data[1]        
                if self.valid(app=app):
                    if app:
                        return self.true_pin, int(self.attempts)
                    else:
                        self.session()
                        return True

        print("Uncknown card number!")
        if app:
            return False, int(self.attempts)
        else:
            return False
    
    def show_menu(self) -> str:
        menu_buttons = ['0', '1', '2', '3']
        print(
            "1 - Show balance",
            "2 - Withdraw cash",
            "3 - Phone payment",
            "0 - exit", 
            sep = "\n"
        )
        while True:
            try:
                operation = input("Enter: ")
                if operation not in menu_buttons:
                    raise ValueError
                return operation
            except ValueError as v:
                print("Incorrect button!")
                
    def session(self) -> None:
        operation = ''
        while operation != '0':
            operation = self.show_menu()

            if operation == '1':
                balance = self.get_balance()
                print("Balance: ", balance)
            elif operation == '2':
                self.withdraw_cash()
            elif operation == '3':
                self.phone_payment()

        self.save_process()

    def valid(self, app: dict = {}):
        if app:
            pin = app["pin"]
        else:
            pin = input("PIN: ")

        while not Bank.check_pin(pin, self.true_pin):
            ATMClient.__attempts -= 1
            ATMClient.check_attempts(app=app)
            if app:
                return False
            else: 
                pin = input("try again! PIN: ")

        ATMClient.__attempts = 3
        return True

    def get_balance(self) -> int:
        return Bank.get_card_balance(self.get_card_data())

    def get_card_data(self) -> tuple:
        return (self.user.card.number, self.true_pin)    

    @staticmethod
    def enter_cash() -> int:
        while True:
            try:
                cash = int(input("Enter cash: "))
                break 
            except ValueError as v:
                print("Incorrect number!")
        return cash

    def withdraw_cash(self, app_cash = None) -> bool:
        while True:
            if not app_cash:
                cash = ATMClient.enter_cash()
            else:
                try:
                    cash = int(app_cash)
                except ValueError as v:
                    return "incorrect withdraw"
            a = Bank.get_all_sum(self.atm.storage.fund)
            # print(a)
            if cash <= a and cash <= self.get_balance():
                money = self.atm.storage.get_money(cash)
                if money:
                    Bank.change_card_balance(self.get_card_data(), -cash)
                    self.user.wallet.store = self.atm.cash_out()
                    if app_cash:
                        return "Succesful!"
                    else: 
                        print("Succesful!")
                        return True
            elif app_cash:
                return "not money"
            else:
                print("Not enought money!")

    def phone_payment(self, app: dict = {}) -> bool:
        while True:
            if app:
                phone_number = app["phone"]
                if not Phone.check_phone_number(phone_number):
                    return "incorrect phone" 
            else:
                while True:
                    phone_number = input("Enter phone number: ")

                    if Phone.check_phone_number(phone_number):
                        break
                    else:
                        print("Incorrect phone number. You should print +375(xx)xxx-xx-xx !")
                
            self.session_phone_number = phone_number
            self.session_phone_balance = Bank.get_phone_balance(self.session_phone_number)

            if app:
                try:
                    cash = int(app["cash"])
                except ValueError as v:
                    cash = 0
            else:
                cash = ATMClient.enter_cash()
            card_balance = self.get_balance()

            if 0 < cash <= card_balance:
                Bank.change_card_balance(self.get_card_data(), -cash)
                
                self.session_phone_balance = cash

                if self.user.phone.number == self.session_phone_number:
                    self.user.phone.balance = cash
                if app:
                    return "Succesful!"
                else: 
                    print("Succesful!")
                    return True
            elif app:
                return "not money" 
            else:
                print("Not enought money or incorrect cash!")      

    def save_process(self, app: bool = False) -> None:
        Server.update_bd(self.user.card.number, Bank.get_card_balance((self.user.card.number, self.true_pin)), \
                                                                self.session_phone_number, self.session_phone_balance)

        if app:
            data = Server.save_in_json_file(self, app)
            return data 
        elif Server.save_in_json_file(self, app):
            print("Process are saved!")
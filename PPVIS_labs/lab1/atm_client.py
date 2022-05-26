from bank import ATM, Bank
from user import User, Phone
from db_and_files import Server


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
        self.__session_phone_balance += cash

    @property
    def user(self) -> User:
        return self.__user 

    @property
    def true_pin(self) -> str:
        return self.__true_pin

    @classmethod
    def check_attempts(cls) -> None:
        if cls.__attempts == 0:
            print("Card is blocked!")
            raise SystemExit

    def insert_card(self) -> bool:
        ''' Check if inserting card is in the bank database, validate card pin and if all right start session '''
        
        for card_data in Bank.get_cards_data().keys():
            if self.user.card.number == card_data[0]:
                self.__true_pin = card_data[1]

                if self.valid():
                    self.session()
                    return True

        print("Unknown card number!")
        return False
    
    def show_menu(self) -> str:
        ''' User "interface" to provide a session '''
        
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
        ''' Process the input number of operation and call specific functions '''
        
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

        # after the closing session, it saves in the json file
        self.save_process()

    def valid(self) -> bool:
        ''' Enter a pin to unlock your card '''
        pin = input("PIN: ")

        while not Bank.check_pin(pin, self.true_pin):
            ATMClient.__attempts -= 1
            ATMClient.check_attempts()
            pin = input("try again! PIN: ")

        # after success
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

    def withdraw_cash(self) -> bool:
        ''' Calculate a right cash that user want to withdraw '''
        
        if self.valid():
            while True:
                cash = ATMClient.enter_cash()
                a = Bank.get_all_sum(self.atm.storage.fund)
                if cash <= a and cash <= self.get_balance():
                    money = self.atm.storage.get_money(cash)
                    if money:
                        Bank.change_card_balance(self.get_card_data(), -cash)
                        self.user.wallet.store = self.atm.cash_out()
                        print("Succesful!")
                        return True
                else:
                    print("Not enought money!")

    def phone_payment(self) -> bool:
        ''' Input a right phone number for payment
            input a right cash for payment '''
            
        while True:
            while True:
                phone_number = input("Enter phone number: ")

                if Phone.check_phone_number(phone_number):
                    break
                else:
                    print("Incorrect phone number. You should print +375(xx)xxx-xx-xx !")
                
            self.session_phone_number = phone_number
            self.session_phone_balance = Bank.get_phone_balance(self.session_phone_number)

            cash = ATMClient.enter_cash()
            card_balance = self.get_balance()

            if 0 < cash <= card_balance:
                Bank.change_card_balance(self.get_card_data(), -cash)
                
                self.session_phone_balance = cash

                if self.user.phone.number == self.session_phone_number:
                    self.user.phone.balance = cash

                print("Succesful!")
                return True      
            else:
                print("Not enought money or incorrect cash!")      

    def save_process(self) -> None:
        ''' When the sesson is ending (enter - "0") 
            we save all balance changes in the file and database '''
            
        Server.update_bd(self.user.card.number, Bank.get_card_balance((self.user.card.number, self.true_pin)), \
                                                                self.session_phone_number, self.session_phone_balance)

        if Server.save_in_json_file(self):
            print("Process are saved!")
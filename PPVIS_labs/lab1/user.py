from banknote import Banknote
import re

class CreditCard:
    def __init__(self, number: str) -> None:
        self.__number = number

    @property
    def number(self) -> str:
        return self.__number

    def __str__(self) -> str:
        return f"Card number: {self.number}"


class Phone:
    def __init__(self, number: str, balance: int = 0) -> None:
        self.__number = number
        self.__balance = balance
    
    @property
    def number(self) -> str:
        return self.__number
    
    @property
    def balance(self) -> int:
        return self.__balance
    
    def __str__(self) -> str:
        return f"Phone number: {self.number}\nPhone balance: {self.balance}"

    @balance.setter 
    def balance(self, money: int) -> None:
        self.__balance += money

    @staticmethod    
    def check_phone_number(phone_number: str) -> bool:
        ''' Check is a input phone number is right by pattern '''
        
        pattern = r'\+375\(\d{2}\)\d{3}-\d{2}-\d{2}'
        if re.match(pattern, phone_number):
            return True
        else:
            return False


class Wallet:
    def __init__(self) -> None:
        self.__store = Banknote.generate_fund() 
    
    @property
    def store(self) -> dict:
        return self.__store

    @store.setter
    def store(self, cash: dict) -> None:
        for c in cash.keys():
            self.__store[c] += cash[c]

    def get_all_sum(self) -> int:
        ''' Return the sum of all money in the wallet '''
        
        all_sum = 0
        for note in self.store.keys():
            for _ in range(self.store[note]):
                all_sum += int(note)

        return all_sum

    def __str__(self) -> str:
        all_sum = self.get_all_sum()
        return f"Wallet: {all_sum}"


class User:
    def __init__(self, card_number: str, phone_number: str) -> None:
        self.__card = CreditCard(card_number)
        self.__wallet = Wallet() 
        self.__phone = Phone(phone_number)

    def __str__(self) -> str:
        view = '\n'.join([self.card.__str__(), self.wallet.__str__(), self.phone.__str__()])
        return view 

    @property
    def card(self) -> CreditCard:
        return self.__card

    @property
    def wallet(self) -> Wallet:
        return self.__wallet

    @property
    def phone(self) -> Phone:
        return self.__phone
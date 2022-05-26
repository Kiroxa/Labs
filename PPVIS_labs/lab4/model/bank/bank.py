from db.db_and_files import Server
from model.bank.banknote import Banknote


class Bank:
    __cards, __phones = Server.get_bd_data()

    def __init__(self) -> None:
        self.atm = ATM()

    def __str__(self) -> str:
        return str(self.__cards) + '\n' + str(self.__phones)

    @classmethod
    def get_cards_data(cls) -> dict:
        return cls.__cards

    @classmethod
    def get_phones_data(cls) -> dict:
        return cls.__phones

    @staticmethod
    def check_pin(pin: str, true_pin: str) -> bool:
        return pin == true_pin

    @classmethod
    def get_card_balance(cls, card_data: tuple) -> int:
        for cd in cls.get_cards_data().keys():
            if card_data == cd:
                return cls.__cards[cd]

    @classmethod
    def get_phone_balance(cls, phone_number: str) -> int:
        for pd in cls.get_phones_data().keys():
            if phone_number == pd:
                return cls.__phones[pd]

    @classmethod
    def change_card_balance(cls, card_data: tuple, value: int) -> None:
        for cd in cls.get_cards_data().keys():
            if card_data == cd:
                cls.__cards[cd] += value

    @staticmethod
    def get_all_sum(store: dict) -> int:
        all_sum = 0
        for note in store.keys():
            for _ in range(store[note]):
                all_sum += int(note)

        return all_sum


class ATM:
    def __init__(self) -> None:
        self.__storage = ATM.Storage()

    @property
    def storage(self):
        return self.__storage
    
    @storage.setter
    def storage(self, cash: dict) -> None:
        self.__storage.fund = cash

    def cash_out(self) -> dict:
        return self.storage.cash_for_out
    
    class Storage:
        def __init__(self) -> None:
            self.__fund = Banknote.generate_fund()
            self.__cash_for_out = Banknote.generate_fund()

        def __str__(self) -> str:
            return f"\n{self.__fund}\nAll fund: {Bank.get_all_sum(self.fund)}"

        @property
        def cash_for_out(self) -> dict:
            return self.__cash_for_out

        @cash_for_out.setter
        def cash_for_out(self, cash: dict) -> None:
            for c in cash.keys():
                self.__cash_for_out[c] = cash[c]

        @property
        def fund(self) -> dict:
            return self.__fund

        @fund.setter
        def fund(self, cash: dict) -> None:
            for c in cash.keys():
                if Banknote.validate(int(c)):
                    self.__fund[c] += cash[c]

        def get_money(self, cash: int) -> bool:
            money = Banknote.generate_fund()
            for note in reversed(self.fund.keys()):
                note_val = int(note)
                while note_val <= cash and self.fund[note] > 0:
                    cash -= note_val
                    self.fund[note] -= 1
                    money[note] += 1
            
            if cash != 0:
                print("Don`t have appropriate banknotes!")
                for note in money:
                    self.fund[note] += money[note]
                return False 
            else:
                self.cash_for_out = money 
                return True 


def main():
    pass


if __name__ == "__main__":
    main()
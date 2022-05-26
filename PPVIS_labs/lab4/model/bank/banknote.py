class Banknote:
        # permission banknote values
        values = ["1", "2", "5", "10", "20", "50", "100", "200"]

        def __init__(self, value: int) -> None:
            self.value = value

        def __str__(self) -> str:
            return f"Banknote: value '{self.__value}'"

        @property
        def value(self) -> int:
            return self.__value

        @value.setter
        def value(self, value: int) -> None:
            if Banknote.validate(value):
                self.__value = value
                return

        @staticmethod
        def validate(value: str) -> bool:
            try:
                if str(value) not in Banknote.values:
                    raise ValueError
            except ValueError as v:
                print("The value doen't correct!")
                return False
            
            return True

        @staticmethod
        def generate_fund() -> dict:
            fund = {}
            for val in Banknote.values:
                fund[val] = 0
            
            return fund
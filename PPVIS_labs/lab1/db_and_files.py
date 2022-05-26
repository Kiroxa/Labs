import sqlite3
import json


class Server:
    DATABASE = "example.db"
    PATH = "files/"
    SAVE = "continue.json"

    def __init__(self) -> None:
        pass 

    @staticmethod
    def read_from_json_file(file_name: str) -> dict:
        ''' Read data about user from file '''
        
        with open(Server.PATH + file_name, 'r') as f:
            data = json.load(f)
        
        return data

    @staticmethod
    def save_in_json_file(client) -> bool:
        ''' Save the current session in the json file '''
        
        with open(Server.PATH + Server.SAVE, 'w') as f:
            to_json = {
                "fund": client.atm.storage.fund,
                "user_card_number": client.user.card.number,
                "user_phone_number": client.user.phone.number,
                "user_wallet": client.user.wallet.store
            }
            f.write(json.dumps(to_json))
        return True

    @classmethod
    def get_bd_data(cls) -> dict:
        ''' Read from database all cards and phones and it's data for bank session '''
        
        cards = {}
        phones = {}
        conn = sqlite3.connect(cls.DATABASE)
        cur = conn.cursor()

        for row in cur.execute('''SELECT * FROM cards'''):
            key = row[0], row[1]
            cards[key] = row[2]
        
        for row in cur.execute('''SELECT * FROM phones'''):
            key = row[0]
            phones[key] = row[1]
        
        conn.close()
        
        return cards, phones

    @classmethod
    def update_bd(cls, *args: list) -> None:
        
        conn = sqlite3.connect(cls.DATABASE)
        cur = conn.cursor()

        cur.execute(f'''UPDATE cards SET balance={args[1]} WHERE number="{args[0]}" ''')
        cur.execute(f'''UPDATE phones SET balance={args[3]} WHERE number="{args[2]}" ''')
        conn.commit()

        conn.close()
#LAB
from model.customer.atm_client import ATMClient
from model.bank.bank import Bank
from model.customer.user import User
from db.db_and_files import Server

from view.app.app import application

#SYSTEM
from cmd.cmd_input import parse_args, set_args
from sys import argv


def main(settings):
    
    if settings["load"]:
        data = Server.read_from_json_file(settings["load"])
        # print(data)
    else:
        data = Server.read_from_json_file("start.json")
        # print(data)

    # bank
    belbank = Bank()
    belbank.atm.storage.fund = data["fund"]
    # user 
    user = User(card_number=data["user_card_number"], phone_number=data["user_phone_number"])
    user.wallet.store = data["user_wallet"]
    # client
    client = ATMClient(user, belbank.atm)
    client.insert_card()

    # DRAFT
    print("\nDraft: \n")
    print(user)
    print('\nbank storage: \n', belbank.atm.storage)


if __name__ == "__main__":
    ''' get args app or cls and start session '''
    args = parse_args(argv[1:])
    # args = parse_args(['-l', 'continue.json'])
    settings = set_args(args)
    # print(settings)
    if settings["mode"] == "console":
        main(settings=settings)
    elif settings["mode"] == "app":
        application()
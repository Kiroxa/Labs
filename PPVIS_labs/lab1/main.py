#LAB
from atm_client import ATMClient
from bank import Bank
from user import User
from db_and_files import Server

#SYSTEM
from cmd_input import parse_args, set_args
from sys import argv



def main():
    
    args = parse_args(argv[1:])
    settings = set_args(args)

    if settings["load"]:
        data = Server.read_from_json_file(settings["load"])
    else:
        data = Server.read_from_json_file("start.json")

    # create bank, user and bank client for session
    belbank = Bank()
    belbank.atm.storage.fund = data["fund"]
    user = User(card_number=data["user_card_number"], phone_number=data["user_phone_number"])
    user.wallet.store = data["user_wallet"]
    client = ATMClient(user, belbank.atm)

    # here start the session
    client.insert_card()

    # DRAFT (it is a info about user that changed due session and don't show in the bank)
    print("\nDraft: \n")
    print(user)
    print('\nbank storage: \n', belbank.atm.storage)


if __name__ == "__main__":
    main()
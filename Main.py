from TodaqAPI import *


def help_command():
    print("ITEMS\t\tDisplay all the items on the marketplace\n"
          "TRANSACTIONS\t\tDisplay all the transactions on the marketplace\n"
          "USERS\t\tDisplay all the users on the marketplace\n"
          "VAULT \t\tDisplay my marketplace vault")


def items_command():
    print("Please wait for a sec...\n")
    files = get_all_files()
    print("Quant\t Items\n====================")
    for file in files:
        print("%sx\t\t %s" % (files[file], file))


def users_command():
    users = get_accounts()
    print("Users\n====================")
    for user in users:
        print(user)


def vault_command():
    address = input("Enter your wallet address: ")

    try:
        files = get_files_from_account(address)
    except Exception as error:
        print(error)
        return

    if len(files) == 0:
        print("Your vault is empty.")

    print("Quant\t Items\n====================")
    for file in files:
        print("%sx\t\t %s" % (files[file], file))


if __name__ == '__main__':
    print("Welcome to CS:GO Marketplace\n"
          "For information on command, type HELP")

    command = ""
    while command != "EXIT":
        user_input = input("> ")
        command = user_input.strip(' \t\n\r').upper()

        if len(command) == 0:
            pass
        elif command == "HELP":
            help_command()
        elif command == "ITEMS":
            items_command()
        elif command == "TRANSACTIONS":
            pass
        elif command == "USERS":
            users_command()
        elif command == "VAULT":
            vault_command()
        else:
            print("%s: command not found" % user_input)

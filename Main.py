from TodaqAPI import *


def help_command():
    print("ITEMS\t\tDisplay all the items on the marketplace\n"
          "TRANSACTIONS\t\tDisplay all the transactions on the marketplace\n"
          "USERS\t\tDisplay all the users on the marketplace\n"
          "VAULT address\t\tDisplay my marketplace vault\n"
          "\taddress\t\tSpecifies the address of your vault")


def items_command():
    print("Please wait for a sec...\n")
    files = get_all_files()
    print("Quant\tItems\n====================")
    for file in files:
        print("%sx\t\t %s" % (files[file], file))


def users_command():
    users = get_accounts()
    print("Users\n====================")
    for user in users:
        print(user)


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
        elif command.split()[0] == "VAULT":
            print("vault")
        else:
            print("%s: command not found" % user_input)

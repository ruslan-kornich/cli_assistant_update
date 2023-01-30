from time import sleep

from AdressBook import AddressBook, Record


def input_error(func):
    def wrapper(user_data):
        try:
            return func(user_data)
        except KeyError:
            msg = "Contact is not found. Try again!"
            return msg
        except ValueError:
            msg = "You didn't enter the phone number. Try again!"
            return msg
        except IndexError:
            msg = "You didn't enter the contact name or phone. Try again!"
            return msg

    return wrapper


@input_error
def handler(command: str):
    return HANDLER[command]


def main():
    user_input = input("For start say 'hello': ").lower()

    while True:
        command, user_data = handle_user_input(user_input)
        try:
            output = handler(command)(user_data)
        except TypeError:
            print(f"I dont understand the command '{command}'. Try again!")
        else:
            print(output)
        user_input = input("\n" + "How can i help you?: ").lower()


@input_error
def handle_user_input(user_input: str) -> tuple:
    """The function decodes the command and contact information"""

    data = user_input.split()
    command, user_data = data[0], data[1:]
    return command, user_data


@input_error
def hello_handler(*args, **kwargs) -> str:
    with open('hello.txt', "r") as hello:
        for line in hello.readlines():
            print(line, end='')
    return f'.'


@input_error
def add_record(user_data: list) -> str:
    """The function adds a new contact to the contact list"""

    name, phone = user_data[0], [] if not user_data[1:] else user_data[1:]
    user_data = Record(name, phone)
    BOOK.add_record(user_data)
    return f"New contact '{name}' is added"


@input_error
def add_phone(user_data: list) -> str:
    BOOK[user_data[0]].add_phone(user_data[1])
    return f"Phone number is added to the contact '{user_data[0]}'"


@input_error
def change_handler(user_data: list) -> str:
    """The function stores the new phone number of an existing contact"""

    return BOOK[user_data[0]].change_phone(user_data[1], user_data[2])


@input_error
def show_phone_handler(user_data: list) -> str:
    """The function displays the phone number of an existing contact"""

    return "%s" % BOOK.get((user_data[0]), "Contact is not found. Try again!")


@input_error
def bye_handler(*args, **kwargs):
    """End of dialogue"""

    print("Goodbye!")
    sleep(3)
    return exit()


@input_error
def del_record(user_data: list) -> str:
    """The function removes a contact from the contact list"""

    del BOOK[user_data[0]]
    return f"'{user_data[0]}' is delete"


@input_error
def del_phone(user_data: list) -> str:
    """The function removes a phones from the contact list"""

    return BOOK[user_data[0]].remove_phone(user_data[1])


@input_error
def show_all_handler(*args, **kwargs) -> str:
    """The function displays the entire list of contacts"""

    dict_to_str, count = [], 0
    for key, value in BOOK.items():
        count += 1
        dict_to_str.append("  {}. {}".format(count, value))
    dict_output = "\n".join(dict_to_str)

    return f"{dict_output}"


BOOK = AddressBook()

HANDLER = {
    "hello": hello_handler,
    "add": add_record,
    "add_phone": add_phone,
    "change": change_handler,
    "show_all": show_all_handler,
    "del": del_record,
    "del_phone": del_phone,
    "phone": show_phone_handler,
    "exit": bye_handler,
    "close": bye_handler,
    "good": bye_handler,
}

if __name__ == "__main__":
    main()

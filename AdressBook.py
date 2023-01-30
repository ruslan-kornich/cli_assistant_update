from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return f"{self.value}"


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone=None) -> None:
        self.name = Name(name)
        self.phones = []
        if phone:
            self.add_phone(phone)

    def __repr__(self, phone):
        return f"{self.name}: {self.phones}"

    def add_phone(self, phone):
        return self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"Phone '{old_phone}' is changed"
        return f"Phone '{old_phone}' is not in AddressBook. Try again!"

    def remove_phone(self, del_phone):
        for phone in self.phones:
            if phone.value == del_phone:
                self.phones.remove(phone)
                return f"Phone '{del_phone}' is delete"
        return f"Phone '{del_phone}' is not in AddressBook. Try again!"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data

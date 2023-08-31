class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone

    def __str__(self):
        return f"Name: {self.name}, Phones: {', '.join(str(p) for p in self.phones)}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, name):
        if name in self.data:
            del self.data[name]

    def find_records_by_name(self, name):
        return [record for record in self.data.values() if record.name.value == name]

    def find_records_by_phone(self, phone):
        return [record for record in self.data.values() if any(str(p) == phone for p in record.phones)]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            break
        elif command == "add":
            name = input("Enter a name: ")
            record = Record(name)
            while True:
                phone = input("Enter a phone (leave empty to finish): ").strip()
                if not phone:
                    break
                record.add_phone(phone)
            address_book.add_record(record)
        elif command == "remove":
            name = input("Enter a name to remove: ")
            address_book.remove_record(name)
        elif command == "find by name":
            name = input("Enter a name to find: ")
            found_records = address_book.find_records_by_name(name)
            for record in found_records:
                print(record)
        elif command == "find by phone":
            phone = input("Enter a phone to find: ")
            found_records = address_book.find_records_by_phone(phone)
            for record in found_records:
                print(record)
        elif command == "show all":
            print(address_book)
        else:
            print("Invalid command. Try again.")

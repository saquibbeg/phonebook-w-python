class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"Contact {name} already exists. Use update_contact to change the number.")
        else:
            self.contacts[name] = phone
            print(f"Added contact: {name} - {phone}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            print(f"Updated contact: {name} - {phone}")
        else:
            print(f"Contact {name} not found. Use add_contact to add it.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print(f"Contact {name} not found.")

    def display_contacts(self):
        if self.contacts:
            print("Phonebook contacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Phonebook is empty.")

def main():
    phonebook = Phonebook()
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phonebook.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to search: ")
            phonebook.search_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            phonebook.update_contact(name, phone)
        elif choice == '4':
            name = input("Enter name to delete: ")
            phonebook.delete_contact(name)
        elif choice == '5':
            phonebook.display_contacts()
        elif choice == '6':
            print("Exiting the phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

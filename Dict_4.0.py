phoneBook = {}


def menu():
    while True:
        print("\nPhone Book Menu")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        try:
            response = int(input("Choose an option: "))
            if response == 1:
                addContact()
            elif response == 2:
                displayContacts()
            elif response == 3:
                searchContact()
            elif response == 4:
                deleteContact()
            elif response == 5:
                print("Exiting Phone Book. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def addContact():
    name = input("Enter the FULL contact name: ").strip()
    if not name:
        print("Name cannot be empty. Try again.")
        return
    try:
        number = int(input("Enter the contact number: ").strip())
        phoneBook[name] = number
        print(f"{name} has been added successfully.")
    except ValueError:
        print("Invalid number. Please enter digits only.")


def displayContacts():
    if not phoneBook:
        print("No contacts found.")
    else:
        print("\nContacts:")
        print(f"{'Name':<20}| {'Number'}")
        print("-" * 30)
        for key, value in phoneBook.items():
            print(f"{key:<20}| {value}")


def searchContact():
    name = input("Enter the full name you wish to search: ").strip()
    if name in phoneBook:
        print(f"{name}'s number is {phoneBook[name]}")
    else:
        print("Contact not found.")


def deleteContact():
    name = input("Enter the name you wish to remove: ").strip()
    if name in phoneBook:
        phoneBook.pop(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found in the phone book.")


menu()

# Exercise 9
phoneBook = {}

def menu():
    print("1. Add Contact")
    print("2. Delete Contacts")
    print("3. Search Contacts")
    response = int(input(""))
    if response == 1:
        addContact()
    else:
        if response == 2:
            displayContacts()
        else:
            if response == 3:
                searchContact()
            else:
                return

def addContact():
    name = input("Please enter the FULL contact name: ")
    number = int(input("Please enter the contact number: "))
    phoneBook[name] = number
    print(f"{name} has been added successfully")
    menu()

def displayContacts():
    text = "Name"
    print(f"{text:<10}|Number")
    for key, value in phoneBook.items():
        print(f"{key:<10}|{value}")

    deleteContact()

def searchContact():
    name = input("Enter the full name you wish to search: ")
    if name in phoneBook:
        print(phoneBook[name])
    else:
        print("Not found.")

    pause = input("Press any Enter")
    menu()

def deleteContact():
    name = input("Enter the name you wish to remove: ")
    phoneBook.pop(name)
    print(f"{name} has been removed")
    menu()

menu()

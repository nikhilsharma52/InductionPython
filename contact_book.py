contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        if contacts:
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No contacts available.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


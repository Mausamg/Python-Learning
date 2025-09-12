contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("✅ Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
    else:
        print("📒 All Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()

def search_contact():
    name = input("🔍 Enter name to search: ")
    found = [c for c in contacts if c["name"].lower() == name.lower()]
    if found:
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(" Contact not found!\n")

def delete_contact():
    name = input("🗑️ Enter name to delete: ")
    global contacts
    contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    print("✅ Contact deleted (if existed).\n")

def show_menu():
    print("📞 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.\n")

import os
import json

# File to store contacts
FILE_NAME = "contacts.json"

# Load contacts from the file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save contacts to the file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    print()

# Search for a contact
def search_contact(contacts):
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Update an existing contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Current details: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    phone = input("Enter new phone number (leave blank to keep current): ").strip()
    email = input("Enter new email (leave blank to keep current): ").strip()
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    print(f"Contact '{name}' updated successfully.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

# Main menu
def main():
    print("Contact Book Application")
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

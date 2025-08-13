# 📂 File name where contacts will be saved
FILENAME = "contacts.txt"

# ✏ Add new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(FILENAME, "a") as f:
        f.write(f"{name},{phone},{email}\n")

    print("✅ Contact saved!")

# 📜 Show all contacts
def view_contacts():
    try:
        with open(FILENAME, "r") as f:
            contacts = f.readlines()

        if not contacts:
            print("📂 No contacts yet.")
            return

        print("\n--- All Contacts ---")
        for i, contact in enumerate(contacts, start=1):
            name, phone, email = contact.strip().split(",")
            print(f"{i}. {name} | {phone} | {email}")
        print("--------------------\n")

    except FileNotFoundError:
        print("📂 No contacts file found. Add some first.")

# 🔍 Search contact by name or phone
def search_contact():
    term = input("Enter name or phone to search: ").lower()
    found = False

    try:
        with open(FILENAME, "r") as f:
            for contact in f:
                name, phone, email = contact.strip().split(",")
                if term in name.lower() or term in phone:
                    print(f"✅ Found: {name} | {phone} | {email}")
                    found = True
        if not found:
            print("❌ Not found.")

    except FileNotFoundError:
        print("📂 No contacts file found.")

# ❌ Delete contact by name
def delete_contact():
    name_to_delete = input("Enter name to delete: ").lower()

    try:
        with open(FILENAME, "r") as f:
            contacts = f.readlines()

        new_contacts = [c for c in contacts if name_to_delete not in c.split(",")[0].lower()]

        if len(new_contacts) == len(contacts):
            print("❌ Contact not found.")
            return

        with open(FILENAME, "w") as f:
            f.writelines(new_contacts)

        print("✅ Contact deleted!")

    except FileNotFoundError:
        print("📂 No contacts file found.")

# 📌 Main Menu
def main():
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose (1-5): ")

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
            print("❌ Invalid choice. Try again.")

# 🔹 Run Program
if __name__ == "__main__":
    main()

import re

CONTACT_FILE = "contacts.txt"
contacts = []

# =========================
# load contacts
# =========================
def load_contacts():
    global contacts
    contacts = []

    try:
        with open(CONTACT_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass


# =========================
# save contacts
# =========================
def save_contacts():
    with open(CONTACT_FILE, "w") as file:
        for c in contacts:
            file.write(f"{c['name']},{c['phone']},{c['email']}\n")


# =========================
# validation functions
# =========================
def valid_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None

def valid_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None


# =========================
# add contact
# =========================
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter 10-digit phone: ").strip()
    email = input("Enter email: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if not valid_phone(phone):
        print("Invalid phone number.")
        return

    if not valid_email(email):
        print("Invalid email.")
        return

    contacts.append({
        "name": name.title(),
        "phone": phone,
        "email": email.lower()
    })

    print("Contact added!")


# =========================
# view contacts
# =========================
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


# =========================
# search contact
# =========================
def search_contact():
    keyword = input("Search name: ").lower()

    found = False
    for c in contacts:
        if keyword in c["name"].lower():
            print(f"Found: {c['name']} | {c['phone']} | {c['email']}")
            found = True

    if not found:
        print("No match found.")


# =========================
# delete contact
# =========================
def delete_contact():
    name = input("Enter name to delete: ").lower()

    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print("Contact deleted.")
            return

    print("Contact not found.")


# =========================
# start menu
# =========================
def main():
    load_contacts()

    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            save_contacts()
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

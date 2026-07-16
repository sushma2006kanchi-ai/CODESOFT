contacts = []

#Add Contact 

def add_contact():
    print("\nAdd New Contact")
    print("-" * 30)

    name = input("Enter Name         : ")
    phone = input("Enter Phone Number : ")
    email = input("Enter Email        : ")
    address = input("Enter Address      : ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)

    print("\nContact Added Successfully!")

# View Contacts 

def view_contacts():

    print("\nContact List")
    print("-" * 60)

    if len(contacts) == 0:
        print("No Contacts Available.")
        return

    print("{:<20} {:<20}".format("Name", "Phone Number"))
    print("-" * 60)

    for contact in contacts:
        print("{:<20} {:<20}".format(contact["Name"], contact["Phone"]))

# Search Contact 

def search_contact():

    if len(contacts) == 0:
        print("\nNo Contacts Available.")
        return

    search = input("\nEnter Name or Phone Number: ")

    found = False

    for contact in contacts:

        if search.lower() == contact["Name"].lower() or search == contact["Phone"]:

            print("\nContact Found")
            print("-" * 30)
            print("Name    :", contact["Name"])
            print("Phone   :", contact["Phone"])
            print("Email   :", contact["Email"])
            print("Address :", contact["Address"])

            found = True

    if not found:
        print("\nContact Not Found.")

#  Update Contact 

def update_contact():

    if len(contacts) == 0:
        print("\nNo Contacts Available.")
        return

    phone = input("\nEnter Phone Number to Update: ")

    for contact in contacts:

        if phone == contact["Phone"]:

            print("\nEnter New Details")

            contact["Name"] = input("Name    : ")
            contact["Phone"] = input("Phone   : ")
            contact["Email"] = input("Email   : ")
            contact["Address"] = input("Address : ")

            print("\nContact Updated Successfully!")
            return

    print("\nContact Not Found.")

#  Delete Contact 

def delete_contact():

    if len(contacts) == 0:
        print("\nNo Contacts Available.")
        return

    phone = input("\nEnter Phone Number to Delete: ")

    for contact in contacts:

        if phone == contact["Phone"]:
            contacts.remove(contact)
            print("\nContact Deleted Successfully!")
            return

    print("\nContact Not Found.")

# Main Program 

while True:

    print("\n" + "=" * 55)
    print("               CONTACT BOOK")
    print("=" * 55)

    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter Your Choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank You for Using Contact Book!")
        print("Program Closed Successfully.")
        break

    else:
        print("\nInvalid Choice! Please Enter a Number Between 1 and 6.")
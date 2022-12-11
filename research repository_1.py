# This is from my software project

def main():
    menu()

def menu():
    print("Welcome to the Help Desk")

    choice = input("""
                      0: Exit
                      1: Submit
                      2: Respond to a ticket
                      3: Re-open a ticket
                      4: Show ticket data

                      Please enter your choice: """)

    if choice == "0":
        exit()
    elif choice == "1":
        submit()
    elif choice == "2":
        respond()
    elif choice == "3":
        reopen()
    elif choice == "4":
        data()
    else:
        print("You must only select either 0-5")
        print("Please try again")
        menu()


def exit():
    print("Goodbye")
    input("Enter anything to return to main menu")
    menu()

def submit():
    staff_ID = input("Staff ID: ")
    name = input("Ticket creator name: ")
    email = input("Email Address: ")
    first_name = name[:4]
    staff_id = staff_ID[:3]
    issue = input("Description of the issue: ")
    print("If submitted, your ticket number is:  ")

    num = 2000

    def ticket():
        global num
        num += 1
        s = str(num).zfill(3)
        return s

    print("Ticket", ticket())

    if issue == 'password change':
        print("Your new password is...")
        print(staff_id,first_name)
    else:
        print("Thank you. We are working on your request.")


def respond():
    print("Not yet provided.")

def reopen():
    pass

def data():
    pass



main()
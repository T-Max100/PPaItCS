class attendee:
    def __init__(self, first_name, last_name, company, state, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.state = state
        self.email = email


def generate_list():
    try:
        with open('mock_data_beta.txt') as f:
            attendees = []
            for i, line in enumerate(f):
                if i < 5:
                    continue
                elif i >= 5 and len(line) < 64:
                    break
                else:
                    attendees.append(
                        attendee(line[13:24].strip(), line[24:35].strip(),
                                 line[:13].strip(), line[61:].strip(),
                                 line[35:61].strip()))
    except FileNotFoundError:
        print("Check the input file again.")
    return attendees


def print_intro():
    print()
    print("This program keeps track of conference attendees.")
    print("To add an attendee, type 'A' below.")
    print("To display info for an attendee, type 'Y' below.")
    print("To delete an attendee, type 'D' below.")
    print("To list all attendees, type 'L' below.")
    print("To exit the program, type 'X' below.")
    print()
    choice = input("What is your choice? ").upper()
    print()
    return choice


def add_new(attendees):
    try:
        first_name, last_name = input(
            "Add the first and last name: ").lower().title().split()
        company = input("Enter the company name: ")
        state = input("Enter the state abbreviation: ").upper()
        email = input("Enter the email address: ")
        guest = attendee(first_name, last_name, company, state, email)
        for a in attendees:
            if ((a.first_name, a.last_name, a.company, a.state, a.email) ==
               (first_name, last_name, company, state, email)):
                return "Guest already in list!"
        else:
            try:
                attendees.append(
                    attendee(guest.first_name, guest.last_name, guest.company,
                             guest.state, guest.email))
                with open('mock_data_beta.txt', 'a') as f:
                    f.write(f'{company:13}{first_name:11}{last_name:11}'
                            f'{email:26}{state}\n')
            except TypeError:
                print("One or more fields not filled.")
        for a in attendees:
            if ((a.first_name, a.last_name, a.company, a.state, a.email) ==
               (first_name, last_name, company, state, email)):
                print(f"\n{first_name} {last_name} added!")
    except ValueError:
        print("\nExpected a first and last name. Please try again.\n")


def display(attendees):
    try:
        first_name, last_name = input(
            "Add the first and last name: ").lower().title().split()
        for a in attendees:
            if (a.first_name, a.last_name) == (first_name, last_name):
                print(f"\n{a.first_name} {a.last_name}\n{a.email}\n"
                      f"{a.company}\n{a.state}\n")
                break
        else:
            print(f'\n{first_name} {last_name} not found.\n')
    except ValueError:
        print("\nExpected a first and last name. Please try again.\n")


def delete(attendees):
    try:
        first_name, last_name = input(
            "Enter the first and last name of the guest to delete: "
        ).lower().title().split()
        for i, a in enumerate(attendees):
            if (a.first_name, a.last_name) == (first_name, last_name):
                del attendees[i]
                with open('mock_data_beta.txt', 'w') as f:
                    f.write("Attendees list\n")
                    f.write("===============\n")
                    f.write(f'\n{"company":13}{"first_name":11}'
                            f'{"last_name":11}{"email":26}{"state"}\n\n')
                    for a in attendees:
                        f.write(f'{a.company:13}{a.first_name:11}'
                                f'{a.last_name:11}{a.email:26}{a.state}\n')
                print(f"\n{first_name} {last_name} deleted!\n")
                break
        else:
            print(f'\n{first_name} {last_name} not found.\n')
    except ValueError:
        print("\nExpected a first and last name. Please try again.\n")


def list_all(attendees):
    choice = input("\nType 'A' To list all names and emails, type 'S'"
                   "for a specific state listing\n").upper()
    if choice == 'A':
        print()
        for a in attendees:
            print(f"{a.first_name} {a.last_name}\n{a.email}\n")
    elif choice == 'S':
        print()
        state = input("\nEnter the state's initials: ").upper()
        print()
        res = [f"\n{a.first_name} {a.last_name}\n{a.email}\n"
               for a in attendees if a.state == state]
        if res:
            print(*res)
        else:
            print("\nNo one from that state!\n")
    else:
        print("\nInvalid choice!\n")


def main():
    while True:
        attendee_list = generate_list()
        choice = print_intro()
        if choice == 'A':
            add_new(attendee_list)
        elif choice == 'Y':
            display(attendee_list)
        elif choice == 'D':
            delete(attendee_list)
        elif choice == 'L':
            list_all(attendee_list)
        elif choice == 'X':
            print("Se ya!")
            break
        else:
            print("Invalid choice!")
            break


if __name__ == '__main__':
    main()

# didn't want to import modules so I saved the thing as a file object to be
# stored in full in memory (this is bad practice as file might be too large
# when called upon). This was to keep from making some duplicate file and
# returning that when deleting. Instead file is read in, saved as file object
# in toto, manipulated (i.e. entry deleted), and then original file is
# rewritten.

# Should also use more getters and setters but the question didn't call for
# much.

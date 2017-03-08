class attendee:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.company = ''
        self.state = ''
        self.email = ''

    def add_new(self, first_name, last_name, company, state, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.state = state
        self.email = email
        try:
            with open('mock_data_beta.txt', 'a') as f:
                f.write(f'{company: 13}{first_name: 11}{last_name: 11}'
                        '{email: 26}{state}\n')
            print(f'{first_name} {last_name} added!')
        except TypeError:
            print("One or more fields not filled.")

    def display(self, first_name, last_name):
        with open('mock_data_beta.txt') as f:
            for line in f:
                e = line.split()
                if e[1] == first_name and e[2] == last_name:
                    return e
                else:
                    return f'{first_name} {last_name} not found.'

    def delete(self, first_name, last_name):
        with open('mock_data_beta.txt') as f:


def main():
    choice = print_intro()
    if choice == 'A':
        guest = attendee()
        first_name, last_name = input("Add the first and last name: ").split()
        company = input("Enter the company name: ")
        state = input("Enter the state abbreviation: ")
        email = input("Enter the email address: ")
        guest.add_new(first_name, last_name, company, state, email)
    elif choice == 'Y':
        guest = attendee()
        first_name, last_name = input("Add the first and last name: ").split()
        print(guest.display(first_name, last_name))
    elif choice == 'D':

    elif choice == 'L':
        choice_2 = input("To list all names and emails: A, for a specific state
                         listing: S")
        if choice_2 == 'A':
        else:


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

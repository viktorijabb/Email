# An Email Simulation

class Email:

    def __init__(self, email_contents, from_address):
        # constructor initializes variables
        self.has_been_read = False  # False by default
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address

    def mark_as_read(self):
        # marks email as read
        self.has_been_read = True

    def mark_as_spam(self):
        # marks email as spam
        self.is_spam = True

    def __str__(self):
        # allows to print out email at a specific index later on
        return f"{str(self.email_contents)},{str(self.from_address)}"

    def __repr__(self):
        return f"{str(self.email_contents)},{str(self.from_address)}"


inbox = []  # stores the body of email and sender


def add_email(contents, email_address, inbox):
    # adds email to inbox
    email = Email(contents, email_address)
    return inbox.append(email)


def get_count(inbox):
    # counts number of emails in inbox
    return len(inbox)


def get_email(i, inbox):
    # returns email at specific index
    if 0 <= i < len(inbox):
        email = inbox[i]
        email.mark_as_read()
        print(email)
        return email
    else:
        print('Invalid index, email does not exist')


def get_unread_emails(inbox):
    # returns unread emails
    return [email for email in inbox if not email.has_been_read]


def get_spam_emails(inbox):
    # returns spam emails
    spams = []
    for email in inbox:
        if email.is_spam:
            spams.append(email)
            print(f"spam: {email.email_contents}")
    return spams


def add_spam(i, inbox):
    # marks email as spam
    message = inbox[i]
    message.mark_as_spam()
    print("Email marked as spam!")


def delete(inbox):
    # deletes email
    if len(inbox) > 0:
        return inbox.pop()
    else:
        print("Could not delete email!")


# initializing Email object with some emails
preset_emails = [
    "This is an email,me@me.com",
    "Another email,sender@email.com"
]

for i in preset_emails:
    body, address = i.split(',')  # splits email into the body text and sender email address
    add_email(body, address, inbox)  # adds the pre-set emails

user_choice = ""  # stores user menu choice

while True:
    user_choice = input("What would you like to do - read/mark spam/send/quit?")  # menu

    # read emails
    if user_choice == "read":  # read email
        print("List of unread emails:\n")

        for i, mail in enumerate(inbox):
            print(f'{i + 1}. {mail}')

        num = int(input("\nEnter number of the email you want to read: "))
        get_email(num - 1, inbox)  # prints  email at specific index

    # display and mark as spam
    elif user_choice == "mark spam":
        print("List of emails\n")
        for i, message in enumerate(inbox):
            print(f'{i + 1}. {message}')
        num = int(input("\nEnter number of email you want to spam :"))
        add_spam(num - 1, inbox)
        get_spam_emails(inbox)
        
    # send email
    elif user_choice == "send":  # mail sending option
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email content: ")
        add_email(email_contents, from_address, inbox)
        print("Email sent successfully!")

    # quit program
    elif user_choice == "quit":  # quit option
        print("Email program exited!")

    # outside the scope of menu options
    else:
        print("Oops - incorrect input")
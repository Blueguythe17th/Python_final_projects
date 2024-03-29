import re, random, string


def check_special(string):
    regex = re.compile("[@_!#$%^&*()<>?/|}{~:]")
    return regex.search(string)


def check_numeric(string):
    regex = re.compile("[0-9]")
    return regex.search(string)


def check_alpha(string):
    regex = re.compile("[a-zA-Z]")
    return regex.search(string)


def password_checker():
    print("Your password must have 8 to 16 characters and at least 1 special character, 1 digit, and 1 lower and upper case letter.")
    while True:
        password = input("Create your password: ")
        if len(password) < 8:
            print("That password is too short! (must be at least 8 characters).")
        elif len(password) > 16:
            print("That password is too long! (must have 16 or less characters).")
        elif password.islower():
            print("Your password must have at least one capital letter!")
        elif password.isupper():
            print("Your password must have at least one lower case letter!")
        elif not check_alpha(password):
            print("Your password must have at least two letters (one upper case and one lower)!")
        elif not check_numeric(password):
            print("Your password must have at least one digit!")
        elif not check_special(password):
            print("Your password must have at least one special character!")
        else:
            print("Your password, " + password + ", has been registered. Thank you!")
            user_and_password[str(username)] = str(password)
            return


def password_generator():
    while True:
        length = input("How many characters do you want your password to be (must be between 8 and 16 characters): ")
        if not length.isnumeric():
            print("You must enter a number.")
            continue
        elif int(length) < 8:
            print("That password is too short! (Must be between 8 and 16 characters).")
            continue
        elif int(length) > 16:
            print("That password is too long! (Must be between 8 and 16 characters).")
            continue
        else:
            break
    new_password = []
    new_password.append(random.choice(string.ascii_uppercase))
    new_password.append(random.choice(string.ascii_lowercase))
    new_password.append(random.choice(string.digits))
    new_password.append(random.choice(string.punctuation))
    length = int(length) - 4
    for i in range(0, length):
        character_generator = random.randint(1, 3)
        if character_generator == 1:
            new_password.append(random.choice(string.ascii_letters))
        elif character_generator == 2:
            new_password.append(random.choice(string.digits))
        else:
            new_password.append(random.choice(string.punctuation))
    random.shuffle(new_password)
    password = "".join(new_password)
    print("Your password is: " + password)
    user_and_password[str(username)] = str(password)
    return password


while True:
    user_and_password = {}
    account_creation = input("Do you want to: 'Create Account', 'Log In' or 'Quit'? Enter: ").lower()
    if account_creation == "create account":
        username = input("Make your username: ")
        print("Time to create a password. Your options are, 1: Use strong password. 2: Make your own.")
        choice = input("Enter 1 or 2: ")
        if choice == "2":
            password_checker()
        else:
            password_generator()
    elif account_creation == "log in":
        user = input("Enter your username: ")
        if user in user_and_password.values():
            password_check = input("Hello " + str(username) + ". Please enter your password: ")
            if user_and_password.get(str(password_check)) == user_and_password.get(str(username)):
                print("Log in successful.")
            else:
                print("This password doesn't match. Please try again.")
                break
        else:
            print("That username doesn't exist. Please try again.")
            break
    elif account_creation == "2":
        break
    else:
        print("Invalid input. Please try again.")
        continue

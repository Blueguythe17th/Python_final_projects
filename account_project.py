import random, time, re, string


class Account:
    def __init__(self, email, username, age, password):
        self.email = email
        self.username = username
        self.age = age
        self.password = password

    @staticmethod
    def check_special(string):
        regex = re.compile("[@_!#$%^&*()<>?/|}{~:]")
        return regex.search(string)

    @staticmethod
    def check_numeric(string):
        regex = re.compile("[0-9]")
        return regex.search(string)

    @staticmethod
    def check_alpha(string):
        regex = re.compile("[a-zA-Z]")
        return regex.search(string)

    @staticmethod
    def password_checker():
        print(
            "Your password must have 8 to 16 characters and at least 1 special character, 1 digit, and 1 lower and upper case letter.")
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
            elif not Account.check_alpha(password):
                print("Your password must have at least two letters (one upper case and one lower)!")
            elif not Account.check_numeric(password):
                print("Your password must have at least one digit!")
            elif not Account.check_special(password):
                print("Your password must have at least one special character!")
            else:
                print("Your password, " + password + ", has been registered. Thank you!")
                return password


    @staticmethod
    def password_generator():
        while True:
            length = input(
                "How many characters do you want your password to be (must be between 8 and 16 characters): ")
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
        return password

    def login(self):
        for i in range(1, 5):
            login = input("Welcome back, " + self.username + "! Please enter your email: ")
            login2 = input("Enter your password: ")
            if login == self.email and login2 == self.password:
                print("Successfully logged in.")
                return
            else:
                print("Email and/or password is incorrect. Please try again.")
        self.reset()

    def reset(self):
        print("Login failed too many times. Please check your email for password reset code.")
        random_code = str(random.randint(1000, 9999))
        print("EMAIL: Your one-time code is " + random_code + ".")
        while True:
            code = input("Enter the code sent to your email: ")
            if code == random_code:
                print("Success.")
                break
            else:
                print("Unsuccessful. Try again.")
        self.password = input("Create a new password: ")
        while 5 > len(self.password) > 15:
            print("Password length is incorrect.")
            self.password = input("Create a new password: ")
        print("Success! New password has been saved.")


    def check_email(self):
        print("Your inbox is currently empty.")


    def do_roman_history(self):
        print("Welcome to Roman history trivia!")
        time.sleep(1)
        print("The questions will get progressively harder, so be ready.")
        time.sleep(1)
        print("There'll be 5 questions about Western rome and 5 about the Byzantine empire (East rome).")
        time.sleep(1)
        return 0


    def do_history_trivia(self):
        print("History trivia selected. Choose what history trivia you'd like: ")
        time.sleep(1)
        print("1. Roman.")
        print("2. Greek.")
        history_choice = input("Enter the number of one of the above to select it: ")
        if history_choice == "1" or history_choice == "1.":
            points = self.do_roman_history()
        else:
            points = 0
        return points


    def lord_of_rings(self):
        points = 0
        print("Welcome to Lord of the Rings movie trivia!")
        time.sleep(1)
        print("The game is about to begin.")
        time.sleep(1)
        print("You'll have to answer 5 EASY questions, 5 MEDIUM questions, and 3 EXTREME questions.")
        time.sleep(2)
        print("Answer all correctly to win!")
        time.sleep(1)
        easy1 = input("#1: Who is the main villain of the movies and books: ").lower()
        if easy1 == "sauron":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. The main villain is Sauron.")
            points -= 1
        easy2 = input("#2: What object needs to be destroyed to defeat Sauron: ").lower()
        if easy2 == "the ring" or easy2 == "ring" or easy2 == "the one ring" or easy2 == "isildur's bane":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. The object is the Ring.")
            points -= 1
        easy3 = input("#3: How many hobbits go on the quest total: ").lower()
        if easy3 == "4" or easy3 == "four":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. Four hobbits went on the quest.")
            points -= 1
        easy4 = input("#4: Where in Middle-Earth do hobbits live: ").lower()
        if easy4 == "the shire" or easy4 == "shire":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. They live in the Shire.")
            points -= 1
        easy5 = input("#5: What is the name of the wizard who helps the protagonists throughout the trilogy: ").lower()
        if easy5 == "gandalf" or easy5 == "gandalf the grey" or easy5 == "gandalf the white":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. The wizard was Gandalf.")
            points -= 1
        print("Here come the harder questions!")
        hard1 = input("#6: What is the name of the inn where the hobbits stay in Bree: ").lower()
        if hard1 == "prancing pony" or hard1 == "the prancing pony":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. They stayed at the Prancing Pony inn.")
            points -= 1
        hard2 = input("#7: What is Aragorn's ranger alias: ").lower()
        if hard2 == "strider":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. His alias was Strider.")
            points -= 1
        hard3 = input("#8: Enter Pippin's last name: ").lower()
        if hard3 == "took":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. Pippin's last name was Took.")
            points -= 1
        hard4 = input("#9: What was the name of Boromir's brother: ").lower()
        if hard4 == "faramir":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. His brother was Faramir.")
            points -= 1
        hard5 = input("#10: What is the name of the elf lord who sends the Fellowship to destroy the Ring: ").lower()
        if hard5 == "elrond":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. His name is Elrond.")
            points -= 1
        print("It's time for the final 3 questions. These ones are EXTREMELY hard and each worth 2 points!")
        extreme1 = input("What is the name of Aragorn's sword given to him by Elrond in Return of the King: ").lower()
        if extreme1 == "anduril" or extreme1 == "anduril, flame of the west":
            print("Correct!")
            points += 2
        else:
            print("Incorrect. It was Anduril.")
            points -= 1
        extreme2 = input("How many Rohirrim defended Helm's Deep: ").lower()
        if extreme2 == "300" or extreme2 == "three hundred":
            print("Correct!")
            points += 2
        else:
            print("Incorrect. There were 300.")
            points -= 1
        extreme3 = input("What is the name of Gimli's father: ")
        if extreme3 == "Gloin":
            print("Correct!")
            points += 1
        else:
            print("Incorrect. His father is Gloin.")
            points -= 1
        return points
        # print("Alright, the trivia is over. You scored " + str(points) + "!")
        # if points < 0:
        #     print("You didn't do very well. Better luck next time!")
        # elif 5 > points > 0:
        #     print("You did OK! Thanks for playing!")
        # elif 10 > points > 5:
        #     print("You did GOOD! Thanks for playing!")
        # elif points > 10:
        #     print("You did GREAT! Thanks for playing!")

    def do_movie_trivia(self):
        points = 0
        print("Move trivia selected. You have four movie series options: ")
        time.sleep(1)
        print("1. Lord of the Rings.")
        print("2. Pirates of the Caribbean.")
        movie_choice = input("Choose one by entering its number: ")
        if movie_choice == "1" or movie_choice == "1.":
            points = self.lord_of_rings()
        else:
            points = 0
        return points

    def do_trivia(self, choice):
        while choice != "history" and choice != "movie":
            choice = input("That's not an option. Please choose either Movie or History.").lower()
        if choice == "history":
            points = self.do_history_trivia()
        elif choice == "movie":
            points = self.do_movie_trivia()
        print("Alright, the trivia is over. You scored " + str(points) + "!")
        if points <= 0:
            print("You didn't do very well. Better luck next time!")
        elif points > 0 and points <= 5:
            print("You did OK! Thanks for playing!")
        elif points > 5 and points <= 10:
            print("You did GOOD! Thanks for playing!")
        else:
            print("You did GREAT! Thanks for playing!")

    def log_out(self):
        checker = input("Confirm logout with password: ")
        if checker == self.password:
            print("Successfully logged out.")
            return True
        else:
            print("Failed. Try again later.")
            return False


accounts = {}
while True:
    choice2 = input("Would you like to sign up or log in? Enter: ").lower()
    if choice2 == "sign up":
        email = input("Enter your email: ")
        username = input("Create a username: ")
        age = input("Enter your age: ")
        # password = input("Create a password: ")
        password_options = input("Would you like to: 1. Create a password. 2. Generate a strong password. Enter 1 or 2: ")
        if password_options == "1":
            password = Account.password_checker()
        else:
            password = Account.password_generator()
        if int(age) < 13:
            print("You are too young to create an account! You have to be 13+.")
            continue
        elif email == username:
            print("Email and username cannot be the same.")
            continue
        elif username in accounts:
            print("Username taken. Try another.")
            continue
        else:
            print("Success! Your account has been created, " + username + ".")
            myaccount = Account(email, username, age, password)
            accounts[username] = (password, myaccount)
    elif choice2 == "log in":
        check = input("Enter your username: ")
        if check in accounts:
            account = accounts[check][1]
            password = accounts[check][0]
            account.login()
        else:
            print("This username is not associated with an account.")
            continue
        while True:
            choice = input("Would you like to: 'Do Trivia', 'Check Email', or 'Log Out'? Enter: ").lower()
            if choice == "log out":
                passed = account.log_out()
                if not passed:
                    continue
                else:
                    break
            elif choice == "check email":
                account.check_email()
            else:
                while True:
                    choice = input("Would you like to do History or Movie trivia: ").lower()
                    account.do_trivia(choice)
                    more = input("Would you like to do more trivia? Yes or No: ").lower()
                    if more == "y" or more == "yes":
                        continue
                    else:
                        break
    else:
        print("This is not an option!")
        continue

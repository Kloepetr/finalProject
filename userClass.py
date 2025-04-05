import pandas as pd

class User:
    def __init__(self, filename):
        # Read in the student csv
        csvFile = pd.read_csv(filename)

        # Get needed data
        studentUsernames = csvFile['Username']
        studentPasswords = csvFile['Password']

        # Admin login loop, only have 5 attempts before the program exits
        numOfAttempts = 5
        while numOfAttempts > 0:
            # Update user on number of attempts left
            print(f"\nYou have {numOfAttempts} attempts left")

            # Get user input
            username = input("Enter username: ")
            password = input("Enter password: ")

            # Check if the provided username is in the csv
            index = -1
            for i, aUsername in enumerate(studentUsernames):
                if username == aUsername:
                    index = i

            if index == -1:
                print("Incorrect username or password, try again.")
                numOfAttempts -= 1
                continue

            # Check if the password matches
            if password == studentPasswords[index]:
                # Username and password match, login successful
                print("Login successful!")
                self.username = username;
                self.password = password;
                return
            else:
                print("Incorrect username or password, try again.")
                numOfAttempts -= 1
                continue

        # Exit if login failed after 5 attempts
        print("Login failed, too many attempts in one session, exiting program");
        self.username = None
        self.password = None
        return



from instructorClass import Instructor
# from courseClass import Course

def main():
    # First, try to login
    retValue = Instructor()

    if retValue.username == None:
        # print("Login failed, too many attempts in one session, exiting program")
        return 0  # Exit if login fails


    # Main menu loop
    while True:
        choice = Instructor.main_menu()  # Static method call

        if choice == "1":
            retValue.viewAssignedCourse()
        elif choice == "2":
            print("Exiting Program. Goodbye!!!\n")
            return 0  # Exit program when choice 2 is selected
        else:
            print("Invalid choice, please choose a valid option!\n")
            # The loop will continue until a valid choice is made

if __name__ == "__main__":
    main()
from studentClass import Student  # Import the Student class

# Main function to drive the program
def main():
    # Try to log in
    # retValue, username,password = Student.student_login()
    retValue = Student()

    if retValue.username == None:
        # print("Login failed, too many attempts in one session, exiting program.")
        return 0

    # print("\nLogin Successful!")

    # Main menu loop
    while True:
        choice = Student.main_menu()  # Get user's menu choice

        if choice == "1":
            Student.enrollCourse(retValue.username,retValue.password) # Enroll in a course
        elif choice == "2":
            Student.viewCourse(retValue.username,retValue.password)  # View enrolled courses
        elif choice == "3":
            print("Exiting Program. Goodbye!!!\n")
            return 0  # Exit program
        else:
            print("Invalid choice, please choose a valid option!\n")


# Run the main function
main();
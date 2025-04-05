from userClass import User;
import pandas;
import os.path;

class Admin(User):
    def __init__(self):
        super().__init__('admin.csv')

    def main_menu():
        print("Select an option from below using the number only!");
        print("1. Add a new student.")
        print("2. Add a new instructor.")
        print("3. Add a new course.")
        print("4. Exit program.")
        print("5. view all students.")
        print("6. view all instructors.")
        print("7. view all courses.")
        print("8. view all enrollment information")
        return input("Enter a number: ");

    #add a new student. Information must include but not be limited to first name,
    #last name, unique username and password. Must ensure that each username is
    #unique among students. Student information will be saved into a csv file

    def add_student():
        # Check if student.csv exists
        if not os.path.isfile("student.csv"):
            with open("student.csv", "a") as stuFile:
                stuFile.write("FirstName,LastName,Username,Password\n")

        # Now the file definitely exists, so read it using pandas
        csvFile = pandas.read_csv('student.csv')

        # Get the student usernames to check for uniqueness
        studentUsernames = csvFile['Username']

        # Tell admin what they need to do
        print("Create a new student by providing First Name, Last Name, Username, and Password.")
        print("Username must be unique for each student! Admin will continue to be prompted until they provide a unique username\n")

        # Get user input for First Name and Last Name
        firstName = input("\nEnter Student First Name: ")
        lastName = input("Enter Student Last Name: ")

        # Loop until a unique username is provided
        while True:
            username = input("Enter username: ").strip()
            if username in studentUsernames.values:
                print("Username already exists, choose a different username for this student!")
            else:
                break  # Exit the loop if the username is unique

        # Get the password
        password = input("Enter password: ")

        # Write the new student's info to the CSV file
        with open("student.csv", "a") as stuFile:
            stuFile.write(f"{firstName},{lastName},{username},{password}\n")

        print("\nStudent was successfully added!\n\n")


    def add_instructor():
        # Check if instructor.csv exists
        if not os.path.isfile("instructor.csv"):
            with open("instructor.csv", "a") as stuFile:
                stuFile.write("FirstName,LastName,Username,Password\n")

        # Now the file definitely exists, so read it using pandas
        csvFile = pandas.read_csv('instructor.csv')

        # Get the instructor usernames
        instructorUsernames = csvFile['Username']

        # Prompt admin to add a new instructor
        print("Add a new instructor by providing First Name, Last Name, Username, and Password.")
        print("Username must be unique for each instructor!Admin will continue to be prompted until they provide a unique username and course ID \n")

        # Get user input for First and Last Name
        firstName = input("Enter Instructor First Name: ")
        lastName = input("Enter Instructor Last Name: ")

        # Ensure a unique username
        username = ""
        while True:
            username = input("Enter username: ").strip()
            if username in instructorUsernames.values:
                print("\nUsername already exists, choose a different username!\n")
            else:
                break  # exit the loop if the username is unique

        # Get the password
        password = input("Enter password: ")

        # Write the new instructor data to the CSV file
        with open("instructor.csv", "a") as insFile:
            insFile.write(f"{firstName},{lastName},{username},{password}\n")

        print("\nInstructor added successfully.\n\n")


    def add_course():
        # Check if course.csv exists
        if not os.path.isfile("course.csv"):
            with open("course.csv", "a") as stuFile:
                stuFile.write("instructorFirstName,instructorLastName,instructorUsername,courseTitle,courseID\n")

        # Read the course CSV file using pandas
        courseFile = pandas.read_csv('course.csv')

        # Prompt admin to add a new course
        print("Add a new course by providing First name of the instructor, Last name of the instructor, instructor username, title of the course, and course ID.")
        print("CourseID must be unique for each course! Admin will continue to be prompted until they provide a unique input.\n")

        # Get user input for instructor's details
        instructorFirstName = input("Enter First Name of the instructor assigned: ")
        instructorLastName = input("Enter Last Name of the instructor assigned: ")
        instructorUsername = input("Enter instructor's username: ")

        # Check if the instructor's username exists in the instructor.csv file
        instructorFile = pandas.read_csv('instructor.csv')
        while instructorUsername not in instructorFile['Username'].values:
            print("Error: Instructor username not found. Please enter a valid username.")
            instructorUsername = input("Enter instructor's username: ")

        # Ensure a unique course ID
        courseTitle = input("Enter course title: ")

        # Check for unique course ID
        courseID = ""
        while True:
            courseID = input("Enter course ID: ").strip()
            if courseID in courseFile['courseID'].values:
                print("Error: Course ID already taken, please enter a unique course ID.")
            else:
                break  # Exit the loop if the course ID is unique

        # Write the new course data to the CSV file
        with open("course.csv", "a") as courseFile:
            courseFile.write(f"{instructorFirstName},{instructorLastName},{instructorUsername},{courseTitle},{courseID}\n")

        print("\nCourse added successfully.\n")


    def showInstructor():
    # Check if enrollment.csv exists
        if not os.path.isfile('instructor.csv'):
            print("No info available. add an instructor and try again")
            return  # Exit the function if the file doesn't exist

        # If the file exists, read it and display the contents
        instructorFile = pandas.read_csv('instructor.csv')

        print("Here are all the instructor information:")
        print(instructorFile)
    print("\n")

    def showCourse():
    # Check if enrollment.csv exists
        if not os.path.isfile('course.csv'):
            print("No info available. add a course and try again")
            return  # Exit the function if the file doesn't exist

        # If the file exists, read it and display the contents
        courseFile = pandas.read_csv('course.csv')

        print("Here are all the course information:")
        print(courseFile)
    print("\n")

    def showStudent():
    # Check if enrollment.csv exists
        if not os.path.isfile('student.csv'):
            print("No info available. add a student and try again")
            return  # Exit the function if the file doesn't exist

        # If the file exists, read it and display the contents
        studentFile = pandas.read_csv('student.csv')

        print("Here are all the student information:")
        print(studentFile)
    print("\n")

    def showEnrollmentInfo():
    # Check if enrollment.csv exists
        if not os.path.isfile('enrollment.csv'):
            print("No info available. no students enrollment available")
            return  # Exit the function if the file doesn't exist

        # If the file exists, read it and display the contents
        enrollmentFile = pandas.read_csv('enrollment.csv')

        print("Here are all the enrollment information:")
        print(enrollmentFile)
    print("\n")
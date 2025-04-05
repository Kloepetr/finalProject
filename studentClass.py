from userClass import User
import os
import pandas as pd

class Student(User):
    def __init__(self):
        super().__init__('student.csv')

    def main_menu():
        print("Select an option from below using the number only!")
        print("1. Enroll in a new course")
        print("2. View enrolled courses")
        print("3. Exit program.")
        return input("Enter a number: ")

    def enrollCourse(username, password):
        # Ensure enrollment.csv exists with proper headers
        if not os.path.isfile("enrollment.csv"):
            with open("enrollment.csv", "w") as enrollmentFile:
                enrollmentFile.write("username,password,courseTitle,courseID,instructorFirstName,instructorLastName,instructorUsername\n")

        # Read the course file
        try:
            courseFile = pd.read_csv('course.csv')
            print("\nAvailable Courses:")
            print(courseFile)
        except FileNotFoundError:
            print("Error: course.csv file not found. Please ensure it exists.")
            return

        while True:
            # Prompt user for course ID
            courseID = input("\nEnter course ID to enroll, or enter 'back' to go back to main menu: ").strip()

            # Exit condition
            if courseID.lower() == 'back':
                print("Back to main menu.")
                break

            # Clean and get list of existing course IDs
            courseFile['courseID'] = courseFile['courseID'].astype(str).str.strip()
            existingCourseID = courseFile['courseID'].tolist()
            courseFile['courseTitle'] = courseFile['courseTitle'].astype(str).str.strip()

            # Get enrollment data
            enrollmentFile = pd.read_csv('enrollment.csv')

            # Check if the entered course ID exists
            if courseID in existingCourseID:
                unique = 1
                for i in range(len(enrollmentFile)):
                    if username == str(enrollmentFile.loc[i, :].values[0]) and courseID == str(enrollmentFile.loc[i, :].values[3]):
                        print("Already enrolled in the given course!")
                        unique = 0

                if unique == 1:
                    # Fetch course details
                    courseRow = courseFile[courseFile['courseID'] == courseID].iloc[0]
                    courseTitle = courseRow['courseTitle']
                    instructorFirstName = courseRow['instructorFirstName']
                    instructorLastName = courseRow['instructorLastName']
                    instructorUsername = courseRow['instructorUsername']

                    print(f"Enrolled successfully in course ID: {courseID}")

                    # Append to enrollment.csv
                    with open("enrollment.csv", "a") as enrollmentFile:
                        enrollmentFile.write(f"{username},{password},{courseTitle},{courseID},{instructorFirstName},{instructorLastName},{instructorUsername}\n")
                    print("Enrollment information saved.")
                    return 1
            else:
                print("Error: Invalid course ID. Please try again.")

    def viewCourse(username, password):
        try:
            # Read the enrollment.csv file
            csvData = pd.read_csv("enrollment.csv")

            # Flag to check if any courses are found
            courses_found = False

            print("\nEnrolled Courses:")

            # Iterate through the enrollment data
            for i in range(len(csvData)):
                if username == str(csvData.loc[i, "username"]) and password == str(csvData.loc[i, "password"]):
                    # Print course details if a match is found
                    courseDisplay = f"Course ID: {csvData.loc[i, 'courseID']} Course title: {csvData.loc[i, 'courseTitle']} Instructor username: {csvData.loc[i, 'instructorUsername']} Instructor name: {csvData.loc[i, 'instructorFirstName']} {csvData.loc[i, 'instructorLastName']} Student username: {username}"
                    print(courseDisplay)
                    courses_found = True

            # If no courses are found, inform the user
            if not courses_found:
                print("No class enrolled. Please first enroll in a class.")

        except FileNotFoundError:
            print("Error: enrollment.csv file not found. No enrollment data available.")

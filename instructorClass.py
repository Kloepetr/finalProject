from userClass import User;
import pandas as pd

class Instructor(User):
    def __init__(self):
        super().__init__('instructor.csv')

    def display_info(self):
        return f"Instructor: {self.first_name} {self.last_name}"

    @staticmethod  # Make this method static so it can be called directly on the class
    def main_menu():
        # Display the menu options and handle user input
        print("\nSelect an option from below using the number only:")
        print("1. View assigned courses")
        print("2. Exit program")

        # Get valid user choice
        choice = input("Enter your choice: ").strip()  # Remove extra spaces from input

        # Validate choice
        while choice not in ["1", "2"]:
            print("Invalid choice, please choose a valid option!")
            choice = input("Enter your choice: ").strip()

        return choice

    def viewAssignedCourse(self):
        try:
            # Read the course.csv file to check if courses are assigned
            csvData = pd.read_csv("course.csv")
            courses_found = False

            print("\nAssigned Courses:")

            # Iterate through the course data to find assigned courses
            for i in range(len(csvData)):
                if self.username == str(csvData.loc[i,:].values[2]): #2 is the Username column
                     # Print course details if a match is found
                    print(f"Course ID: {csvData.loc[i, 'courseID']}, Course Title: {csvData.loc[i, 'courseTitle']}")
                    courses_found = True

            # If no courses are found, inform the user
            if not courses_found:
                print("No class assigned.")

        except FileNotFoundError:
            print("Error: No assigned classes available for display.")

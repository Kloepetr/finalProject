import pandas as pd;

# courseClass.py

class Course:
    def __init__(self, instructor, username, password, courseTitle, courseID):
        self.instructor = instructor  # Instructor object (can be an instance of the Instructor class)
        self.username = username
        self.password = password
        self.courseTitle = courseTitle
        self.courseID = courseID

    def viewAssignedCourse(self, username):
        try:
            # Read the course.csv file to check if courses are assigned
            csvData = pd.read_csv("course.csv")
            courses_found = False

            print("\nAssigned Courses:")

            # Iterate through the course data to find assigned courses
            for i in range(len(csvData)):
                if self.username == str(csvData.loc[i, "username"]):
                    # Print course details if a match is found
                    print(f"Course ID: {csvData.loc[i, 'courseID']}, Course Title: {csvData.loc[i, 'courseTitle']}")
                    courses_found = True

            # If no courses are found, inform the user
            if not courses_found:
                print("No class assigned.")

        except FileNotFoundError:
            print("Error: No assigned classes available for display.")






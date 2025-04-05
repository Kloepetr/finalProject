from adminClass import Admin;
#Vairables use camel case, methods use underscores

def main():
    #First we want to try and login
    #login comes from util.py by doing "from util import login"
    #retValue = login("admin.csv");
    #def login(filename):

    # retValue = Admin.admin_login();
    retValue = Admin();

    if retValue.username == None:
        # print("Login failed, too many attempts in one session, exiting program");
        return 0;

    # print("\nLogin Successful!");
    choice = -1
    while(1):
        choice = Admin.main_menu();
        if choice == "1":
            Admin.add_student();
        elif choice == "2":
            Admin.add_instructor();
        elif choice == "3":
            Admin.add_course();
        elif choice == "4":
            print("Exiting Program. Goodbye!!!\n")
            return 0;
        elif choice == "5":
            Admin.showStudent();
            print("\n")
        elif choice == "6":
            Admin.showInstructor();
            print("\n")
        elif choice == "7":
            Admin.showCourse();
            print("\n")
        elif choice == "8":
            Admin.showEnrollmentInfo();
            print("\n")
        else:
            print("Invalid choice, please choose a valid option!\n");

main();

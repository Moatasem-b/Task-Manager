from user import User
from task import Task

class TaskManager:
    def __init__(self) -> None:
        self.__users = []

    def register(self):
        username = input("Enter username: ")
        pw = input("Enter password: ")
        self.add_user(username, pw)

    def add_user(self, name, pw):
        new_user = User(name, pw)
        self.__users.append(new_user)

    def log_in(self):
        username = input("Enter username: ")
        pw = input("Enter password: ")
        self.confirm_login(username, pw)

    def confirm_login(self, username, pw): 
        for user in self.__users:
            if user.get_username() == username and user.get_password() == pw:
                self.display_user_page(user)

        print("Incorrect username or password")

    def get_choice(self, start, end):
        choice = None
        while True:
            choice = input("Enter a choice: ")
            if choice < start or choice > end:
                print("Invalid choice")
            else:
                break
        return choice
    
    def display_main_menu(self):
        print("1. Admin login")
        print("2. User login")
        print("3. User registration")
        print("4. Quit")


    def display_user_menu(self):
        print("1. Add task")
        print("2. Delete task")
        print("3. Modify task")
        print("4. Sort tasks")
        print("5. display tasks")
        print("6. log out")

    def main_operations(self, choice):
        match choice:
            case "1":
                print("Coming soon!")    # admin login
            case "2":
                self.log_in()
            case "3":
                self.register()
            case "4":
                print("Thanks for using our app.")

    def user_operations(self, user, choice):
        match choice:
            case "1":
                user.add_task()
            case "2":
                user.delete_task()
            case "3":
                print("Coming soon!")    # modify task
            case "4":
                user.sort_tasks()
            case "5":
                user.display_tasks()
            case "6":
                print("Logging out...")

    def display_main_page(self):
        print(f"Welcome To Task Manager")
        print("-------------------------------------------")
        while True:
            self.display_main_menu()
            choice = self.get_choice("1", "4")
            self.main_operations(choice)
            print("-------------------------------------------")
            if choice == "4":
                break

    def display_user_page(self, user):
        print(f"Welcome back {user.get_username()}")
        print("-------------------------------------------")
        while True:
            self.display_user_menu()
            choice = self.get_choice("1", "6")
            self.user_operations(user, choice)
            print("-------------------------------------------")
            if choice == "6":
                break


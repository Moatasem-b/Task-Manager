from task import Task

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__tasks = []

    def set_username(self, new_username):
        self.__username = new_username

    def set_password(self, new_password):
        self.__password = new_password

    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password

    def add_task(self):
        task_name = input("Enter a task: ")
        task_deadline = input("Enter the deadline (YYYY-MM-DD): ")
        self.create_task(task_name, task_deadline)

    def create_task(self, task_name, task_deadline):
        new_task = Task(task_name, task_deadline)
        self.__tasks.append(new_task)

    def delete_task(self):
        task_name = input("Enter the task to be deleted: ")
        self.confirm_delete_task(task_name)

    def confirm_delete_task(self, task_name):
        answer = input("Are you sure? (Y/N): ")
        if answer.upper() == "Y":
            try:
                self.__tasks.remove(Task(task_name, None))
            except ValueError:
                print("No matching task found")

    def sort_tasks(self):
        self.__tasks.sort()

    def get_task_index(self, task_name):
        return self.__tasks.index(task_name)

    def check_task(self, task_name, bool = True):
        try:
            index = self.get_task_index(task_name)
            self.__tasks[index].check(bool)
        except ValueError:
            print("No matching task found")

    def display_tasks(self):
        for task in self.__tasks:
            print(task)

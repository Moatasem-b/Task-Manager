class Task:
    def __init__(self, name, deadline):
        self.__name = name
        self.__deadline = deadline
        self.__is_completed = False

    def set_name(self, new_name):
        self.__name = new_name

    def set_date(self, new_deadline):
        self.__deadline = new_deadline

    def check(self, bool = True):
        self.__is_completed = bool

    def get_name(self):
        return self.__name
    
    def get_deadline(self):
        return self.__deadline
    
    def is_completed(self):
        return self.__is_completed
    
    def clear(self):
        self.__name = None
        self.__deadline = None
        self.__is_completed = None

    def __eq__(self, other):
        if not isinstance(other, Task):
            raise TypeError

        if self.__name == other.__name:
            return True
        
        return False
    
    def __lt__(self, other):
        if not isinstance(other, Task):
            raise TypeError

        return self.__deadline < other.__deadline

    def __str__(self):
        try:
            task = "Task: " + self.__name + "\n"
            deadline = "Deadline: " + self.__deadline + "\n"
            status = "Completed" if self.__is_completed else "Holding"
            return (task + deadline + status)
        except TypeError:
            return ""
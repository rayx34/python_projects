from typing_extensions import Self


class Tasks:

    def __init__(self):
        self.task_dict = {
            'high': [],
            'medium': [],
            'low': [],
        }
    def display_tasks(self):
        for key in self.task_dict.keys():
            print(key)
        priority = input("\nChoose what priority to display: ")
        if len(self.task_dict[priority]) < 1:
            print("No tasks in this priority.")
        else:
            for task in self.task_dict[priority]:
                print(task)
    
    def add_task(self):
        '''Adds new task to dictionary under user picked priority'''
        priority = input("\nEnter priority: ")
        task = input("Enter task: \n")
        self.task_dict[priority].append(task)
        print("Task added!")
    
    def remove_task(self):
        '''Removes task from user picked priority'''
        count = 1
        priority = input("\nEnter priority: ")
        if len(self.task_dict[priority]) < 1:
            print("No tasks to remove.")
        else:
            for task in self.task_dict[priority]:
                print(f"{count}. {task}")
            remove_task = int(input("Choose what task to remove: "))
            self.task_dict[priority].remove(self.task_dict[priority][remove_task - 1])
            print("Task removed!")

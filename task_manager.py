import csv
import re

# this represents a single task 
class Task:
    def __init__(self, description, priority="Low", completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
        }

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = []
# adds a task to the list 
    def add_task(self, description, priority="Low"):
        # makes sure the priority is valid using regex
        if priority and not re.match(r"^(High|Medium|Low)$", priority, re.IGNORECASE):
            raise ValueError("Priority must be High, Medium, or Low.")
        #creats the task and add it to the list 
        task = Task(description, priority.capitalize())
        self.tasks.append(task)
# returns all the tasks in a a simple format 
    def get_all_tasks(self):
        return [task.to_dict() for task in self.tasks]
#marks down a task as completed 
    def mark_task_complete(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.completed = True
                return True
        return False
# saves all the tasks to a csv file 
    def save_tasks(self):
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Priority", "Completed"])
            for task in self.tasks:
                writer.writerow([task.description, task.priority, task.completed])
# loads task from the csv file 
    def load_tasks(self):
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                self.tasks = [
                    Task(row["Description"], row["Priority"], row["Completed"] == "True")
                    for row in reader
                ]
        except FileNotFoundError:
            print("No saved tasks found. Starting with an empty list.")
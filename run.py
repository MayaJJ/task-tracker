import argparse
import json

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Incomplete"
                print(f"[{index}] Description: {task.description} | Due Date: {task.due_date} | Status: {status}")

    def update_task(self, index, description, due_date):
        if index >= 0 and index < len(self.tasks):
            task = self.tasks[index]
            task.description = description
            task.due_date = due_date
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def mark_task_complete(self, index):
        if index >= 0 and index < len(self.tasks):
            task = self.tasks[index]
            task.mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def save_tasks_to_file(self, filename):
        with open(filename, "w") as file:
            tasks_data = []
            for task in self.tasks:
                task_data = {
                    "description": task.description,
                    "due_date": task.due_date,
                    "completed": task.completed
                }
                tasks_data.append(task_data)
            json.dump(tasks_data, file)

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(task_data["description"], task_data["due_date"])
                    task.completed = task_data["completed"]
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

def main():
    tracker = TaskTracker()
    tracker.load_tasks_from_file("tasks.json")

    parser = argparse.ArgumentParser(description="Task Tracker")
    parser.add_argument("-a", "--add", metavar="description due_date", nargs=2, help="Add a new task")
    parser.add_argument("-v", "--view", action="store_true", help="View tasks")
    parser.add_argument("-u", "--update", metavar="index description due_date", nargs=3, help="Update task")
    parser.add_argument("-c", "--complete", metavar="index", type=int, help="Mark task as complete")

    args = parser.parse_args()

    if args.add:
        description, due_date = args.add
        tracker.add_task(description, due_date)
        print("Task added successfully.")
        tracker.save_tasks_to_file("tasks.json")

    if args.view:
        print("Task List:")
        tracker.display_tasks()

    if args.update:
        index, description, due_date = args.update
        tracker.update_task(int(index), description, due_date)
        tracker.save_tasks_to_file("tasks.json")

    if args.complete is not None:
        index = args.complete
        tracker.mark_task_complete(index)
        tracker.save_tasks_to_file("tasks.json")

if __name__ == "__main__":
    main()







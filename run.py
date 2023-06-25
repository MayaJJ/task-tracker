import argparse

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

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

def main():
    tracker = TaskTracker()

    parser = argparse.ArgumentParser(description="Task Tracker")
    parser.add_argument("-a", "--add", metavar="description due_date", nargs=2, help="Add a new task")
    parser.add_argument("-v", "--view", action="store_true", help="View tasks")

    args = parser.parse_args()

    if args.add:
        description, due_date = args.add
        tracker.add_task(description, due_date)
        print("Task added successfully.")

    if args.view:
        print("Task List:")
        tracker.display_tasks()

if __name__ == "__main__":
    main()



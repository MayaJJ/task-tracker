import argparse
from datetime import datetime
from operator import attrgetter


class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        due_date = self.due_date.strftime("%Y-%m-%d") if self.due_date else "Not specified"
        return f"Description: {self.description} | Due Date: {due_date} | Status: {status}"


class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        task = Task(description, due_date)
        self.tasks.append(task)
        print("Task added successfully!")

    def update_task(self, task_index, description=None, due_date=None):
        task = self.tasks[task_index]
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        print("Task updated successfully!")

    def delete_task(self, task_index):
        del self.tasks[task_index]
        print("Task deleted successfully!")

    def complete_task(self, task_index):
        task = self.tasks[task_index]
        task.completed = True
        print("Task marked as completed!")

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        else:
            for index, task in enumerate(self.tasks):
                print(f"[{index}] {task}")

    def view_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if not incomplete_tasks:
            print("No incomplete tasks found!")
        else:
            for index, task in enumerate(incomplete_tasks):
                print(f"[{index}] {task}")

    def view_overdue_tasks(self):
        today = datetime.today().date()
        overdue_tasks = [task for task in self.tasks if not task.completed and task.due_date and task.due_date < today]
        if not overdue_tasks:
            print("No overdue tasks found!")
        else:
            for index, task in enumerate(overdue_tasks):
                print(f"[{index}] {task}")

    def sort_tasks_by_due_date(self):
        sorted_tasks = sorted(self.tasks, key=attrgetter("due_date"))
        if not sorted_tasks:
            print("No tasks found!")
        else:
            for index, task in enumerate(sorted_tasks):
                print(f"[{index}] {task}")


def main():
    parser = argparse.ArgumentParser(description="Task Tracker - Manage your tasks")
    parser.add_argument("-a", "--add", metavar=("DESCRIPTION", "DUE_DATE"), nargs="+", help="Add a new task")
    parser.add_argument("-u", "--update", metavar=("INDEX", "DESCRIPTION", "DUE_DATE"), nargs="+",
                        help="Update a task")
    parser.add_argument("-d", "--delete", metavar="INDEX", type=int, help="Delete a task")
    parser.add_argument("-c", "--complete", metavar="INDEX", type=int, help="Complete a task")
    parser.add_argument("-va", "--view-all", action="store_true", help="View all tasks")
    parser.add_argument("-vi", "--view-incomplete", action="store_true", help="View incomplete tasks")
    parser.add_argument("-vo", "--view-overdue", action="store_true", help="View overdue tasks")
    parser.add_argument("-s", "--sort", action="store


import argparse
import json
from datetime import datetime


class Task:
    """Class representing a task."""

    def __init__(self, description, due_date):
        """
        Initialize a task object.

        Args:
            description (str): Description of the task.
            due_date (str): Due date of the task in format 'YYYY-MM-DD'.
        """
        self.description = description
        self.due_date = due_date
        self.completed = False
def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

class TaskTracker:
    """Class representing a task tracker application."""

    def __init__(self):
        """Initialize a task tracker object."""
        self.tasks = []

    def add_task(self, description, due_date):
        """
        Add a new task to the task tracker.

        Args:
            description (str): Description of the task.
            due_date (str): Due date of the task in format 'YYYY-MM-DD'.
        """
        if not description or not due_date:
            print("Description and due date cannot be empty.")
            return

        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid due date format. Please use 'YYYY-MM-DD' format.")
            return

        task = Task(description, due_date)
        self.tasks.append(task)

    def display_tasks(self):
        """Display the list of tasks in the task tracker."""
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Incomplete"
                print(f"[{index}] Description: {task.description}")
                print(f"Due Date: {task.due_date}")
                print(f"Status: {status}")

    def update_task(self, index, description, due_date):
        """
        Update the details of a task in the task tracker.

        Args:
            index (int): Index of the task to update.
            description (str): Updated description of the task.
            due_date (str): Updated due date of the task in format
            'YYYY-MM-DD'.
        """
        if index >= 0 and index < len(self.tasks):
            if not description or not due_date:
                print("Description and due date cannot be empty.")
                return

            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid due date format.")
                print("Please use 'YYYY-MM-DD' format.")
                return

            task = self.tasks[index]
            task.description = description
            task.due_date = due_date
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def mark_task_complete(self, index):
        """
        Mark a task as complete in the task tracker.

        Args:
            index (int): Index of the task to mark as complete.
        """
        if index >= 0 and index < len(self.tasks):
            task = self.tasks[index]
            task.mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task index.")
def delete_task(self, index):
        """
        Delete a task from the task tracker.

        Args:
            index (int): Index of the task to delete.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def save_tasks_to_file(self, filename):
        """
        Save the tasks in the task tracker to a JSON file.

        Args:
            filename (str): Name of the file to save the tasks.
        """
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
        """
        Load tasks from a JSON file into the task tracker.

        Args:
            filename (str): Name of the file to load the tasks from.
        """
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(
                        task_data["description"],
                        task_data["due_date"]
                    )
                    task.completed = task_data["completed"]
                    self.tasks.append(task)
        except FileNotFoundError:
            print("File not found hence it has been created.")

    def display_incomplete_tasks(self):
        """View incomplete tasks in the task tracker."""
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if not incomplete_tasks:
            print("No incomplete tasks found.")
        else:
            for index, task in enumerate(incomplete_tasks):
                print(f"[{index}] Description: {task.description}")
                print(f"Due Date: {task.due_date}")
 def display_overdue_tasks(self):
        """View overdue tasks in the task tracker."""
        today = datetime.now().date()
        overdue_tasks = [task for task in self.tasks if isOverdue(task, today)]
        if not overdue_tasks:
            print("No overdue tasks found.")
        else:
            for index, task in enumerate(overdue_tasks):
                print(f"[{index}] Description: {task.description} | Due Date: {task.due_date}")

    def sort_tasks_by_due_date(self):
        """Sort tasks by due date."""
        self.tasks.sort(key=lambda task: datetime.strptime(task.due_date, '%Y-%m-%d'))
        print("Tasks sorted by due date.")


def isOverdue(task, today):
    return not task.completed and datetime.strptime(task.due_date, '%Y-%m-%d').date() < today















































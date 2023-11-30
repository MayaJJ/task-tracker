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














































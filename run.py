import argparse
from datetime import datetime 
from operator import attrgetter

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed
        



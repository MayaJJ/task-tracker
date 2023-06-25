![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

# Task Tracker

## Project Description
Task Tracker is a command-line application that allows you to manage and track your tasks. It provides functionality to add new tasks, view existing tasks, update task details, and mark tasks as complete. The purpose of this project is to provide a simple and efficient way to keep track of your tasks and their due dates.

## Installation Instructions
To run the Task Tracker application, please ensure you have the following dependencies installed:

- Python 3

Follow these steps to install and set up the application:

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required dependencies by running the following command:

pip install -r requirements.txt


## Usage Instructions
To use the Task Tracker application, follow the instructions below:

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the following command to add a new task:

python3 run.py -a "Task description" "Due date (YYYY-MM-DD)"      

This will add a new task with the provided description and due date.

3. Run the following command to view the list of tasks:

python3 run.py -v

This will display all the tasks along with their descriptions, due dates, and completion status.

4. Run the following command to update a task:

python3 run.py -u task_index "New task description" "New due date (YYYY-MM-DD)"

Replace `task_index` with the index of the task you want to update. This command will update the task with the provided index to the new description and due date.

5. Run the following command to mark a task as complete:

python3 run.py -c task_index

Replace `task_index` with the index of the task you want to mark as complete. This will mark the task as complete.

## Additional Features
There are no additional features implemented beyond the basic requirements at this time.

## Known Issues or Limitations
There are no known issues or limitations in the Task Tracker application.

Feel free to reach out if you have any questions or need further assistance.

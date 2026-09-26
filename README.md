# Task Manager

A lightweight, menu-driven task manager that runs in the console. Add tasks, review their completion status, mark tasks as complete, and remove tasks by selecting their number. Tasks are stored in memory for the current session and are cleared when the application exits.

## Requirements

- Python 3
- No third-party packages

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.

## Usage

Start the application with:

```powershell
python main.py
```

Choose an option from the menu:

1. **View tasks** displays tasks with their current completion status.
2. **Add a task** prompts for a task description. Empty descriptions are not accepted.
3. **Mark a task as complete** displays the task list and prompts for the number to complete.
4. **Delete a task** displays the task list and prompts for the number to remove.
5. **Exit** closes the application.

Task numbers are shown in the list. Enter a valid number when completing or deleting a task; the list is numbered again after changes.

# # Commands
#
# - `add`: Add a new task
# - `remove <task_number>`: Remove a task by its number
# - `list`: List all tasks
# - `complete <task_number>`: Mark a task as completed
# - `exit`: Exit the task manager

from Art import logo

print(logo)

task_number = 0
choice = input("What task do you want to perform? (Add/Remove/list/complete/exit): ").lower()
if choice == "add":
    task_number += 1
    task = input(f"what is the task?{task_number}: ")
    print(task)
# This is what I have, please don't be angry because I'm slow









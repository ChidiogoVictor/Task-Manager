# Commands
# - `add`: Add a new task
# - `remove <task_number>`: Remove a task by its number
# - `list`: List all tasks
# - `complete <task_number>`: Mark a task as completed
# - `exit`: Exit the task manager

from Art import logo

print(logo)
# create a list for storing tasks
tasks = []
# create  a while loop which will be terminated if the user selects the corect
# choice else the loop will continue
while True:
    # collect the user input through the menu (eihter number or the word)
    # and convert it to lowercase this will also convert int to str
    choice = input(
        "What task do you want to perform?\n1. Add\n2. Remove\n3. List\n4. Complete\n5. Exit\n "
    ).lower()
    # add Functionality
    if choice in ["add", "1"]:
        task = input("What is the task?: ")
        # put the tasks in a dict  to mantain if its done or not
        taskdict = {"tsk": task, "completed": False}
        # add the tasks to the tasklist
        tasks.append(taskdict)
        for task in tasks:
            print(f"Task: {task['tsk']}, Completed: {task['completed']}")

    elif choice in ["remove", "2"]:
        print("rm")
        # Handle remove functionality
    elif choice in ["list", "3"]:
        print("ls")
        # Handle list functionality

    elif choice in ["complete", "4"]:
        print("done")
        # Handle complete functionality

    elif choice in ["exit", "5"]:
        print("byeee")
        break  # Exit the loop if 'exit' is chosen

    else:
        print("Invalid choice. Please enter a valid option.")

# This is what I have, please don't be angry because I'm slow

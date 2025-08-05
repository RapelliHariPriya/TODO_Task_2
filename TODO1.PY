# task_manager.py

import os

FILE_PATH = "my_tasks.txt"

def load_all_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return [line.strip() for line in f.readlines()]

def store_tasks(task_list):
    with open(FILE_PATH, "w") as f:
        for item in task_list:
            f.write(item + "\n")

def list_tasks(task_list):
    if not task_list:
        print("Your task list is empty!\n")
        return
    print("\n--- Your Tasks ---")
    for idx, val in enumerate(task_list, start=1):
        print(f"{idx}) {val}")
    print()

def create_task(task_list):
    item = input("Enter task to add: ").strip()
    if item:
        task_list.append(item)
        store_tasks(task_list)
        print("Task successfully added.\n")
    else:
        print("Empty input. No task was added.\n")

def delete_task(task_list):
    if not task_list:
        print("No tasks to delete.\n")
        return

    list_tasks(task_list)

    while True:
        choice = input("Enter task number to delete (or type 'x' to cancel): ").strip()
        if choice.lower() == 'x':
            print("Cancelled.\n")
            return
        if not choice.isdigit():
            print("Invalid input. Enter a number.")
            continue

        index = int(choice)
        if 1 <= index <= len(task_list):
            removed = task_list.pop(index - 1)
            store_tasks(task_list)
            print(f"Deleted: {removed}\n")
            return
        else:
            print("Out of range. Try again.")

def start_task_manager():
    print("📋 Welcome to Simple Task Manager")

    tasks = load_all_tasks()

    while True:
        print("Choose one:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Quit")

        selection = input("Option (1-4): ").strip()

        if selection == '1':
            list_tasks(tasks)
        elif selection == '2':
            create_task(tasks)
        elif selection == '3':
            delete_task(tasks)
        elif selection == '4':
            print("Exiting... See you next time!")
            break
        else:
            print("Invalid option. Please select between 1 and 4.\n")

if __name__ == "__main__":
    start_task_manager()

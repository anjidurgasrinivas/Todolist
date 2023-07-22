import os

def display_tasks(tasks):
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()

def add_task(tasks, task):
    tasks.append(task)
    print(f"\n'{task}' added to the To-Do List.\n")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"\n'{removed_task}' removed from the To-Do List.\n")
    else:
        print("\nInvalid task index. No task removed.\n")

def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
    return tasks

def main():
    filename = "todo.txt"
    tasks = load_tasks(filename)

    while True:
        display_tasks(tasks)
        print("Options:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Exit")

        choice = input("Enter the option number: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(tasks, task)
        elif choice == "2":
            index = int(input("Enter the task number to remove: "))
            remove_task(tasks, index)
        elif choice == "3":
            save_tasks(tasks, filename)
            print("To-Do List saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


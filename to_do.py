import os

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return [task.strip() for task in file.readlines()]
    return []

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()

# Function to add a task
def add_task(tasks):
    task = input("Enter a task to add: ").strip()
    if task:
        tasks.append(task)
        print(f"'{task}' has been added to your to-do list.\n")
    else:
        print("Task cannot be empty.\n")

# Function to delete a task
def delete_task(tasks):
    if tasks:
        display_tasks(tasks)
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from your to-do list.\n")
            else:
                print("Invalid task number. Please try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")
    else:
        print("Your to-do list is empty, no tasks to delete.\n")

# Main function to run the to-do list application
def main():
    filename = "todo_list.txt"  # File to store tasks
    tasks = load_tasks(filename)  # Load existing tasks from file

    while True:
        print("To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)  # Save tasks to file before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

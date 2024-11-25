# todo.py

# List to store tasks
tasks = []

# Function to show the menu
def show_menu():
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to view tasks
def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks to display.")

def remove_task():
    view_tasks()
    try: 
        task_num = int(input("Enter the task number to remove: "))
        if 1<= task_num <= len(tasks): 
            removed_task = tasks.pop(task_num -1)
            print(f"Task '{removed_task}' removed.")
        else: 
            print("Invalid task number.")
    except ValueError: 
        print("Please enter a valid number.")

def main(): 
    while True: 
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
# To-Do List in Python

def display_todo_list(todo_list):
    print("To-Do List:")
    for task, status in todo_list.items():
        print(f"[{'X' if status else ' '}] {task}")

def add_task(todo_list, task):
    todo_list[task] = False
    print(f"Task '{task}' added to the to-do list.")

def complete_task(todo_list, task):
    if task in todo_list:
        todo_list[task] = True
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def remove_task(todo_list, task):
    if task in todo_list:
        del todo_list[task]
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

if __name__ == "__main__":
    todo_list = {}

    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter the task to add in to-do list: ")
            add_task(todo_list, task)
        elif choice == '3':
            task = input("Enter the task to mark as task completed: ")
            complete_task(todo_list, task)
        elif choice == '4':
            task = input("Enter the task to remove from the to-do list: ")
            remove_task(todo_list, task)
        elif choice == '5':
            print("Good to make code on to-do list using python program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4/5).")

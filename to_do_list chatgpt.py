def add_task(todo_list):
    task = input("Add your task: ")
    todo_list.append(task)
    print("Task added.")

def view_tasks(todo_list):
    if not todo_list:
        print("There is no task.")
    else:
        print("Tasks:")
        for task in todo_list:
            print(task)

def remove_task(todo_list):
    if not todo_list:
        print("There is no task.")
    else:
        task_to_remove = input("Type the task you want to remove: ")
        if task_to_remove in todo_list:
            todo_list.remove(task_to_remove)
            print("Task removed.")
        else:
            print("Task not found.")

def main():
    todo_list = []

    while True:
        command = input("Choose your command (add, view, remove, exit): ")

        if command == "add":
            add_task(todo_list)

        elif command == "view":
            view_tasks(todo_list)

        elif command == "remove":
            remove_task(todo_list)

        elif command == "exit":
            print("Exiting the app.")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

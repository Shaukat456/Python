# index.py

# A simple Python project: Task Manager (without OOP)
# Concepts used: functions, lists, dictionaries, loops, conditionals, input/output

tasks = []


def add_task(description):
    task = {"description": description, "completed": False}
    tasks.append(task)
    print(f"Task added: {description}")


def list_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx}. {task['description']} [{status}]")


def complete_task(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed['description']}")
    else:
        print("Invalid task number.")


def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            num = int(input("Enter task number to complete: "))
            complete_task(num)
        elif choice == "4":
            num = int(input("Enter task number to delete: "))
            delete_task(num)
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

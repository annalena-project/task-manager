def display_menu():
    print("\nTask Manager")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice == "1":
            if tasks:
                print("\nTasks:")
                for index, task in enumerate(tasks, start=1):
                    status = "x" if task["completed"] else " "
                    print(f"{index}. [{status}] {task['description']}")
            else:
                print("No tasks yet.")
        elif choice == "2":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append({"description": task, "completed": False})
                print(f'Task added: "{task}"')
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("No tasks to mark as complete.")
                continue

            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                status = "x" if task["completed"] else " "
                print(f"{index}. [{status}] {task['description']}")

            task_choice = input("Enter the task number to mark complete: ").strip()
            if not task_choice.isdigit() or not 1 <= int(task_choice) <= len(tasks):
                print("Invalid task number.")
                continue

            selected_task = tasks[int(task_choice) - 1]
            selected_task["completed"] = True
            print(f'Task marked complete: "{selected_task["description"]}"')
        elif choice == "4":
            if not tasks:
                print("No tasks to delete.")
                continue

            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                status = "x" if task["completed"] else " "
                print(f"{index}. [{status}] {task['description']}")

            task_choice = input("Enter the task number to delete: ").strip()
            if not task_choice.isdigit() or not 1 <= int(task_choice) <= len(tasks):
                print("Invalid task number.")
                continue

            deleted_task = tasks.pop(int(task_choice) - 1)
            print(f'Task deleted: "{deleted_task["description"]}"')
        elif choice in {"1", "2", "3", "4"}:
            print("That option is not available yet.")
        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
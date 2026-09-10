tasks = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task removed.")
            else:
                print("Invalid task number.")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

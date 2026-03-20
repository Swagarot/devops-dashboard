def manage_tasks():
    tasks = []  # This list stays in memory while the function runs
    
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task by number")
        print("4. Return to main menu")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            new_task = input("Enter the task description: ")
            tasks.append(new_task)
            print("Task added successfully!")
            
        elif choice == '2':
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Current Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                    
        elif choice == '3':
            if not tasks:
                print("Nothing to remove.")
                continue
            
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '4':
            print("Returning to main menu...")
            break
            
        else:
            print("Invalid choice, please try again.")

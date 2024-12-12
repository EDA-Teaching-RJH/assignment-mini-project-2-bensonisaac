from task_manager import TaskManager

# this displays the main menu
def display_menu():
    print("\nTask Manager")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Save tasks to file")
    print("5. Load tasks from file")
    print("6. Exit")

# this runs the main function of the task manager 
def main():
    task_manager = TaskManager("tasks.csv")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
# this handles each menu option
        if choice == "1":
            description = input("Enter the task description: ")
            priority = input("Enter priority (High, Medium, Low) or leave blank: ")
            task_manager.add_task(description, priority)
            print("Task added successfully!")
        elif choice == "2":
            tasks = task_manager.get_all_tasks()
            print("\nTasks:")
            for task in tasks:
                status = "Completed" if task["completed"] else "Pending"
               # prints each task with the details of it 
                print(f"- {task['description']} (Priority: {task['priority']}) [{status}]")
        elif choice == "3":
            description = input("Enter the description of the task to mark as complete: ")
            if task_manager.mark_task_complete(description):
                print("Task marked as complete!")
            else:
                print("Task not found.")
        elif choice == "4":
            task_manager.save_tasks() # saves task to the file 
            print("Tasks saved to file.")
        elif choice == "5":
            task_manager.load_tasks() # loads task from the file 
            print("Tasks loaded from file.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            # stops invalid inputs 

if __name__ == "__main__":
    main()
    #runs the main function of the script 
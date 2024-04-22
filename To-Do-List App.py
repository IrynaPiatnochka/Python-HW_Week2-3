# Creating an empty list for tasks.

tasks = []

# Creating a function for "Invalid input".

def invalid():
    print("Invalid input.")

# Building a menu with choices for the application.

while True:
    print("\n~~~~~ To-Do List App ~~~~~")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task")
    print("4. Delete task")
    print("5. Quit")
    
# Implementing feature of adding a task to a list.
 
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Add a task to the list:")
        tasks.append({"desc": task, "status": "incomplete"})

# Implementing feature of viewing the list of tasks with their titles and statuses .
   
    elif choice == 2:
        for index, task in enumerate(tasks, start = 1):
            print(f"{index}. {task['desc']} - {task['status']}")

# Implementing feature of marking task as complete in the list.

    elif choice == 3:
        task_index = int(input("Which task do you want to mark? "))
        tasks[task_index - 1]["status"] = "complete"

# Implementing feature of deleting a task from the list.

    elif choice == 4:
        try:
            task_index = int(input("Which task do you want to delete? "))
            removed_task = tasks.pop(task_index - 1)
        except ValueError:
            print("Please enter a number.")
        except:
            invalid()
        else:
            print(f"Task {removed_task["desc"]} was successfully deleted !")

# Implementing feature of quiting the application.

    elif choice == 5:
        print("You successfully exited the application.")
        break

    else:
        invalid()


    


    
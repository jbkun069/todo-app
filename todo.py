tasks = []

def addtask():
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})
    print(f"{task} is added")

def showtasks():
    if not tasks:
        print("No tasks added yet")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "X"
            print(f"{i+1}.[{status}] {task['task']}")
            
def marktasks():
    showtasks()
    if tasks:
        try:
            num = int(input("Enter task to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num-1]["done"] = True
                print(f"Task '{tasks[num-1]['task']}' marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    else:
        print("No task to mark!")
        


while True:
    print("Todo-App")
    print("1.Add Task\n2.Show tasks\n3.Mark task as done\n4.Quit")
    choice = int(input("Enter a choice(1,2,3): "))
    
    if choice == 1:
        addtask()
    elif choice == 2:
        showtasks()
    elif choice == 3:
        marktasks()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")
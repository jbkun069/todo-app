tasks = []

def addtask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"{task} is added")

def showtasks():
    if not tasks:
        print("No tasks added yet")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")

while True:
    print("Todo-App")
    print("1.Add Task\n2.Show tasks\n3.Quit")
    choice = int(input("Enter a choice(1,2,3): "))
    
    if choice == 1:
        addtask()
    elif choice == 2:
        showtasks()
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")
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
            print(f"{i}.{task}")


addtask()
addtask()
addtask()

showtasks()
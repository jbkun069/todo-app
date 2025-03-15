tasks = []

def addtask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"{task} is added")

addtask()    
addtask()    
print("Current tasks: ", tasks)

import tkinter as tk

# List to store tasks as dictionaries
tasks = []

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x500")

# Entry box for new tasks
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=20, pady=20)

# Add Task button
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        update_task_list()
        task_entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(root, height=20, width=80)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Function to update the Listbox
def update_task_list():
    task_listbox.delete(0, tk.END)
    for item in tasks:
        status = "[✓]" if item["done"] else "[X]"
        task_listbox.insert(tk.END, f"{status} {item['task']}")

# Mark Task as Done button
def mark_task_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        update_task_list()

mark_button = tk.Button(root, text="Mark Done", command=mark_task_done)
mark_button.grid(row=2, column=0, padx=10, pady=0, sticky="ew")

# Delete Task button
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)  # Remove the task
        update_task_list()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Start the app
root.mainloop()
import tkinter as tk

# List to store tasks as dictionaries
tasks = []

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x500")
root.configure(bg="#A8C1FF")  # Set window background color

# Entry box for new tasks
task_entry = tk.Entry(root, width=30, bg="#F5F5F5", fg="#000000", borderwidth=2)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Add Task button
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        update_task_list()
        task_entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#6f0b94", fg="white", activebackground="#45A049")
add_button.grid(row=0, column=1, padx=10, pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(root, height=20, width=80, bg="#FFFFFF", fg="#000000", selectbackground="#BBDEFB")
task_listbox.grid(row=1, column=0, columnspan=10, padx=10, pady=8)

# Function to update the Listbox with colors
def update_task_list():
    task_listbox.delete(0, tk.END)
    for item in tasks:
        status = "[✓]" if item["done"] else "[ ]"
        task_text = f"{status} {item['task']}"
        task_listbox.insert(tk.END, task_text)
        # Get the index of the last inserted item
        last_index = task_listbox.size() - 1
        # Color based on done status
        if item["done"]:
            task_listbox.itemconfig(last_index, {'fg': "#2E7D32"})  # Dark green for done
        else:
            task_listbox.itemconfig(last_index, {'fg': "#000000"})  # Black for undone

# Toggle Task status button
def toggle_task_status():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_task_list()

mark_button = tk.Button(root, text="Toggle Status", command=toggle_task_status, bg="#6f0b94", fg="white", activebackground="#45A049")
mark_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Delete Task button
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_task_list()

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#6f0b94", fg="white", activebackground="#45A049")
delete_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Initial list update
update_task_list()

# Start the app
root.mainloop()
import tkinter as tk
from tkinter import messagebox  # Added import for messagebox
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# List to store tasks as dictionaries
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                tasks = json.load(file)
    except Exception as e:
        print(f"Error loading tasks: {e}")

# Save tasks to file
def save_tasks():
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file)
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x550")  # Adjusted height slightly
root.configure(bg="#A8C1FF")
root.resizable(True, True)  # Allow resizing

# Create a main frame to contain everything
main_frame = tk.Frame(root, bg="#A8C1FF", padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Top frame for task entry
top_frame = tk.Frame(main_frame, bg="#A8C1FF")
top_frame.pack(fill=tk.X, pady=(0, 5))

# Entry box for new tasks
task_entry = tk.Entry(top_frame, width=30, bg="#F5F5F5", fg="#000000", borderwidth=2)
task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

# Add Task button
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        update_task_list()
        task_entry.delete(0, tk.END)
        save_tasks()

add_button = tk.Button(top_frame, text="Add Task", command=add_task, bg="#6f0b94", fg="white", activebackground="#45A049")
add_button.pack(side=tk.RIGHT)

# Create a frame for the listbox
list_frame = tk.Frame(main_frame, bg="#A8C1FF")
list_frame.pack(fill=tk.BOTH, expand=True, pady=5)

# Add scrollbars to the listbox
scrollbar_y = tk.Scrollbar(list_frame)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_x = tk.Scrollbar(list_frame, orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

# Listbox to display tasks
task_listbox = tk.Listbox(list_frame, height=15, bg="#FFFFFF", fg="#000000", 
                         selectbackground="#BBDEFB",
                         yscrollcommand=scrollbar_y.set,
                         xscrollcommand=scrollbar_x.set)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure the scrollbars
scrollbar_y.config(command=task_listbox.yview)
scrollbar_x.config(command=task_listbox.xview)

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

# Button frame for task actions
button_frame = tk.Frame(main_frame, bg="#A8C1FF")
button_frame.pack(fill=tk.X, pady=5)

# Toggle Task status button
def toggle_task_status():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_task_list()
        save_tasks()

mark_button = tk.Button(button_frame, text="Toggle Status", command=toggle_task_status, bg="#6f0b94", fg="white", activebackground="#45A049")
mark_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

# Delete Task button
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_task_list()
        save_tasks()

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#6f0b94", fg="white", activebackground="#45A049")
delete_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

# Clear all tasks button
def clear_all_tasks():
    if tasks:
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
            tasks.clear()
            update_task_list()
            save_tasks()

# Add Clear All button
clear_button = tk.Button(main_frame, text="Clear All", command=clear_all_tasks, bg="#FF5252", fg="white", activebackground="#D32F2F")
clear_button.pack(fill=tk.X, pady=5)

# Add a search frame
search_frame = tk.Frame(main_frame, bg="#A8C1FF")
search_frame.pack(fill=tk.X, pady=(10, 0))

search_label = tk.Label(search_frame, text="Search:", bg="#A8C1FF")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame, width=15, bg="#F5F5F5")
search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

# Filter options
filter_var = tk.StringVar(root)
filter_var.set("All")
filter_options = ["All", "Done", "Not Done"]
filter_menu = tk.OptionMenu(search_frame, filter_var, *filter_options)
filter_menu.config(bg="#F5F5F5")
filter_menu.pack(side=tk.LEFT, padx=5)

def search_tasks():
    search_term = search_entry.get().lower()
    filter_option = filter_var.get()
    
    task_listbox.delete(0, tk.END)
    for i, item in enumerate(tasks):
        # Apply filters
        if filter_option == "Done" and not item["done"]:
            continue
        if filter_option == "Not Done" and item["done"]:
            continue
            
        # Apply search
        if search_term and search_term not in item["task"].lower():
            continue
            
        # Display matching task
        status = "[✓]" if item["done"] else "[ ]"
        task_text = f"{status} {item['task']}"
        task_listbox.insert(tk.END, task_text)
        
        # Color based on done status
        last_index = task_listbox.size() - 1
        if item["done"]:
            task_listbox.itemconfig(last_index, {'fg': "#2E7D32"})
        else:
            task_listbox.itemconfig(last_index, {'fg': "#000000"})

search_button = tk.Button(search_frame, text="Search", command=search_tasks, bg="#6f0b94", fg="white")
search_button.pack(side=tk.LEFT, padx=2)

clear_search_button = tk.Button(search_frame, text="Clear", command=update_task_list, bg="#6f0b94", fg="white")
clear_search_button.pack(side=tk.LEFT, padx=2)

# Keyboard shortcuts
def handle_keypress(event):
    if event.keysym == "Return":
        add_task()
    elif event.keysym == "Delete":
        delete_task()
    elif event.keysym == "space":
        toggle_task_status()

root.bind("<KeyPress>", handle_keypress)

# Load existing tasks
load_tasks()

# Initial list update
update_task_list()

# Handle window close
def on_closing():
    save_tasks()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the app
root.mainloop()
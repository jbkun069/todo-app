# To-Do List App

This is a feature-rich To-Do List application built with Python and Tkinter with persistent storage.

## Features
- Add new tasks with duplicate prevention
- Mark tasks as done/incomplete
- Delete individual tasks or clear all with confirmation
- Persistent storage using JSON file (tasks.json)
- Search functionality with filters (All/Done/Not Done)
- Keyboard shortcuts (Enter=Add, Delete=Remove, Space=Toggle)
- UI enhancements: 
  - Scrollable list with color coding
  - Button hover effects
  - Status indicators
- Automatic save on changes

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## Usage
1. Open a terminal or command prompt.
2. Navigate to the project folder:
   ```
   cd "d:\Coding notes\todo-app"
   ```
3. Run the application:
   ```
   python todo.py
   ```

## Notes
- Tasks are stored in-memory. Closing the application will erase the current list.

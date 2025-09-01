# Flask To-Do List

A simple To-Do List web app built with **Flask**, **SQLite**, HTML, CSS, and JavaScript.  
Users can add, update, and delete tasks.  

## Features
- Add tasks with a timestamp
- Mark tasks as complete or delete them
- Edit tasks
- Simple UI with CSS styling

## Tech Stack
- Python (Flask)
- SQLite
- HTML, CSS, JavaScript

## Setup
1. Clone the repo
2. Create a virtual environment:
   ```bash
   python -m venv venv
3. Install dependencies: pip install -r requirements.txt
4. Run the app: flask run


## Database Note
This project uses **SQLite** as the database.  
For security and simplicity, the database file (`todo.db`) is not included in this repository.  

When you run the app for the first time, a new database will be created automatically inside the `instance/` folder.  

If you want to reset your tasks, simply delete the `todo.db` file and restart the app.
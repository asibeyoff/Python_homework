import csv
import json
from abc import ABC, abstractmethod
from datetime import datetime

class Task:
    """A class representing a to-do task."""
    
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        """Initialize a task with given attributes."""
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def __str__(self):
        """Return string representation of the task."""
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or 'No due date'}, {self.status}"

class StorageHandler(ABC):
    """Abstract base class for handling task storage."""
    
    @abstractmethod
    def save(self, tasks):
        """Save tasks to the storage."""
        pass
    
    @abstractmethod
    def load(self):
        """Load tasks from the storage."""
        pass

class CSVStorageHandler(StorageHandler):
    """Storage handler for CSV files."""
    
    def __init__(self, filename="tasks.csv"):
        """Initialize with the filename."""
        self.filename = filename
    
    def save(self, tasks):
        """Save tasks to a CSV file."""
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['task_id', 'title', 'description', 'due_date', 'status'])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
    
    def load(self):
        """Load tasks from a CSV file."""
        tasks = []
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tasks.append(Task(
                        row['task_id'],
                        row['title'],
                        row['description'],
                        row['due_date'] if row['due_date'] != '' else None,
                        row['status']
                    ))
        except FileNotFoundError:
            pass
        return tasks

class JSONStorageHandler(StorageHandler):
    """Storage handler for JSON files."""
    
    def __init__(self, filename="tasks.json"):
        """Initialize with the filename."""
        self.filename = filename
    
    def save(self, tasks):
        """Save tasks to a JSON file."""
        data = [
            {
                'task_id': task.task_id,
                'title': task.title,
                'description': task.description,
                'due_date': task.due_date,
                'status': task.status
            } for task in tasks
        ]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load(self):
        """Load tasks from a JSON file."""
        tasks = []
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    tasks.append(Task(
                        item['task_id'],
                        item['title'],
                        item['description'],
                        item['due_date'],
                        item['status']
                    ))
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return tasks

class ToDoManager:
    """A class to manage to-do tasks."""
    
    def __init__(self, storage_handler):
        """Initialize with a storage handler."""
        self.storage_handler = storage_handler
        self.tasks = self.storage_handler.load()
    
    def add_task(self, task):
        """Add a new task."""
        if any(t.task_id == task.task_id for t in self.tasks):
            raise ValueError(f"Task ID {task.task_id} already exists")
        self.tasks.append(task)
        self.storage_handler.save(self.tasks)
    
    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)
    
    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        """Update a task's details."""
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                self.storage_handler.save(self.tasks)
                print("Task updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        """Delete a task."""
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.storage_handler.save(self.tasks)
        print("Task deleted successfully!")
    
    def filter_tasks(self, status):
        """Filter tasks by status."""
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print(f"No tasks found with status '{status}'.")
            return
        print(f"Tasks with status '{status}':")
        for task in filtered:
            print(task)
    
    def menu(self):
        """Display the menu and handle user input."""
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    task_id = input("Enter Task ID: ")
                    title = input("Enter Title: ")
                    description = input("Enter Description: ")
                    due_date = input("Enter Due Date (YYYY-MM-DD, or press Enter to skip): ")
                    status = input("Enter Status (Pending/In Progress/Completed): ")
                    try:
                        task = Task(
                            task_id,
                            title,
                            description,
                            due_date if due_date else None,
                            status if status else "Pending"
                        )
                        self.add_task(task)
                        print("Task added successfully!")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                elif choice == 2:
                    self.view_tasks()
                
                elif choice == 3:
                    task_id = input("Enter Task ID to update: ")
                    title = input("Enter new Title (or press Enter to skip): ")
                    description = input("Enter new Description (or press Enter to skip): ")
                    due_date = input("Enter new Due Date (YYYY-MM-DD, or press Enter to skip): ")
                    status = input("Enter new Status (or press Enter to skip): ")
                    self.update_task(
                        task_id,
                        title if title else None,
                        description if description else None,
                        due_date if due_date else None,
                        status if status else None
                    )
                
                elif choice == 4:
                    task_id = input("Enter Task ID to delete: ")
                    self.delete_task(task_id)
                
                elif choice == 5:
                    status = input("Enter Status to filter (Pending/In Progress/Completed): ")
                    self.filter_tasks(status)
                
                elif choice == 6:
                    self.storage_handler.save(self.tasks)
                    print("Tasks saved successfully!")
                
                elif choice == 7:
                    self.tasks = self.storage_handler.load()
                    print("Tasks loaded successfully!")
                
                elif choice == 8:
                    print("Goodbye!")
                    break
                
                else:
                    print("Invalid choice. Please try again.")
            
            except ValueError as e:
                print(f"Invalid input: {e}")

# Example usage
if __name__ == "__main__":
    # Choose storage handler (CSV or JSON)
    storage_handler = JSONStorageHandler()  # Switch to CSVStorageHandler() for CSV
    manager = ToDoManager(storage_handler)
    manager.menu()
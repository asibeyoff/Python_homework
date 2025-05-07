import json
import csv

# Load tasks
def load_tasks(filename="tasks.json"):
    with open(filename, "r") as f:
        return json.load(f)

# Display tasks
def display_tasks(tasks):
    for task in tasks:
        print(f"{task['id']}. {task['task']} - Completed: {task['completed']} - Priority: {task['priority']}")

# Save tasks
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

# Stats calculation
def task_statistics(tasks):
    total = len(tasks)
    completed = sum(task['completed'] for task in tasks)
    pending = total - completed
    avg_priority = sum(task['priority'] for task in tasks) / total if total else 0
    print(f"Total: {total}, Completed: {completed}, Pending: {pending}, Avg. Priority: {avg_priority:.2f}")

# Convert to CSV
def json_to_csv(json_file="tasks.json", csv_file="tasks.csv"):
    tasks = load_tasks(json_file)
    with open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# Running 
tasks = load_tasks()
display_tasks(tasks)
task_statistics(tasks)
json_to_csv()

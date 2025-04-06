# Zero Check Decorator
def check(func):
    def wrapper(a, b):
        if b == 0: return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# Test decorator
print(div(6, 2))  # Output: 3
print(div(6, 0))  # Output: "Denominator can't be zero"

# Employee Records Manager
def employee_manager():
    while True:
        # Display menu
        print("\nEmployee Records Manager\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
        choice = input("Choice (1-6): ")
        
        if choice == "1":  # Add record
            with open("employees.txt", "a") as f:
                f.write(f"{input('ID: ')}, {input('Name: ')}, {input('Position: ')}, {input('Salary: ')}\n")
            print("Added!")  # Output: "Added!"
            
        elif choice == "2":  # View all
            try:
                with open("employees.txt", "r") as f:
                    print(f.read())  # Output: All records or empty
            except FileNotFoundError:
                print("No records!")  # Output: "No records!"
                
        elif choice == "3":  # Search by ID
            emp_id = input("ID: ")
            try:
                with open("employees.txt", "r") as f:
                    found = any(print(line) or True for line in f if line.startswith(emp_id)) or print("Not found!")
            except FileNotFoundError:
                print("No records!")  # Output: "Not found!" or record
                
        elif choice == "4":  # Update by ID
            emp_id = input("ID: ")
            try:
                with open("employees.txt", "r") as f:
                    lines = f.readlines()
                with open("employees.txt", "w") as f:
                    found = False
                    for line in lines:
                        if line.startswith(emp_id):
                            f.write(f"{emp_id}, {input('Name: ')}, {input('Position: ')}, {input('Salary: ')}\n")
                            found = True
                        else:
                            f.write(line)
                    print("Updated!" if found else "Not found!")  # Output: "Updated!" or "Not found!"
            except FileNotFoundError:
                print("No records!")
                
        elif choice == "5":  # Delete by ID
            emp_id = input("ID: ")
            try:
                with open("employees.txt", "r") as f:
                    lines = f.readlines()
                with open("employees.txt", "w") as f:
                    found = any(f.write(line) or True for line in lines if not line.startswith(emp_id))
                    print("Deleted!" if found else "Not found!")  # Output: "Deleted!" or "Not found!"
            except FileNotFoundError:
                print("No records!")
                
        elif choice == "6":  # Exit
            print("Exiting...")  # Output: "Exiting..."
            break
            
        else:
            print("Invalid!")  # Output: "Invalid!"

# Word Frequency Counter
import string
from collections import Counter

def word_frequency_counter():
    # Read or create file
    try:
        with open("sample.txt", "r") as f:
            text = f.read()
    except FileNotFoundError:
        text = input("Enter text: ")
        with open("sample.txt", "w") as f:
            f.write(text)
    
    # Process text
    words = text.translate(str.maketrans("", "", string.punctuation)).lower().split()
    word_counts = Counter(words)
    
    # Get top N
    top_n = int(input("Top words count: ") or 5)
    top_words = word_counts.most_common(top_n)
    
    # Console output
    print(f"Total words: {len(words)}")  # Output: "Total words: 14"
    print("Top words:")
    for w, c in top_words:
        print(f"{w} - {c}")  # Output: e.g., "is - 3"
    
    # Write report
    with open("word_count_report.txt", "w") as f:
        f.write(f"Total: {len(words)}\n")
        for w, c in top_words:
            f.write(f"{w} - {c}\n")
    # Output in word_count_report.txt: "Total: 14\nis - 3\nfile - 3\n..."

# Run all
if __name__ == "__main__":
    print(div(6, 2))  # Output: 3
    print(div(6, 0))  # Output: "Denominator can't be zero"
    employee_manager()
    word_frequency_counter()
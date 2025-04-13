import os

class Employee:
    """A class representing an employee."""
    
    def __init__(self, employee_id, name, position, salary):
      
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)
    
    def __str__(self):
        """Return string representation of the employee."""
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    
    
    def __init__(self, filename="employees.txt"):
        """Initialize with the filename for storage."""
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass  # Create empty file if it doesn't exist
    
    def add_employee(self, employee):
        """Add a new employee to the file."""
        if self._employee_exists(employee.employee_id):
            raise ValueError(f"Employee ID {employee.employee_id} already exists")
        with open(self.filename, 'a') as f:
            f.write(str(employee) + '\n')
    
    def view_all_employees(self, sort_by=None):
        """Display all employee records, optionally sorted."""
        employees = self._read_employees()
        if not employees:
            print("No employee records found.")
            return
        
        if sort_by:
            if sort_by == 'name':
                employees.sort(key=lambda x: x.name)
            elif sort_by == 'salary':
                employees.sort(key=lambda x: x.salary)
        
        print("Employee Records:")
        for emp in employees:
            print(emp)
    
    def search_employee(self, employee_id):
        """Search for an employee by ID."""
        employees = self._read_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                print("Employee Found:")
                print(emp)
                return emp
        print(f"Employee with ID {employee_id} not found.")
        return None
    
    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Update an employee's information."""
        employees = self._read_employees()
        updated = False
        for emp in employees:
            if emp.employee_id == employee_id:
                if name:
                    emp.name = name
                if position:
                    emp.position = position
                if salary is not None:
                    emp.salary = float(salary)
                updated = True
                break
        if updated:
            self._write_employees(employees)
            print("Employee updated successfully!")
        else:
            print(f"Employee with ID {employee_id} not found.")
    
    def delete_employee(self, employee_id):
        """Delete an employee's record."""
        employees = self._read_employees()
        new_employees = [emp for emp in employees if emp.employee_id != employee_id]
        if len(new_employees) < len(employees):
            self._write_employees(new_employees)
            print("Employee deleted successfully!")
        else:
            print(f"Employee with ID {employee_id} not found.")
    
    def _employee_exists(self, employee_id):
        """Check if an employee ID already exists."""
        employees = self._read_employees()
        return any(emp.employee_id == employee_id for emp in employees)
    
    def _read_employees(self):
        """Read all employees from the file."""
        employees = []
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(', ')
                    if len(parts) == 4:
                        emp = Employee(parts[0], parts[1], parts[2], parts[3])
                        employees.append(emp)
        except FileNotFoundError:
            pass
        return employees
    
    def _write_employees(self, employees):
        """Write employees to the file."""
        with open(self.filename, 'w') as f:
            for emp in employees:
                f.write(str(emp) + '\n')
    
    def menu(self):
        """Display the menu and handle user input."""
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    employee_id = input("Enter Employee ID: ")
                    name = input("Enter Name: ")
                    position = input("Enter Position: ")
                    salary = input("Enter Salary: ")
                    try:
                        employee = Employee(employee_id, name, position, salary)
                        self.add_employee(employee)
                        print("Employee added successfully!")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                elif choice == 2:
                    sort_choice = input("Sort by (name/salary/none)? ").lower()
                    sort_by = sort_choice if sort_choice in ['name', 'salary'] else None
                    self.view_all_employees(sort_by)
                
                elif choice == 3:
                    employee_id = input("Enter Employee ID to search: ")
                    self.search_employee(employee_id)
                
                elif choice == 4:
                    employee_id = input("Enter Employee ID to update: ")
                    name = input("Enter new Name (or press Enter to skip): ")
                    position = input("Enter new Position (or press Enter to skip): ")
                    salary = input("Enter new Salary (or press Enter to skip): ")
                    self.update_employee(
                        employee_id,
                        name if name else None,
                        position if position else None,
                        float(salary) if salary else None
                    )
                
                elif choice == 5:
                    employee_id = input("Enter Employee ID to delete: ")
                    self.delete_employee(employee_id)
                
                elif choice == 6:
                    print("Goodbye!")
                    break
                
                else:
                    print("Invalid choice. Please try again.")
            
            except ValueError as e:
                print(f"Invalid input: {e}")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
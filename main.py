import csv
import random


class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Child:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class FileHandler:
    @staticmethod
    def getAllEmployees(file_path):
        employees = []
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for employee in reader:
                    employees.append(Employee(employee['Employee_Name'], employee['Employee_EmailID']))
        except (FileNotFoundError) as e:
            raise Exception(f"Error: {e}")
        
        file.close()
        return employees

    @staticmethod
    def readFromPrevFile(file_path):
        previous_assignments = {}
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Storing the key as employee_name and value as Secret_Child_Name
                    previous_assignments[row['Employee_Name']] = row['Secret_Child_Name']
        except (FileNotFoundError) as e:
            print(f"Error: {e}")
        
        file.close()
        return previous_assignments

    @staticmethod
    def writeAssignments(file_path, assignments):
        try:
            with open(file_path, 'w', newline='') as file:
                fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for emp_name, details in assignments.items():
                    writer.writerow({
                        'Employee_Name': emp_name,
                        'Employee_EmailID': details['emp_email'],
                        'Secret_Child_Name': details['name'],
                        'Secret_Child_EmailID': details['email']
                    })
        except Exception as e:
            raise Exception(f"Error: {e}")
        
        finally:
            file.close()


class SecretSanta:
    def __init__(self, employees, previous_assignments):
        self.employees = employees
        self.previous_assignments = previous_assignments

    def assignChildren(self):
        children = [Child(emp.name, emp.email) for emp in self.employees]
        random.shuffle(children)
        assignments = {}

        for emp in self.employees:
            #Checking if child name is in children and it is not equal to value of emp name and it was not assigned to the same employee in prev year
            valid_children = [child for child in children if child.name != emp.name and child.name not in self.previous_assignments.get(emp.name, [])]

            if not valid_children:
                raise Exception(f"No valid secret child available for {emp.name}")

            chosen_child = random.choice(valid_children)
            assignments[emp.name] = {
                'name': chosen_child.name,
                'email': chosen_child.email,
                'emp_email': emp.email
            }
            children.remove(chosen_child)

        return assignments


def main():
    employees_file = 'employee_secret_children_20.csv'
    previous_assignments_file = 'previous_assignments.csv'
    output_file = 'secret_santa_assignments.csv'

    employees = FileHandler.getAllEmployees(employees_file)
    previous_assignments = FileHandler.readFromPrevFile(previous_assignments_file)

    secret_santa = SecretSanta(employees, previous_assignments)
    try:
        assignments = secret_santa.assignChildren()

        FileHandler.writeAssignments(output_file, assignments)

        print("Secret Santa assignments have been generated successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()

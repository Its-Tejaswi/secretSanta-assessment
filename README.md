# Secret Santa Assignment

This project implements a Secret Santa assignment program in Python. The program assigns each employee a "secret child" to whom they will give a gift. The assignments ensure that an employee does not get themselves or the same person they had the previous year.

## Project Structure

- **Employee and Child Classes**: Represent the participants.
- **FileHandler**: Handles file reading and writing.
- **SecretSanta**: Manages the assignment logic.
- **Main Function**: Orchestrates the entire process.

## Data Generation

The employee data used in this project is randomly generated for demonstration purposes.

## Usage Instructions

1. Ensure you have the necessary CSV files:
   - `employee_secret_children_20.csv`: Contains employee names and emails.
   - `previous_assignments.csv`: Contains last year's assignments.

2. Run the program:

```bash
python3 main.py
```

3. The program will generate `secret_santa_assignments.csv` with the assignments.

## CSV File Formats

**employee_secret_children_20.csv**

| Employee_Name | Employee_EmailID |
|----------------|------------------|
| John Doe      | john@example.com |

**previous_assignments.csv**

| Employee_Name | Secret_Child_Name |
|----------------|-------------------|
| John Doe      | Jane Smith        |

**secret_santa_assignments.csv**

| Employee_Name | Employee_EmailID | Secret_Child_Name | Secret_Child_EmailID |
|----------------|------------------|--------------------|-----------------------|
| John Doe      | john@example.com | Jane Smith        | jane@example.com     |

## Error Handling

- Handles missing files gracefully.
- Ensures that no invalid assignments are made.

## Notes

- The data is randomly generated and does not correspond to real individuals.
- Ensure that the files are in the same directory as the script or update file paths accordingly.

Enjoy your Secret Santa event!

# Python Conditions and Loops Assessment

## Project Overview

This repository contains two separate beginner-friendly Python applications developed for the Conditions and Loops assessment. The programs demonstrate how Python can solve everyday business problems using conditional statements, loops, input validation, counters, and accumulators.

## Project Structure

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## Task 1: Student Scholarship Eligibility System

**File:** `student_scholarship_system.py`

This application evaluates a student's eligibility for a university scholarship. It collects the student's name, academic marks, attendance percentage, and monthly family income.

### Eligibility Rules

A student must meet all three requirements:

- Academic marks must be at least 80%.
- Attendance must be at least 85%.
- Monthly family income must be Rs. 50,000 or less.

If all requirements are met:

- Marks of 90% or above: Full Scholarship.
- Marks from 80% to below 90%: Partial Scholarship.

If one or more requirements are not met, the application displays each reason for ineligibility.

### Python Concepts Used

- `input()` and `print()` for input and output.
- Variables and meaningful variable names.
- `if`, `elif`, and `else` conditional statements.
- Comparison and logical conditions.
- `while` loops for input validation.
- A `for` loop to display multiple ineligibility reasons.
- Lists to store reasons.
- Functions to organize reusable validation logic.
- Exception handling with `try` and `except`.

### Sample Execution

```text
Enter student name: Ali
Enter academic marks percentage: 92
Enter attendance percentage: 90
Enter monthly family income (Rs.): 40000

SCHOLARSHIP EVALUATION REPORT
Student Name              : Ali
Academic Marks            : 92.00%
Attendance                : 90.00%
Monthly Family Income     : Rs. 40,000.00
Eligibility Status        : Eligible
Scholarship Decision      : Full Scholarship

Congratulations! You have met all scholarship requirements.
```

Another test: if marks are 75%, attendance is 80%, and income is Rs. 60,000, the student is declared **Not Eligible**, and all three reasons are displayed.

## Task 2: Smart Pharmacy Inventory & Sales Management System

**File:** `pharmacy_inventory_system.py`

This application processes medicine sales for a pharmacy. It asks how many different medicines need to be processed and then collects the name, available stock, price per unit, and quantity sold for each medicine.

The application checks stock availability before completing a sale. Successful sales update the total revenue and remaining stock. If the requested quantity is greater than the available stock, the sale is rejected and stock remains unchanged. A low-stock warning is displayed whenever the remaining stock is below 10 units.

At the end, the application displays the total number of medicines processed, total revenue, and number of medicines requiring restocking.

### Python Concepts Used

- `input()` and `print()` for input and output.
- Variables and arithmetic operators.
- `for` loop and `range()` to process medicines.
- `if` and `else` statements inside a loop.
- Input validation using `while` loops.
- Counters to count medicines requiring restocking.
- An accumulator (`total_revenue`) to calculate total sales.
- Functions and exception handling.

### Sample Execution

```text
How many different medicines do you want to process? 2

--- Medicine 1 of 2 ---
Enter medicine name: Panadol
Enter available stock (units): 50
Enter price per unit (Rs.): 20
Enter quantity to sell (units): 45

Sale processed successfully.
Medicine Name       : Panadol
Quantity Sold        : 45
Sales Amount         : Rs. 900.00
Remaining Stock      : 5 units
LOW-STOCK WARNING: This medicine needs restocking.

--- Medicine 2 of 2 ---
Enter medicine name: Brufen
Enter available stock (units): 30
Enter price per unit (Rs.): 15
Enter quantity to sell (units): 10

Sale processed successfully.
Medicine Name       : Brufen
Quantity Sold        : 10
Sales Amount         : Rs. 150.00
Remaining Stock      : 20 units
Stock level is sufficient.

DAILY PHARMACY REPORT
Total Medicines Processed : 2
Total Pharmacy Revenue    : Rs. 1,050.00
Medicines Requiring Restock: 1
```

## Requirements

- Python 3.8 or later.
- Any Python editor, such as Visual Studio Code, PyCharm, or IDLE.
- No external Python libraries are required.

## How to Run the Programs

1. Download or clone this repository.
2. Open the project folder in your code editor or terminal.
3. Run either application separately.

### Run Task 1

```bash
python student_scholarship_system.py
```

### Run Task 2

```bash
python pharmacy_inventory_system.py
```

On some systems, use `python3` instead of `python`.

## Input Validation and Testing

Both programs validate their inputs and ask again when invalid data is entered.

Suggested test scenarios:

### Scholarship System

| Test | Marks | Attendance | Monthly Income | Expected Result |
|---|---:|---:|---:|---|
| 1 | 95% | 90% | Rs. 40,000 | Full Scholarship |
| 2 | 85% | 88% | Rs. 45,000 | Partial Scholarship |
| 3 | 75% | 90% | Rs. 40,000 | Not Eligible: marks |
| 4 | 90% | 80% | Rs. 40,000 | Not Eligible: attendance |
| 5 | 90% | 90% | Rs. 60,000 | Not Eligible: income |
| 6 | 75% | 80% | Rs. 60,000 | All three reasons displayed |

### Pharmacy System

| Test | Available Stock | Quantity Sold | Expected Result |
|---|---:|---:|---|
| 1 | 50 | 20 | Sale successful; 30 units remain |
| 2 | 15 | 15 | Sale successful; low-stock warning |
| 3 | 5 | 8 | Sale rejected; stock remains 5 |
| 4 | 20 | 0 | Zero-quantity sale; stock remains 20 |

## Author

Student Name: ____________________

Course: ____________________

Assessment: Python Conditions and Loops

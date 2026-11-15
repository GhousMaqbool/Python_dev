# Python Conditions and Loops Assessment

## Project Overview

This repository contains two independent Python applications developed as part of the Python Programming Assessment. The project demonstrates the practical implementation of conditional statements, loops, input validation, arithmetic operations, counters, and accumulators.

The applications are designed to solve two real-world business problems:

1. **Student Scholarship Eligibility System** – Evaluates students' eligibility for university scholarships based on academic marks, attendance percentage, and monthly family income.
2. **Smart Pharmacy Inventory & Sales Management System** – Manages medicine stock, processes sales, calculates revenue, and identifies medicines that require restocking.

Both applications are developed using Python and follow structured programming practices.

---

## Project Structure

```text
python-conditions-loops-assessment/
│
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## Task 1: Student Scholarship Eligibility System

### Description

The Student Scholarship Eligibility System is a Python-based application that determines whether a student qualifies for a university scholarship.

The program collects the following information:

- Student name
- Academic marks (percentage)
- Attendance percentage
- Monthly family income (PKR)

### Scholarship Eligibility Criteria

| Requirement | Eligibility Condition |
|---|---|
| Academic Marks | 80% or above |
| Attendance | 85% or above |
| Monthly Family Income | Rs. 50,000 or less |

### Scholarship Categories

- **Full Scholarship:** Students achieving 90% or above, provided all eligibility conditions are satisfied.
- **Partial Scholarship:** Students achieving 80% to 89%, provided all eligibility conditions are satisfied.
- **Not Eligible:** Students who fail to meet one or more eligibility requirements.

The application also identifies the specific reason or reasons for ineligibility and generates a complete scholarship evaluation report.

### Python Concepts Used

- `input()` and `print()` functions
- Variables and data types
- Type conversion using `float()`
- Conditional statements (`if`, `elif`, `else`)
- Logical operators (`and`)
- Input validation
- Arithmetic and comparison operators
- Formatted output using f-strings

---

## Task 2: Smart Pharmacy Inventory & Sales Management System

### Description

The Smart Pharmacy Inventory & Sales Management System is a Python-based application designed to manage medicine inventory and calculate daily sales revenue.

The application first asks the user how many different medicines need to be processed. It then uses a `for` loop to process each medicine individually.

For every medicine, the program collects:

- Medicine name
- Available stock
- Price per unit (PKR)
- Quantity sold

### Main Features

1. Processes multiple medicines using a `for` loop.
2. Validates medicine details and numerical inputs.
3. Checks whether the requested sales quantity is available in stock.
4. Calculates the total sales amount for successful sales.
5. Updates and displays the remaining stock.
6. Displays a low-stock warning when remaining stock is below 10 units.
7. Maintains total pharmacy revenue using an accumulator.
8. Counts medicines requiring restocking.
9. Generates a final pharmacy sales report.

### Python Concepts Used

- Variables and data types
- `input()` and `print()` functions
- `for` loop and `range()`
- Conditional statements (`if`, `else`)
- Nested conditional statements
- Input validation
- Type conversion
- Arithmetic operators
- Counters and accumulators
- Formatted output using f-strings

---

## Software Requirements

Before running these applications, ensure that you have:

- Python 3.8 or later
- A code editor such as Visual Studio Code (VS Code)
- Git (for cloning the repository)
- A GitHub account

No external Python libraries are required. Both applications use Python's built-in functionality.

## Installation and Setup Instructions

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify the installation by opening Command Prompt or Terminal and executing:

```bash
python --version
```

### Step 2: Clone the GitHub Repository

Open your terminal and execute:

```bash
git clone https://github.com/YOUR-USERNAME/python-conditions-loops-assessment.git
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### Step 3: Navigate to the Project Directory

```bash
cd python-conditions-loops-assessment
```

### Step 4: Run the Scholarship Application

```bash
python student_scholarship_system.py
```

### Step 5: Run the Pharmacy Application

```bash
python pharmacy_inventory_system.py
```

**Note:** If the `python` command does not work on Windows, try using `py` instead.

---

## Sample Execution and Expected Output

The following examples demonstrate the expected behavior of both applications.

### Task 1: Scholarship System

**Sample Input**

```text
Enter Student Name: Ali
Enter Academic Marks: 92
Enter Attendance Percentage: 90
Enter Monthly Family Income: 40000
```

**Expected Output**

```text
========================================
       STUDENT SCHOLARSHIP REPORT
========================================

Student Name: Ali
Academic Marks: 92%
Attendance: 90%
Monthly Family Income: Rs. 40000

Scholarship Status: ELIGIBLE
Scholarship Category: FULL SCHOLARSHIP

All eligibility requirements have been satisfied.

========================================
```

**Additional Testing Scenarios**

| Test Case | Marks | Attendance | Income | Expected Result |
|---|---:|---:|---:|---|
| 1 | 95 | 90 | 30000 | Full Scholarship |
| 2 | 85 | 88 | 45000 | Partial Scholarship |
| 3 | 75 | 90 | 30000 | Not Eligible |
| 4 | 90 | 80 | 30000 | Not Eligible |
| 5 | 90 | 90 | 60000 | Not Eligible |
| 6 | Invalid text | 90 | 30000 | Input validation |

### Task 2: Pharmacy Inventory System

**Sample Input**

```text
Enter number of medicines: 2

Medicine 1:
Enter Medicine Name: Paracetamol
Enter Available Stock: 50
Enter Price Per Unit: 20
Enter Quantity Sold: 45

Medicine 2:
Enter Medicine Name: Amoxicillin
Enter Available Stock: 30
Enter Price Per Unit: 50
Enter Quantity Sold: 10
```

**Expected Output**

```text
========================================
       PHARMACY SALES REPORT
========================================

Medicine: Paracetamol
Quantity Sold: 45
Total Sales: Rs. 900
Remaining Stock: 5
WARNING: Low stock! Restocking required.

Medicine: Amoxicillin
Quantity Sold: 10
Total Sales: Rs. 500
Remaining Stock: 20

========================================
          FINAL SUMMARY
========================================

Total Medicines Processed: 2
Total Pharmacy Revenue: Rs. 1400
Medicines Requiring Restocking: 1

========================================
```

**Additional Testing Scenarios**

| Test Case | Available Stock | Quantity Sold | Expected Result |
|---|---:|---:|---|
| 1 | 50 | 20 | Sale successful |
| 2 | 20 | 20 | Sale successful, zero stock |
| 3 | 15 | 10 | Low-stock warning |
| 4 | 10 | 15 | Insufficient stock |
| 5 | 40 | 0 | Invalid sales quantity |
| 6 | Invalid text | 10 | Input validation |

*Note: These are sample test scenarios and expected results. Actual output formatting may vary slightly depending on the implementation.*

---

## Input Validation and Error Handling

Both applications include input validation to improve reliability and prevent invalid data from affecting program execution.

Examples of validation include:

- Rejecting empty student and medicine names.
- Accepting only numerical values for marks, attendance, income, stock, prices, and quantities.
- Ensuring academic marks and attendance remain between 0 and 100.
- Preventing negative family income, stock, prices, and sales quantities.
- Ensuring the number of medicines is a valid positive integer.
- Preventing pharmacy sales quantities from exceeding available stock.

Invalid entries should display an appropriate error message and request valid input again.

## Testing Strategy

Both applications should be tested with multiple input scenarios to verify their functionality.

Testing includes:

1. Valid inputs that satisfy all requirements.
2. Invalid text inputs in numerical fields.
3. Boundary values for scholarship eligibility.
4. Students who fail individual eligibility conditions.
5. Successful pharmacy sales.
6. Insufficient stock situations.
7. Low-stock situations.
8. Multiple medicines to verify revenue calculations and restocking counters.

The expected results are documented in the sample testing tables above.

## Learning Outcomes

Through this assessment, I developed practical understanding of:

- Applying conditional statements to real-world problems.
- Using loops to process multiple records.
- Validating user input and handling incorrect values.
- Performing calculations using arithmetic operators.
- Maintaining totals using accumulators.
- Tracking quantities using counters.
- Organizing Python programs using meaningful variable names.
- Documenting and managing projects using Git and GitHub.

## Author

**Project:** Python Conditions and Loops Assessment

**Programming Language:** Python

**Repository:** `python-conditions-loops-assessment`

**Purpose:** Academic Programming Assessment

---

## Conclusion

This project demonstrates the practical application of Python conditional statements and loop structures through two independent applications.

The Student Scholarship Eligibility System applies decision-making logic to evaluate scholarship applications, while the Smart Pharmacy Inventory & Sales Management System demonstrates inventory processing, sales calculations, and stock monitoring.

Both programs aim to provide accurate results, validate user inputs, and demonstrate fundamental Python programming concepts through practical business scenarios.

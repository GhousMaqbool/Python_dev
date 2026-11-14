"""
Student Scholarship Eligibility System
Topic: Conditional Statements (if, elif, else)

This program checks a student's scholarship eligibility using academic
marks, attendance percentage, and monthly family income.
"""


def get_non_empty_name(prompt):
    """Ask until the user enters a name containing at least one character."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Error: Name cannot be empty. Please try again.")


def get_percentage(prompt):
    """Read and validate a percentage between 0 and 100."""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Error: Enter a value between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_non_negative_income(prompt):
    """Read and validate a non-negative monthly family income."""
    while True:
        try:
            income = float(input(prompt))
            if income >= 0:
                return income
            print("Error: Income cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid amount.")


def main():
    print("=" * 55)
    print("       STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
    print("=" * 55)

    # Collect and validate student information.
    student_name = get_non_empty_name("Enter student name: ")
    academic_marks = get_percentage("Enter academic marks percentage: ")
    attendance = get_percentage("Enter attendance percentage: ")
    monthly_income = get_non_negative_income(
        "Enter monthly family income (Rs.): "
    )

    # Check every eligibility condition and record all reasons for rejection.
    ineligibility_reasons = []

    if academic_marks < 80:
        ineligibility_reasons.append(
            "Academic marks are below the required 80%."
        )

    if attendance < 85:
        ineligibility_reasons.append(
            "Attendance is below the required 85%."
        )

    if monthly_income > 50000:
        ineligibility_reasons.append(
            "Monthly family income is greater than Rs. 50,000."
        )

    # Prepare the scholarship decision.
    if len(ineligibility_reasons) == 0:
        eligibility_status = "Eligible"
        if academic_marks >= 90:
            scholarship_type = "Full Scholarship"
        elif academic_marks >= 80:
            scholarship_type = "Partial Scholarship"
        else:
            # This branch is a safety fallback; eligible marks are at least 80.
            scholarship_type = "No Scholarship"
    else:
        eligibility_status = "Not Eligible"
        scholarship_type = "No Scholarship"

    # Display the complete evaluation report.
    print("\n" + "=" * 55)
    print("             SCHOLARSHIP EVALUATION REPORT")
    print("=" * 55)
    print(f"Student Name              : {student_name}")
    print(f"Academic Marks            : {academic_marks:.2f}%")
    print(f"Attendance                : {attendance:.2f}%")
    print(f"Monthly Family Income     : Rs. {monthly_income:,.2f}")
    print("-" * 55)
    print(f"Eligibility Status        : {eligibility_status}")
    print(f"Scholarship Decision      : {scholarship_type}")

    if ineligibility_reasons:
        print("\nReason(s) for Ineligibility:")
        for reason_number, reason in enumerate(ineligibility_reasons, start=1):
            print(f"{reason_number}. {reason}")
    else:
        print("\nCongratulations! You have met all scholarship requirements.")

    print("=" * 55)


if __name__ == "__main__":
    main()

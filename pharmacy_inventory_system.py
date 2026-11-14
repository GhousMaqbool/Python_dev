"""
Smart Pharmacy Inventory & Sales Management System
Topic: for loop, range(), conditions, counters, and accumulators

This program processes medicine sales, updates stock, calculates revenue,
and identifies medicines that need restocking.
"""


def get_positive_integer(prompt):
    """Read an integer greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Error: Enter a whole number greater than zero.")
        except ValueError:
            print("Error: Please enter a valid whole number.")


def get_non_negative_integer(prompt):
    """Read an integer that is zero or greater."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Error: Value cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid whole number.")


def get_positive_price(prompt):
    """Read a medicine price greater than zero."""
    while True:
        try:
            price = float(input(prompt))
            if price > 0:
                return price
            print("Error: Price must be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid price.")


def get_medicine_name(prompt):
    """Read a medicine name that is not empty."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Error: Medicine name cannot be empty.")


def main():
    print("=" * 60)
    print("       SMART PHARMACY INVENTORY & SALES MANAGEMENT")
    print("=" * 60)

    # Ask how many different medicines will be processed.
    total_medicines = get_positive_integer(
        "How many different medicines do you want to process? "
    )

    # Accumulator for total revenue and counter for restocking.
    total_revenue = 0.0
    restock_count = 0

    # Process each medicine using a for loop and range().
    for medicine_number in range(1, total_medicines + 1):
        print(f"\n--- Medicine {medicine_number} of {total_medicines} ---")

        medicine_name = get_medicine_name("Enter medicine name: ")
        available_stock = get_non_negative_integer(
            "Enter available stock (units): "
        )
        price_per_unit = get_positive_price("Enter price per unit (Rs.): ")
        quantity_sold = get_non_negative_integer(
            "Enter quantity to sell (units): "
        )

        # Check stock before completing the sale.
        if quantity_sold <= available_stock:
            sales_amount = quantity_sold * price_per_unit
            remaining_stock = available_stock - quantity_sold

            # Add this medicine's sales to the pharmacy's total revenue.
            total_revenue += sales_amount

            print("\nSale processed successfully.")
            print(f"Medicine Name       : {medicine_name}")
            print(f"Quantity Sold        : {quantity_sold}")
            print(f"Sales Amount         : Rs. {sales_amount:,.2f}")
            print(f"Remaining Stock      : {remaining_stock} units")

        else:
            # Do not sell or change stock when requested quantity is unavailable.
            sales_amount = 0.0
            remaining_stock = available_stock

            print("\nSale could not be processed.")
            print(
                f"Insufficient stock: only {available_stock} unit(s) "
                f"of {medicine_name} are available."
            )
            print("No revenue was added and stock remains unchanged.")
            print(f"Remaining Stock      : {remaining_stock} units")

        # Check the final stock level, including when a sale was not possible.
        if remaining_stock < 10:
            print("LOW-STOCK WARNING: This medicine needs restocking.")
            restock_count += 1
        else:
            print("Stock level is sufficient.")

    # Display the final pharmacy report.
    print("\n" + "=" * 60)
    print("                  DAILY PHARMACY REPORT")
    print("=" * 60)
    print(f"Total Medicines Processed : {total_medicines}")
    print(f"Total Pharmacy Revenue    : Rs. {total_revenue:,.2f}")
    print(f"Medicines Requiring Restock: {restock_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()

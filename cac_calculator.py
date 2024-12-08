# cac_calculator.py

import argparse

def calculate_cac(total_marketing_expenses, total_sales_expenses, new_customers):
    if new_customers == 0:
        return None  # Avoid division by zero
    return (total_marketing_expenses + total_sales_expenses) / new_customers

def main():
    print("Starting Customer Acquisition Cost (CAC) Calculator...")
    parser = argparse.ArgumentParser(description="Calculate Customer Acquisition Cost (CAC).")
    parser.add_argument('--total_marketing_expenses', type=float, default=1000.0, help='Total marketing expenses')
    parser.add_argument('--total_sales_expenses', type=float, default=500.0, help='Total sales expenses')
    parser.add_argument('--new_customers', type=float, default=10, help='Number of new customers acquired')

    args = parser.parse_args()
    cac = calculate_cac(args.total_marketing_expenses, args.total_sales_expenses, args.new_customers)

    if cac is None:
        print("Error: Number of new customers is zero. Cannot calculate CAC.")
    else:
        print(f"\nCAC Calculation Result:")
        print(f"CAC: ${cac:.2f}")

if __name__ == '__main__':
    main()

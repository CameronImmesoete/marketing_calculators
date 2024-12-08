# churn_rate_calculator.py

import argparse

def calculate_churn_rate(customers_start, customers_lost):
    if customers_start == 0:
        return None
    return (customers_lost / customers_start) * 100

def main():
    print("Starting Churn Rate Calculator...")
    parser = argparse.ArgumentParser(description="Calculate Churn Rate.")
    parser.add_argument('--customers_start', type=int, default=100, help='Number of customers at start of period')
    parser.add_argument('--customers_lost', type=int, default=10, help='Number of customers lost during the period')

    args = parser.parse_args()
    churn_rate = calculate_churn_rate(args.customers_start, args.customers_lost)

    if churn_rate is None:
        print("Error: Number of customers at the start cannot be zero.")
    else:
        print(f"\nChurn Rate Calculation Result:")
        print(f"Churn Rate: {churn_rate:.2f}%")

if __name__ == '__main__':
    main()

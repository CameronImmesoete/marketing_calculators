# romi_calculator.py

import argparse

def calculate_romi(revenue, marketing_expenses):
    if marketing_expenses == 0:
        return None
    return ((revenue - marketing_expenses) / marketing_expenses) * 100

def main():
    print("Starting Return on Marketing Investment (ROMI) Calculator...")
    parser = argparse.ArgumentParser(description="Calculate Return on Marketing Investment (ROMI).")
    parser.add_argument('--revenue', type=float, default=5000.0, help='Revenue generated from the marketing campaign')
    parser.add_argument('--marketing_expenses', type=float, default=1000.0, help='Total marketing expenses')

    args = parser.parse_args()
    romi = calculate_romi(args.revenue, args.marketing_expenses)

    if romi is None:
        print("Error: Marketing expenses cannot be zero.")
    else:
        print(f"\nROMI Calculation Result:")
        print(f"ROMI: {romi:.2f}%")

if __name__ == '__main__':
    main()

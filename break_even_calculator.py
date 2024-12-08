# break_even_calculator.py

import argparse

def calculate_break_even_point(fixed_costs, variable_cost_per_unit, price_per_unit):
    contribution_margin = price_per_unit - variable_cost_per_unit
    if contribution_margin <= 0:
        return None
    return fixed_costs / contribution_margin

def main():
    print("Starting Break-Even Analysis Calculator...")
    parser = argparse.ArgumentParser(description="Calculate Break-Even Point (in units).")
    parser.add_argument('--fixed_costs', type=float, default=1000.0, help='Total fixed costs')
    parser.add_argument('--variable_cost_per_unit', type=float, default=10.0, help='Variable cost per unit')
    parser.add_argument('--price_per_unit', type=float, default=50.0, help='Price per unit')

    args = parser.parse_args()
    be_point = calculate_break_even_point(args.fixed_costs, args.variable_cost_per_unit, args.price_per_unit)

    if be_point is None:
        print("Error: Price per unit must be greater than variable cost per unit to break even.")
    else:
        print(f"\nBreak-Even Analysis Result:")
        print(f"Break-Even Point: {be_point:.2f} units")

if __name__ == '__main__':
    main()

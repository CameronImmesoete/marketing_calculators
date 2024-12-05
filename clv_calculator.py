# clv_calculator.py

import numpy as np
import argparse


def calculate_clv(
    margin=100,
    retention_rate=0.8,
    interest_rate=0.1,
    periods=5,
    time_unit='years',
    margins_over_time=None,
    retention_rates_over_time=None,
    interest_rates_over_time=None,
):
    """
    Calculate CLV over a fixed time horizon and into perpetuity.

    Parameters:
        margin (float): Default margin per customer.
        retention_rate (float): Default retention rate per period.
        interest_rate (float): Default interest rate per period.
        periods (int): Number of periods to calculate CLV for.
        time_unit (str): Unit of time (e.g., 'years', 'months').
        margins_over_time (list): Optional list of margins for each period.
        retention_rates_over_time (list): Optional list of retention rates for each period.
        interest_rates_over_time (list): Optional list of interest rates for each period.

    Returns:
        dict: Dictionary containing CLV per period and CLV in perpetuity.
    """

    # Initialize lists to store values per period
    clv_per_period = []
    cumulative_retention = 1.0

    # Use provided lists or default values
    margins = margins_over_time if margins_over_time else [margin] * periods
    retention_rates = retention_rates_over_time if retention_rates_over_time else [retention_rate] * periods
    interest_rates = interest_rates_over_time if interest_rates_over_time else [interest_rate] * periods

    for t in range(periods):
        # Adjust cumulative retention
        if t > 0:
            cumulative_retention *= retention_rates[t - 1]

        # Present value factor
        discount_factor = (1 + interest_rates[t]) ** (t + 1)

        # CLV calculation for the period
        period_clv = (margins[t] * cumulative_retention) / discount_factor
        clv_per_period.append(period_clv)

    # Total CLV over periods
    total_clv = sum(clv_per_period)

    # CLV in perpetuity using the formula:
    # CLV = (Margin) / (1 + Discount Rate - Retention Rate)
    clv_in_perpetuity = (margins[-1]) / (1 + interest_rates[-1] - retention_rates[-1])

    # Prepare results
    results = {
        'CLV per Period': clv_per_period,
        'Total CLV over Periods': total_clv,
        'CLV in Perpetuity': clv_in_perpetuity,
        'Time Unit': time_unit,
    }

    return results


def main():
    """
    Main function to run the CLV calculator.
    """
    print("Starting Customer Lifetime Value (CLV) Calculator...")

    # Default inputs
    margin = 100
    retention_rate = 0.8
    interest_rate = 0.1
    periods = 5
    time_unit = 'years'

    # Collect user inputs
    parser = argparse.ArgumentParser(description="Customer Lifetime Value (CLV) Calculator")

    parser.add_argument('--margin', type=float, default=margin, help='Margin per customer')
    parser.add_argument('--retention_rate', type=float, default=retention_rate, help='Retention rate as a decimal')
    parser.add_argument('--interest_rate', type=float, default=interest_rate, help='Interest rate as a decimal')
    parser.add_argument('--periods', type=int, default=periods, help='Number of periods (optional)')
    parser.add_argument('--time_unit', type=str, default=time_unit, help='Unit of time (e.g., years, months)')
    parser.add_argument('--margins_over_time', type=float, nargs='*', help='List of margins for each period')
    parser.add_argument('--retention_rates_over_time', type=float, nargs='*', help='List of retention rates for each period')
    parser.add_argument('--interest_rates_over_time', type=float, nargs='*', help='List of interest rates for each period')

    args = parser.parse_args()

    margin = args.margin
    retention_rate = args.retention_rate
    interest_rate = args.interest_rate
    periods = args.periods
    time_unit = args.time_unit
    margins_over_time = args.margins_over_time if args.margins_over_time else [margin] * periods
    retention_rates_over_time = args.retention_rates_over_time if args.retention_rates_over_time else [retention_rate] * periods
    interest_rates_over_time = args.interest_rates_over_time if args.interest_rates_over_time else [interest_rate] * periods

    # Calculate CLV
    results = calculate_clv(
        margin=margin,
        retention_rate=retention_rate,
        interest_rate=interest_rate,
        periods=periods,
        time_unit=time_unit,
        margins_over_time=margins_over_time,
        retention_rates_over_time=retention_rates_over_time,
        interest_rates_over_time=interest_rates_over_time,
    )

    # Output results
    print("\nCLV Calculation Results:")
    for i, clv in enumerate(results['CLV per Period']):
        if periods <= 10 or i >= periods - 1:
            print(f"CLV {results['Time Unit'].capitalize()} {i + 1}: ${clv:.2f}")

    print(f"\nTotal CLV over {periods} {results['Time Unit']}: ${results['Total CLV over Periods']:.2f}")
    print(f"CLV in Perpetuity: ${results['CLV in Perpetuity']:.2f}")


if __name__ == '__main__':
    main()

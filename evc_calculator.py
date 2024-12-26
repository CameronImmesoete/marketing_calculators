import argparse

# evc_calculator.py

def calculate_evc(reference_value, positive_diff, negative_diff):
    """
    Calculate Economic Value to the Customer (EVC).

    Parameters:
        reference_value (float): Price of the next best alternative.
        positive_diff (float): Monetary value of the positive differentiation.
        negative_diff (float): Monetary value of the negative differentiation.

    Returns:
        float: Calculated EVC.
    """
    evc = reference_value + positive_diff + negative_diff
    return evc


def main():
    """
    Main function to run the EVC calculator.
    """
    print("Starting Economic Value to the Customer (EVC) Calculator...")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Calculate Economic Value to the Customer (EVC).')
    parser.add_argument('--reference_value', type=float, default=100, help='Price of the next best alternative')
    parser.add_argument('--positive_diff', type=float, default=25, help='Monetary value of the positive differentiation')
    parser.add_argument('--negative_diff', type=float, default=-15, help='Monetary value of the negative differentiation (expects negative value)')
    args = parser.parse_args()

    reference_value = args.reference_value
    positive_diff = args.positive_diff
    negative_diff = args.negative_diff

    # Calculate EVC
    evc = calculate_evc(reference_value, positive_diff, negative_diff)

    # Output results
    print(f"\nEVC Calculation Result:")
    print(f"EVC: ${evc:.2f}")


if __name__ == '__main__':
    main()

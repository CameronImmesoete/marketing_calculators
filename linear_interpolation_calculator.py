import argparse

# linear_interpolation_calculator.py

def linear_interpolate(x1, x2, y1, y2, y3):
    """
    Perform linear interpolation to find X corresponding to a given Y.

    Parameters:
        x1 (float): First X value.
        x2 (float): Second X value.
        y1 (float): First Y value corresponding to x1.
        y2 (float): Second Y value corresponding to x2.
        y3 (float): Y value for which to find the corresponding X.

    Returns:
        float: Interpolated X value corresponding to y3.
    """
    # Linear interpolation formula
    x3 = x1 + ((y3 - y1) * (x2 - x1)) / (y2 - y1)
    return x3


def main():
    """
    Main function to run the Linear Interpolation calculator.
    """
    print("Starting Linear Interpolation Calculator...")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Linear Interpolation Calculator")
    parser.add_argument("x1", type=float, help="First X value")
    parser.add_argument("x2", type=float, help="Second X value")
    parser.add_argument("y1", type=float, help="Y value corresponding to X1")
    parser.add_argument("y2", type=float, help="Y value corresponding to X2")
    parser.add_argument("y3", type=float, help="Y value for which to find corresponding X")
    args = parser.parse_args()

    x1 = args.x1
    x2 = args.x2
    y1 = args.y1
    y2 = args.y2
    y3 = args.y3

    # Perform interpolation
    x3 = linear_interpolate(x1, x2, y1, y2, y3)

    # Output result
    print(f"\nLinear Interpolation Result:")
    print(f"The X value corresponding to Y = {y3} is X = {x3:.2f}")


if __name__ == '__main__':
    main()

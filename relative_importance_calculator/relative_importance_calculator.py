# relative_importance_calculator.py

import pandas as pd
import os


def calculate_relative_importance(data):
    """
    Calculate relative importance based on max and min values of features.

    Parameters:
        data (pd.DataFrame): DataFrame containing 'Feature', 'Max', and 'Min' columns.

    Returns:
        pd.DataFrame: DataFrame with calculated differences and relative importances.
    """
    data['Difference'] = data['Max'] - data['Min']
    total_difference = data['Difference'].sum()
    data['Relative Importance (%)'] = (data['Difference'] / total_difference) * 100
    return data


def main():
    """
    Main function to run the Relative Importance calculator.
    """
    print("Starting Relative Importance Calculator...")

    # Define file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    importance_file = os.path.join(script_dir, 'RelativeImportance.xlsx')
    if not os.path.exists(importance_file):
        importance_file = os.path.join(script_dir, 'RelativeImportance.csv')
        if not os.path.exists(importance_file):
            print("Error: Neither 'RelativeImportance.xlsx' nor 'RelativeImportance.csv' found.")
            return

    # Load data
    try:
        if importance_file.endswith('.xlsx'):
            data = pd.read_excel(importance_file)
        elif importance_file.endswith('.csv'):
            data = pd.read_csv(importance_file)
        else:
            print(f"Error: Unsupported file format for {importance_file}")
            return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Validate data
    required_columns = {'Feature', 'Max', 'Min'}
    if not required_columns.issubset(data.columns):
        print(f"Error: Input file must contain columns: {required_columns}")
        return

    # Calculate relative importance
    result = calculate_relative_importance(data)

    # Save results
    result_file = 'RelativeImportanceResults.csv'
    result.to_csv(result_file, index=False)
    print(f"\nRelative importance calculations saved to {result_file}.")

    # Output results
    print("\nRelative Importance Results:")
    print(result)


if __name__ == '__main__':
    main()

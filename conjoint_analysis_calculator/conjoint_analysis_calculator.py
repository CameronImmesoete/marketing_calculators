import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import itertools
import os
import matplotlib.pyplot as plt
import openpyxl


def load_attributes(attributes_file):
    """Load attributes from Excel or CSV file and validate."""
    try:
        if attributes_file.endswith('.xlsx'):
            attributes_df = pd.read_excel(attributes_file)
        elif attributes_file.endswith('.csv'):
            attributes_df = pd.read_csv(attributes_file)
        else:
            print(f"Error: Unsupported file format for {attributes_file}")
            return None
    except FileNotFoundError:
        print(f"Error: {attributes_file} not found.")
        return None

    # Check for missing attribute names or levels
    if attributes_df['Attribute Name'].isnull().any():
        print("Error: One or more attribute names are missing.")
        return None

    if attributes_df.drop('Attribute Name', axis=1).isnull().any().any():
        print("Error: One or more attribute levels are missing.")
        return None

    return attributes_df


def generate_profiles(attributes_df):
    """Generate all possible profiles from the attributes."""
    attributes = {}
    for _, row in attributes_df.iterrows():
        attribute_name = row['Attribute Name']
        levels = row.dropna()[1:].tolist()
        attributes[attribute_name] = levels

    # Create all possible combinations of attributes
    levels_list = list(attributes.values())
    profiles = list(itertools.product(*levels_list))
    profiles_df = pd.DataFrame(profiles, columns=attributes.keys())

    # Assign profile numbers
    profiles_df['Profile Number'] = range(1, len(profiles_df) + 1)
    profiles_df = profiles_df[['Profile Number'] + list(attributes.keys())]

    return profiles_df, attributes


def save_profiles(profiles_df, profiles_file):
    """Save generated profiles to a CSV file."""
    profiles_df.to_csv(profiles_file, index=False)
    print(f"Generated product profiles saved to {profiles_file}.")


def load_ratings(ratings_file):
    """Load respondent ratings from Excel or CSV file and validate."""
    try:
        if ratings_file.endswith('.xlsx'):
            ratings_df = pd.read_excel(ratings_file)
        elif ratings_file.endswith('.csv'):
            ratings_df = pd.read_csv(ratings_file)
        else:
            print(f"Error: Unsupported file format for {ratings_file}")
            return None
    except FileNotFoundError:
        print(f"Error: {ratings_file} not found.")
        return None

    # Check for missing ratings
    if ratings_df.isnull().any().any():
        print("Error: Missing ratings detected. Please ensure all profiles are rated.")
        return None

    return ratings_df


def prepare_regression_data(profiles_df, ratings_df):
    """Prepare data for regression analysis."""
    # Include all dummy variables without dropping any levels
    dummy_vars = pd.get_dummies(profiles_df.drop(['Profile Number'], axis=1), drop_first=False)

    # Ensure the number of profiles matches
    num_profiles = dummy_vars.shape[0]
    expected_num_profiles = ratings_df.shape[1] - 1  # Subtract Respondent ID column
    if num_profiles != expected_num_profiles:
        print("Error: The number of profiles in Ratings file does not match the generated profiles.")
        return None, None, None

    # Combine data from all respondents
    respondent_ids = ratings_df['Respondent ID'].values
    ratings = ratings_df.drop('Respondent ID', axis=1).values

    # Repeat the design matrix for each respondent
    X = np.tile(dummy_vars.values, (len(respondent_ids), 1))
    y = ratings.flatten()

    return X, y, dummy_vars


def perform_regression(X, y, dummy_vars):
    """Perform linear regression on the combined data."""
    # Set fit_intercept=False to handle multicollinearity
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)

    coefficients = model.coef_
    intercept = model.intercept_

    # Create a Series for part-worth utilities
    part_worths = pd.Series(coefficients, index=dummy_vars.columns, name='Part-Worth')

    return part_worths, intercept


def calculate_importance(part_worths, attributes):
    """Calculate attribute importance based on part-worth utilities."""
    importance = {}
    for attribute in attributes.keys():
        levels = [col for col in part_worths.index if col.startswith(attribute)]
        range_of_levels = part_worths[levels].max() - part_worths[levels].min()
        importance[attribute] = range_of_levels

    total_range = sum(importance.values())
    for attribute in importance:
        importance[attribute] = (importance[attribute] / total_range) * 100 if total_range != 0 else 0

    importance_df = pd.DataFrame(list(importance.items()), columns=['Attribute', 'Importance (%)'])
    return importance_df


def save_results(part_worths, importance_df):
    """Save the part-worth utilities and attribute importances to CSV files."""
    part_worths.to_csv('PartWorthUtilities.csv')
    importance_df.to_csv('AttributeImportances.csv', index=False)

    print("Conjoint analysis completed successfully.")
    print("Results saved to 'PartWorthUtilities.csv' and 'AttributeImportances.csv'.")


def plot_importance(importance_df):
    """Generate a bar chart for attribute importances."""
    importance_df.plot(kind='bar', x='Attribute', y='Importance (%)')
    plt.title('Attribute Importances')
    plt.ylabel('Importance (%)')
    plt.tight_layout()
    plt.savefig('AttributeImportances.png')
    print("Attribute importances chart saved as 'AttributeImportances.png'.")


def main():
    """
    Main function to run the conjoint analysis calculator.
    """
    print("Starting Conjoint Analysis Calculator...")

    # Define file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Try to find Attributes file
    attributes_file = os.path.join(script_dir, 'Attributes.xlsx')
    if not os.path.exists(attributes_file):
        attributes_file = os.path.join(script_dir, 'Attributes.csv')
        if not os.path.exists(attributes_file):
            print("Error: Neither 'Attributes.xlsx' nor 'Attributes.csv' found.")
            return

    # Try to find Ratings file
    ratings_file = os.path.join(script_dir, 'Ratings.xlsx')
    if not os.path.exists(ratings_file):
        ratings_file = os.path.join(script_dir, 'Ratings.csv')
        if not os.path.exists(ratings_file):
            print("Error: Neither 'Ratings.xlsx' nor 'Ratings.csv' found.")
            return

    profiles_file = 'GeneratedProfiles.csv'

    # Load attributes
    attributes_df = load_attributes(attributes_file)
    if attributes_df is None:
        return

    # Generate profiles
    profiles_df, attributes = generate_profiles(attributes_df)

    # Save profiles
    save_profiles(profiles_df, profiles_file)

    # Prompt user to collect ratings
    input("Please collect respondent ratings for the generated profiles.\n"
          f"Use the 'Ratings.xlsx' or 'Ratings.csv' template and save it in the same directory.\n"
          f"Press Enter to continue after you have collected the ratings...")

    # Load ratings
    ratings_df = load_ratings(ratings_file)
    if ratings_df is None:
        return

    # Prepare data for regression
    X, y, dummy_vars = prepare_regression_data(profiles_df, ratings_df)
    if X is None:
        return

    # Perform regression 
    part_worths, intercept = perform_regression(X, y, dummy_vars)

    # Calculate attribute importance
    importance_df = calculate_importance(part_worths, attributes)

    # Save results
    save_results(part_worths, importance_df)

    # Plot attribute importance
    plot_importance(importance_df)


if __name__ == '__main__':
    main()

# Marketing Calculators

This repository contains a collection of marketing calculators implemented in Python. These tools are designed to assist marketers, business analysts, and students in performing essential calculations related to customer lifetime value, economic value to the customer, linear interpolation, and relative importance of attributes.

## **Give it a try!**

Try these out on my website: https://immesoete.cam/tools/marketing/

## **Calculators Included**

1. **Customer Lifetime Value (CLV) Calculator** (`clv_calculator.py`)
    - Calculates CLV over a fixed time horizon and into perpetuity.
    - Supports changing margins, retention rates, and interest rates over time.
    - **Inputs:**
      - Margin per customer (default: \$100)
      - Retention rate (default: 80%)
      - Interest rate (default: 10%)
      - Number of periods (default: 5)
      - Time unit (default: years)
    - **Outputs:**
      - CLV per period
      - Total CLV over the specified periods
      - CLV in perpetuity

2. **Economic Value to the Customer (EVC) Calculator** (`evc_calculator.py`)
    - Calculates the EVC based on reference value and differentiation.
    - **Inputs:**
      - Reference value (price of the next best alternative)
      - Positive differentiation value
      - Negative differentiation value
    - **Outputs:**
      - EVC

3. **Linear Interpolation Calculator** (`linear_interpolation_calculator.py`)
    - Performs linear interpolation to find an unknown X corresponding to a given Y.
    - **Inputs:**
      - X1, X2 (known X values)
      - Y1, Y2 (Y values corresponding to X1 and X2)
      - Y3 (Y value for which to find the corresponding X)
    - **Outputs:**
      - Interpolated X value corresponding to Y3

4. **Relative Importance Calculator** (`relative_importance_calculator.py`)
    - Calculates the relative importance of features based on their max and min values.
    - **Inputs:**
      - CSV or Excel file (`RelativeImportance.csv` or `RelativeImportance.xlsx`) containing:
         - Feature names
         - Max values
         - Min values
    - **Outputs:**
      - CSV file with calculated differences and relative importances

5. **Conjoint Analysis Calculator** (`conjoint_analysis_calculator.py`)
     - Performs conjoint analysis to determine the relative importance of product attributes.
     - **Inputs:**
          - Attributes file (`Attributes.xlsx` or `Attributes.csv`) containing:
                - Attribute names
                - Levels for each attribute
          - Ratings file (`Ratings.xlsx` or `Ratings.csv`) containing:
                - Respondent IDs
                - Ratings for each profile
     - **Outputs:**
          - Generated product profiles (`GeneratedProfiles.csv`)
          - Part-worth utilities (`PartWorthUtilities.csv`)
          - Attribute importances (`AttributeImportances.csv`)
          - Attribute importances chart (`AttributeImportances.png`)

## **Getting Started**

### **Prerequisites**

- Python 3.x
- Required Python packages:
  - `numpy`
  - `pandas`
  - `openpyxl` (for Excel support)
  - `matplotlib` (optional, for plotting in some calculators)

Install the required packages using:

```bash
pip install -r requirements.txt
```

### **Usage**

To use any of the calculators, run the corresponding Python script with the required input files. For example, to use the CLV calculator:

```bash
python clv_calculator.py
```

Ensure that the input files are in the same directory as the script or provide the full path to the files.

### **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### **Contact**

For any questions or feedback, please contact Cam.


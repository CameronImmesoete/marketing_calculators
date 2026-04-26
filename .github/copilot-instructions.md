# Copilot Instructions

> Base instructions: [CameronImmesoete/.github/.github/copilot-instructions.md@1f79bfb](https://github.com/CameronImmesoete/.github/blob/1f79bfb3e9eee277d05ecdd3332220204cb0f38b/.github/copilot-instructions.md)

## Repository-Specific Guidelines

This is a Python calculator library for marketing analytics (conjoint analysis, CLV, CAC, NPS, ROMI, break-even, churn rate, EVC, linear interpolation, relative importance).

- All calculators follow the same pattern: input validation, computation, output formatting
- Mathematical formulas must match standard marketing textbook definitions
- Division-by-zero guards are required on every calculator function
- Use numpy, pandas, scikit-learn, matplotlib as needed (declared in pyproject.toml)
- Type annotations on all public functions

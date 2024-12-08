# nps_calculator.py

import argparse

def calculate_nps(promoters, passives, detractors):
    total_respondents = promoters + passives + detractors
    if total_respondents == 0:
        return None
    return ((promoters - detractors) / total_respondents) * 100

def main():
    print("Starting Net Promoter Score (NPS) Calculator...")
    parser = argparse.ArgumentParser(description="Calculate Net Promoter Score (NPS).")
    parser.add_argument('--promoters', type=int, default=30, help='Number of promoters')
    parser.add_argument('--passives', type=int, default=10, help='Number of passives')
    parser.add_argument('--detractors', type=int, default=5, help='Number of detractors')

    args = parser.parse_args()
    nps = calculate_nps(args.promoters, args.passives, args.detractors)

    if nps is None:
        print("Error: Total respondents cannot be zero.")
    else:
        print(f"\nNPS Calculation Result:")
        print(f"NPS: {nps:.2f}")

if __name__ == '__main__':
    main()

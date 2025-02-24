# Example usage
marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}
# Expected Output:
# Best Performing Channel: Organic Search (5.6%)
# Average Conversion Rate: 4.0%

def analyze_marketing_performance(marketing_performance):
    highest_channel = max(marketing_performance, key=marketing_performance.get)
    highest_rate = marketing_performance[highest_channel]

    avg_rate = sum(marketing_performance.values()) / len(marketing_performance)

    print(f"Best Performing Channel: {highest_channel} ({highest_rate}%)")
    print(f"Average Conversion Rate: {avg_rate}%")

analyze_marketing_performance(marketing_performance)

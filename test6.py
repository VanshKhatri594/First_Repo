# Given a dictionary where marketing channels are keys and their conversion rates (as percentages) are values, find:
#
# The marketing channel with the highest conversion rate.
#
# The average conversion rate across all channels

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

highest_marketing_channel = max(marketing_performance,key=marketing_performance.get)
print(f"Best Performing Channel: {highest_marketing_channel}")

total = sum(marketing_performance.values())

avg = total / len(marketing_performance)

print(f"Average Conversion Rate: {avg}%")
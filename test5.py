# Given a dictionary where complaint types are keys and their occurrence counts are values, determine:
#
# The most common complaint type.
# The percentage share of each complaint type

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}

# Expected Output:

# Most Common Complaint: Late Delivery
# Complaint Percentage Distribution:
# {'Late Delivery': 32%, 'Damaged Product': 25%, 'Wrong Item': 16%, 'Customer Service': 20%, 'Billing Issues': 7%}

most_common_complain = max(complaints,key=complaints.get)
print(most_common_complain)

total_complaints = sum(complaints.values())
print(total_complaints)

percentage_distribution = {}
for complaint, count in complaints.items():
    percentage_distribution[complaint] = f"{(count / total_complaints) * 100}%"

print(percentage_distribution)

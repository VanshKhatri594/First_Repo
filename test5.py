# Example usage
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


def analyze_complaints(complaints):
    most_common_complaint = max(complaints, key=complaints.get)
    total_complaints = sum(complaints.values())

    percentage_distribution = {
        complaint: f"{(count / total_complaints) * 100}%"
        for complaint, count in complaints.items()
    }

    return most_common_complaint, percentage_distribution

most_common, distribution = analyze_complaints(complaints)

print("Most Common Complaint:", most_common)
print("Complaint Percentage Distribution:", distribution)

marks = {
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}

# Finding total marks of each student
total_marks = {}
subject_count = {}

for key, value in marks.items():
    name = key.split('-')[0]
    if name in total_marks:
        total_marks[name] += value
        subject_count[name] += 1
    else:
        total_marks[name] = value
        subject_count[name] = 1

print("Total Marks:", total_marks)

# Finding average marks of each student
avg_marks = {name: total_marks[name] / subject_count[name] for name in total_marks}
print("Average Marks:", avg_marks)

# Finding Highest Scoring Student
highest_scoring_student = None
highest_score = 0

for student, mark in total_marks.items():
    if mark > highest_score:
        highest_scoring_student = student
        highest_score = mark

if highest_scoring_student:
    print(f"Highest Scoring Student: {highest_scoring_student} with {highest_score} marks")
else:
    print("No student data available.")

# Sorting students based on their marks
sorted_marks = dict(sorted(total_marks.items(), key=lambda x: x[1], reverse=True))
print(f"Students sorted by total marks: {sorted_marks}")

#Subject Wise-Highest Marks
subject_highest_marks = {}

for key, value in marks.items():
    subject = key.split('-')[1]
    if subject in subject_highest_marks:
        subject_highest_marks[subject] = value if value > subject_highest_marks[subject] else subject_highest_marks[subject]
    else:
        subject_highest_marks[subject] = value
print("Subject-wise Highest Marks:", subject_highest_marks)




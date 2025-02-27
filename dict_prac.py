students = {
    "Alice": {"Math": 85, "Science": 92, "English": 78},
    "Bob": {"Math": 79, "Science": 85, "English": 88},
    "Charlie": {"Math": 92, "Science": 89, "English": 95},
    "David": {"Math": 70, "Science": 80, "English": 85}
}
# 1)Find the student with the highest average marks.
# 2)Sort the students based on their total marks.
# 3)Add a new student "Eve" with marks Math: 90, Science: 87, English: 93.
# 4)Find the subject in which "Charlie" scored the highest.

# 1)
highest_avg_student = None
highest_avg = 0

for student, subjects in students.items():
    avg_marks = sum(subjects.values()) / len(subjects)
    if avg_marks > highest_avg:
        highest_avg = avg_marks
        highest_avg_student = student
print(f"Student with highest avg marks {highest_avg_student} : {highest_avg}")

# 2)
sorted_students = sorted(students.items(), key=lambda x: sum(x[1].values()), reverse=True)
for student, total_marks in sorted_students:
    final = sum(total_marks.values())
    print(f"Sorted Students {student} : {final}")

# 3)
students["Eve"] = {"Math" : 90, "Science": 87, "English": 93}
print(students)

# 4)
for student, subjects in students.items():
    if student == "Charlie":
        highest_marks = max(subjects, key=subjects.get)
        print(f"Charlie scored highest in {highest_marks} : {subjects[highest_marks]}")






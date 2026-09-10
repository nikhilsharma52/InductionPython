students = [
    {"name": "Rahul", "marks": 75},
    {"name": "Aman", "marks": 90},
    {"name": "Priya", "marks": 85}
]

students.sort(key=lambda student: student["marks"])

print(students)

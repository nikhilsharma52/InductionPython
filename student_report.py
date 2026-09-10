import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    total_marks = 0
    count = 0

    for row in reader:
        total_marks += int(row["marks"])
        count += 1

average = total_marks/count

with open("report.txt", "w") as file:
    file.write("Student Summary Report\n")
    file.write("----------------------\n")
    file.write(f"Total Students: {count}\n")
    file.write(f"Average Marks: {average:.2f}\n")

print("Report created successfully!")

import csv

total_marks = 0
count = 0

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            try:
                marks = int(row["marks"])
                total_marks += marks
                count += 1
            except KeyError:
                print(f"Missing marks column on row {row_number}")
            except ValueError:
                print(f"Invalid marks on row {row_number}: {row.get('marks')}")

except FileNotFoundError:
    print("students.csv was not found.")

else:
    if count > 0:
        average = total_marks / count

        with open("report.txt", "w") as file:
            file.write("Student Summary Report\n")
            file.write("----------------------\n")
            file.write(f"Total Students: {count}\n")
            file.write(f"Average Marks: {average:.2f}\n")

        print("Report created successfully!")
    else:
        print("No valid student records found.")

    
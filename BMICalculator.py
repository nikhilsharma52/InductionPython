height = float(input("Enter your Height(m): "))
weight = float(input("Enter Your Weight(KG): "))

bmi = weight/(height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
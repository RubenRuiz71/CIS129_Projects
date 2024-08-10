# Initialize an empty list to store grades
grades = []

# Prompt the user to enter grades until they enter the sentinel value (-1)
while True:
    grade = input("Enter a grade (or -1 to stop): ")
    if grade == "-1":
        break
    else:
        try:
            # Convert the input to a float and store it in the grades list
            grades.append(float(grade))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Write the grades to a file called grades.txt
with open("grades.txt", "w") as file:
    for grade in grades:
        file.write(f"{grade}\n")

print("Grades have been saved to grades.txt")

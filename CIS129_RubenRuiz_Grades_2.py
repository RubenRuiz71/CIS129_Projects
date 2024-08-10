# Initialize variables
grades = []
total = 0
count = 0

# Open and read the grades from the grades.txt file
with open("grades.txt", "r") as file:
    for line in file:
        grade = float(line.strip())  # Convert the line to a float and strip any extra whitespace
        grades.append(grade)  # Add the grade to the list
        total += grade  # Add the grade to the total
        count += 1  # Increment the count

# Calculate the average
if count > 0:
    average = total / count
else:
    average = 0  # Avoid division by zero if no grades are present

# Display the individual grades
print("Individual grades:")
for grade in grades:
    print(grade)

# Display the total, count, and average
print(f"\nTotal of grades: {total}")
print(f"Number of grades: {count}")
print(f"Average grade: {average:.2f}")

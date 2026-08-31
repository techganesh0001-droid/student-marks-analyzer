name = input("Enter your name: ")

mark1 = int(input("Enter your marks in Math: "))
mark2 = int(input("Enter your marks in Science: "))
mark3 = int(input("Enter your marks in English: "))
mark4 = int(input("Enter your marks in Social Studies: "))
mark5 = int(input("Enter your marks in Computer Science: "))

marks = [mark1, mark2, mark3, mark4, mark5]

total_marks = sum(marks)
percentage = total_marks / 5
highest_marks = max(marks)
lowest_marks = min(marks)

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# Check pass/fail
if all(mark >= 33 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")

# Grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)

# Message
if grade == "A":
    print(f"Congratulations, {name}! Excellent performance.")
elif grade == "F":
    print(f"Sorry, {name}. Better luck next time.")
else:
    print(f"Good job, {name}! Keep improving.")

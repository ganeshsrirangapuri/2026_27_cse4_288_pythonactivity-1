
# University Scholarship Allocation System
students = []
# Function to check eligibility
def check_eligibility(student):

    if student["marks"] < 75:
        return False

    if student["math"] < 50:
        return False

    if student["science"] < 50:
        return False

    if student["english"] < 50:
        return False

    if student["attendance"] < 75:
        return False

    if student["income"] > 250000:
        return False

    return True


# Get number of students
n = int(input("Enter number of students: "))

# Collect student information
for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = float(input("Enter aggregate marks: "))
    math = float(input("Enter Mathematics marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    student = {
        "name": name,
        "marks": marks,
        "math": math,
        "science": science,
        "english": english,
        "attendance": attendance,
        "income": income
    }

    # Check eligibility
    if check_eligibility(student):
        students.append(student)

# Sort eligible students
# 1. Highest aggregate marks
# 2. Highest attendance
# 3. Lowest family income
# 4. Alphabetical name if all previous values are equal

students.sort(
    key=lambda s: (
        -s["marks"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

# Display eligible students
print("\n========== SCHOLARSHIP RESULTS ==========")

if len(students) > 0:

    print("\nELIGIBLE STUDENTS")

    print("-" * 75)
    print(f"{'Rank':<8}{'Name':<18}{'Marks':<12}"
          f"{'Attendance':<15}{'Income':<15}")
    print("-" * 75)

    for rank, s in enumerate(students, start=1):

        print(f"{rank:<8}{s['name']:<18}"
              f"{s['marks']:<12.2f}"
              f"{s['attendance']:<15.2f}"
              f"{s['income']:<15.2f}")

else:
    print("\nNo eligible students found.")

# Display ineligible students
print("\nINELIGIBLE STUDENTS")

# Recheck all applicants to find those who failed
# Eligibility (using a separate applicant list)
print("Students who do not satisfy the criteria are not eligible.")

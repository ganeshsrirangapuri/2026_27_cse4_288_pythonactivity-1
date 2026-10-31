
# University Scholarship Allocation System

applicants = []
eligible = []
ineligible = []

n = int(input("Enter number of students: "))

for i in range(n):

    print("\nStudent", i + 1)

    student = {
        "name": input("Name: "),
        "marks": float(input("Aggregate marks: ")),
        "math": float(input("Mathematics marks: ")),
        "science": float(input("Science marks: ")),
        "english": float(input("English marks: ")),
        "attendance": float(input("Attendance: ")),
        "income": float(input("Annual family income: "))
    }

    applicants.append(student)

    # Eligibility conditions
    if (
        student["marks"] >= 75
        and student["math"] >= 50
        and student["science"] >= 50
        and student["english"] >= 50
        and student["attendance"] >= 75
        and student["income"] <= 250000
    ):
        eligible.append(student)
    else:
        ineligible.append(student)

# Ranking and tie-breaking
eligible.sort(
    key=lambda s: (
        -s["marks"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

print("\n========== SCHOLARSHIP RESULTS ==========")

print("\nELIGIBLE STUDENTS")

if eligible:
    print(f"{'Rank':<8}{'Name':<18}{'Marks':<12}"
          f"{'Attendance':<15}{'Income':<12}")

    for rank, s in enumerate(eligible, 1):
        print(f"{rank:<8}{s['name']:<18}"
              f"{s['marks']:<12.2f}"
              f"{s['attendance']:<15.2f}"
              f"{s['income']:<12.2f}")
else:
    print("No eligible students.")

print("\nINELIGIBLE STUDENTS")

if ineligible:
    for s in ineligible:
        print(s["name"], "- Not Eligible")
else:
    print("No ineligible students.")

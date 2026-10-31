
# Employee Payroll and Deduction Analysis System

print("==========================================")
print(" EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
print("==========================================")

# Employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

# Salary details
basic = float(input("Enter Basic Salary: Rs. "))
allowances = float(input("Enter Allowances: Rs. "))
overtime_hours = float(input("Enter Overtime Hours: "))
overtime_rate = float(input("Enter Overtime Rate per Hour: Rs. "))
incentives = float(input("Enter Incentives: Rs. "))

# Input validation
if (name.strip() == "" or emp_id.strip() == "" or
    basic < 0 or allowances < 0 or
    overtime_hours < 0 or overtime_rate < 0 or
    incentives < 0):

    print("\nInvalid Employee Details or Salary Inputs!")

else:

    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = basic + allowances + overtime_pay + incentives

    # Calculate progressive deductions
    if gross_salary <= 10000:
        deduction = 0

    elif gross_salary <= 20000:
        deduction = (gross_salary - 10000) * 0.05

    elif gross_salary <= 40000:
        deduction = (10000 * 0.05) + (
            (gross_salary - 20000) * 0.10)

    else:
        deduction = (10000 * 0.05) + (
            20000 * 0.10) + (
            (gross_salary - 40000) * 0.15)

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Display salary statement
    print("\n==========================================")
    print("           EMPLOYEE SALARY SLIP")
    print("==========================================")

    print("Employee Name      :", name)
    print("Employee ID        :", emp_id)

    print("------------------------------------------")
    print("Basic Salary       : Rs.", basic)
    print("Allowances         : Rs.", allowances)
    print("Overtime Pay       : Rs.", overtime_pay)
    print("Incentives         : Rs.", incentives)

    print("------------------------------------------")
    print("Gross Salary       : Rs.", gross_salary)
    print("Total Deductions   : Rs.", deduction)

    print("------------------------------------------")
    print("Net Salary         : Rs.", net_salary)

    print("==========================================")
    print("       SALARY CALCULATION COMPLETED")
    print("==========================================")


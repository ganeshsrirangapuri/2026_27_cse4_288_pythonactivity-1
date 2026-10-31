. Problem Statement
Develop a Python program for an Employee Payroll and Deduction Analysis System. The system calculates the employee's gross salary based on basic pay, allowances, overtime, and incentives.

The program should:
- Accept employee details such as employee name and ID.
- Accept basic salary, allowances, overtime hours, overtime rate, and incentives.
- Calculate overtime pay.
- Calculate gross salary.
- Apply progressive deductions based on salary slabs.
- Calculate net salary after deductions.
- Validate employee details and salary inputs.
- Generate and display a formatted salary statement.
2. Algorithm
1. Start the program.
2. Enter employee name and employee ID.
3. Enter basic salary.
4. Enter allowances.
5. Enter overtime hours and overtime rate.
6. Enter incentives.
7. Validate all input values.
8. Calculate overtime pay.
   Overtime Pay = Overtime Hours × Overtime Rate

9. Calculate gross salary.

   Gross Salary = Basic Salary + Allowances + Overtime Pay + Incentives
10. Apply progressive deductions:
    - First ₹10,000: 0% deduction.
    - Next ₹10,000: 5% deduction.
    - Next ₹20,000: 10% deduction.
    - Above ₹40,000: 15% deduction.
11. Calculate total deductions.
12. Calculate net salary.
    Net Salary = Gross Salary − Total Deductions
13. Display the formatted salary statement.
14. Stop the program.
flowchart TD

    A([Start]) --> B[/Enter Employee Name and ID/]

    B --> C[/Enter Basic Salary, Allowances, Overtime and Incentives/]

    C --> D{Inputs Valid?}

    D -- No --> E[Display Invalid Input]
    E --> Z([Stop])

    D -- Yes --> F[Calculate Overtime Pay]

    F --> G[Calculate Gross Salary]

    G --> H{Gross Salary Slab?}

    H -- Up to 10000 --> I[0% Deduction]

    H -- 10001 to 20000 --> J[5% Deduction on Amount Above 10000]

    H -- 20001 to 40000 --> K[5% and 10% Progressive Deduction]

    H -- Above 40000 --> L[5%, 10% and 15% Progressive Deduction]

    I --> M[Calculate Total Deductions]
    J --> M
    K --> M
    L --> M

    M --> N[Calculate Net Salary]

    N --> O[Generate Salary Statement]

    O --> P[/Display Employee Salary Slip/]

    P --> Z([Stop])


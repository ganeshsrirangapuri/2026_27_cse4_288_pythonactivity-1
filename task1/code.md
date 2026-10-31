
mermaid flowchart code
1. University Scholarship Allocation System
1. Problem Statement
The University Scholarship Allocation System is designed to identify eligible students for scholarships based on their academic performance, attendance, and family income.

The system evaluates each student's:

Aggregate Marks: Minimum 75%.

Subject-wise Marks: Mathematics, Science, and English must each be at least 50%.

Attendance: Minimum 75%.

Family Income: Annual income must not exceed ₹2,50,000.

Students who satisfy all the eligibility criteria are considered eligible for scholarships.

The system ranks eligible students according to the following rules:

First priority: Highest aggregate marks.

Second priority: Highest attendance.

Third priority: Lowest annual family income.

The system displays the eligible students with their ranks and identifies students who are not eligible.

2. Algorithm
Start the program.

Read the number of students.

Enter each student's name.

Enter aggregate marks.

Enter Mathematics, Science, and English marks.

Enter attendance percentage.

Enter annual family income.

Check all eligibility conditions.

If all conditions are satisfied, add the student to the eligible list.

Otherwise, add the student to the ineligible list.

Sort eligible students using:

Highest aggregate marks.

Highest attendance.

Lowest family income.

Assign ranks to eligible students.

Display eligible and ineligible students.

Stop the program.flowchart TD
    A([Start]) --> B[/Enter Number of Students/]
    B --> C[/Enter Student Details/]
    C --> D[/Enter Aggregate Marks/]
    D --> E[/Enter Subject-wise Marks/]
    E --> F[/Enter Attendance and Income/]

    F --> G{Aggregate >= 75?}

    G -- No --> N[Not Eligible]
    G -- Yes --> H{All Subject Marks >= 60?}

    H -- No --> N
    H -- Yes --> I{Attendance >= 75?}

    I -- No --> N
    I -- Yes --> J{Income <= 250000?}

    J -- No --> N
    J -- Yes --> K[Mark as Eligible]

    K --> L{More Students?}
    N --> L

    L -- Yes --> C
    L -- No --> M[Collect Eligible Students]

    M --> O[Sort by Aggregate Marks]
    O --> P[Break Ties Using Attendance]
    P --> Q[Break Ties Using Lower Income]
    Q --> R[Break Remaining Ties Using Subject Marks]

    R --> S[/Display Ranked Scholarship List/]
    S --> T[/Display Not Eligible Students/]
    T --> U([End])

10. Campus Event Financial Planning – Python Program
1. Problem Statement
Develop a Python program for Campus Event Financial Planning to calculate the total expenses involved in organizing a college event.

The program should calculate the costs of:1. Venue charges
2. Equipment charges
3. Catering charges
4. Transportation charges
5. Certificate charges
The program should also:
- Calculate the total event cost.
- Calculate the sponsorship amount received.
- Identify the sponsorship shortfall.
- Calculate the participant contribution.
- Determine the minimum number of registrations required to break even.
- Display whether the event makes a profit or incurs a loss.
2. Algorithm
1. Start the program.
2. Enter venue cost.
3. Enter equipment cost.
4. Enter catering cost per participant.
5. Enter transport cost.
6. Enter certificate cost per participant.
7. Enter expected number of participants.
8. Enter sponsorship amount.
9. Calculate fixed costs (venue + equipment + transport).
10. Calculate variable costs (catering + certificates).
11. Calculate total event cost.
12. Calculate sponsorship shortfall.
13. Calculate participant contribution per person.
14. Calculate minimum registrations required to break even.
15. Display all financial details.
16. Stop the program.

flowchart TD

    A([Start]) --> B[Display Event Financial Planning]

    B --> C[/Enter Venue Cost/]

    C --> D[/Enter Equipment Cost/]

    D --> E[/Enter Transport Cost/]

    E --> F[/Enter Catering Cost per Participant/]

    F --> G[/Enter Certificate Cost per Participant/]

    G --> H[/Enter Expected Participants/]

    H --> I[/Enter Sponsorship Amount/]

    I --> J[/Enter Registration Fee/]

    J --> K{Are Inputs Valid?}

    K -- No --> L[Display Invalid Input]

    L --> Z([End])

    K -- Yes --> M[Calculate Fixed Cost]

    M --> N[Calculate Variable Cost]

    N --> O[Calculate Total Event Cost]

    O --> P[Calculate Sponsorship Shortfall]

    P --> Q[Calculate Participant Contribution]

    Q --> R[Calculate Minimum Break Even Registrations]

    R --> S[Calculate Total Income]

    S --> T{Income Greater Than Cost?}

    T -- Yes --> U[Display Profit]

    T -- No --> V{Income Less Than Cost?}

    V -- Yes --> W[Display Loss]

    V -- No --> X[Display Break Even]

    U --> Y[Display Financial Report]

    W --> Y

    X --> Y

    Y --> Z([End])

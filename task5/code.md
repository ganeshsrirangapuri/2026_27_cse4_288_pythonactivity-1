1. Problem Statement
Develop a Python program for a Multi-Plan Telecommunications Cost Optimization System. The system evaluates multiple mobile recharge plans based on the user's data usage, call minutes, SMS usage, validity period, and budget.

The program should:
- Accept customer details and usage requirements.
- Accept multiple mobile plans with their prices, data limits, call limits, SMS limits, and validity.
- Calculate excess charges when usage exceeds plan limits.
- Check whether each plan satisfies the customer's usage and budget requirements.
- Identify eligible mobile plans.
- Compare the total costs of eligible plans.
- Select and display the most economical eligible plan.
- Display all plan details and the final recommendation.
2. Algorithm
1. Start the program.
2. Enter customer name.
3. Enter required data usage in GB.
4. Enter required call minutes.
5. Enter required SMS count.
6. Enter required validity in days.
7. Enter the customer's maximum budget.
8. Enter the number of mobile plans.
9. For each plan, enter:
   - Plan name.
   - Plan price.
   - Data limit.
   - Call minutes limit.
   - SMS limit.
   - Validity days.
10. Calculate excess data, call, and SMS usage.
11. Calculate excess charges.
12. Calculate the total plan cost.
13. Check budget and validity constraints.
14. Identify eligible plans.
15. Compare the total costs of eligible plans.
16. Select the plan with the lowest total cost.
17. Display all plan comparisons.
18. Display the most economical eligible plan.
19. If no plan is eligible, display a suitable message.
20. Stop.
  
flowchart TD

    A([Start]) --> B[/Enter Customer Details/]

    B --> C[/Enter Data, Calls, SMS, Validity and Budget/]

    C --> D{Customer Inputs Valid?}

    D -- No --> E[Display Invalid Requirements]
    E --> Z([Stop])

    D -- Yes --> F[/Enter Number of Mobile Plans/]

    F --> G[Initialize Plan List]

    G --> H[/Enter Plan Details/]

    H --> I{Plan Details Valid?}

    I -- No --> H

    I -- Yes --> J[Calculate Excess Usage]

    J --> K[Calculate Excess Charges]

    K --> L[Calculate Total Plan Cost]

    L --> M{Usage and Validity Satisfied?}

    M -- No --> N[Mark Plan Not Eligible]

    M -- Yes --> O{Within Budget?}

    O -- No --> N

    O -- Yes --> P[Mark Plan Eligible]

    N --> Q{More Plans?}
    P --> Q

    Q -- Yes --> H

    Q -- No --> R{Eligible Plans Available?}

    R -- No --> S[Display No Eligible Plan]

    R -- Yes --> T[Compare Total Costs]

    T --> U[Select Lowest Cost Plan]

    U --> V[Display Recommended Plan]

    S --> W([Stop])
    V --> W


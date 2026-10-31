2. Progressive Electricity Billing System
1. Problem Statement
The Progressive Electricity Billing System is designed to calculate household electricity bills based on monthly electricity consumption.

The system calculates electricity charges using different consumption slabs. It also includes fixed charges, surcharges, and rebates to determine the final bill amount.

The system performs the following operations:
1. Accepts household electricity consumption in units (kWh).
2. Calculates charges using multiple electricity slabs.
3. Adds fixed monthly charges.
4. Calculates additional surcharges.
5. Applies rebates if applicable.
6. Calculates the final electricity bill.
7. Compares electricity bills across several months.
8. Identifies unusual increases in monthly bills.
Electricity billing rules used in this project (sample rates):
Consumption slab	Rate per unit
0–100 units	₹2.00
101–200 units	₹3.00
201–300 units	₹5.00
Above 300 units	₹7.00

Additional charges:
Charge type	Amount
Fixed charge	₹50
Surcharge	5% of energy charges
Rebate	5% if consumption is below 100 units

These are assumed rates for an educational project, not official electricity tariff rates.
2. Algorithm
1. Start the program.
2. Enter the number of months.
3. Enter the month name and electricity consumption for each month.
4. Calculate electricity charges using progressive slabs:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Next 100 units: ₹5 per unit.
   - Above 300 units: ₹7 per unit.
5. Add the fixed charge of ₹50.
6. Calculate a 5% surcharge on energy charges.
7. If consumption is below 100 units, apply a 5% rebate on energy charges.
8. Calculate the final bill.
9. Store the monthly bill details.
10. Compare each month's bill with the previous month's bill.
11. If the bill increases by more than 30%, identify it as an unusual increase.
12. Display monthly bills and comparison results.
13. Stop the program.
flowchart TD

    A([Start]) --> B[Define Slab Rates and Charges]

    B --> C[/Enter Number of Months/]

    C --> D[/Enter Monthly Units Consumed/]

    D --> E{Units Valid?}

    E -- No --> D
    E -- Yes --> F[Calculate Energy Charges]

    F --> G[Add Fixed Charges]

    G --> H[Calculate Surcharge]

    H --> I{Units Below 100?}

    I -- Yes --> J[Apply 5% Rebate]
    I -- No --> K[No Rebate]

    J --> L[Calculate Final Bill]
    K --> L

    L --> M[Store Monthly Bill]

    M --> N{More Months?}

    N -- Yes --> D
    N -- No --> O[Display Monthly Bills]

    O --> P[Compare Consecutive Bills]

    P --> Q{Increase Greater Than 30%?}

    Q -- Yes --> R[Display Unusual Increase Alert]
    Q -- No --> S[Display Normal Bill Variation]

    R --> T[Calculate Total Expenditure]
    S --> T

    T --> U[/Display Final Report/]

    U --> V([End])

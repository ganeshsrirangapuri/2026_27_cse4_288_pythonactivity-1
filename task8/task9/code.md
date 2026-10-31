
9. Multi-Currency Travel Budget Analysis
1. Problem Statement
Develop a Python program for a Multi-Currency Travel Budget Analysis System. The system calculates travel expenses in different currencies by using supplied exchange rates and conversion fees.

The program should:

Accept traveller name and total travel budget in Indian Rupees (INR).

Accept multiple travel expense categories.

Accept expense amounts in different foreign currencies.

Convert foreign currency expenses into INR using supplied exchange rates.

Calculate currency conversion fees.

Calculate the total travel expenditure.

Compare total expenditure against the planned budget.

Identify the largest expense category.

Display the remaining budget or excess spending.

Generate a formatted travel expense report.

2. Algorithm
Start the program.

Enter traveller name.

Enter total travel budget in INR.

Enter the number of expense categories.

For each expense, enter:

Expense category.

Currency code.

Expense amount.

Exchange rate against INR.

Conversion fee percentage.

Validate all input values.

Convert the foreign currency amount into INR.

Converted Amount = Foreign Amount × Exchange Rate

8. Calculate conversion fee.

Conversion Fee = Converted Amount × Fee Percentage / 100

9. Calculate total expense.

Total Expense = Converted Amount + Conversion Fee

Add all expenses to calculate total travel expenditure.

Compare total expenditure with the planned budget.

Identify the largest expense category.

Calculate remaining budget or excess spending.

Display the complete travel expense report.

Stop.

flowchart TD

    A([Start]) --> B[/Enter Traveller Name and Budget/]

    B --> C[/Enter Number of Expense Categories/]

    C --> D{Input Details Valid?}

    D -- No --> E[Display Invalid Input]
    E --> Z([Stop])

    D -- Yes --> F[/Enter Expense Category and Currency/]

    F --> G[/Enter Amount, Exchange Rate and Conversion Fee/]

    G --> H{Expense Details Valid?}

    H -- No --> I[Display Invalid Expense]

    H -- Yes --> J[Convert Foreign Currency into INR]

    J --> K[Calculate Conversion Fee]

    K --> L[Calculate Total Expense]

    L --> M[Add Expense to Total Expenditure]

    I --> N{More Expenses?}
    M --> N

    N -- Yes --> F

    N -- No --> O[Calculate Total Travel Expenditure]

    O --> P[Identify Largest Expense Category]

    P --> Q[Compare Expenditure with Budget]

    Q --> R{Expenditure Within Budget?}

    R -- Yes --> S[Calculate Remaining Budget]

    R -- No --> T[Calculate Excess Spending]

    S --> U[Generate Travel Expense Report]

    T --> U

    U --> V[/Display Total Expenses and Largest Category/]

    V --> W([Stop])

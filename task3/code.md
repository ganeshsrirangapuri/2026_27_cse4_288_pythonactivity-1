mermaid flowchart code
3. Hospital Billing and Patient Classification System
1. Problem Statement
Develop a Python program to calculate hospital bills based on consultation charges, diagnostic charges, and treatment charges.

The system should:

Accept patient details such as name, age, and patient type.

Calculate consultation, diagnostic, and treatment charges.

Apply conditional concessions based on patient category.

Validate billing constraints, such as negative charges and invalid inputs.

Calculate the final bill after applying discounts.

Classify patients according to their payment amount.

Display the complete billing details.

Patient classification policy used in this program:

Below ₹5,000 – Low Payment

₹5,000 to ₹15,000 – Medium Payment

Above ₹15,000 – High Payment

Concession policy:

Senior citizens (age 60 or above) receive a 10% concession.

Patients with a valid insurance card receive a 5% concession.

Both concessions are not combined; the higher concession is applied.

2. Algorithm
Start the program.

Enter patient name and age.

Enter consultation charges.

Enter diagnostic charges.

Enter treatment charges.

Enter insurance status.

Validate all input values.

Calculate the total bill:

Total Bill = Consultation + Diagnostic + Treatment

Check patient eligibility for concessions.

Apply the highest eligible concession.

Calculate the final bill.

Classify the patient based on the final payment:

Below ₹5,000: Low Payment.

₹5,000–₹15,000: Medium Payment.

Above ₹15,000: High Payment.

Display the patient details and final bill.

Stop.
flowchart TD

    A([Start]) --> B[/Enter Patient Details/]

    B --> C[/Enter Consultation, Diagnostic and Treatment Charges/]

    C --> D{Patient Details Valid?}

    D -- No --> E[Display Invalid Details]
    E --> Z([Stop])

    D -- Yes --> F{Charges Valid?}

    F -- No --> G[Display Invalid Charges]
    G --> Z

    F -- Yes --> H[Calculate Total Bill]

    H --> I{Patient Category?}

    I -- General --> J[No Discount]
    I -- Senior Citizen --> K[Apply 10% Discount]
    I -- Below Poverty Line --> L[Apply 25% Discount]

    J --> M[Calculate Final Bill]
    K --> M
    L --> M

    M --> N[/Enter Amount Paid/]

    N --> O{Payment Valid?}

    O -- No --> P[Display Invalid Payment]
    P --> N

    O -- Yes --> Q[Calculate Balance Amount]

    Q --> R{Amount Paid?}

    R -- Equal to Final Bill --> S[Full Payment]
    R -- Greater than Zero --> T[Partial Payment]
    R -- Zero --> U[Payment Pending]

    S --> V[Display Patient Bill]
    T --> V
    U --> V

    V --> Z([Stop])

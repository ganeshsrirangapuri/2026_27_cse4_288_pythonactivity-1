Railway Fare and Reservation Calculator
1. Problem Statement
Develop a Python program for a Railway Fare and Reservation Calculator. The system calculates railway ticket fares for multiple passengers based on travel distance, travel class, age-based concessions, reservation fees, and cancellation penalties.

The program should:
- Accept passenger details such as name and age.
- Accept the travel distance in kilometers.
- Allow passengers to select their travel class (Sleeper, AC 3-Tier, or AC 2-Tier).
- Calculate basic fare based on distance slabs.
- Apply age-based concessions for children and senior citizens.
- Add reservation charges.
- Calculate the total ticket fare for multiple passengers.
- Apply cancellation penalties when a ticket is cancelled.
- Display the final fare and reservation details.
2. Algorithm
1. Start the program.
2. Enter the number of passengers.
3. Enter the travel distance in kilometers.
4. Select the travel class.
5. Enter passenger name and age for each passenger.
6. Calculate basic fare based on distance:
   - Up to 100 km: ₹1.50 per km.
   - 101–300 km: ₹1.30 per km.
   - Above 300 km: ₹1.10 per km.
7. Apply class multipliers:
   - Sleeper: 1.0
   - AC 3-Tier: 2.0
   - AC 2-Tier: 3.0
8. Apply age-based concessions:
   - Children below 5 years: Free fare.
   - Senior citizens aged 60 and above: 20% concession.
   - Other passengers: No concession.
9. Add reservation charges based on travel class.
10. Calculate the total fare for all passengers.
11. Ask whether the ticket should be cancelled.
12. If cancelled, calculate the cancellation penalty (20% of the ticket fare).
13. Calculate the refund amount.
14. Display passenger details, ticket fare, cancellation penalty, and final payable or refund amount.
15. Stop the program.
flowchart TD

    A([Start]) --> B[/Enter Travel Distance and Passenger Count/]

    B --> C{Journey Details Valid?}

    C -- No --> D[Display Invalid Details]
    D --> Z([Stop])

    C -- Yes --> E[Select Travel Class]

    E --> F{Valid Travel Class?}

    F -- No --> G[Display Invalid Class]
    G --> Z

    F -- Yes --> H[Determine Distance Slab and Fare Rate]

    H --> I[Calculate Basic Fare Using Class Multiplier]

    I --> J[/Enter Passenger Name and Age/]

    J --> K{Passenger Details Valid?}

    K -- No --> L[Display Invalid Passenger Details]

    K -- Yes --> M{Check Passenger Age}

    M -- Below 5 --> N[Apply 100% Fare Concession]

    M -- Age 60 or Above --> O[Apply 20% Concession]

    M -- Other Ages --> P[No Concession]

    N --> Q[Calculate Passenger Fare]
    O --> Q
    P --> Q
    L --> R{More Passengers?}
    Q --> S[Add Reservation Fee]
    S --> T[Calculate Final Passenger Fare]
    T --> U[Add to Total Fare]
    U --> R

    R -- Yes --> J
    R -- No --> V[Display Total Ticket Fare]

    V --> W{Cancel Ticket?}

    W -- Yes --> X[Calculate 20% Cancellation Penalty]
    X --> Y[Calculate Refund Amount]
    Y --> AA[Display Cancellation Details]

    W -- No --> AB[Confirm Reservation and Display Fare]

    AA --> AC([Stop])
    AB --> AC


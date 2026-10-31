
# Railway Fare and Reservation Calculator

print("==========================================")
print(" RAILWAY FARE AND RESERVATION CALCULATOR")
print("==========================================")

# Enter passenger and journey details
distance = float(input("Enter Travel Distance (KM): "))
n = int(input("Enter Number of Passengers: "))

# Validate journey details
if distance <= 0 or n <= 0:
    print("Invalid Distance or Passenger Count!")

else:

    total_fare = 0
    passengers = []

    # Distance slab calculation
    if distance <= 100:
        rate = 1.50

    elif distance <= 300:
        rate = 1.30

    else:
        rate = 1.10

    # Travel class selection
    print("\nTravel Classes:")
    print("1. Sleeper")
    print("2. AC 3-Tier")
    print("3. AC 2-Tier")

    choice = int(input("Select Travel Class: "))

    if choice == 1:
        travel_class = "Sleeper"
        multiplier = 1.0
        reservation_fee = 20

    elif choice == 2:
        travel_class = "AC 3-Tier"
        multiplier = 2.0
        reservation_fee = 40

    elif choice == 3:
        travel_class = "AC 2-Tier"
        multiplier = 3.0
        reservation_fee = 60

    else:
        travel_class = ""
        print("Invalid Travel Class!")

    if travel_class:

        # Calculate base fare
        basic_fare = distance * rate * multiplier

        # Passenger details
        for i in range(n):

            print("\nPassenger", i + 1)

            name = input("Enter Passenger Name: ")
            age = int(input("Enter Passenger Age: "))

            if name.strip() == "" or age < 0 or age > 120:
                print("Invalid Passenger Details!")
                continue

            # Age-based concession
            if age < 5:
                concession = 100

            elif age >= 60:
                concession = 20

            else:
                concession = 0

            # Calculate fare after concession
            passenger_fare = basic_fare * (
                1 - concession / 100
            )

            # Free fare for children under 5
            if age < 5:
                reservation = 0
            else:
                reservation = reservation_fee

            final_fare = passenger_fare + reservation

            passengers.append({
                "name": name,
                "age": age,
                "basic": basic_fare,
                "concession": concession,
                "reservation": reservation,
                "fare": final_fare
            })

            total_fare += final_fare

        # Display ticket details
        if passengers:

            print("\n==========================================")
            print("          RAILWAY TICKET DETAILS")
            print("==========================================")

            print("Travel Distance :", distance, "KM")
            print("Travel Class    :", travel_class)
            print("Distance Rate   : Rs.", rate)
            print("Class Multiplier:", multiplier)

            for p in passengers:
                print("\nPassenger Name  :", p["name"])
                print("Passenger Age   :", p["age"])
                print("Basic Fare      : Rs.", p["basic"])
                print("Concession      :", p["concession"], "%")
                print("Reservation Fee : Rs.", p["reservation"])
                print("Passenger Fare  : Rs.", p["fare"])

            print("\n------------------------------------------")
            print("Total Ticket Fare: Rs.", total_fare)

            # Cancellation option
            cancel = input(
                "\nDo you want to cancel the tickets? (yes/no): "
            ).lower()

            if cancel == "yes":

                penalty = total_fare * 0.20
                refund = total_fare - penalty

                print("\n========== CANCELLATION DETAILS ==========")
                print("Original Fare   : Rs.", total_fare)
                print("Cancellation Fee: Rs.", penalty)
                print("Refund Amount   : Rs.", refund)

            elif cancel == "no":

                print("\nReservation Confirmed!")
                print("Amount Payable  : Rs.", total_fare)

            else:
                print("Invalid Cancellation Choice!")

            print("==========================================")

        else:
            print("No valid passenger details entered.")


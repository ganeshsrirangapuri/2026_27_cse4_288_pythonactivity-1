
# Progressive Electricity Billing System

# Function to calculate electricity charges
def calculate_bill(units):

    energy_charge = 0

    # Progressive electricity slabs
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + ((units - 100) * 3)

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        energy_charge = (
            (100 * 2) +
            (100 * 3) +
            (100 * 5) +
            ((units - 300) * 7)
        )

    # Fixed charge
    fixed_charge = 50

    # 5% surcharge on energy charge
    surcharge = energy_charge * 0.05

    # 5% rebate if consumption is below 100 units
    if units < 100:
        rebate = energy_charge * 0.05
    else:
        rebate = 0

    # Calculate final bill
    total_bill = (
        energy_charge +
        fixed_charge +
        surcharge -
        rebate
    )

    return energy_charge, fixed_charge, surcharge, rebate, total_bill


# Main program
bills = []

n = int(input("Enter number of months: "))

if n <= 0:
    print("Please enter a valid number of months.")

else:

    # Get monthly consumption
    for i in range(n):

        print("\nMonth", i + 1)

        month = input("Enter month name: ")
        units = float(input("Enter electricity units: "))

        if units < 0:
            print("Invalid units. Please restart the program.")
            break

        energy, fixed, surcharge, rebate, total = calculate_bill(units)

        bills.append({
            "month": month,
            "units": units,
            "energy": energy,
            "fixed": fixed,
            "surcharge": surcharge,
            "rebate": rebate,
            "total": total
        })

    # Display bills if all months were entered
    if len(bills) == n:

        print("\n========== ELECTRICITY BILL REPORT ==========")

        for bill in bills:

            print("\nMonth:", bill["month"])
            print("Units Consumed:", bill["units"])
            print("Energy Charges: Rs.", round(bill["energy"], 2))
            print("Fixed Charges: Rs.", round(bill["fixed"], 2))
            print("Surcharge: Rs.", round(bill["surcharge"], 2))
            print("Rebate: Rs.", round(bill["rebate"], 2))
            print("Final Bill: Rs.", round(bill["total"], 2))

        # Compare monthly bills
        print("\n========== MONTHLY BILL COMPARISON ==========")

        for i in range(1, len(bills)):

            previous = bills[i - 1]["total"]
            current = bills[i]["total"]

            increase = current - previous

            if previous > 0:
                percentage = (increase / previous) * 100
            else:
                percentage = 0

            print("\n", bills[i]["month"])

            print("Previous Bill: Rs.", round(previous, 2))
            print("Current Bill: Rs.", round(current, 2))

            print("Change: Rs.", round(increase, 2))
            print("Percentage Change:", round(percentage, 2), "%")

            if percentage > 30:
                print("WARNING: Unusual Bill Increase!")

            elif percentage > 0:
                print("Bill Increased Normally.")

            elif percentage < 0:
                print("Bill Decreased.")

            else:
                print("Bill Remained Same.")

        print("\nTotal Electricity Bill: Rs.",
              round(sum(b["total"] for b in bills), 2))

        print("\nAverage Monthly Bill: Rs.",
              round(sum(b["total"] for b in bills) / n, 2))


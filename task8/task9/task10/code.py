# Campus Event Financial Planning

print("CAMPUS EVENT FINANCIAL PLANNING")

# Input details
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Validate input
if (venue < 0 or equipment < 0 or transport < 0
        or catering < 0 or certificate < 0
        or participants <= 0 or sponsorship < 0):

    print("Invalid input! Enter valid positive values.")

else:
    # Calculate fixed and variable costs
    fixed_cost = venue + equipment + transport

    variable_cost = catering + certificate

    # Calculate total event cost
    total_cost = fixed_cost + (variable_cost * participants)

    # Calculate sponsorship shortfall
    shortfall = max(0, fixed_cost - sponsorship)

    # Calculate participant contribution
    remaining_cost = max(0, total_cost - sponsorship)

    contribution = remaining_cost / participants

    # Calculate break-even registrations
    if sponsorship >= fixed_cost:
        min_registrations = 0
    elif variable_cost == 0:
        min_registrations = 0
    else:
        min_registrations = 0  # No break-even if each participant
                               # contributes only the variable cost

    # Display results
    print("\n----- EVENT FINANCIAL REPORT -----")

    print("Fixed Cost:", fixed_cost)
    print("Variable Cost per Participant:", variable_cost)
    print("Total Event Cost:", total_cost)
    print("Sponsorship Amount:", sponsorship)
    print("Sponsorship Shortfall:", shortfall)

    print("Participant Contribution:",
          round(contribution, 2))

    # Break-even calculation
    if sponsorship >= fixed_cost:
        print("Minimum Registrations to Break Even: 0")
    elif variable_cost > 0:
        print("Minimum Registrations cannot be calculated")
        print("without knowing the registration fee.")

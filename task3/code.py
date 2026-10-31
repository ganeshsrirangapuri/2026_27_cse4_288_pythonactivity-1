
# Hospital Billing and Patient Classification System

print("======================================")
print("   HOSPITAL BILLING SYSTEM")
print("======================================")

try:
    # Patient details
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))

    # Enter hospital charges
    consultation = float(input("Enter Consultation Charges: "))
    diagnostic = float(input("Enter Diagnostic Charges: "))
    treatment = float(input("Enter Treatment Charges: "))

    # Insurance details
    insurance = input("Do you have Insurance? (yes/no): ").lower()

    # Validate inputs
    if name.strip() == "":
        print("Error: Patient name cannot be empty.")

    elif age <= 0:
        print("Error: Invalid patient age.")

    elif consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Error: Charges cannot be negative.")

    elif insurance not in ["yes", "no"]:
        print("Error: Invalid insurance option.")

    else:
        # Calculate total bill
        total = consultation + diagnostic + treatment

        # Calculate concession
        discount = 0
        reason = "No concession"

        if age >= 60 and insurance == "yes":
            discount = 10
            reason = "Senior Citizen Concession (10%)"

        elif age >= 60:
            discount = 10
            reason = "Senior Citizen Concession (10%)"

        elif insurance == "yes":
            discount = 5
            reason = "Insurance Concession (5%)"

        # Calculate final bill
        concession = total * discount / 100
        final_bill = total - concession

        # Patient classification
        if final_bill < 5000:
            category = "Low Payment"

        elif final_bill <= 15000:
            category = "Medium Payment"

        else:
            category = "High Payment"

        # Display billing details
        print("\n======================================")
        print("          HOSPITAL BILL")
        print("======================================")

        print("Patient Name       :", name)
        print("Patient Age        :", age)
        print("Consultation       : Rs.", consultation)
        print("Diagnostic         : Rs.", diagnostic)
        print("Treatment          : Rs.", treatment)

        print("--------------------------------------")
        print("Total Bill         : Rs.", total)
        print("Concession Reason  :", reason)
        print("Discount           :", discount, "%")
        print("Concession Amount  : Rs.", concession)
        print("--------------------------------------")

        print("Final Bill         : Rs.", final_bill)
        print("Patient Category   :", category)

        print("======================================")
        print("Thank you for visiting our hospital!")

except ValueError:
    print("Error: Please enter valid numeric values.")


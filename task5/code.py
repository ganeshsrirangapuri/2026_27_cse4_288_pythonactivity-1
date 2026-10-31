
# Multi-Plan Telecommunications Cost Optimization

print("==========================================")
print(" TELECOMMUNICATION PLAN OPTIMIZATION")
print("==========================================")

# Customer details
name = input("Enter Customer Name: ")

# Customer requirements
data_needed = float(input("Enter Required Data (GB): "))
calls_needed = int(input("Enter Required Call Minutes: "))
sms_needed = int(input("Enter Required SMS: "))
validity_needed = int(input("Enter Required Validity (Days): "))
budget = float(input("Enter Maximum Budget: Rs. "))

# Validate customer requirements
if (name.strip() == "" or data_needed < 0 or
    calls_needed < 0 or sms_needed < 0 or
    validity_needed <= 0 or budget < 0):

    print("\nInvalid Customer Requirements!")

else:

    # Excess usage rates
    data_rate = 10       # Rs. per extra GB
    call_rate = 0.50     # Rs. per extra minute
    sms_rate = 0.20      # Rs. per extra SMS

    # Number of plans
    n = int(input("\nEnter Number of Mobile Plans: "))

    if n <= 0:
        print("Invalid Number of Plans!")

    else:
        plans = []
        eligible_plans = []

        # Get plan details
        for i in range(n):

            print("\nEnter Details for Plan", i + 1)

            plan_name = input("Plan Name: ")
            price = float(input("Plan Price: Rs. "))
            data = float(input("Data Limit (GB): "))
            calls = int(input("Call Minutes: "))
            sms = int(input("SMS Limit: "))
            validity = int(input("Validity (Days): "))

            # Validate plan details
            if (plan_name.strip() == "" or price < 0 or
                data < 0 or calls < 0 or sms < 0 or
                validity <= 0):

                print("Invalid Plan Details! Re-enter this plan.")
                continue

            # Calculate excess usage
            extra_data = max(0, data_needed - data)
            extra_calls = max(0, calls_needed - calls)
            extra_sms = max(0, sms_needed - sms)

            # Calculate excess charges
            data_charge = extra_data * data_rate
            call_charge = extra_calls * call_rate
            sms_charge = extra_sms * sms_rate

            extra_charge = (
                data_charge + call_charge + sms_charge
            )

            # Calculate total cost
            total_cost = price + extra_charge

            # Check eligibility
            eligible = (
                data >= data_needed and
                calls >= calls_needed and
                sms >= sms_needed and
                validity >= validity_needed and
                total_cost <= budget
            )

            plan = {
                "name": plan_name,
                "price": price,
                "data": data,
                "calls": calls,
                "sms": sms,
                "validity": validity,
                "extra": extra_charge,
                "total": total_cost,
                "eligible": eligible
            }

            plans.append(plan)

            if eligible:
                eligible_plans.append(plan)

        # Display plan comparison
        print("\n==========================================")
        print("          MOBILE PLAN COMPARISON")
        print("==========================================")

        for p in plans:
            print("\nPlan Name       :", p["name"])
            print("Base Price      : Rs.", p["price"])
            print("Excess Charges  : Rs.", p["extra"])
            print("Total Cost      : Rs.", p["total"])

            if p["eligible"]:
                print("Status          : Eligible")
            else:
                print("Status          : Not Eligible")

        # Find the most economical plan
        if eligible_plans:

            best_plan = min(
                eligible_plans,
                key=lambda x: x["total"]
            )

            print("\n==========================================")
            print("       MOST ECONOMICAL MOBILE PLAN")
            print("==========================================")

            print("Customer Name   :", name)
            print("Plan Name       :", best_plan["name"])
            print("Plan Price      : Rs.", best_plan["price"])
            print("Excess Charges  : Rs.", best_plan["extra"])
            print("Total Cost      : Rs.", best_plan["total"])
            print("Validity        :", best_plan["validity"], "Days")
            print("Budget          : Rs.", budget)

            print("------------------------------------------")
            print("Recommended Plan:", best_plan["name"])
            print("==========================================")

        else:
            print("\nNo Eligible Mobile Plan Found!")
            print("Please increase your budget or")
            print("choose different usage requirements.")


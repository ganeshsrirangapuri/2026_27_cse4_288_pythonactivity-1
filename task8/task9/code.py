
# Multi-Currency Travel Budget Analysis

print("==========================================")
print(" MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
print("==========================================")

# Traveller details
name = input("Enter Traveller Name: ")

budget = float(
    input("Enter Total Travel Budget (INR): Rs. ")
)

n = int(input("Enter Number of Expense Categories: "))

# Validate basic inputs
if name.strip() == "" or budget < 0 or n <= 0:

    print("\nInvalid Traveller Details or Budget!")

else:

    expenses = []
    total_expense = 0

    # Enter expense details
    for i in range(n):

        print("\nEnter Expense", i + 1, "Details")

        category = input("Expense Category: ")
        currency = input("Currency Code: ").upper()

        amount = float(
            input("Enter Expense Amount: ")
        )

        exchange_rate = float(
            input("Enter Exchange Rate (INR): ")
        )

        fee_percent = float(
            input("Enter Conversion Fee Percentage: ")
        )

        # Validate expense details
        if (category.strip() == "" or
            amount < 0 or
            exchange_rate <= 0 or
            fee_percent < 0):

            print("Invalid Expense Details!")
            continue

        # Convert foreign currency into INR
        converted_amount = amount * exchange_rate

        # Calculate conversion fee
        conversion_fee = (
            converted_amount * fee_percent / 100
        )

        # Calculate total expense
        final_amount = converted_amount + conversion_fee

        total_expense += final_amount

        # Store expense details
        expenses.append({
            "category": category,
            "currency": currency,
            "amount": amount,
            "rate": exchange_rate,
            "converted": converted_amount,
            "fee": conversion_fee,
            "total": final_amount
        })

    # Generate report
    if expenses:

        # Identify largest expense category
        largest_expense = max(
            expenses,
            key=lambda x: x["total"]
        )

        # Calculate budget balance
        balance = budget - total_expense

        print("\n==========================================")
        print("       TRAVEL EXPENSE REPORT")
        print("==========================================")

        print("Traveller Name :", name)
        print("Travel Budget  : Rs.", round(budget, 2))

        print("------------------------------------------")

        for e in expenses:

            print("\nExpense Category :", e["category"])
            print("Currency         :", e["currency"])
            print("Original Amount  :", e["amount"])
            print("Exchange Rate    :", e["rate"])
            print("Converted Amount: Rs.",
                  round(e["converted"], 2))
            print("Conversion Fee   : Rs.",
                  round(e["fee"], 2))
            print("Total Expense    : Rs.",
                  round(e["total"], 2))

        print("\n------------------------------------------")

        print("Total Expenditure: Rs.",
              round(total_expense, 2))

        print("Largest Expense  :",
              largest_expense["category"])

        print("Largest Amount   : Rs.",
              round(largest_expense["total"], 2))

        print("------------------------------------------")

        # Check budget status
        if balance > 0:

            print("Budget Status   : Within Budget")
            print("Remaining Budget: Rs.",
                  round(balance, 2))

        elif balance == 0:

            print("Budget Status   : Budget Fully Utilized")
            print("Remaining Budget: Rs. 0")

        else:

            print("Budget Status   : Budget Exceeded")
            print("Extra Spending  : Rs.",
                  round(abs(balance), 2))

        print("==========================================")
        print("       ANALYSIS COMPLETED")
        print("==========================================")

    else:

        print("\nNo Valid Expenses Entered!")


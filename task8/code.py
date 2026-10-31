
# Manufacturing Cost and Profitability Analysis

print("==========================================")
print(" MANUFACTURING COST ANALYSIS SYSTEM")
print("==========================================")

# Product details
product = input("Enter Product Name: ")

quantity = int(input("Enter Production Quantity: "))

# Cost details
material_rate = float(
    input("Enter Material Cost per Unit: Rs. ")
)

labour_rate = float(
    input("Enter Labour Cost per Unit: Rs. ")
)

wastage_percent = float(
    input("Enter Wastage Percentage: ")
)

machine_rate = float(
    input("Enter Machine Cost per Unit: Rs. ")
)

selling_price = float(
    input("Enter Selling Price per Unit: Rs. ")
)

target_profit = float(
    input("Enter Target Profit Percentage: ")
)

# Validate inputs
if (product.strip() == "" or quantity <= 0 or
    material_rate < 0 or labour_rate < 0 or
    wastage_percent < 0 or wastage_percent > 100 or
    machine_rate < 0 or selling_price < 0 or
    target_profit < 0):

    print("\nInvalid Production or Cost Details!")

else:

    # Calculate material cost
    material_cost = material_rate * quantity

    # Calculate labour cost
    labour_cost = labour_rate * quantity

    # Calculate wastage cost
    wastage_cost = material_cost * wastage_percent / 100

    # Calculate machine cost
    machine_cost = machine_rate * quantity

    # Calculate total manufacturing cost
    total_cost = (
        material_cost +
        labour_cost +
        wastage_cost +
        machine_cost
    )

    # Calculate sales revenue
    revenue = selling_price * quantity

    # Calculate profit or loss
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0

    # Check profit target
    if profit >= 0 and profit_percent >= target_profit:
        status = "Profit Target Achieved"

    elif profit > 0:
        status = "Profit Target Not Achieved"

    elif profit == 0:
        status = "No Profit No Loss"

    else:
        status = "Production Resulted in Loss"

    # Display manufacturing report
    print("\n==========================================")
    print("       MANUFACTURING COST REPORT")
    print("==========================================")

    print("Product Name          :", product)
    print("Production Quantity   :", quantity)

    print("------------------------------------------")
    print("Material Cost         : Rs.", material_cost)
    print("Labour Cost           : Rs.", labour_cost)
    print("Wastage Cost          : Rs.", wastage_cost)
    print("Machine Cost          : Rs.", machine_cost)

    print("------------------------------------------")
    print("Total Manufacturing Cost: Rs.", total_cost)
    print("Selling Price per Unit : Rs.", selling_price)
    print("Total Sales Revenue    : Rs.", revenue)

    print("------------------------------------------")
    print("Profit / Loss         : Rs.", profit)
    print("Profit Percentage     :", round(profit_percent, 2), "%")
    print("Target Profit         :", target_profit, "%")

    print("------------------------------------------")
    print("Production Status     :", status)

    print("==========================================")
    print("       ANALYSIS COMPLETED")
    print("==========================================")


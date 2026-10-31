
# Retail Billing with Multiple Discount Rules

print("==========================================")
print("       RETAIL BILLING MANAGEMENT")
print("==========================================")

# Customer details
customer = input("Enter Customer Name: ")

# Number of products
n = int(input("Enter Number of Products: "))

# Category tax rates
tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "groceries": 3,
    "furniture": 12
}

products = []

subtotal = 0
total_tax = 0

# Validate customer and product count
if customer.strip() == "" or n <= 0:
    print("\nInvalid Customer Details or Product Count!")

else:

    # Enter product details
    for i in range(n):

        print("\nEnter Product", i + 1, "Details")

        name = input("Product Name: ")
        category = input("Category: ").lower()
        price = float(input("Product Price: Rs. "))
        quantity = int(input("Quantity: "))

        # Validate product details
        if (name.strip() == "" or
            category not in tax_rates or
            price < 0 or quantity <= 0):

            print("Invalid Product Details!")
            continue

        # Calculate product subtotal
        item_total = price * quantity

        # Calculate category-specific tax
        tax_rate = tax_rates[category]
        tax = item_total * tax_rate / 100

        # Calculate product total
        product_total = item_total + tax

        subtotal += item_total
        total_tax += tax

        products.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "subtotal": item_total,
            "tax_rate": tax_rate,
            "tax": tax,
            "total": product_total
        })

    # Calculate threshold discount
    if subtotal > 20000:
        discount_rate = 15

    elif subtotal > 10000:
        discount_rate = 10

    elif subtotal > 5000:
        discount_rate = 5

    else:
        discount_rate = 0

    # Calculate discount
    discount = subtotal * discount_rate / 100

    # Apply maximum discount limit
    maximum_discount = 2000

    if discount > maximum_discount:
        discount = maximum_discount

    # Calculate final bill
    final_bill = subtotal + total_tax - discount

    # Display invoice
    if products:

        print("\n==========================================")
        print("              RETAIL INVOICE")
        print("==========================================")

        print("Customer Name:", customer)

        print("------------------------------------------")
        print("Product      Category      Qty    Amount")
        print("------------------------------------------")

        for p in products:

            print(
                p["name"], " ",
                p["category"], " ",
                p["quantity"], " ",
                "Rs.", p["subtotal"]
            )

        print("------------------------------------------")

        print("Subtotal          : Rs.", round(subtotal, 2))
        print("Total Tax         : Rs.", round(total_tax, 2))
        print("Discount Rate     :", discount_rate, "%")
        print("Discount Amount   : Rs.", round(discount, 2))
        print("Maximum Discount  : Rs.", maximum_discount)

        print("------------------------------------------")

        print("FINAL BILL        : Rs.", round(final_bill, 2))

        print("==========================================")
        print("        THANK YOU FOR SHOPPING!")
        print("==========================================")

    else:
        print("\nNo Valid Products Entered!")

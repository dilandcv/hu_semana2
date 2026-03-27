# List to store all products
inventory = []

# Control variable for the main loop
loop = True


# -------------------------------
# FUNCTION: ADD PRODUCT
# -------------------------------
def add_product():
    name = input("Enter product name: ")

    # Validate price
    valid_price = False
    while valid_price == False:
        try:
            price = float(input("Enter price: "))
            if price < 0:
                print("Price cannot be negative.")
            else:
                valid_price = True
        except:
            print("Invalid input. Enter a number.")

    # Validate quantity
    valid_quantity = False
    while valid_quantity == False:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                valid_quantity = True
        except:
            print("Invalid input. Enter an integer.")

    # Create product as a dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add product to inventory list
    inventory.append(product)

    print("Product added successfully.\n")


# -------------------------------
# FUNCTION: SHOW INVENTORY
# -------------------------------
def show_inventory():
    # Check if inventory is empty
    if len(inventory) == 0:
        print("Inventory is empty.\n")
    else:
        print("\n--- INVENTORY ---")
        # Loop through each product
        for product in inventory:
            print("Product:", product["name"],
                  "| Price:", product["price"],
                  "| Quantity:", product["quantity"])
        print()


# -------------------------------
# FUNCTION: CALCULATE STATISTICS
# -------------------------------
def calculate_statistics():
    # Check if inventory is empty
    if len(inventory) == 0:
        print("No products available.\n")
        return

    total_value = 0
    total_quantity = 0

    # Loop to calculate totals
    for product in inventory:
        total_value += product["price"] * product["quantity"]
        total_quantity += product["quantity"]

    print("\n--- STATISTICS ---")
    print("Total inventory value:", total_value)
    print("Total number of products:", total_quantity)
    print()


# -------------------------------
# MAIN MENU LOOP
# -------------------------------
while loop:
    print("=== MENU ===")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Choose an option: ")

    # Conditional structure to handle options
    if option == "1":
        add_product()

    elif option == "2":
        show_inventory()

    elif option == "3":
        calculate_statistics()

    elif option == "4":
        print("Exiting program...")
        # Change control variable to stop the loop
        loop = False

    else:
        print("Invalid option. Try again.\n")

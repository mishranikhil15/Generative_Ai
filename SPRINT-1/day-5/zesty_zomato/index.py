menu = []       # List to store dishes
orders = {}     # Dictionary to store orders
order_count = 1 # Counter for generating order IDs

def add_dish():
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    price = float(input("Enter price: "))
    availability = input("Is the dish available? (yes/no): ")

    dish = {
        "dish_id": dish_id,
        "dish_name": dish_name,
        "price": price,
        "availability": availability.lower() == "yes"
    }

    menu.append(dish)
    print("Dish added to the menu.")

def remove_dish():
    dish_id = input("Enter the dish ID to remove: ")

    for dish in menu:
        if dish["dish_id"] == dish_id:
            menu.remove(dish)
            print("Dish removed from the menu.")
            break
    else:
        print("Dish not found in the menu.")

def update_availability():
    dish_id = input("Enter the dish ID to update availability: ")

    for dish in menu:
        if dish["dish_id"] == dish_id:
            availability = input("Is the dish available now? (yes/no): ")
            dish["availability"] = availability.lower() == "yes"
            print("Availability updated.")
            break
    else:
        print("Dish not found in the menu.")

def take_order():
    global order_count
    customer_name = input("Enter customer name: ")
    order_items = input("Enter dish IDs (comma-separated): ").split(",")

    items_available = []
    items_unavailable = []
    for item in order_items:
        item = item.strip()
        for dish in menu:
            if dish["dish_id"] == item and dish["availability"]:
                items_available.append(dish)
                break
        else:
            items_unavailable.append(item)

    if items_unavailable:
        print(f"The following dishes are unavailable: {', '.join(items_unavailable)}")
        return

    order_id = order_count
    order_count += 1
    order = {
        "customer_name": customer_name,
        "order_items": items_available,
        "status": "received"
    }
    orders[order_id] = order
    print(f"Order placed successfully. Order ID: {order_id}")

def update_order_status():
    order_id = int(input("Enter the order ID: "))

    if order_id in orders:
        status = input("Enter the new order status: ")
        orders[order_id]["status"] = status
        print("Order status updated.")
    else:
        print("Order not found.")

def review_orders():
    for order_id, order in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Customer Name: {order['customer_name']}")
        print("Order Items:")
        for dish in order["order_items"]:
            print(f"- {dish['dish_name']}")
        print(f"Status: {order['status']}")
        print()

def exit_system():
    print("Exiting the system. Have a nice day!")
    exit()

def main():
    while True:
        print("===== Zesty Zomato Menu Management =====")
        print("1. Add Dish")
        print("2. Remove Dish")
        print("3. Update Dish Availability")
        print("4. Take Order")
        print("5. Update Order Status")
        print("6. Review Orders")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        try:
            choice = int(choice)
            if choice == 1:
                add_dish()
            elif choice == 2:
                remove_dish()
            elif choice == 3:
                update_availability()
            elif choice == 4:
                take_order()
            elif choice == 5:
                update_order_status()
            elif choice == 6:
                review_orders()
            elif choice == 7:
                exit_system()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

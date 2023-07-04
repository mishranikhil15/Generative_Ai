class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability


class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack):
        self.inventory.append(snack)
        print(f"Snack '{snack.name}' added to the inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print(f"Snack '{snack.name}' removed from the inventory.")
                return
        print("Snack not found in the inventory.")

    def update_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print(f"Availability of snack '{snack.name}' updated to {availability}.")
                return
        print("Snack not found in the inventory.")

    def record_sale(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    self.sales_records.append(snack)
                    snack.availability = "no"
                    print(f"Snack '{snack.name}' sold.")
                    return
                else:
                    print(f"Snack '{snack.name}' is not available for sale.")
                    return
        print("Snack not found in the inventory.")

    def display_inventory(self):
        print("\nCurrent Snack Inventory:")
        if self.inventory:
            for snack in self.inventory:
                print(f"ID: {snack.snack_id}, Name: {snack.name}, Price: {snack.price}, "
                      f"Availability: {snack.availability}")
        else:
            print("Inventory is empty.")

    def display_sales_records(self):
        print("\nSales Records:")
        if self.sales_records:
            for snack in self.sales_records:
                print(f"ID: {snack.snack_id}, Name: {snack.name}, Price: {snack.price}")
        else:
            print("No sales records found.")


# Creating a canteen object
canteen = Canteen()

# Menu loop
while True:
    print("\n---------- Canteen Management System ----------")
    print("1. Add Snack to Inventory")
    print("2. Remove Snack from Inventory")
    print("3. Update Snack Availability")
    print("4. Record Snack Sale")
    print("5. Display Snack Inventory")
    print("6. Display Sales Records")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        snack_id = input("Enter snack ID: ")
        name = input("Enter snack name: ")
        price = input("Enter snack price: ")
        availability = input("Is the snack available? (yes/no): ")
        canteen.add_snack(Snack(snack_id, name, price, availability))
    elif choice == "2":
        snack_id = input("Enter snack ID to remove: ")
        canteen.remove_snack(snack_id)
    elif choice == "3":
        snack_id = input("Enter snack ID to update availability: ")
        availability = input("Is the snack available now? (yes/no): ")
        canteen.update_availability(snack_id, availability)
    elif choice == "4":
        snack_id = input("Enter snack ID sold: ")
        canteen.record_sale(snack_id)
    elif choice == "5":
        canteen.display_inventory()
    elif choice == "6":
        canteen.display_sales_records()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# Delicious-Taste
Delicious food ordering platform.

# S2 D1 - Live Project(In Class)

## **Project: "Zomato Chronicles: The Great Food Fiasco" with Flask**

Once upon a time in the bustling city of Mumbai, there was a newly opened restaurant, "Zesty Zomato", that was swiftly gaining popularity. To further improve their services, they decided to digitize their operations. You, as a brilliant Flask developer, have been hired to create a Flask web application to help Zesty Zomato manage its food delivery service more effectively and efficiently.

**Objective:** Your goal is to use Flask, along with Python's core concepts like conditional statements, loops, lists, and dictionaries, to develop a robust and interactive web application to help Zesty Zomato in its quest for delivering culinary delights to its eager customers.

### **Key Features:**

1. **Menu Mastery**: Your web application should enable Zesty Zomato to manage its mouth-watering menu of dishes. Each dish will have unique attributes, such as dish ID, dish name, price, and availability (yes or no). You can use Flask routes to implement CRUD operations for the dishes.
2. **User Interaction Euphoria**: Zesty Zomato staff should be able to perform the following tasks through the web application:
    - Add a delicious new dish to the menu.
    - Remove a dish that is no longer served.
    - Update the availability of a dish based on their dynamic kitchen operations.
    - Take a new order from a ravenous customer.
    - Update the status of an order as it goes from 'received' to 'preparing', then 'ready for pickup' and finally 'delivered'.
    - Review all the orders to ensure everything is going as per plan.
    - An exit option to wind up the day's operations.
3. **Taking Orders**: When a customer places an order, Zesty Zomato staff should be able to enter the customer's name and the dish IDs. The web application should check whether each dish is available. If so, it should process the order, assigning a unique order ID and setting the initial order status as 'received'.
4. **Order Updates**: When the status of the order changes, staff should be able to enter the unique order ID and update the new status.
5. **Edge Case Excellence**: The web application should be smart enough to handle invalid inputs and edge cases, such as ordering a dish that doesn't exist or isn't available.

### **Extra Adventures:**

For those who finish early or are seeking an extra challenge, consider adding these advanced features:

1. **Price Calculation**: The web application should also calculate and display the total price of each order based on the price of each ordered dish.
2. **Status Filter**: Add an option to view only the orders with a certain status (e.g., only the 'ready for pickup' orders).
3. **Data Persistence**: To keep track of the culinary journey, the web application should save the menu and order data to a file and load it when the system starts, ensuring data persists across multiple system usages. Consider using Flask sessions or cookies for this purpose.

### **Ensure the following points during implementation :**

1. **Functionality**: Does the web application behave as expected, adhering to the requirements, and helping Zesty Zomato manage its operations effectively?
2. **Code Style**: Is the code well-structured into functions and Flask routes? Is the code easy to read and understand, just like a well-presented dish?
3. **Robustness**: Like a versatile chef, does the web application handle unexpected or invalid user input gracefully, ensuring the operations run smoothly?

The culinary world of Zesty Zomato is waiting for your Flask web application. Unleash your Flask skills to create an efficient system that will keep the taste buds of Mumbai satiated. Good luck!

document.addEventListener('DOMContentLoaded', () => {
    const menuList = document.getElementById('menu-list');
    const ordersList = document.getElementById('orders-list');
    const addDishForm = document.getElementById('add-dish-form');
    const placeOrderForm = document.getElementById('place-order-form');
    const updateOrderForm = document.getElementById('update-order-form');

    // Function to fetch menu items from the backend
    const fetchMenu = () => {
        fetch('http://127.0.0.1:5000/menu')
            .then(response => response.json())
            .then(menuItems => {
                menuList.innerHTML = '';
                menuItems.forEach(menuItem => {
                    const li = document.createElement('li');
                    li.textContent = `${menuItem.dish_name} - $${menuItem.price} (Availability: ${menuItem.availability})`;
                    menuList.appendChild(li);

                    // Populate dish IDs in the place order form
                    const option = document.createElement('option');
                    option.value = menuItem.dish_id;
                    option.textContent = menuItem.dish_name;
                    document.getElementById('dish-ids').appendChild(option);
                });
            })
            .catch(error => console.error('Error:', error));
    };

    // Function to fetch orders from the backend
    const fetchOrders = () => {
        fetch('http://127.0.0.1:5000/orders')
            .then(response => response.json())
            .then(orders => {
                ordersList.innerHTML = '';
                orders.forEach(order => {
                    const li = document.createElement('li');
                    li.textContent = `Order ID: ${order.order_id}, Customer Name: ${order.customer_name}, Status: ${order.status}`;
                    ordersList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    };

    // Fetch initial menu and orders
    fetchMenu();
    fetchOrders();

    // Handle add dish form submission
    addDishForm.addEventListener('submit', event => {
        event.preventDefault();

        const dishIdInput = document.getElementById('dish-id');
        const dishNameInput = document.getElementById('dish-name');
        const priceInput = document.getElementById('price');
        const availabilitySelect = document.getElementById('availability');

        const dish = {
            dish_id: dishIdInput.value,
            dish_name: dishNameInput.value,
            price: parseFloat(priceInput.value),
            availability: availabilitySelect.value
        };

        fetch('http://127.0.0.1:5000/menu', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dish)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // Refresh the menu to show the updated list
                dishIdInput.value = '';
                dishNameInput.value = '';
                priceInput.value = '';
                availabilitySelect.value = 'yes';
                fetchMenu();
            })
            .catch(error => console.error('Error:', error));
    });

    // Handle place order form submission
    placeOrderForm.addEventListener('submit', event => {
        event.preventDefault();

        const customerNameInput = document.getElementById('customer-name');
        const dishIdsSelect = document.getElementById('dish-ids');

        const order = {
            customer_name: customerNameInput.value,
            dish_ids: Array.from(dishIdsSelect.selectedOptions, option => option.value)
        };

        fetch('http://127.0.0.1:5000/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(order)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // Refresh the orders list to show the updated order
                customerNameInput.value = '';
                dishIdsSelect.selectedIndex = -1;
                fetchOrders();
            })
            .catch(error => console.error('Error:', error));
    });

    // Handle update order form submission
    updateOrderForm.addEventListener('submit', event => {
        event.preventDefault();

        const orderIdInput = document.getElementById('order-id');
        const statusSelect = document.getElementById('status');

        const updatedOrder = {
            status: statusSelect.value
        };

        fetch(`http://127.0.0.1:5000/order/${orderIdInput.value}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedOrder)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // Refresh the orders list to show the updated order status
                orderIdInput.value = '';
                statusSelect.value = 'received';
                fetchOrders();
            })
            .catch(error => console.error('Error:', error));
    });
});

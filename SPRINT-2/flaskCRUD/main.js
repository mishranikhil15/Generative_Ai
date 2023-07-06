document.addEventListener('DOMContentLoaded', function() {
    const createForm = document.getElementById('create-form');
    const editForm = document.getElementById('edit-form');
    const contactsList = document.getElementById('contacts');
    const editModal = document.getElementById('edit-modal');
    const editModalCloseBtn = editModal.querySelector('.close');
    const editModalIndexInput = document.getElementById('edit-index');
    const editModalNameInput = document.getElementById('edit-name');
    const editModalEmailInput = document.getElementById('edit-email');
    const editModalPhoneInput = document.getElementById('edit-phone');

    // Add event listener for create form submission
    createForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(createForm);
        const contact = {
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone')
        };

        fetch('/api/contacts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(contact)
        })
        .then(response => response.json())
        .then(data => {
            const newContact = {
                name: data.name,
                email: data.email,
                phone: data.phone
            };
            appendContact(newContact);
            createForm.reset();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Add event listeners for edit and delete buttons
    contactsList.addEventListener('click', function(event) {
        if (event.target.classList.contains('edit-btn')) {
            const index = event.target.dataset.index;
            const contact = JSON.parse(contactsList.querySelector(`li:nth-child(${parseInt(index) + 1})`).dataset.contact);
            openEditModal(contact, index);
        } else if (event.target.classList.contains('delete-btn')) {
            const index = event.target.dataset.index;
            deleteContact(index);
        }
    });

    // Add event listener for edit form submission
    editForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(editForm);
        const index = editModalIndexInput.value;
        const contact = {
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone')
        };

        fetch(`/api/contacts/${index}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(contact)
        })
        .then(response => response.json())
        .then(data => {
            const updatedContact = {
               name: data.name,
                email: data.email,
                phone: data.phone
            };
            updateContact(updatedContact, index);
            closeModal();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Add event listener for closing the edit modal
    editModalCloseBtn.addEventListener('click', function() {
        closeModal();
    });

    // Helper function to append a contact to the contacts list
    function appendContact(contact) {
        const li = document.createElement('li');
        li.dataset.contact = JSON.stringify(contact);
        li.innerHTML = `
            <span class="contact-name">${contact.name}</span>
            <span class="contact-email">${contact.email}</span>
            <span class="contact-phone">${contact.phone}</span>
            <span class="contact-actions">
                <button class="edit-btn" data-index="${contactsList.children.length}">Edit</button>
                <button class="delete-btn" data-index="${contactsList.children.length}">Delete</button>
            </span>
        `;
        contactsList.appendChild(li);
    }

    // Helper function to update a contact in the contacts list
    function updateContact(contact, index) {
        const li = contactsList.querySelector(`li:nth-child(${parseInt(index) + 1})`);
        li.dataset.contact = JSON.stringify(contact);
        li.querySelector('.contact-name').textContent = contact.name;
        li.querySelector('.contact-email').textContent = contact.email;
        li.querySelector('.contact-phone').textContent = contact.phone;
    }

    // Helper function to delete a contact from the contacts list
    function deleteContact(index) {
        fetch(`/api/contacts/${index}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            contactsList.removeChild(contactsList.querySelector(`li:nth-child(${parseInt(index) + 1})`));
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Helper function to open the edit modal with the contact details
    function openEditModal(contact, index) {
        editModalIndexInput.value = index;
        editModalNameInput.value = contact.name;
        editModalEmailInput.value = contact.email;
        editModalPhoneInput.value = contact.phone;
        editModal.style.display = 'block';
    }

    // Helper function to close the edit modal
    function closeModal() {
        editModal.style.display = 'none';
        editForm.reset();
    }
});

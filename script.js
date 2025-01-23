// JavaScript to handle login form submission
const loginForm = document.getElementById('login-form');

// Replace this with your Render backend URL
const backendBaseUrl = 'https://expense-tracker-tjr9.onrender.com';

loginForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'admin' && password === 'password') {
        alert('Login successful!');

        // Example of sending an expense to the backend
        const expense = {
            date: '2025-01-23',
            amount: 50.75,
            category: 'Food',
            description: 'Groceries'
        };

        try {
            const response = await fetch(`${backendBaseUrl}/add_expense`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(expense)
            });

            if (response.ok) {
                const result = await response.json();
                alert(result.message);
            } else {
                alert('Failed to add expense. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error communicating with the backend.');
        }
    } else {
        alert('Invalid credentials. Please try again.');
    }
});

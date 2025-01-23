const loginForm = document.getElementById('login-form');
const loginContainer = document.getElementById('login-container');
const dashboardContainer = document.getElementById('dashboard-container');
const totalExpensesEl = document.getElementById('total-expenses');
const categoryListEl = document.getElementById('category-list');

const backendBaseUrl = 'http://127.0.0.1:5000'; // Adjust if hosted elsewhere

// Handle login form submission
loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch(`${backendBaseUrl}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            alert('Login successful!');
            showDashboard(); // Fetch expenses and show the dashboard
        } else {
            const error = await response.json();
            alert(error.message || 'Invalid credentials. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error connecting to the server. Please try again later.');
    }
});

// Show dashboard and fetch expense stats
async function showDashboard() {
    loginContainer.style.display = 'none';
    dashboardContainer.style.display = 'block';

    try {
        const response = await fetch(`${backendBaseUrl}/expenses`);
        if (response.ok) {
            const expenses = await response.json();
            displayStats(expenses);
        } else {
            alert('Failed to fetch expenses.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error fetching expenses from the backend.');
    }
}

// Display expense stats
function displayStats(expenses) {
    const total = expenses.reduce((sum, expense) => sum + expense[1], 0); // Assuming amount is at index 1
    totalExpensesEl.textContent = total.toFixed(2);

    const categoryTotals = {};
    expenses.forEach(expense => {
        const category = expense[2]; // Assuming category is at index 2
        categoryTotals[category] = (categoryTotals[category] || 0) + expense[1];
    });

    categoryListEl.innerHTML = '';
    for (const [category, total] of Object.entries(categoryTotals)) {
        const li = document.createElement('li');
        li.textContent = `${category}: $${total.toFixed(2)}`;
        categoryListEl.appendChild(li);
    }
}

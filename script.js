const loginForm = document.getElementById('login-form');
const loginContainer = document.getElementById('login-container');
const dashboardContainer = document.getElementById('dashboard-container');
const totalExpensesEl = document.getElementById('total-expenses');
const categoryListEl = document.getElementById('category-list');

const backendBaseUrl = 'https://expense-tracker-tjr9.onrender.com';

// Show dashboard and fetch stats after successful login
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
    const total = expenses.reduce((sum, expense) => sum + expense[2], 0); // Assuming amount is at index 2
    totalExpensesEl.textContent = total.toFixed(2);

    const categoryTotals = {};
    expenses.forEach(expense => {
        const category = expense[3]; // Assuming category is at index 3
        categoryTotals[category] = (categoryTotals[category] || 0) + expense[2];
    });

    categoryListEl.innerHTML = '';
    for (const [category, total] of Object.entries(categoryTotals)) {
        const li = document.createElement('li');
        li.textContent = `${category}: $${total.toFixed(2)}`;
        categoryListEl.appendChild(li);
    }
}

// Handle login form submission
loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'Jennifer' && password === '330316') {
        alert('Login successful!');
        showDashboard();
    } else {
        alert('Invalid credentials. Please try again.');
    }
});

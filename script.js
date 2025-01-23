// JavaScript to handle login form submission
const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'admin' && password === 'password') {
        alert('Login successful!');
    } else {
        alert('Invalid credentials. Please try again.');
    }
});

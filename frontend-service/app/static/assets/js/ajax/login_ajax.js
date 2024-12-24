document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const errorMessage = document.getElementById('error-message');

    loginBtn.addEventListener('click', function () {
        const nic = document.getElementById('nic').value;
        const password = document.getElementById('password').value;

        fetch('/validate-login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nic, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                errorMessage.style.display = 'none';
                errorMessage.textContent = '';
                window.location.href = '/dashboard';
            } else {
                errorMessage.style.display = 'block';
                errorMessage.textContent = data.error || 'Invalid credentials';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.style.display = 'block';
            errorMessage.textContent = 'An unexpected error occurred. Please try again.';
        });
    });
});

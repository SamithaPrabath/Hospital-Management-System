document.addEventListener('DOMContentLoaded', function () {
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.addEventListener('click', function () {
        errorMessage.style.display = 'none';
        errorMessage.textContent = '';

        const staff_id = document.getElementById('staff_id').value;
        const current_password = document.getElementById('current_password').value;
        const new_password = document.getElementById('new_password').value;
        const confirm_password = document.getElementById('confirm_password').value;

        if (!current_password || !new_password || !confirm_password) {
            errorMessage.textContent = 'All fields are required.';
            errorMessage.style.display = 'block';
            return;
        }

        if (new_password !== confirm_password) {
            errorMessage.textContent = 'New Password and Confirm Password do not match.';
            errorMessage.style.display = 'block';
            return;
        }

        fetch('/dashboard/change-password', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ staff_id, current_password, new_password })
        })
        .then(updateResponse => updateResponse.json())
        .then(updateData => {
                    if (updateData.success) {
                        alert('Password update successfully!');
                        window.location.href = '/receptionist/view-staff-members'
                    } else {
                        errorMessage.textContent = createData.message || 'Failed to update password';
                        errorMessage.style.display = 'block';
                    }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.style.display = 'block';
            errorMessage.textContent = 'An unexpected error occurred. Please try again.';
        });
    });
});
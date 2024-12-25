document.addEventListener('DOMContentLoaded', function () {
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.addEventListener('click', function () {
        errorMessage.style.display = 'none';
        errorMessage.textContent = '';

        const name = document.getElementById('name').value;
        const nic = document.getElementById('nic').value;
        const role_id = roleSelect.value;
        const specialization_id = specializationSelect.value;
        const address = document.getElementById('address').value;
        const phone_number_1 = document.getElementById('phone_number_1').value;
        const phone_number_2 = document.getElementById('phone_number_2').value;
        const registered_by = document.getElementById('registered_by').value;
        const password = document.getElementById('password').value;
        const confirm_password = document.getElementById('confirm_password').value;

        // Input validation
        if (!name || !nic || !address || !registered_by || !password || !confirm_password) {
            errorMessage.textContent = 'All fields are required.';
            errorMessage.style.display = 'block';
            return;
        }

        if (password !== confirm_password) {
            errorMessage.textContent = 'Password and Confirm Password do not match.';
            errorMessage.style.display = 'block';
            return;
        }

        if (roleSelect.options[roleSelect.selectedIndex].text.toLowerCase() === "doctor" && !specialization_id) {
            errorMessage.textContent = 'Specialization is required for doctors.';
            errorMessage.style.display = 'block';
            return;
        }

        fetch('/receptionist/create-staff', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, nic, role_id, specialization_id, address, phone_number_1, phone_number_2, registered_by, password })
        })
        .then(createResponse => createResponse.json())
        .then(createData => {
                    if (createData.success) {
                        alert('Staff created successfully!');
                        window.location.href = '/receptionist/view-staff-members'
                    } else {
                        errorMessage.textContent = createData.message || 'Failed to create staff.';
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
document.addEventListener('DOMContentLoaded', function () {
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.addEventListener('click', function () {
        errorMessage.style.display = 'none';
        errorMessage.textContent = '';

        const name = document.getElementById('name').value;
        const nic = document.getElementById('nic').value;
        const age = document.getElementById('age').value;
        const address = document.getElementById('address').value;
        const phone_number_1 = document.getElementById('phone_number_1').value;
        const phone_number_2 = document.getElementById('phone_number_2').value;
        const registered_by = document.getElementById('registered_by').value;

        // Input validation
        if (!name || !nic || !age || !address) {
            errorMessage.textContent = 'All fields are required.';
            errorMessage.style.display = 'block';
            return;
        }

        fetch('/receptionist/create-patient', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, nic, age, address, phone_number_1, phone_number_2, registered_by })
        })
        .then(createResponse => createResponse.json())
        .then(createData => {
                    if (createData.success) {
                        alert('Patient created successfully!');
//                        window.location.href = '/receptionist/view-staff-members'
                    } else {
                        errorMessage.textContent = createData.message || 'Failed to create patient.';
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
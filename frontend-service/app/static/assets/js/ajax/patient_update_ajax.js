document.addEventListener('DOMContentLoaded', function () {
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.addEventListener('click', function () {
        errorMessage.style.display = 'none';
        errorMessage.textContent = '';

        const patient_id = document.getElementById('patient_id').value;
        const name = document.getElementById('name').value;
        const nic = document.getElementById('nic').value;
        const age = document.getElementById('age').value;
        const address = document.getElementById('address').value;
        const phone_number_1 = document.getElementById('phone_number_1').value;
        const phone_number_2 = document.getElementById('phone_number_2').value;
        const registered_by = document.getElementById('registered_by').value;
        const registered_date = document.getElementById('registered_date').value;

        // Input validation
        if (!name || !nic || !address || !age || !registered_by) {
            errorMessage.textContent = 'All fields are required.';
            errorMessage.style.display = 'block';
            return;
        }

        fetch('/receptionist/update-patient', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ patient_id, name, nic, age, address, phone_number_1, phone_number_2, registered_by, registered_date })
        })
        .then(updateResponse => updateResponse.json())
        .then(updateData => {
                    if (updateData.success) {
                        alert('Patient updated successfully!');
                        window.location.href = '/receptionist/view-patients'
                    } else {
                        errorMessage.textContent = updateData.message || 'Failed to update patient.';
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
document.addEventListener('DOMContentLoaded', function () {
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.addEventListener('click', function () {
        errorMessage.style.display = 'none';
        errorMessage.textContent = '';

        const staff_id = document.getElementById('staff_id').value;
        const name = document.getElementById('name').value;
        const nic = document.getElementById('nic').value;
        const role_id = roleSelect.value;
        const specialization_id = specializationSelect.value;
        const address = document.getElementById('address').value;
        const phone_number_1 = document.getElementById('phone_number_1').value;
        const phone_number_2 = document.getElementById('phone_number_2').value;
        const registered_by = document.getElementById('registered_by').value;
//        const password = document.getElementById('password').value;
//        const confirm_password = document.getElementById('confirm_password').value;

        // Input validation
        if (!name || !nic || !address || !registered_by) {
            errorMessage.textContent = 'All fields are required.';
            errorMessage.style.display = 'block';
            return;
        }

//        if (password !== confirm_password) {
//            errorMessage.textContent = 'Password and Confirm Password do not match.';
//            errorMessage.style.display = 'block';
//            return;
//        }

        if (roleSelect.options[roleSelect.selectedIndex].text.toLowerCase() === "doctor" && !specialization_id) {
            errorMessage.textContent = 'Specialization is required for doctors.';
            errorMessage.style.display = 'block';
            return;
        }

        fetch('/receptionist/update-staff', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ staff_id, name, nic, role_id, specialization_id, address, phone_number_1, phone_number_2, registered_by })
        })
        .then(updateResponse => updateResponse.json())
        .then(updateData => {
                    if (updateData.success) {
                        alert('Staff updated successfully!');
                        window.location.href = '/receptionist/view-staff-members'
                    } else {
                        errorMessage.textContent = updateData.message || 'Failed to update staff.';
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
class PatientPhoneNumber:
    def __init__(self, patient_id, phone_number):
        self.patient_id = patient_id
        self.phone_number = phone_number

    @staticmethod
    def from_tuple(data):
        """Create a PatientPhoneNumber object from a tuple or dictionary."""
        return PatientPhoneNumber(
            patient_id=data['patient_id'],
            phone_number=data['phone_number']
        )

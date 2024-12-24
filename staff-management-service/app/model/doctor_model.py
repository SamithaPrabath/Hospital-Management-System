class Doctor:
    def __init__(self, staff_id, doctor_id, specialization_id, status, price):
        self.doctor_id = doctor_id
        self.staff_id = staff_id
        self.specialization_id = specialization_id
        self.status = status
        self.price = price

    @staticmethod
    def from_tuple(data):
        """Create a Doctor object from a tuple or dictionary."""
        return Doctor(
            staff_id=data['staff_id'],
            doctor_id=data['doctor_id'],
            specialization_id=data['specialization_id'],
            status=data['status'],
            price=data['price']
        )

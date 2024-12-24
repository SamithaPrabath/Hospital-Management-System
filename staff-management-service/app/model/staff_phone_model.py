class StaffPhoneNumber:
    def __init__(self, staff_id, phone_number):
        self.staff_id = staff_id
        self.phone_number = phone_number

    @staticmethod
    def from_tuple(data):
        """Create a StaffPhoneNumber object from a tuple or dictionary."""
        return StaffPhoneNumber(
            staff_id=data['staff_id'],
            phone_number=data['phone_number']
        )

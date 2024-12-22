class Staff:
    def __init__(self, staff_id, nic, name, password, role_id, address, registered_by, registered_date):
        self.staff_id = staff_id
        self.nic = nic
        self.name = name
        self.password = password
        self.role_id = role_id
        self.address = address
        self.registered_by = registered_by
        self.registered_date = registered_date

    @staticmethod
    def from_tuple(data):
        """Create a Staff object from a tuple."""
        return Staff(staff_id=data['staff_id'], nic=data['nic'], name=data['name'], password=data['password'], role_id=data['role_id'], address=data['address'], registered_by=data['registerd_by'], registered_date=data['registerd_date'])

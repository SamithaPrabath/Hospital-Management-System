class Staff:
    def __init__(self, id, nic, name, password, role_id, address, registered_by, registered_date):
        self.id = id
        self.nic = nic
        self.name = name
        self.password = password
        self.role_id = role_id
        self.address = address
        self.registered_by = registered_by
        self.registered_date = registered_date

    @staticmethod
    def from_tuple(data):
        """Create a Patient object from a tuple."""
        return Staff(id=data['staff_id'], nic=data['nic'], name=data['name'], password=data['password'], role_id=data['role_id'], address=data['address'], registered_by=data['registerd_by'], registered_date=data['registerd_date'])

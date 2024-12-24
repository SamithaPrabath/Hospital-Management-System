class Patient:
    def __init__(self, patient_id, nic, name, age, address, registered_by, registered_date):
        self.patient_id = patient_id
        self.nic = nic
        self.name = name
        self.age = age
        self.address = address
        self.registered_by = registered_by
        self.registered_date = registered_date

    @staticmethod
    def from_tuple(data):
        """Create a Patient object from a tuple."""
        return Patient(patient_id=data['patient_id'], nic=data['nic'], name=data['name'], age=data['age'],
                       address=data['address'], registered_by=data['registerd_by'],
                       registered_date=data['registerd_date'])

from app.model.patient_model import Patient
from app.model.patient_phone_model import PatientPhoneNumber


class PatientController:
    def __init__(self, query_executor):
        self.query_executor = query_executor

    def create_patient(self, data):
        query = "SELECT * FROM patient WHERE nic = %s;"
        existing_patient = self.query_executor.fetch_one(query, (data['nic'],))
        if existing_patient:
            return 0
        else:
            patient_query = """
                    INSERT INTO patient (nic, name, age, address, registerd_by, registerd_date)
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """
            patient_values = (
                data['nic'],
                data['name'],
                data['age'],
                data['address'],
                data['registered_by'],
                data['registered_date'],
            )
            self.query_executor.execute(patient_query, patient_values)

            new_patient_id = self.query_executor.fetch_one("SELECT LAST_INSERT_ID();")['LAST_INSERT_ID()']

            if 'phone_numbers' in data and data['phone_numbers']:
                phone_query = "INSERT INTO patient_phone (patient_id, phone_number) VALUES (%s, %s);"
                for phone_number in data['phone_numbers']:
                    self.query_executor.execute(phone_query, (new_patient_id, phone_number))

            return new_patient_id

    def get_patient_by_id(self, patient_id):
        patient_query = "SELECT * FROM patient WHERE patient_id = %s;"
        patient_data = self.query_executor.fetch_one(patient_query, (patient_id,))
        if not patient_data:
            return None

        patient = Patient.from_tuple(patient_data)

        phone_query = "SELECT * FROM patient_phone WHERE patient_id = %s;"
        phone_data = self.query_executor.fetch_all(phone_query, (patient_id,))

        if phone_data:
            phone_numbers = [
                PatientPhoneNumber.from_tuple(phone)
                for phone in phone_data
            ]

            patient.phone_numbers = [p.phone_number for p in phone_numbers]
        else:
            patient.phone_numbers = []

        return patient

    def delete_patient(self, patient_id):
        query = "DELETE FROM patient WHERE patient_id = %s;"
        self.query_executor.execute(query, (patient_id,))
        return True

    def update_patient(self, patient_id, data):
        patient_query = """
            UPDATE patient
            SET nic = %s, name = %s, age = %s, address = %s, registerd_by = %s, registerd_date = %s
            WHERE patient_id = %s;
        """
        patient_values = (
            data['nic'],
            data['name'],
            data['age'],
            data['address'],
            data['registered_by'],
            data['registered_date'],
            patient_id
        )
        self.query_executor.execute(patient_query, patient_values)

        self.query_executor.execute("DELETE FROM patient_phone WHERE patient_id = %s;", (patient_id,))
        if 'phone_numbers' in data and data['phone_numbers']:
            phone_query = "INSERT INTO patient_phone (patient_id, phone_number) VALUES (%s, %s);"
            for phone_number in data['phone_numbers']:
                self.query_executor.execute(phone_query, (patient_id, phone_number))

        return True

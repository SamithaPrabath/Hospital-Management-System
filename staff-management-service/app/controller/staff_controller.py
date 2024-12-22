from app.model.doctor_model import Doctor
from app.model.staff_model import Staff
from app.model.staff_phone_model import StaffPhoneNumber


class StaffController:
    def __init__(self, query_executor):
        self.query_executor = query_executor

    def create_staff(self, data):
        query = "SELECT * FROM staff WHERE nic = %s;"
        existing_staff = self.query_executor.fetch_one(query, (data['nic'],))
        if existing_staff:
            return 0
        else:
            staff_query = f"""
                    INSERT INTO staff (nic, name, password, role_id, address, registerd_by, registerd_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """
            staff_values = (
                data['nic'],
                data['name'],
                data['password'],
                data['role_id'],
                data['address'],
                data['registered_by'],
                data['registered_date'],
            )
            self.query_executor.execute(staff_query, staff_values)

            new_staff_id = self.query_executor.fetch_one("SELECT LAST_INSERT_ID();")['LAST_INSERT_ID()']

            if 'phone_numbers' in data and data['phone_numbers']:
                phone_query = "INSERT INTO staff_phone (staff_id, phone_number) VALUES (%s, %s);"
                for phone_number in data['phone_numbers']:
                    self.query_executor.execute(phone_query, (new_staff_id, phone_number))

            role_query = "SELECT * FROM role WHERE role_id = %s;"
            role_data = self.query_executor.fetch_one(role_query, (data['role_id'],))

            if role_data['name'].lower() == "doctor" and 'specialization_id' in data:
                doctor_query = """
                                INSERT INTO doctor (doctor_id, staff_id, specialization_id)
                                VALUES (%s, %s, %s);
                            """
                self.query_executor.execute(doctor_query, (new_staff_id, new_staff_id, data['specialization_id']))

            return new_staff_id

    def get_staff_by_id(self, staff_id):
        staff_query = "SELECT * FROM staff WHERE staff_id = %s;"
        staff_data = self.query_executor.fetch_one(staff_query, (staff_id,))
        if not staff_data:
            return None

        staff = Staff.from_tuple(staff_data)

        phone_query = "SELECT * FROM staff_phone WHERE staff_id = %s;"
        phone_data = self.query_executor.fetch_all(phone_query, (staff_id,))

        if phone_data:
            phone_numbers = [
                StaffPhoneNumber.from_tuple(phone)
                for phone in phone_data
            ]

            staff.phone_numbers = [p.phone_number for p in phone_numbers]
        else:
            staff.phone_numbers = []

        doctor_query = "SELECT * FROM doctor WHERE staff_id = %s;"
        doctor_data = self.query_executor.fetch_one(doctor_query, (staff_id,))

        if doctor_data:
            doctor_data = Doctor.from_tuple(doctor_data)
            staff.specialization_id = doctor_data.specialization_id
        else:
            staff.specialization_id = None
        return staff

    def delete_staff(self, staff_id):
        query = "DELETE FROM staff WHERE staff_id = %s;"
        self.query_executor.execute(query, (staff_id,))
        return True

    def update_staff(self, staff_id, data):
        staff_query = """
            UPDATE staff 
            SET nic = %s, name = %s, password = %s, role_id = %s, address = %s, registerd_by = %s, registerd_date = %s
            WHERE staff_id = %s;
        """
        staff_values = (
            data['nic'],
            data['name'],
            data['password'],
            data['role_id'],
            data['address'],
            data['registered_by'],
            data['registered_date'],
            staff_id
        )
        self.query_executor.execute(staff_query, staff_values)

        self.query_executor.execute("DELETE FROM staff_phone WHERE staff_id = %s;", (staff_id,))
        if 'phone_numbers' in data and data['phone_numbers']:
            phone_query = "INSERT INTO staff_phone (staff_id, phone_number) VALUES (%s, %s);"
            for phone_number in data['phone_numbers']:
                self.query_executor.execute(phone_query, (staff_id, phone_number))

        role_query = "SELECT * FROM role WHERE role_id = %s;"
        role_data = self.query_executor.fetch_one(role_query, (data['role_id'],))
        if role_data['name'].lower() == "doctor":
            doctor_query = """
                INSERT INTO doctor (doctor_id, staff_id, specialization_id)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE specialization_id = VALUES(specialization_id);
            """
            self.query_executor.execute(doctor_query, (staff_id, staff_id, data['specialization_id']))
        else:
            self.query_executor.execute("DELETE FROM doctor WHERE staff_id = %s;", (staff_id,))

        return True
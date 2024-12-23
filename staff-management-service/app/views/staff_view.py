from flask import Blueprint, jsonify, request
from app.controller.staff_controller import StaffController


def create_staff_blueprint(query_executor):
    staff_bp = Blueprint('staff', __name__)

    staff_controller = StaffController(query_executor)

    @staff_bp.route('/', methods=['POST'])
    def create_staff():
        data = request.json
        try:
            staff_id = staff_controller.create_staff(data)
            if staff_id == 0:
                return jsonify({"error": "Staff with the same NIC already exists"}), 400
            else:
                return jsonify({"message": "Staff created successfully", "id": staff_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @staff_bp.route('/<int:staff_id>', methods=['GET'])
    def get_staff(staff_id):
        try:
            staff = staff_controller.get_staff_by_id(staff_id)
            if staff:
                return jsonify({
                    "staff_id": staff.staff_id,
                    "nic": staff.nic,
                    "name": staff.name,
                    "role_id": staff.role_id,
                    "address": staff.address,
                    "registered_by": staff.registered_by,
                    "registered_date": staff.registered_date,
                    "phone_numbers": staff.phone_numbers,
                    "specialization_id": staff.specialization_id
                }), 200
            else:
                return jsonify({"error": "Staff not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staff_bp.route('/<int:staff_id>', methods=['DELETE'])
    def delete_staff(staff_id):
        try:
            staff_controller.delete_staff(staff_id)
            return jsonify({"message": "Staff deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @staff_bp.route('/<int:staff_id>', methods=['PUT'])
    def update_staff(staff_id):
        data = request.json
        try:
            staff_controller.update_staff(staff_id, data)
            return jsonify({"message": "Staff updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400\


    @staff_bp.route('/<int:staff_id>/change-password', methods=['PATCH'])
    def change_password(staff_id):
        data = request.json
        try:
            if 'current_password' not in data or 'new_password' not in data:
                return jsonify({"error": "Both 'current_password' and 'new_password' are required."}), 400

            current_password = data['current_password']
            new_password = data['new_password']

            result = staff_controller.change_password(staff_id, current_password, new_password)

            if result['success']:
                return jsonify({"message": result['message']}), 200
            else:
                return jsonify({"error": result['message']}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staff_bp.route('/login', methods=['POST'])
    def check_login():
        data = request.json
        try:
            if 'nic' not in data or 'password' not in data:
                return jsonify({"error": "Both 'nic' and 'password' are required."}), 400

            nic = data['nic']
            password = data['password']

            result = staff_controller.check_login(nic, password)

            if result['success']:
                return jsonify({
                    "message": "Login successful.",
                    "is_authenticated": result['is_authenticated'],
                    "staff_id": result['staff_id'],
                    "name": result['name'],
                    "role_id": result['role_id']
                }), 200
            else:
                return jsonify({"error": result['message']}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return staff_bp

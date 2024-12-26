from flask import Blueprint, jsonify, request
from app.controller.patient_controller import PatientController


def create_patient_blueprint(query_executor):
    patient_bp = Blueprint('patient', __name__)

    patient_controller = PatientController(query_executor)

    @patient_bp.route('/', methods=['POST'])
    def create_patient():
        data = request.json
        try:
            patient_id = patient_controller.create_patient(data)
            if patient_id == 0:
                return jsonify({"error": "Patient with the same NIC already exists"}), 400
            else:
                return jsonify({"message": "Patient created successfully", "id": patient_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @patient_bp.route('/<int:patient_id>', methods=['GET'])
    def get_patient(patient_id):
        try:
            patient = patient_controller.get_patient_by_id(patient_id)
            if patient:
                return jsonify({
                    "patient_id": patient.patient_id,
                    "nic": patient.nic,
                    "name": patient.name,
                    "age": patient.age,
                    "address": patient.address,
                    "registered_by": patient.registered_by,
                    "registered_date": patient.registered_date,
                    "phone_numbers": patient.phone_numbers,
                }), 200
            else:
                return jsonify({"error": "Patient not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @patient_bp.route('/<int:patient_id>', methods=['DELETE'])
    def delete_patient(patient_id):
        try:
            patient_controller.delete_patient(patient_id)
            return jsonify({"message": "Patient deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @patient_bp.route('/<int:patient_id>', methods=['PUT'])
    def update_patient(patient_id):
        data = request.json
        try:
            patient_controller.update_patient(patient_id, data)
            return jsonify({"message": "Patient updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @patient_bp.route('/patient-list', methods=['GET'])
    def get_all_patients():
        try:
            patient_list = patient_controller.get_all_patients()
            if patient_list:
                return jsonify(patient_list), 200
            else:
                return jsonify({"message": "No patient found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return patient_bp

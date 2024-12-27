import base64
import os

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, make_response
from weasyprint import HTML
from werkzeug.utils import secure_filename

from app.views.radiologist.radiologist import get_receipt_reports, create_medical_reports, update_receipt_reports, \
    get_medical_reports
from app.views.receptionist.receptionist import update_receipt_status, update_total_amount
from app.views.views import get_staff_by_id

radiologist = Blueprint('radiologist', __name__)

@radiologist.route('/')
def index():
    validate_logged_user()
    staff_name = session.get('name')
    return render_template('radiologist/radiologist.html', staff_name=staff_name)

@radiologist.route('/check_reports')
def go_to_check_receipt_reports():
    validate_logged_user()
    report_details = []

    return render_template(
        'radiologist/check_reports.html',
        staff_name=session.get('name'),
        staff_id=session.get('staff_id'),
        report_details=report_details
    )


@radiologist.route('/upload_report')
def go_to_upload_report():
    validate_logged_user()

    report_type = request.args.get('type')
    receipt_id = request.args.get('receipt_id')
    report_id = request.args.get('report_id')
    price = request.args.get('price')

    return render_template(
        'radiologist/upload_report.html',
        staff_name=session.get('name'),
        report_type=report_type,
        receipt_id=receipt_id,
        report_id=report_id,
        price=price
    )


@radiologist.route('/filter_reports', methods=['POST'])
def filter_reports():
    validate_logged_user()
    receipt_id = int(request.form.get('receipt_id'))
    report_details = get_receipt_reports(receipt_id)

    return render_template(
        'radiologist/check_reports.html',
        receipt_id=receipt_id,
        staff_name=session.get('name'),
        staff_id=session.get('staff_id'),
        report_details=report_details
    )


@radiologist.route('/submit_upload_report', methods=['POST'])
def upload_reports():
    validate_logged_user()
    image = request.files['scan_image']
    receipt_id = request.args.get('receipt_id')
    report_id = request.args.get('report_id')
    price = int(request.args.get('price'))

    filename = secure_filename(image.filename)

    uploads_folder = 'app/static/uploads'

    if not os.path.exists(uploads_folder):
        os.makedirs(uploads_folder)

    image.save(os.path.join(uploads_folder, filename))

    create_medical_reports(
        report_id=int(report_id),
        receipt_id=int(receipt_id),
        image=filename,
        description=request.form.get('description'),
        issued_by=session.get('staff_id')
    )
    update_receipt_reports(receipt_id=int(receipt_id), report_id=int(report_id))
    update_total_amount(int(receipt_id), price)

    report_details = get_receipt_reports(int(receipt_id))

    return render_template(
        'radiologist/check_reports.html',
        receipt_id=receipt_id,
        staff_name=session.get('name'),
        staff_id=session.get('staff_id'),
        report_details=report_details
    )


@radiologist.route('/delete_receipt_report', methods=['GET'])
def delete_receipt_reports():
    validate_logged_user()

    receipt_id = request.args.get('receipt_id')
    report_id = request.args.get('report_id')
    status = request.args.get('status')
    update_receipt_reports(
        receipt_id=int(receipt_id),
        report_id=int(report_id),
        status=status
    )

    report_details = get_receipt_reports(int(receipt_id))

    return render_template(
        'radiologist/check_reports.html',
        receipt_id=receipt_id,
        staff_name=session.get('name'),
        staff_id=session.get('staff_id'),
        report_details=report_details
    )


@radiologist.route('/generate_pdf_report', methods=['GET'])
def generate_pdf_report():
    validate_logged_user()

    return render_template(
        'radiologist/generate_pdf_report.html',
        staff_name=session.get('name')
    )


@radiologist.route('/filter_medical_reports', methods=['POST'])
def filter_medical_reports():
    validate_logged_user()
    receipt_id = int(request.form.get('receipt_id'))
    receipt_report_details = get_receipt_reports(receipt_id)
    medical_report = get_medical_reports(receipt_id)

    report_details = []

    for report in medical_report:
        report_type, status =__get_report_type_and_status(report['report_id'], report['receipt_id'], receipt_report_details)
        generated_by = get_staff_by_id(int(report['issued_by']))['data']['name']
        report_details.append({
            'report_id': report['report_id'],
            'receipt_id': report['receipt_id'],
            'image': report['image'],
            'description': report['description'],
            'generated_by': generated_by,
            'generated_date': report['issued_date'],
            'status': status,
            'report_type': report_type
        })
    return render_template(
        'radiologist/generate_pdf_report.html',
        receipt_id=receipt_id,
        staff_name=session.get('name'),
        report_details=report_details
    )


@radiologist.route('/download_report_pdf', methods=['GET'])
def download_report_pdf():
    receipt_id = int(request.args.get('receipt_id'))
    receipt_report_details = get_receipt_reports(receipt_id)
    medical_report = get_medical_reports(receipt_id)

    report_details = []

    for report in medical_report:
        report_type, status = __get_report_type_and_status(report['report_id'], report['receipt_id'],
                                                           receipt_report_details)
        generated_by = get_staff_by_id(int(report['issued_by']))['data']['name']
        report_details.append({
            'report_id': report['report_id'],
            'receipt_id': report['receipt_id'],
            'image': url_for('static', filename='uploads/'+report['image'], _external=True),
            'description': report['description'],
            'generated_by': generated_by,
            'generated_date': report['issued_date'],
            'status': status,
            'report_type': report_type
        })

    context = {
        'title': f'Medical Report For Receipt - {receipt_id}',
        'description': "This medical report provides a detailed summary of the patient's health status, diagnostic findings, and treatment recommendations. It is prepared by ABC Hospital's professional medical team to assist in ongoing care and decision-making."
                       "For further inquiries, please contact ABC Hospital at +1 (123) 456-7890 or visit us at",
        'report_details': report_details
    }

    # Render the HTML template with context
    html_content = render_template('radiologist/report_template.html', **context)

    # Generate PDF from HTML
    pdf = HTML(string=html_content).write_pdf()

    # Create a response for file download
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=medical_report.pdf'
    update_receipt_status(receipt_id, 4)
    return response


def __get_report_type_and_status(report_id: int, receipt_id: int, receipt_report: list):
    report_type = ''
    status = ''
    for report in receipt_report:
        if report['report_id'] == report_id and report['receipt_id'] == receipt_id:
            report_type = report['report_type']
            status = report['status']
            if status == 'Pending':
                update_receipt_status(receipt_id, 3)
            break
    return report_type, status


def validate_logged_user():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')
    if not staff_name or not staff_id:
        return redirect(url_for('login.index'))

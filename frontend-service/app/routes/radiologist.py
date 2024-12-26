from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from app.views.radiologist.radiologist import get_receipt_reports

radiologist = Blueprint('radiologist', __name__)


@radiologist.route('/')
def index():
    validate_logged_user()
    return render_template('radiologist/radiologist.html', staff_name=staff_name)

@radiologist.route('/check_reports')
def go_to_check_receipt_reports():
    validate_logged_user()
    # report_details = [
    #     {
    #         "type": "X-Ray",
    #         "Status": "Pending",
    #     }
    # ]
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
    report_details = []

    return render_template(
        'radiologist/upload_report.html',
        staff_name=session.get('name'),
        staff_id=session.get('staff_id'),
        report_details=report_details
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
    receipt_id = int(request.form.get('receipt_id'))
    report_details = get_receipt_reports(receipt_id)

    return render_template(
        'radiologist/check_reports.html',
        receipt_id=receipt_id,
        staff_name=session.get('name'),
        staff_id=session.get('staff_id'),
        report_details=report_details
    )

@radiologist.route('/')
def view_appointments():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('radiologist.html', staff_name=staff_name)

@radiologist.route('/')
def staff_register():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('radiologist.html', staff_name=staff_name)


def validate_logged_user():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')
    if not staff_name or not staff_id:
        return redirect(url_for('login.index'))

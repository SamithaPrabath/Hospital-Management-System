from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

report = Blueprint('report', __name__)


@report.route('/')
def index():
    staff_name = session.get('name', 'samitha')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('report-index.html', staff_name=staff_name)


@report.route('/generate')
def go_to_generate_report_page():
    staff_name = session.get('name')
    return render_template('add_report.html', staff_name=staff_name)

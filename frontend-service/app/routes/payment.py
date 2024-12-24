from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

payment = Blueprint('payment', __name__)


@payment.route('/')
def index():
    staff_name = session.get('name', 'samitha')
    if not staff_name:
        return redirect(url_for('login.index'))

    return render_template('payment-index.html', staff_name=staff_name)


@payment.route('/pay')
def go_to_pay_page():
    staff_name = session.get('name')
    return render_template('add-payment.html', staff_name=staff_name)

from flask import Blueprint

from app.base.views import views

base_route = Blueprint(name='base', import_name=__name__)

# Create a route for the receipt endpoints

# create a receipt
base_route.add_url_rule(
    rule='/payment',
    endpoint='create_receipt',
    view_func=views.generate_payment,
    methods=['POST']
)

# get a receipt
base_route.add_url_rule(
    rule='/payment/<int:receipt_id>',
    endpoint='get_receipt',
    view_func=views.get_payment_view,
    methods=['GET']
)

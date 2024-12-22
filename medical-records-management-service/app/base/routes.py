from flask import Blueprint

from app.base.views import views

base_route = Blueprint(name='base', import_name=__name__)

# Create a route for the receipt endpoints

# create a receipt
base_route.add_url_rule(
    rule='/report',
    endpoint='create_receipt',
    view_func=views.generate_report,
    methods=['POST']
)

# get a receipt
base_route.add_url_rule(
    rule='/receipt/<int:receipt_id>',
    endpoint='get_receipt',
    view_func=views.get_receipt_view,
    methods=['GET']
)

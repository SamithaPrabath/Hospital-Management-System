from flask import Blueprint

from app.base.views import views

base_route = Blueprint(name='base', import_name=__name__)

# Create a route for the receipt endpoints

# create a receipt
base_route.add_url_rule(
    rule='/receipt',
    endpoint='create_receipt',
    view_func=views.generate_receipt,
    methods=['POST']
)

# get a receipt
base_route.add_url_rule(
    rule='/receipt/<int:receipt_id>',
    endpoint='get_receipt',
    view_func=views.get_receipt_view,
    methods=['GET']
)

# get a receipt
base_route.add_url_rule(
    rule='/receipts',
    endpoint='get_all_receipt',
    view_func=views.get_all_receipts_view,
    methods=['GET']
)

# get a receipt status types
base_route.add_url_rule(
    rule='/receipt/status/<int:status_id>',
    endpoint='get_status_types',
    view_func=views.get_status_types_view,
    methods=['GET']
)

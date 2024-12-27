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

base_route.add_url_rule(
    rule='/receipt/doctor/<int:doctor_id>',
    endpoint='get_doctor_receipt',
    view_func=views.get_receipt_by_doc_id_view,
    methods=['GET']
)

# update receipt status
base_route.add_url_rule(
    rule='/receipt/<int:receipt_id>/status/<int:status_id>',
    endpoint='update_receipt_status',
    view_func=views.update_receipt_status_view,
    methods=['PUT']
)


# update receipt total amount
base_route.add_url_rule(
    rule='/receipt/<int:receipt_id>/total_amount/<int:total_amount>',
    endpoint='update_total_amount',
    view_func=views.update_total_amount_view,
    methods=['PUT']
)

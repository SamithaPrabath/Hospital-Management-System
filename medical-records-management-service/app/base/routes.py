from flask import Blueprint

from app.base.views import views

base_route = Blueprint(name='base', import_name=__name__)

# get a receipt report details
base_route.add_url_rule(
    rule='/receipt_reports/<int:receipt_id>',
    endpoint='get_receipt_report',
    view_func=views.get_receipt_report_view,
    methods=['GET']
)

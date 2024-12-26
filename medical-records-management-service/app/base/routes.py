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


# create a medical report
base_route.add_url_rule(
    rule='/medical_reports',
    endpoint='create_medical_report',
    view_func=views.create_medical_report_view,
    methods=['POST']
)

base_route.add_url_rule(
    rule='/receipt_reports/<int:receipt_id>/update/<int:report_id>',
    endpoint='update_receipt_report',
    view_func=views.update_receipt_report_view,
    methods=['PUT']
)

base_route.add_url_rule(
    rule='/medical_reports/<int:receipt_id>',
    endpoint='get_medical_report',
    view_func=views.get_medical_report_view,
    methods=['GET']
)

base_route.add_url_rule(
    rule='/medical_reports/<int:receipt_id>/delete/<int:report_id>',
    endpoint='delete_medical_report',
    view_func=views.delete_medical_report_view,
    methods=['DELETE']
)

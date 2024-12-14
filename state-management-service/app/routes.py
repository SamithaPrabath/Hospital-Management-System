from quart import Blueprint

from app.views import views

base_route = Blueprint('base_route')

# Create a route for the receipt endpoints

# create a receipt
base_route.add_url_rule(
    rule='/receipt',
    endpoint='create_receipt',
    view_func=views.generate_receipt,
    methods=['POST']
)

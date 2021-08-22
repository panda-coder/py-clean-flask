from flask import Blueprint, request

from main.adapters import adapt_route
from main.factories import make_sum_controller, make_subtract_controller, make_multiply_controller, make_divide_controller

calculations_router = Blueprint('calculations', __name__)


@calculations_router.route('/sum', methods=['POST'])
def sum():
    return adapt_route(
        request,
        make_sum_controller()
    )


@calculations_router.route('/subtract', methods=['POST'])
def subtract():
    return adapt_route(
        request,
        make_subtract_controller()
    )

@calculations_router.route('/multiply', methods=['POST'])
def multiply():
    return adapt_route(
        request,
        make_multiply_controller()
    )

@calculations_router.route('/divide', methods=['POST'])
def divide():
    return adapt_route(
        request,
        make_divide_controller()
    )

from .calculations import calculations_router

from flask import Blueprint

v1_router = Blueprint('v1', __name__, url_prefix='/v1')
v1_router.register_blueprint(calculations_router)
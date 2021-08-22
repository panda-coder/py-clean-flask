# Global import
from flask import Flask

# Local Import
from main.routes import v1

server = Flask(__name__)
server.register_blueprint(v1.v1_router)


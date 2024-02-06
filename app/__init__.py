from flask import Flask, request
from .routes import init_app_routes


def create_app():
    """
    Creates and configures an instance of the Flask application.

    Registers a before_request handler to log request details and
    initializes application routes.

    Returns:
        app: The configured Flask application instance.
    """
    app = Flask(__name__)

    @app.before_request
    def log_request_info():
        """
        Logs the headers and body of each incoming request.
        This function is executed before each request is processed.
        """
        app.logger.debug("Headers: %s", request.headers)
        app.logger.debug("Body: %s", request.get_data())

    init_app_routes(app) # initialise routes for the app

    return app

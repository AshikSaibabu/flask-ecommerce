from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configuration settings
    app.config.from_object('config.Config')

    @app.route('/')
    def home():
        return "Hello, Flask!"

    return app

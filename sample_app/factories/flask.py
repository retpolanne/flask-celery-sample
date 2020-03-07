import os
from flask import Flask, jsonify
from sample_app.blueprints import echo


def create_app():
    app = Flask(__name__)

    if os.getenv("ENV") == "production":
        app.config.from_object('sample_app.config.ProductionConfig')
    if os.getenv("ENV") == "testing":
        app.config.from_object('sample_app.config.TestingConfig')
    if os.getenv("ENV") == "development":
        app.config.from_object('sample_app.config.DevelopmentConfig')

    app.register_blueprint(echo.bp)

    @app.route("/healthcheck")
    def healthcheck():
        return jsonify({"message": "ok"})

    return app

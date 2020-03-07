from flask import Flask, jsonify
from sample_app.blueprints import echo


def create_app():
    app = Flask(__name__)

    app.register_blueprint(echo.bp)

    @app.route("/healthcheck")
    def healthcheck():
        return jsonify({"message": "ok"})
    
    return app

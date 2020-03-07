from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    from . import echo
    app.register_blueprint(echo.bp)

    @app.route("/healthcheck")
    def healthcheck():
        return jsonify({"message": "ok"})
    
    return app

from flask import Blueprint, current_app, jsonify, request, Response
from sample_app.factories.celery import make_celery

bp = Blueprint('echo', __name__, url_prefix='/echo')

@bp.route('/send-message', methods=['POST'])
def echo():
    if request.method != 'POST':
        return Response(status=405)
    message = request.get_json().get("message")
    return jsonify({"message": message})


@bp.route('/send-email', methods=['POST'])
def send_email():
    if request.method != 'POST':
        return Response(status=405)
    payload = request.get_json()
    message = payload.get("message")
    email_address = payload.get("email_address")
    celery = make_celery(current_app)
    celery.send_task('tasks.send_email', args=[email_address, message])

    return Response(status=201)

from flask import Blueprint, jsonify, request, Response

bp = Blueprint('echo', __name__, url_prefix='/echo')

@bp.route('/send-message', methods=['POST'])
def echo():
    if request.method != 'POST':
        return Response(status=405)
    message = request.get_json().get("message")
    return jsonify({"message": message})

from flask import Blueprint, request, jsonify


file = Blueprint('file', __name__)

@file.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    f = request.files['testfile']
    print(f.filename)
    print(f)
    print(request.files)
    return jsonify({'code': 200})
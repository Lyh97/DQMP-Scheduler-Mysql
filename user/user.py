from flask import Blueprint, request, jsonify
from db.query_db import query_db_outside
from .sql import query

user = Blueprint('user', __name__)

@user.route('/getimg', methods=['POST'])
def getImg():
    username = request.form.get('username')
    imgurl = query_db_outside(query['selectUserImg'], (username,))
    if (imgurl):
        return jsonify({'code': 200, 'meaasge': 'ok', 'data': imgurl[0]['imgpath']})
    else:
        return jsonify({'code': 300, 'meaasge': 'ok', 'data': ''})

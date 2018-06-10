import sys
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify, flash, redirect
import os

file = Blueprint('file', __name__)

UPLOAD_FOLDER = sys.path[0] + '/static/uploads'
ALLOWED_EXTENSIONS = set(['sql'])

@file.route('/uploads/', methods=['GET', 'POST'])
def upload_file():
    f = request.files['testfile']
    print(f.filename)
    print(f)
    print(request.files)
    return jsonify({'code': 200})

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 上传任务文件
@file.route('/add', methods=['GET', 'POST'])
def uploadfile():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    print(file)
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        file_object = open(sys.path[0]+'/static/uploads/'+filename)
        try:
            all_the_text = file_object.read()
            all_the_text_sql = all_the_text.replace('\n', ' ')
            all_the_text_temp = all_the_text.replace(' ', '')
            if all_the_text_temp.find("SELECT*") != -1 or all_the_text_temp.find("DELETEFROM") != -1:
                return jsonify({'code':300,'message':'There are illegal statements in the SQL file','data': ''})
        finally:
            file_object.close()
        return jsonify({'code':200,'data': '/static/uploads/'+filename,'sql':all_the_text_sql})
  return 'fail';

# 删除上传的任务文件
@file.route('/remove', methods=['GET', 'POST'])
def removefile():
  filepath = request.form.get('filename', default='')
  os.remove(os.path.join(UPLOAD_FOLDER, filepath))
  return 'remove success'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
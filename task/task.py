from flask import Blueprint, request, jsonify, g
from db.query_db import query_db

from .sql import query

task = Blueprint('task', __name__)

@task.route('/add/')
def add_task():
    # scheduler.add_job(interval_job, trigger='interval', seconds=5, id='interval_id2')
    # scheduler.add_job(func=interval_job, id='123', trigger='interval', seconds=5)
    # sqlTask = SqlTask.SqlTask()
    # scheduler.add_job(func=interval_job, id='sqlaa', trigger='interval', seconds=100)
    username = request.form.get('username')               # The owner's username
    description = request.form.get('description')         # The description of the task
    tag = request.form.get('tag')                         # The tag of the task
    enable = request.form.get('enable')                   # Whether the available
    threshold = request.form.get('threshold')             # The threshold of result for sending the notice to owner
    file_path = request.form.get('file_path')             # The path of the task need to run
    enable = request.form.get('enabled')                  # Whether add to queen
    run_now = request.form.get('run_now')                 # just run now

    cur = query_db(query['add_task'],(1,'1','1','1','1','1','1','1','1','1','1','1','1',1,'1',))
    print(cur)
    return jsonify(cur)
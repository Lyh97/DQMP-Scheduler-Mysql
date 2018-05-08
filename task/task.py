from flask import Blueprint, request, jsonify, g
from db.query_db import query_db
from .sql import query
import time

task = Blueprint('task', __name__)

@task.route('/add/')
def add_task():
    # scheduler.add_job(interval_job, trigger='interval', seconds=5, id='interval_id2')
    # scheduler.add_job(func=interval_job, id='123', trigger='interval', seconds=5)
    # sqlTask = SqlTask.SqlTask()
    # scheduler.add_job(func=interval_job, id='sqlaa', trigger='interval', seconds=100)
    taskid = request.form.get('taskid')
    category = request.form.get('category')
    owner = request.form.get('owner')
    email = request.form.get('email')
    description = request.form.get('description')         # The description of the task
    tag = request.form.get('tag')                         # The tag of the task
    enabled = request.form.get('enable')                  # Whether the available
    frequency = request.form.get('freqency')
    task_type = request.form.get('task_type')
    threshold = request.form.get('threshold')             # The threshold of result for sending the notice to owner
    filepath = request.form.get('file_path')              # The path of the task need to run
    run_now = eval(request.form.get('run_now'))           # just run now
    upload_user_id = request.form.get('upload_user_id')

    upload_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    cur = query_db(query['add_task'], (taskid, category, owner, email,
                                       description, tag, enabled, frequency,
                                       task_type, threshold, filepath, upload_time,
                                       update_time, upload_user_id))

    return jsonify(cur)
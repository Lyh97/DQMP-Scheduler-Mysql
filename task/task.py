from flask import Blueprint, request, jsonify
from db.query_db import query_db_outside
from .sql import query
from SqlTask.SqlTask import run
import time
import __main__



task = Blueprint('task', __name__)

@task.route('/add/', methods=['GET', 'POST'])
def add_task():
    # scheduler.add_job(interval_job, trigger='interval', seconds=5, id='interval_id2')
    # scheduler.add_job(func=interval_job, id='123', trigger='interval', seconds=5)
    # sqlTask = SqlTask.SqlTask()
    # scheduler.add_job(func=interval_job, id='sqlaa', trigger='interval', seconds=100)
    print(request.form)
    taskid = request.form.get('taskid')
    print(taskid)
    category = request.form.get('category')
    owner = request.form.get('owner')
    email = request.form.get('email')
    description = request.form.get('description')         # The description of the task
    tag = request.form.get('tag')                         # The tag of the task
    enabled = eval(request.form.get('enabled'))               # Whether the available
    freqency = request.form.get('freqency')
    task_type = request.form.get('task_type')
    threshold = int(request.form.get('threshold'))             # The threshold of result for sending the notice to owner
    filepath = request.form.get('file_path')              # The path of the task need to run
    run_now = eval(request.form.get('run_now'))           # just run now
    upload_user_id = int(request.form.get('upload_user_id'))

    upload_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    cur = query_db_outside(query['add_task'], (taskid, category, owner, email,
                                       description, tag, enabled, freqency,
                                       task_type, threshold, filepath, upload_time,
                                       update_time, upload_user_id))
    if run_now:
        run(user_id=upload_user_id, taskid=taskid, filepath=filepath, freqency=freqency)

    if enabled:
        if freqency == 'daily':
            __main__.scheduler.add_job(func=run, kwargs={'user_id':upload_user_id, 'taskid':taskid, 'filepath':filepath, 'freqency':freqency}, id=taskid, trigger='interval', seconds=20)
            pass
    return jsonify({'code': 200 })

# 查询task列表
@task.route('/list',methods=['POST'])
def selectTaskListByUserId():
    taskList = query_db_outside(query['select_tasklist'])
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': taskList})

# 按条件筛选task
@task.route('/filtrate',methods=['POST'])
def filtrateSelect():
    freqency = request.form.get('freqency')
    enabled = request.form.get('enabled')
    category = request.form.get('category')
    sql = "SELECT * ,(select COUNT(taskid) from result_tab a WHERE a.taskid = task.taskid) as totalrun,(select COUNT(taskid) from result_tab a WHERE a.taskid = task.taskid And a.status = 0) as totalfails From task WHERE owner = 'Account'"

    if freqency:
        sql += " AND freqency = '" + freqency + "'"
    if enabled != '':
        sql += " AND enabled = '" + enabled + "'"
    if category != '':
        sql += " AND category = '" + category + "'"

    taskList = query_db_outside(sql)

    return jsonify({'code': 200, 'meaasge': 'ok', 'data': taskList})

# 查看任务详情
@task.route('/select',methods=['POST'])
def selectById():
    taskid = request.form.get('taskid')

    task = query_db_outside(query['select_task'], (taskid,))

    return jsonify({'code': 200, 'meaasge': 'ok', 'data': task})

# 查询特定task的运行记录
@task.route('/selctTaskLogById',methods=['POST'])
def selectTaskLogByTaskId():
    taskid = request.form.get('taskid')

    task = query_db_outside(query['selctTaskLogById'], (taskid,))

    return jsonify({'code':200,'message':'ok','data':task})

# 查询任务history
@task.route('/select_history',methods=['POST'])
def selectHistoryById():
    return jsonify({'code': 200, 'message': 'ok', 'data': ''})
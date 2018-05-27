from flask import Blueprint, request, jsonify
from redis import Redis

from db.query_db import query_db_outside
from .sql import query

log = Blueprint('log', __name__)
redis = Redis()

# 查询task列表
@log.route('/list',methods=['POST','GET'])
def selectTaskListByUserId():
    sessionid = request.args.get('sessionid')
    userid = redis.get(sessionid).decode()

    taskList = query_db_outside(query['select_tasklist'],(userid,))
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': taskList})

# 按条件筛选task
@log.route('/filtrate',methods=['POST','GET'])
def filtrateSelect():
    freqency = request.form.get('freqency')
    enabled = request.form.get('enabled')
    category = request.form.get('category')
    sessionid = request.form.get('sessionid')
    userid = redis.get(sessionid).decode()

    sql = "SELECT * ,(select COUNT(taskid) from result_tab a WHERE a.taskid = task.taskid) as totalrun,(select COUNT(taskid) from result_tab a WHERE a.taskid = task.taskid And a.status = 0) as totalfails From task WHERE upload_user_id = " + userid

    if freqency:
        sql += " AND freqency = '" + freqency + "'"
    if enabled:
        sql += " AND enabled = '" + enabled + "'"
    if category:
        sql += " AND category = '" + category + "'"

    taskList = query_db_outside(sql)

    return jsonify({'code': 200, 'meaasge': 'ok', 'data': taskList})

# 查看任务详情
@log.route('/select',methods=['POST'])
def selectById():
    taskid = request.form.get('taskid')

    task = query_db_outside(query['select_task'], (taskid,))

    return jsonify({'code': 200, 'meaasge': 'ok', 'data': task})

# 查询特定task的运行记录
@log.route('/selctTaskLogById',methods=['POST'])
def selectTaskLogByTaskId():
    taskid = request.form.get('taskid')

    task = query_db_outside(query['selctTaskLogById'], (taskid,))

    date = []
    result = []

    for i in task:
        date.append(i['run_time'])
        result.append(i['result'])

    return jsonify({'code':200,'message':'ok','data':{'tab_data':task,'chart_data':{'run_time':date,'result':result}}})

# 修改comments
@log.route('/updateComment',methods=['POST'])
def selectHistoryById():
    id = request.form.get('id')
    comments = request.form.get('comments')

    taskList = query_db_outside(query['updateComment'], (comments,id,))

    return jsonify({'code': 200, 'message': 'ok', 'data': ''})

#查询errortask 通过时间
@log.route('/error_list',methods=['GET','POST'])
def selectErrorTaskByResulttime():
    date = request.form.get('date')
    fre = request.form.get('fre')
    sessionid = request.form.get('sessionid')
    userid = redis.get(sessionid).decode()

    taskList = []
    if fre == 'daily':
      taskList = query_db_outside(query['SelectDailyErrorList'], (date,userid,))
    if fre == 'weekly':
      taskList = query_db_outside(query['SelectWeeklyErrorList'], (date,userid,))
    if fre == 'monthly':
      taskList = query_db_outside(query['SelectMonthlyErrorList'], (date,userid,))
    return jsonify({'code': 200, 'message': 'ok', 'data': taskList})

#查询特定模块的errortask 通过时间
@log.route('/spe_error_list',methods=['GET','POST'])
def selectSpeErrorTaskByResulttime():
    date = request.form.get('date')
    fre = request.form.get('fre')
    module = request.form.get('module')
    sessionid = request.form.get('sessionid')
    userid = redis.get(sessionid).decode()

    taskList = []
    if fre == 'daily':
        taskList = query_db_outside(query['SelectSpeDailyErrorList'], (date,module,userid,))
    if fre == 'weekly':
        taskList = query_db_outside(query['SelectSpeWeeklyErrorList'], (date,module,userid,))
    if fre == 'monthly':
        taskList = query_db_outside(query['SelectSpeMonthlyErrorList'], (date,module,userid,))
    return jsonify({'code': 200, 'message': 'ok', 'data': taskList})
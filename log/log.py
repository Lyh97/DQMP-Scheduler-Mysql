from flask import Blueprint, request, jsonify
from db.query_db import query_db_outside
from .sql import query

log = Blueprint('log', __name__)

# 查询task列表
@log.route('/list',methods=['POST'])
def selectTaskListByUserId():
    taskList = query_db_outside(query['select_tasklist'])
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': taskList})

# 按条件筛选task
@log.route('/filtrate',methods=['POST'])
def filtrateSelect():
    freqency = request.form.get('freqency')
    enabled = request.form.get('enabled')
    category = request.form.get('category')
    sql = "SELECT * ,(select COUNT(taskid) from result_tab a WHERE a.taskid = task.taskid) as totalrun,(select COUNT(taskid) from result_tab a WHERE a.taskid = task.taskid And a.status = 0) as totalfails From task WHERE owner = 'Account'"

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

    return jsonify({'code':200,'message':'ok','data':task})

# 查询任务history
@log.route('/select_history',methods=['POST'])
def selectHistoryById():
    return jsonify({'code': 200, 'message': 'ok', 'data': ''})
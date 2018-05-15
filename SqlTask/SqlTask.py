import ibm_db
import sys
import json
from db.query_db import query_db_outside
from .sql import query
import time
from functools import wraps


def run(user_id, taskid, filepath, freqency, threshold, taskname):
    print('\033[4;32m' + 'Start to running <' + taskname + '> [id:' + taskid +']' + '\033[0m')
    config = open(sys.path[0] + '/SqlTask/config.json', 'r')
    config = config.read()
    config = json.loads(config)
    dns = "DATABASE=%s;HOSTNAME=%s;PORT=%s;PROTOCOL=TCPIP;UID=%s;PWD=%s" % (
        config['database'], config['hostname'], config['port'], config['user_id'], config['password'])
    conn = ibm_db.connect(dns, "", "")
    sqlfile = open(sys.path[0] + filepath, 'r')
    sql = sqlfile.read()
    stmt = ibm_db.exec_immediate(conn, sql)
    result = ibm_db.fetch_assoc(stmt)
    result_count = int(result['1'])
    result_time = time.strftime('%Y-%m-%d', time.localtime())
    insert_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    if freqency == 'daily':
        daily_status = 1
        query_db_outside(query['add_dailylog'], (taskid, result_count, result_time, 1, user_id, insert_time))

    if freqency == 'weekly':
        query_db_outside(query['add_dailylog'], (taskid, result_count, result_time, 1, user_id, insert_time))

    if freqency == 'monthly':
        query_db_outside(query['add_dailylog'], (taskid, result_count, result_time, 1, user_id, insert_time))

    table = {'daily': 'add_dailylog',
             'weekly': 'add_dailylog',
             'monthly': 'add_dailylog'}

    if result_count > threshold:
        daily_status = 0
        resulttab_status = 'Fail'
        print('\033[1;33;41m<' + taskname + '> [id:' + taskid +']' + 'Exceed the threshold [count:'+ str(result_count) +']' + '\033[0m')
    else:
        daily_status = 1
        resulttab_status = 'Success'
        print('\033[1;30;47m<' + taskname + '> [id:' + taskid +']' + 'success!' + '\033[0m')

    query_db_outside(query[table[freqency]], (taskid, result_count, result_time, daily_status, user_id, insert_time))
    query_db_outside(query['add_resulttab'], (taskname, taskid, result_count, resulttab_status, insert_time, '10s'))

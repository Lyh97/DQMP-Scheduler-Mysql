import ibm_db
import sys
import json
from db.query_db import query_db_outside
from .sql import query
import time
from functools import wraps


def run(user_id, taskid, filepath, freqency, threshold, taskname):
    config = open(sys.path[0] + '/SqlTask/config.json', 'r')
    config = config.read()
    config = json.loads(config)
    dns = "DATABASE=%s;HOSTNAME=%s;PORT=%s;PROTOCOL=TCPIP;UID=%s;PWD=%s" % (
        config['database'], config['hostname'], config['port'], config['user_id'], config['password'])
    conn = ibm_db.connect(dns, "", "")
    sqlfile = open(sys.path[0] + filepath, 'r')
    sql = sqlfile.read()
    print('running sql')
    stmt = ibm_db.exec_immediate(conn, sql)
    print(type(stmt))
    result = ibm_db.fetch_assoc(stmt)
    result_count = int(result['1'])
    print(result)
    print(type(result))
    result_time = time.strftime('%Y-%m-%d', time.localtime())
    insert_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    table = {'daily': 'add_dailylog',
             'weekly': 'add_dailylog',
             'monthly': 'add_dailylog'}

    if result_count > threshold:
        daily_status = 'Fail'
        resulttab_status = 'Fail'
    else:
        daily_status = 'Success'
        resulttab_status = 'Success'

    query_db_outside(query[table[freqency]], (taskid, result_count, result_time, daily_status, user_id, insert_time, taskname))
    query_db_outside(query['add_resulttab'], (taskname, taskid, result_count, resulttab_status, insert_time, '10s'))
    #(taskname, taskid, result, status, run_time, duration)

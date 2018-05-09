import ibm_db
import sys
import json
from db.query_db import query_db_outside
from .sql import query
import time
from functools import wraps


def run(user_id, taskid, filepath, freqency):
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
    result_count = result['1']
    print(result)
    print(type(result))
    result_time = time.strftime('%Y-%m-%d', time.localtime())
    insert_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    query_db_outside(query['add_dailylog'], (taskid, result_count, result_time, 1, user_id, insert_time))
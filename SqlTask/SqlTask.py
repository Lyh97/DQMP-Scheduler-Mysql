import ibm_db
import sys
import json



class SqlTask(object):

  def __init__(self):
    self.str = 'self'

  def run(self):
    config = open(sys.path[0] + '/SqlTask/config.json', 'r')
    config = config.read()
    config = json.loads(config)
    dns = "DATABASE=%s;HOSTNAME=%s;PORT=%s;PROTOCOL=TCPIP;UID=%s;PWD=%s" % (
    config['database'], config['hostname'], config['port'], config['user_id'], config['password'])
    conn = ibm_db.connect(dns, "", "")


    sqlfile = open(sys.path[0] + '/file/sql/test.sql', 'r')
    sql = sqlfile.read()
    print('running sql')
    stmt = ibm_db.exec_immediate(conn, sql)
    print(type(stmt))
    result = ibm_db.fetch_assoc(stmt)
    print(result)
    # print(sys.path[0])

from _datetime import datetime
from flask import Flask
from flask_apscheduler import APScheduler
from functools import wraps
from Config import Config
from flask import jsonify
from SqlTask import SqlTask


app = Flask(__name__)
scheduler = APScheduler()


# @wraps(None)
def interval_job(*args, **kwargs):
    print('%s: interval job' % datetime.now())
    return interval_job

def runsql():
  sqlTask = SqlTask.SqlTask()
  sqlTask.run()


@app.route('/add_task')
def job1():
  # scheduler.add_job(interval_job, trigger='interval', seconds=5, id='interval_id2')
  # scheduler.add_job(func=interval_job, id='123', trigger='interval', seconds=5)
  # sqlTask = SqlTask.SqlTask()
  scheduler.add_job(func=runsql, id='sql', trigger='interval', seconds=100)
  return 'ok'


if __name__ == '__main__':
    app.config.from_object(Config())

    # scheduler = APScheduler()
    # it is also possible to enable the API directly
    scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    app.run(host='0.0.0.0')

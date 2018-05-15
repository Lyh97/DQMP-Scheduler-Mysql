from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import sys

from datetime import date


class Config(object):
    JOBS = [
        {
            'id': 'jobmiss',
            'func': 'main:interval_job',
            'args': (),
            'trigger': 'date',
            'run_date': date(2018, 5, 13),
            'misfire_grace_time': 60 * 60 * 24
        }
    ]

    SCHEDULER_API_ENABLED = True

    SCHEDULER_JOBSTORES = {
      'default': SQLAlchemyJobStore(url='sqlite:///db/jobs.sqlite')
    }

    SCHEDULER_EXECUTORS = {
      'default': {'type': 'threadpool', 'max_workers': 20}
    }

    UPLOAD_FOLDER = sys.path[0] + '/uploads'

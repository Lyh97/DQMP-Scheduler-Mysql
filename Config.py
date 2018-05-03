from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


class Config(object):
    # JOBS = [
    #     {
    #         'id': 'job5',
    #         'func': 'main:interval_job',
    #         'args': (),
    #         'trigger': 'interval',
    #         'seconds': 10
    #     }
    # ]

    SCHEDULER_API_ENABLED = True

    SCHEDULER_JOBSTORES = {
      'default': SQLAlchemyJobStore(url='sqlite:///db/jobs.sqlite')
    }

    SCHEDULER_EXECUTORS = {
      'default': {'type': 'threadpool', 'max_workers': 20}
    }

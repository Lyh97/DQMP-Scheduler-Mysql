from flask import Flask, g
from flask_apscheduler import APScheduler
from Config import Config
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
scheduler = APScheduler()

DATABASE = './db/taskDB.db'


@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.commit()
        g.db.close()


from task.task import task
app.register_blueprint(task, url_prefix='/task')

from file.file import file
app.register_blueprint(file, url_prefix='/file')

from board.board import board
app.register_blueprint(board, url_prefix='/board')


if __name__ == '__main__':
    app.config.from_object(Config())
    # it is also possible to enable the API directly
    scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()
    CORS(app)
    app.run(host='0.0.0.0')

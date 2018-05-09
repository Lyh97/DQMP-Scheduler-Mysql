


query = {
    'add_task': '''
    INSERT INTO task (taskid, category, owner, email,
                      description, tag, enabled, freqency,
                      task_type, threshold, filepath, upload_time,
                      update_time, upload_user_id)
              VALUES (?, ?, ?, ?,
                      ?, ?, ?, ?,
                      ?, ?, ?, ?,
                      ?, ?)
    ''',
    'select_tasklist': '''
      SELECT * ,
      (select COUNT(taskid)
       from result_tab a
       WHERE a.taskid = task.taskid) as totalrun,
      (select COUNT(taskid)
       from result_tab a
       WHERE a.taskid = task.taskid And a.status = 0) as totalfails
      From task
      ORDER BY last_runtime DESC
    ''',
    'select_task':'''
      select *
      FROM task
      WHERE
      taskid = ?
    '''
}





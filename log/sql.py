


query = {
    'select_tasklist': '''
      SELECT * ,
       (select COUNT(taskid)
         from result_tab a
         WHERE a.taskid = task.taskid) as totalrun,
       (select COUNT(taskid)
         from result_tab a
         WHERE a.taskid = task.taskid And a.status = 'Fail') as totalfails
      From task
      ORDER BY last_runtime DESC
    ''',
    'select_task':'''
      select *
      FROM task
      WHERE
      taskid = ?
    ''',
    'selctTaskLogById': '''
      SELECT *
      FROM result_tab
      WHERE
      taskid = ?
      ORDER BY run_time ASC
    ''',
    'updateComment': '''
      UPDATE result_tab
      SET comments = ?
      WHERE
      id = ?
    ''',
    'SelectDailyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from dailylog
      WHERE result_time = ? AND status = 'Fail')
    ''',
    'SelectWeeklyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from weeklylog
      WHERE result_time = ? AND status = 'Fail')
    ''',
    'SelectMonthlyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from monthlylog
      WHERE result_time = ? AND status = 'Fail')
    '''
}





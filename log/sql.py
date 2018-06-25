


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
      WHERE remove = 0 AND upload_user_id = IFNULL(?,upload_user_id)
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
      ORDER BY run_time DESC
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
      WHERE result_time = ? AND status = 'Fail') AND upload_user_id = IFNULL(?,upload_user_id)
    ''',
    'SelectWeeklyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from weeklylog
      WHERE result_time = ? AND status = 'Fail') AND upload_user_id = IFNULL(?,upload_user_id)
    ''',
    'SelectMonthlyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from monthlylog
      WHERE result_time = ? AND status = 'Fail') AND upload_user_id = IFNULL(?,upload_user_id)
    ''',
    'SelectSpeDailyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from dailylog
      WHERE result_time = ? AND status = 'Fail' AND category = ?) AND upload_user_id = IFNULL(?,upload_user_id)
    ''',
    'SelectSpeWeeklyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from weeklylog
      WHERE result_time = ? AND status = 'Fail' AND category = ?) AND upload_user_id = IFNULL(?,upload_user_id)
    ''',
    'SelectSpeMonthlyErrorList':'''
      SELECT * 
      FROM task 
      WHERE taskid in (SELECT taskid 
      from monthlylog
      WHERE result_time = ? AND status = 'Fail' AND category = ?) AND upload_user_id = IFNULL(?,upload_user_id)
    ''',
    'filtrateSelect':'''
      SELECT * ,
        (select COUNT(taskid) FROM result_tab a WHERE a.taskid = task.taskid) as totalrun,
        (select COUNT(taskid) FROM result_tab a WHERE a.taskid = task.taskid And a.status = 0) as totalfails 
      From task 
      WHERE upload_user_id = IFNULL(?,upload_user_id) AND freqency = IFNULL(?,freqency) AND enabled = IFNULL(?,enabled) AND category = IFNULL(?,category)
    '''
}





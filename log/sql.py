


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
      SELECT a.* 
      FROM
        (SELECT *
            from dailylog
            WHERE result_time = ? AND status = 'Fail' AND user_id = IFNULL(?,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectWeeklyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
            from weeklylog
            WHERE result_time = ? AND status = 'Fail' AND user_id = IFNULL(?,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectMonthlyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
            from monthlylog
            WHERE result_time = ? AND status = 'Fail' AND user_id = IFNULL(?,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectSpeDailyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
            from dailylog
            WHERE result_time = ? AND status = 'Fail' AND category = ? AND user_id = IFNULL(?,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectSpeWeeklyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
          from weeklylog
          WHERE result_time = ? AND status = 'Fail' AND category = ? AND user_id = IFNULL(?,user_id)) b
      LEFT JOIN task a 
      ON a.taskid = b.taskid
    ''',
    'SelectSpeMonthlyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
          from monthlylog
          WHERE result_time = ? AND status = 'Fail' AND category = ? AND user_id = IFNULL(?,user_id)) b
      LEFT JOIN task a 
      ON a.taskid = b.taskid
    ''',
    'filtrateSelect':'''
      SELECT * ,
        (select COUNT(taskid) FROM result_tab a WHERE a.taskid = task.taskid) as totalrun,
        (select COUNT(taskid) FROM result_tab a WHERE a.taskid = task.taskid And a.status = 0) as totalfails 
      From task 
      WHERE upload_user_id = IFNULL(?,upload_user_id) AND freqency = IFNULL(?,freqency) AND enabled = IFNULL(?,enabled) AND category = IFNULL(?,category)
    '''
}





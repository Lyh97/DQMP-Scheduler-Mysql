


query = {
    'select_tasklist': '''
      SELECT * ,
       (select COUNT(taskid)
         from result_tab a
         WHERE a.taskid = t.taskid) as totalrun,
       (select COUNT(taskid)
         from result_tab a
         WHERE a.taskid = t.taskid And a.status = 'Fail') as totalfails,
       (select result FROM result_tab WHERE taskid = t.taskid ORDER BY run_time DESC limit 1) as count
      From task t
      WHERE remove = 0 AND upload_user_id = IFNULL(%s,upload_user_id)
      ORDER BY last_runtime DESC
    ''',
    'select_task':'''
      select *
      FROM task
      WHERE
      taskid = %s
    ''',
    'selctTaskLogById': '''
      SELECT *
      FROM result_tab
      WHERE
      taskid = %s
      ORDER BY run_time DESC
    ''',
    'updateComment': '''
      UPDATE result_tab
      SET comments = %s
      WHERE
      id = %s
    ''',
    'SelectDailyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
            from dailylog
            WHERE result_time = %s AND status = 'Fail' AND user_id = IFNULL(%s,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectWeeklyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
            from weeklylog
            WHERE result_time = %s AND status = 'Fail' AND user_id = IFNULL(%s,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectMonthlyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
            from monthlylog
            WHERE result_time = %s AND status = 'Fail' AND user_id = IFNULL(%s,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectSpeDailyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
            from dailylog
            WHERE result_time = %s AND status = 'Fail' AND category = %s AND user_id = IFNULL(%s,user_id)) b
        LEFT JOIN task a 
        ON a.taskid = b.taskid
    ''',
    'SelectSpeWeeklyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
          from weeklylog
          WHERE result_time = %s AND status = 'Fail' AND category = %s AND user_id = IFNULL(%s,user_id)) b
      LEFT JOIN task a 
      ON a.taskid = b.taskid
    ''',
    'SelectSpeMonthlyErrorList':'''
      SELECT a.* 
      FROM
        (SELECT *
          from monthlylog
          WHERE result_time = %s AND status = 'Fail' AND category = %s AND user_id = IFNULL(%s,user_id)) b
      LEFT JOIN task a 
      ON a.taskid = b.taskid
    ''',
    'filtrateSelect':'''
      SELECT * ,
        (select COUNT(taskid) FROM result_tab a WHERE a.taskid = task.taskid) as totalrun,
        (select COUNT(taskid) FROM result_tab a WHERE a.taskid = task.taskid And a.status = 0) as totalfails 
      From task 
      WHERE upload_user_id = IFNULL(%s,upload_user_id) AND freqency = IFNULL(%s,freqency) AND enabled = IFNULL(%s,enabled) AND category = IFNULL(%s,category)
    ''',
    'SelectTaskOfMike': '''
      SELECT
      (SELECT result FROM result_tab WHERE run_time = MAX(r.run_time) limit 1) as last_count, 
      MAX(r.run_time) as last_runtimes,
      (SELECT result FROM result_tab WHERE run_time = MAX(r.run_time) limit 1) - (SELECT a.result FROM result_tab  a WHERE a.taskid = t.taskid  order by a.run_time desc limit 1,1) as chang, 
      t.*
      FROM   (SELECT * FROM result_tab WHERE taskid in (SELECT taskid from task WHERE category = %s)) r  
      left join task t ON t.taskid = r.taskid  
      group by r.taskid
    ''',
    'selctMikeTaskLogById':'''
      SELECT *
      FROM result_tab
      WHERE
      taskid = %s
      ORDER BY run_time DESC
    '''
}





query = {
    'select_daily': '''
       select result_time as Statistictime ,
       ifnull((select COUNT(taskid)
       FROM dailylog a
       WHERE a.result_time = dailylog.result_time),0) as Totalnumberoftasks,
       ifnull((select COUNT(taskid)
       FROM dailylog b
       where status='Fail' AND b.result_time = dailylog.result_time ),0) as Totalnumberoferrortasks
    FROM dailylog
    WHERE user_id = ?
    GROUP BY result_time
    ''',
    'select_weekly': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM weeklylog a
      WHERE a.result_time = weeklylog.result_time),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM weeklylog b
      where status='Fail' AND b.result_time = weeklylog.result_time ),0) as Totalnumberoferrortasks
    FROM weeklylog
    WHERE user_id = ?
    GROUP BY result_time
    ''',
    'monthly_list': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM monthlylog a
      WHERE a.result_time = monthlylog.result_time),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM monthlylog b
      where status='Fail' AND b.result_time = monthlylog.result_time ),0) as Totalnumberoferrortasks
    FROM monthlylog
    WHERE user_id = ?
    GROUP BY result_time
    ''',

    'select_daily_desc': '''
    select result_time as Statistictime ,
       ifnull((select COUNT(taskid)
       FROM dailylog a
       WHERE a.result_time = dailylog.result_time),0) as Totalnumberoftasks,
       ifnull((select COUNT(taskid)
       FROM dailylog b
       where status='Fail' AND b.result_time = dailylog.result_time ),0) as Totalnumberoferrortasks
    FROM dailylog
    WHERE user_id = ?
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',
    'select_weekly_desc': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM weeklylog a
      WHERE a.result_time = weeklylog.result_time),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM weeklylog b
      where status='Fail' AND b.result_time = weeklylog.result_time ),0) as Totalnumberoferrortasks
    FROM weeklylog
    WHERE user_id = ?
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',
    'monthly_list_desc': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM monthlylog a
      WHERE a.result_time = monthlylog.result_time),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM monthlylog b
      where status='Fail' AND b.result_time = monthlylog.result_time ),0) as Totalnumberoferrortasks
    FROM monthlylog
    WHERE user_id = ?
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',

    'select_fail_daily': '''
    select *
    FROM dailylog
    where result_time in (select max(result_time) from dailylog) AND user_id = ?
    ORDER BY result_time DESC
    ''',
    'select_fail_weekly': '''
    select *
    FROM weeklylog
    where result_time in (select max(result_time) from weeklylog) AND user_id = ?
    ORDER BY result_time DESC
    ''',
    'monthly_fail_list': '''
    select *
    FROM monthlylog
    where result_time in (select max(result_time) from monthlylog) AND user_id = ?
    ORDER BY result_time DESC
    ''',
    'category_select_daily': '''
    select result_time as Statistictime ,
       ifnull((select COUNT(taskid)
       FROM dailylog a
       WHERE a.result_time = dailylog.result_time AND category = ?),0) as Totalnumberoftasks,
       ifnull((select COUNT(taskid)
       FROM dailylog b
       where status='Fail' AND b.result_time = dailylog.result_time AND category = ?),0) as Totalnumberoferrortasks
    FROM dailylog
    WHERE category = ? AND user_id = ?
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',
    'category_select_weekly': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM weeklylog a
      WHERE a.result_time = weeklylog.result_time AND category = ?),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM weeklylog b
      where status='Fail' AND b.result_time = weeklylog.result_time AND category = ?),0) as Totalnumberoferrortasks
    FROM weeklylog
    WHERE category = ? AND user_id = ?
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',
    'category_monthly_list': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM monthlylog a
      WHERE a.result_time = monthlylog.result_time AND category = ?),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM monthlylog b
      where status='Fail' AND b.result_time = monthlylog.result_time AND category = ?),0) as Totalnumberoferrortasks
    FROM monthlylog
    WHERE category = ? AND user_id = ?
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',
    'category_select_fail_daily': '''
    select *
    FROM dailylog
    where result_time in (select max(result_time) from dailylog where category = ?) AND category = ? AND user_id = ?
    ORDER BY result_time DESC 
    ''',
    'category_select_fail_weekly': '''
    select *
    FROM weeklylog
    where result_time in (select max(result_time) from weeklylog where category = ?) AND category = ? AND user_id = ?
    ORDER BY result_time DESC 
    ''',
    'category_monthly_fail_list': '''
    select *
    FROM monthlylog
    where result_time in (select max(result_time) from monthlylog where category = ?) AND category = ? AND user_id = ?
    ORDER BY result_time DESC 
    ''',
    'select_being_performed':'''
    select *
    FROM being_performed
    WHERE status = '1' AND user_id = ?
    ''',
    'select_execution_results':'''
    select *
    FROM execution_results 
    WHERE user_id = ?
    '''
}
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
    GROUP BY result_time 
    ORDER BY result_time DESC
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
    GROUP BY result_time
    ORDER BY result_time DESC
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
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',
    'select_fail_daily': '''
    select *
    FROM dailylog
    where result_time in (select max(result_time) from dailylog)
    ORDER BY result_time DESC
    ''',
    'select_fail_weekly': '''
    select *
    FROM weeklylog
    where result_time in (select max(result_time) from weeklylog)
    ORDER BY result_time DESC
    ''',
    'monthly_fail_list': '''
    select *
    FROM monthlylog
    where result_time in (select max(result_time) from monthlylog)
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
    WHERE category = ?
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
    WHERE category = ?
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
    WHERE category = ?
    GROUP BY result_time
    ORDER BY result_time DESC
    ''',
    'category_select_fail_daily': '''
    select *
    FROM dailylog
    where result_time in (select max(result_time) from dailylog where category = ?) AND category = ?
    ORDER BY result_time DESC 
    ''',
    'category_select_fail_weekly': '''
    select *
    FROM weeklylog
    where result_time in (select max(result_time) from weeklylog where category = ?) AND category = ?
    ORDER BY result_time DESC 
    ''',
    'category_monthly_fail_list': '''
    select *
    FROM monthlylog
    where result_time in (select max(result_time) from monthlylog where category = ?) AND category = ?
    ORDER BY result_time DESC 
    '''
}
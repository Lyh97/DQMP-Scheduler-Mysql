query = {
    'select_daily': '''
    select result_time as Statistictime ,
       ifnull((select COUNT(taskid)
       FROM dailylog a
       WHERE a.result_time = dailylog.result_time),0) as Totalnumberoftasks,
       ifnull((select COUNT(taskid)
       FROM dailylog b
       where status=0 AND b.result_time = dailylog.result_time ),0) as Totalnumberoferrortasks
    FROM dailylog
    GROUP BY result_time
    ''',
    'select_weekly': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM weeklylog a
      WHERE a.result_time = weeklylog.result_time),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM weeklylog b
      where status=0 AND b.result_time = weeklylog.result_time ),0) as Totalnumberoferrortasks
    FROM weeklylog
    GROUP BY result_time
    ''',
    'monthly_list': '''
    select result_time as Statistictime ,
      ifnull((select COUNT(taskid)
      FROM monthlylog a
      WHERE a.result_time = monthlylog.result_time),0) as Totalnumberoftasks,
      ifnull((select COUNT(taskid)
      FROM monthlylog b
      where status=0 AND b.result_time = monthlylog.result_time ),0) as Totalnumberoferrortasks
    FROM monthlylog
    GROUP BY result_time
    '''
}
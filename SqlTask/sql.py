





query = {
    'add_dailylog': '''
    INSERT INTO dailylog (taskid, result_count, result_time, status, user_id, insert_time, taskname)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    'add_weeklylog': '''
    INSERT INTO dailylog (taskid, result_count, result_time, status, user_id, insert_time, taskname)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    'add_monthlylog': '''
    INSERT INTO dailylog (taskid, result_count, result_time, status, user_id, insert_time, taskname)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    'add_resulttab': '''
    INSERT INTO result_tab (taskname, taskid, result, status, run_time, duration)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
}
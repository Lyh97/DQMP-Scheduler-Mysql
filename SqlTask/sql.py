





query = {
    'add_dailylog': '''
    INSERT INTO dailylog (taskid, result_count, result_time, status, user_id, insert_time, taskname, category, description)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''',
    'add_weeklylog': '''
    INSERT INTO weeklylog (taskid, result_count, result_time, status, user_id, insert_time, taskname, category, description)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''',
    'add_monthlylog': '''
    INSERT INTO monthlylog (taskid, result_count, result_time, status, user_id, insert_time, taskname, category, description)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''',
    'add_resulttab': '''
    INSERT INTO result_tab (taskname, taskid, result, status, run_time, duration)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''',
    'tasklog':'''
    INSERT INTO tasklog (taskname, taskid, status, description, insert_time)
    VALUES (%s, %s, %s, %s, %s)
    '''
}

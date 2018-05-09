





query = {
    'add_dailylog': '''
    INSERT INTO dailylog (taskid, result_count, result_time, status, user_id, insert_time)
    VALUES (?, ?, ?, ?, ?, ?)
    ''',
    'add_weeklylog': '''
    INSERT INTO dailylog (taskid, result_count, result_time, status, user_id, insert_time)
    VALUES (?, ?, ?, ?, ?, ?)
    ''',
    'add_monthlylog': '''
    INSERT INTO dailylog (taskid, result_count, result_time, status, user_id, insert_time)
    VALUES (?, ?, ?, ?, ?, ?)
    ''',
}
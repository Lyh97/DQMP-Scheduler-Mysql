


query = {
    'add_task': '''
    INSERT INTO task (taskid, category, owner, email,
                      description, tag, enabled, freqency,
                      task_type, threshold, filepath, upload_time,
                      update_time, content, upload_user_id, taskname)
              VALUES (%s, %s, %s, %s,
                      %s, %s, %s, %s,
                      %s, %s, %s, %s,
                      %s, %s, %s, %s)
    ''',
    'update_task': '''
    UPDATE task
    SET category=%s, owner=%s, email=%s, description=%s, tag=%s, freqency=%s,
    task_type=%s, threshold=%s, content=%s, update_time=%s, upload_user_id=%s, taskname=%s
    WHERE taskid=%s
    ''',
    'remove_task': '''
    UPDATE task
    SET remove=1
    WHERE taskid=%s
    '''
}





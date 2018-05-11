


query = {
    'add_task': '''
    INSERT INTO task (taskid, category, owner, email,
                      description, tag, enabled, freqency,
                      task_type, threshold, filepath, upload_time,
                      update_time, upload_user_id)
              VALUES (?, ?, ?, ?,
                      ?, ?, ?, ?,
                      ?, ?, ?, ?,
                      ?, ?)
    '''
}





query = {
    'selectUserInfo':'''
        SELECT * from sys_user_tab WHERE username = ? AND password = ?
    ''',
    'selectUserImg':'''
        SELECT imgpath from sys_user_tab WHERE username = ?
    '''
}
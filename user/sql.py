query = {
    'selectUserInfo':'''
        SELECT * from sys_user_tab WHERE username = %s AND password = %s
    ''',
    'selectUserImg':'''
        SELECT imgpath from sys_user_tab WHERE username = %s
    ''',
    'selectUserImgByUserid':'''
        SELECT imgpath from sys_user_tab WHERE user_id = %s
    '''
}
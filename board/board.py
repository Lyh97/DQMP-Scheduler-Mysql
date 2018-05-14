from db.query_db import query_db_outside
from flask import Blueprint, jsonify, request
from .sql import query

board = Blueprint('board', __name__)

# 查询daily数据
@board.route('/daily_list', methods=['GET','POST'])
def selectDailyListByUserId():
    dailyList = query_db_outside(query['select_daily'])

    daily_date_list=[]
    daily_data = []
    daily_err = []

    for i in dailyList:
      daily_date_list.append(i['Statistictime'])
      daily_data.append(i['Totalnumberoftasks'])
      daily_err.append(i['Totalnumberoferrortasks'])

    dailyLists = []
    dailyLists.append(daily_date_list)
    dailyLists.append(daily_data)
    dailyLists.append(daily_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData':dailyList,'chartData':dailyLists}})

# 查询weekly数据
@board.route('/weekly_list', methods=['GET','POST'])
def selectWeeklyByUserId():
    weeklyList = query_db_outside(query['select_weekly'])

    weekly_date_list = []
    weekly_data = []
    weekly_err = []

    for weeklylist in weeklyList:
        weekly_date_list.append(weeklylist['Statistictime'])
        weekly_data.append(weeklylist['Totalnumberoftasks'])
        weekly_err.append(weeklylist['Totalnumberoferrortasks'])

    weeklyLists = []
    weeklyLists.append(weekly_date_list)
    weeklyLists.append(weekly_data)
    weeklyLists.append(weekly_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData': weeklyList, 'chartData': weeklyLists}})

# 查询monthly数据
@board.route('/monthly_list', methods=['GET','POST'])
def selectMonthlyByUserId():
    monthlyList = query_db_outside(query['monthly_list'])

    monthly_date_list = []
    monthly_data = []
    monthly_err = []

    for i in range(len(monthlyList)):
        monthly_date_list.append(monthlyList[i]['Statistictime'])
        monthly_data.append(monthlyList[i]['Totalnumberoftasks'])
        monthly_err.append(monthlyList[i]['Totalnumberoferrortasks'])

    monthlyLists = []
    monthlyLists.append(monthly_date_list)
    monthlyLists.append(monthly_data)
    monthlyLists.append(monthly_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData': monthlyList, 'chartData': monthlyLists}})


# 查询daily错误数据
@board.route('/daily_fail_list', methods=['GET','POST'])
def selectFailDailyList():
    dailyList = query_db_outside(query['select_fail_daily'])
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': dailyList})

# 查询weekly数据
@board.route('/weekly_fail_list', methods=['GET','POST'])
def selectFailWeekly():
    weeklyList = query_db_outside(query['select_fail_weekly'])
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': weeklyList})


# 查询monthly数据
@board.route('/monthly_fail_list', methods=['GET','POST'])
def selectFailMonthly():
    monthlyList = query_db_outside(query['monthly_fail_list'])
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': monthlyList})



# 查询特定类别的daily数据
@board.route('/category_daily_list', methods=['GET','POST'])
def selectDailyListByCategory():
    category = request.args.get('category')

    dailyList = query_db_outside(query['category_select_daily'],(category,category,category,))

    daily_date_list=[]
    daily_data = []
    daily_err = []

    for i in dailyList:
      daily_date_list.append(i['Statistictime'])
      daily_data.append(i['Totalnumberoftasks'])
      daily_err.append(i['Totalnumberoferrortasks'])

    dailyLists = []
    dailyLists.append(daily_date_list)
    dailyLists.append(daily_data)
    dailyLists.append(daily_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData':dailyList,'chartData':dailyLists}})

# 查询特定类别的weekly数据
@board.route('/category_weekly_list', methods=['GET','POST'])
def selectWeeklyByCategory():
    category = request.args.get('category')

    weeklyList = query_db_outside(query['category_select_weekly'],(category,category,category,))

    weekly_date_list = []
    weekly_data = []
    weekly_err = []

    for weeklylist in weeklyList:
        weekly_date_list.append(weeklylist['Statistictime'])
        weekly_data.append(weeklylist['Totalnumberoftasks'])
        weekly_err.append(weeklylist['Totalnumberoferrortasks'])

    weeklyLists = []
    weeklyLists.append(weekly_date_list)
    weeklyLists.append(weekly_data)
    weeklyLists.append(weekly_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData': weeklyList, 'chartData': weeklyLists}})


# 查询特定类别的monthly数据
@board.route('/category_monthly_list', methods=['GET','POST'])
def selectMonthlyByCategory():
    category = request.args.get('category')

    monthlyList = query_db_outside(query['category_monthly_list'],(category,category,category,))

    monthly_date_list = []
    monthly_data = []
    monthly_err = []

    for i in range(len(monthlyList)):
        monthly_date_list.append(monthlyList[i]['Statistictime'])
        monthly_data.append(monthlyList[i]['Totalnumberoftasks'])
        monthly_err.append(monthlyList[i]['Totalnumberoferrortasks'])

    weeklyLists = []
    weeklyLists.append(monthly_date_list)
    weeklyLists.append(monthly_data)
    weeklyLists.append(monthly_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData': monthlyList, 'chartData': weeklyLists}})

# 查询daily错误数据
@board.route('/category_daily_fail_list', methods=['GET','POST'])
def selectCategoryFailDailyList():
    category = request.args.get('category')
    dailyList = query_db_outside(query['category_select_fail_daily'],(category,category,))
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': dailyList})

# 查询weekly数据
@board.route('/category_weekly_fail_list', methods=['GET','POST'])
def selectCategoryFailWeekly():
    category = request.args.get('category')
    weeklyList = query_db_outside(query['category_select_fail_weekly'],(category,category,))
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': weeklyList})


# 查询monthly数据
@board.route('/category_monthly_fail_list', methods=['GET','POST'])
def selectCategoryFailMonthly():
    category = request.args.get('category')
    monthlyList = query_db_outside(query['category_monthly_fail_list'],(category,category,))
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': monthlyList})

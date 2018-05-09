import sqlite3
import sys
from db.query_db import query_db_outside
from flask import Blueprint, jsonify
from .sql import query
from file.file import dict_factory

board = Blueprint('board', __name__)

# 查询daily数据
@board.route('/daily_list', methods=['POST'])
def selectDailyListByUserId():
    dailyList = query_db_outside(query['select_daily'])

    daily_date_list=[]
    daily_data = []
    daily_err = []

    for i in range(len(dailyList)):
      daily_date_list.append(dailyList[i]['Statistictime'])
      daily_data.append(dailyList[i]['Totalnumberoftasks'])
      daily_err.append(dailyList[i]['Totalnumberoferrortasks'])

    dailyLists = []
    dailyLists.append(daily_date_list)
    dailyLists.append(daily_data)
    dailyLists.append(daily_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData':dailyList,'chartData':dailyLists}})

# 查询weekly数据
@board.route('/weekly_list', methods=['POST'])
def selectWeeklyByUserId():
    weeklyList = query_db_outside(query['select_weekly'])

    weekly_date_list = []
    weekly_data = []
    weekly_err = []

    for i in range(len(weeklyList)):
        weekly_date_list.append(weeklyList[i]['Statistictime'])
        weekly_data.append(weeklyList[i]['Totalnumberoftasks'])
        weekly_err.append(weeklyList[i]['Totalnumberoferrortasks'])

    weeklyLists = []
    weeklyLists.append(weekly_date_list)
    weeklyLists.append(weekly_data)
    weeklyLists.append(weekly_err)
    return jsonify({'code': 200, 'meaasge': 'ok', 'data': {'tabData': weeklyList, 'chartData': weeklyLists}})

# 查询monthly数据
@board.route('/monthly_list', methods=['POST'])
def selectMonthlyByUserId():
    monthlyList = query_db_outside(query['monthly_list'])

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
import pandas as pd
import requests
import datetime
from dateutil.relativedelta import relativedelta
import csv
import json
import os
from pymongo import MongoClient
import pymysql
from sqlalchemy import create_engine


wildfire= pymysql.connect(
    user='hy', 
    passwd='multi1234!', 
    host='localhost', 
    db='wildfire', 
    charset='utf8'
)

today = datetime.datetime.today()
month_ago = today - relativedelta(months=1)


cursor = wildfire.cursor(pymysql.cursors.DictCursor)

sql = f"SELECT w.tm as 일시,w.stnNm as 지점명,w.ta as 기온,w.rn as 강수량,w.ws as 풍속,w.wd as 풍향,w.hm as 습도,h.humidcurr as 실효습도 \
FROM weather_info AS w \
JOIN Humidity_info AS h \
ON w.tm = h.tm AND w.stnNm = h.stnNm \
WHERE DATE(w.tm) BETWEEN '{month_ago.strftime('%Y-%m-%d')}' AND '{today.strftime('%Y-%m-%d')}';"

cursor.execute(sql)
result = cursor.fetchall()
result = pd.DataFrame(result)



# # data 형태 일시,지점명,기온,강수량,풍속,풍향,습도,실효습도,label,day_name,Month,hour  <= ?
result['label'] = 0
result['day_name'] = pd.to_datetime(result['일시'], format='%Y-%m-%d %H:%M', errors='raise').dt.day_name()
result['Month'] = pd.to_datetime(result['일시'], format='%Y-%m-%d %H:%M', errors='raise').dt.month
result['hour']= pd.to_datetime(result['일시'], format='%Y-%m-%d %H:%M', errors='raise').dt.hour





#(파일명 수정해야함)
result.to_csv('/home/lab20/airflow/dags/data/processed_data.csv', mode='a', header=False)


import pandas as pd
import requests
import datetime
import time
import csv
import json
import os
from pymongo import MongoClient
import pymysql
from sqlalchemy import create_engine




today = datetime.datetime.today()

con= pymysql.connect(user='hy',passwd='multi1234!',host='localhost', db='wildfire', charset='utf8')
cursor = con.cursor(pymysql.cursors.DictCursor)
sql = f"SELECT analdate FROM wildfire.Forest_fire_forecast_geongug where analdate = '{today.strftime('%Y-%m-%d %H')}';"
dup_check = cursor.execute(sql)


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36'
           
           }

serviceKey = "V+rzIXebDm5pwQpEu5hfSDy9T4AkXgorf0B1Ah0L5rFiwLBY1CDBRDepkZj7VyKHzKVf6M3B+UikY0lCh3OsFw=="
numOfRows = 9999
pageNo = 1
_type = "json"


#전국
all_url = 'http://apis.data.go.kr/1400377/forestPoint/forestPointListGeongugSearch'
#시도
sido_url = 'http://apis.data.go.kr/1400377/forestPoint/forestPointListSidoSearch'
#시군구
sigungu_url = 'http://apis.data.go.kr/1400377/forestPoint/forestPointListSigunguSearch'
#읍면동
umd_url = 'http://apis.data.go.kr/1400377/forestPoint/forestPointListEmdSearch'
#param
params = {'serviceKey':serviceKey, 'numOfRows':numOfRows, 'pageNo':pageNo, '_type':_type}

url_list= [ ['geongug', all_url],['sido',sido_url], ['sigungu',sigungu_url], ['umd',umd_url]]
#, 



# request 접속
def bs(url, params):
    #10번 시도
    for i in range(20):
        time.sleep(1)
        try:
            response = requests.get(url,params=params)
            js = json.loads(response.text)
            if js['response']['header']['resultCode'] != '00':
                continue
            return js

        except:
            continue
        
    return False


#mongodb 접속
client = MongoClient("mongodb://localhost:27017/")
db = client['fire_forecast']


#mysql 접속
# db_connection_str = 'mysql+pymysql://hy:multi1234!@localhost/wildfire'
# db_connection = create_engine(db_connection_str)
# conn = db_connection.connect()



for u in url_list:
    if dup_check == 1:
        break
    collection = db[u[0]]
    res = bs(u[1], params)
    item = res['response']['body']['items']['item']
    
    df = pd.DataFrame(item) if u[0]!='geongug' else pd.DataFrame([item])
    # print(item[0])
    # df.to_csv('/home/lab20/airflow/data/forestPoint/test.csv', index=False, mode='w')
    if not os.path.exists(f"/home/lab20/airflow/data/forestPoint/{u[0]}.csv"):
        df.to_csv(f"/home/lab20/airflow/data/forestPoint/{u[0]}.csv", index=False,mode='w')
    else:
        df.to_csv(f"/home/lab20/airflow/data/forestPoint/{u[0]}.csv", index=False,mode='a', header=False)
    
    # data = item
    # collection.insert_one(data) if u[0]=='geongug' else collection.insert_many(data)
    # df.to_sql(name=f'forest_fire_forecast_{u[0]}', con=db_connection, if_exists='append',index=False)


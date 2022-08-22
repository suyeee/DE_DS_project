from tracemalloc import start
import requests
import json
import pandas as pd


# df = pd.read_csv('C:\Users\c1\mc_python\project_san\산불발생일자19841201-20140619.csv')

url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'

#화재발생시각 2주전이 startDt
startDt = '19860401'
startHh = '01'
endDt = '19860402'
endHh = '01'
stnIds = '114'

times = []

params ={'serviceKey' : 'V+rzIXebDm5pwQpEu5hfSDy9T4AkXgorf0B1Ah0L5rFiwLBY1CDBRDepkZj7VyKHzKVf6M3B+UikY0lCh3OsFw==', 'pageNo' : '1', 'numOfRows' : '999', 'dataType' : 'json', 'dataCd' : 'ASOS', 'dateCd' : 'HR',
        'startDt' : startDt, 'startHh' : startHh, 'endDt' : endDt, 'endHh' : endHh, 'stnIds' : stnIds }

response = requests.get(url, params=params)
js= json.loads(response.text)
item= js['response']['body']['items']['item']

print('일시, 풍속, 풍향, 습도, 기온, 강수량')
for i in range(10):
    
    print(item[i]['tm'],item[i]['ws'],item[i]['wd'],item[i]['hm'],item[i]['ta'],item[i]['rn'],'', sep=' | ')
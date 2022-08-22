import pandas as pd
import numpy as np
import pymysql

df = pd.read_csv('/Users/yunjimin/Desktop/실효습도_train_data/2000-2003_weather.csv')

# 컬럼명 바꾸기
df = df.rename(columns={'지점':'stnId'})
df = df.rename(columns={"일시":'tm'})
df = df.rename(columns={'지점명':"stnNm"})
df = df.rename(columns={'기온(°C)':"ta"})
df = df.rename(columns={'풍향(deg)':"wd"})
df = df.rename(columns={'풍속(m/s)':"ws"})
df = df.rename(columns={'강수량(mm)':"rn"})
df = df.rename(columns={'습도(%)':"hm"})

# 필요컬럼 추리기
df = df[['stnId','stnNm','tm','ta','wd','ws','rn','hm']]

# MySQL에 넣기 위해 null값 None으로 대체
data = df.astype(object).where(pd.notnull(df),None)

# 데이터프레임을 리스트로 바꿈
dic_list = data.values.tolist()
print(type(dic_list))

db = pymysql.connect(host='ec2-35-77-169-139.ap-northeast-1.compute.amazonaws.com', port=3306, user='username', password='password', db='wildfire', charset='utf8') 
cursor = db.cursor() 

sql = 'INSERT INTO weather_info(stnId, stnNm, tm, ta, wd, ws, rn, hm,weather_his_id, rnum,taQcflg, rnQcflg, wsQcFlg, wdQcFlg, hmQcFlg, pv, td, pa, paQcFlg, ps, psQcFlg, ss, ssQcFlg, icsr, dsnw, hr3Fhsc, dc10Tca, dc10LmcsCa, clfmAbbrCd, lcsCh, vs, gndSttCd, dmstMtphNo,ts, tsQcflg, m005Te,m01Te,m02Te,m03Te) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)'

# 데이터베이스 업데이트
cursor.executemany(sql, dic_list)

# 데이터베이스 업데이트 및 작업 종료
db.commit()

# 데이터베이스 닫기 
db.close()

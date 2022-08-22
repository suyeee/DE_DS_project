from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import time

import pandas as pd
import json
import joblib

# 인공지능 부분
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
import joblib
from lightgbm import early_stopping, LGBMClassifier


HOST = "ec2-35-77-169-139.ap-northeast-1.compute.amazonaws.com"
DB_USER   = "yjy"
DB_PASSWD = "1111"
DB_NAME = "wildfire"
conn = f"mysql://{DB_USER}:{DB_PASSWD}@{HOST}/{DB_NAME}?charset=utf8mb4"
engine = create_engine(conn)
Base = declarative_base()


temp_scaler = joblib.load('./temp_scaler.pkl')
ws_scaler = joblib.load('./ws_scaler.pkl')
humid_scaler = joblib.load('./humid_scaler.pkl')
effhumid_scaler = joblib.load('./effhumid_scaler.pkl')

class Weather_Info(Base):
    
    __tablename__ = "weather_info"
    
    weather_his_id = Column(Integer, primary_key=True)
    tm = Column(DateTime)
    rnum = Column(Integer)
    stnId = Column(Integer)
    stnNm = Column(String(6))
    ta = Column(Float)
    taQcflg = Column(Float)
    rn = Column(Float)
    rnQcflg = Column(Float)
    ws = Column(Float)
    wsQcFlg = Column(Float)
    wd = Column(Float)
    wdQcFlg = Column(Float)
    hm = Column(Float)
    hmQcFlg = Column(Float)
    pv = Column(Float)
    td = Column(Float)
    pa = Column(Float)
    paQcFlg = Column(Float)
    ps = Column(Float)
    psQcFlg = Column(Float)
    ss = Column(Float)
    ssQcFlg = Column(Float)
    icsr = Column(Float)
    dsnw = Column(Float)
    hr3Fhsc = Column(Float)
    dc10Tca = Column(Float)
    dc10LmcsCa = Column(Float)
    clfmAbbrCd = Column(String(6))
    lcsCh = Column(Float)
    vs = Column(Float)
    gndSttCd = Column(Float)
    dmstMtphNo = Column(Float)
    ts = Column(Float)
    tsQcflg = Column(Float)
    m005Te = Column(Float)
    m01Te = Column(Float)
    m02Te = Column(Float)
    m03Te = Column(Float)
    
    def __init__(self, tm, rnum, stnId, stnNm, ta, taQcflg, rn, rnQcflg, ws, wsQcflg, wd, wdQcflg, hm, hmQcflg, pv, td, pa, paQcflg, ps, psQcflg, ss, ssQcflg, icsr, dsnw, hr3Fhsc, dc10Tca, dc10LmcsCa, clfmAbbrCd, lcsCh, vs, gndSttCd, dmstMtphNo, ts, tsQcflg, m005Te, m01Te, m02Te, m03Te):
        self.tm = tm
        self.rnum = rnum
        self.stnId = stnId
        self.stnNm = stnNm
        self.ta = ta
        self.taQcflg = taQcflg
        self.rn = rn
        self.rnQcflg = rnQcflg
        self.ws = ws
        self.wsQcFlg = wsQcflg
        self.wd = wd
        self.wdQcFlg = wdQcflg
        self.hm = hm
        self.hmQcFlg = hmQcflg
        self.pv = pv
        self.td = td
        self.pa = pa
        self.paQcFlg = paQcflg
        self.ps = ps
        self.psQcFlg = psQcflg
        self.ss = ss
        self.ssQcFlg = ssQcflg
        self.icsr = icsr
        self.dsnw = dsnw
        self.hr3Fhsc = hr3Fhsc
        self.dc10Tca = dc10Tca
        self.dc10LmcsCa = dc10LmcsCa
        self.clfmAbbrCd = clfmAbbrCd
        self.lcsCh = lcsCh
        self.vs = vs
        self.gndSttCd = gndSttCd
        self.dmstMtphNo = dmstMtphNo
        self.ts = ts
        self.tsQcflg = tsQcflg
        self.m005Te = m005Te
        self.m01Te = m01Te
        self.m02Te = m02Te
        self.m03Te = m03Te
        
    def __repr__(self):
        return "<{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}>".format(self.tm, self.rnum, self.stnId, self.stnNm, self.ta, self.taQcflg, self.rn, self.rnQcflg, self.ws, self.wsQcFlg, self.wd, self.wdQcFlg, self.hm, self.hmQcFlg, self.pv, self.td, self.pa, self.paQcFlg, self.ps, self.psQcFlg, self.ss, self.ssQcFlg, self.icsr, self.dsnw, self.hr3Fhsc, self.dc10Tca, self.dc10LmcsCa, self.clfmAbbrCd, self.lcsCh, self.vs, self.gndSttCd, self.dmstMtphNo, self.ts, self.tsQcflg, self.m005Te, self.m01Te, self.m02Te, self.m03Te)

class Effective_Humidity(Base):
    
    __tablename__ = "Humidity_info" # 수정 필요
    
    prId = Column(Integer,primary_key=True)
    stnId = Column(Integer)
    stnNm = Column(String(12))
    tm = Column(DateTime)
    humidcurr = Column(Float)
    
    def __init__(self, stnId, stnNm, tm, humidcurr):
        self.stnId = stnId
        self.stnNm = stnNm
        self.tm = tm
        self.humidcurr = humidcurr
        
    def __repr__(self):
        return "{}, {}, {}, {}".format(self.stnId, self.stnNm, self.tm, self.humidcurr)
    
Base.metadata.create_all(engine)
Session = sessionmaker(engine) # python-mysql 연결 작업.
sess = Session()


model = joblib.load('./ensemble_model.pkl')
df = pd.read_csv('one_day.csv', encoding='utf-8')

df['sigun_code'] = df['sigun_code'].astype(str)

for i in range(0, 24):
    n = i
    if i<10:
        cond_hour = '0'+str(i)
    else:
        cond_hour = str(i)
    
    weatherInfo = sess.query(Weather_Info).filter(func.substr(Weather_Info.tm,1,13)=='2022-07-24 '+cond_hour).all()
    effHm = sess.query(Effective_Humidity).filter(func.substr(Effective_Humidity.tm,1,13)=='2022-07-24 '+cond_hour).all()


    weather_df_list = []
    effHm_df_list = []
    for i in weatherInfo:
        weather_df_list.append([i.tm, i.stnNm, i.ta, i.rn, i.ws, i.wd, i.hm])
    for i in effHm:
        effHm_df_list.append([i.stnId, i.stnNm, i.tm, i.humidcurr])
        

    weather_df = pd.DataFrame(data=weather_df_list, columns=['일시','지점명','기온','강수량','풍속','풍향','습도'])
    effHm_df = pd.DataFrame(data=effHm_df_list, columns=['지점번호','지점명','일시','실효습도'])
    effHm_df.loc[effHm_df['지점번호']==115,'지점명'] = '울릉도'
    effHm_df.loc[effHm_df['지점번호']==185, '지점명'] = '고산'

    before_predict_df = pd.merge(left = weather_df, right = effHm_df, how = "inner", on='지점명')
    merged_df = before_predict_df.copy()
    before_predict_df = before_predict_df.fillna(0)
    before_predict_df['day_name'] = before_predict_df['일시_x'].dt.day_name()
    before_predict_df['Month'] = before_predict_df['일시_x'].dt.month

    before_predict_df['Month'] = before_predict_df['Month'].astype(str)
    before_predict_df.drop(['일시_x','일시_y', '지점명','풍향','지점번호'], axis=1, inplace=True)

    #scaler = StandardScaler()
    scaled1 = temp_scaler.fit_transform(before_predict_df['기온'].values.reshape(-1, 1))
    before_predict_df.insert(0,'scaled1',scaled1)
    before_predict_df.drop(['기온'], axis=1, inplace=True)

    # scaled2 = ws_scaler.fit_transform(before_predict_df['강수량'].values.reshape(-1, 1))
    # before_predict_df.insert(1,'scaled2',scaled2)
    # before_predict_df.drop(['강수량'], axis=1, inplace=True)

    scaled2 = ws_scaler.fit_transform(before_predict_df['풍속'].values.reshape(-1, 1))
    before_predict_df.insert(2,'scaled3',scaled2)
    before_predict_df.drop(['풍속'], axis=1, inplace=True)

    scaled3 = humid_scaler.fit_transform(before_predict_df['습도'].values.reshape(-1, 1))
    before_predict_df.insert(3,'scaled4',scaled3)
    before_predict_df.drop(['습도'], axis=1, inplace=True)

    scaled4 = effhumid_scaler.fit_transform(before_predict_df['실효습도'].values.reshape(-1, 1))
    before_predict_df.insert(4,'scaled5',scaled4)
    before_predict_df.drop(['실효습도'], axis=1, inplace=True)

    before_predict_df = pd.get_dummies(before_predict_df)

    for i in ['day_name_Sunday','day_name_Monday','day_name_Tuesday','day_name_Wednesday','day_name_Thursday','day_name_Friday','day_name_Saturday']:
        if before_predict_df.columns[4] != i:
            before_predict_df[i]=0.0
    for i in [f'Month_{k}' for k in range(1,13)]:
        if before_predict_df.columns[5] != i:
            before_predict_df[i]=0.0


    proba = model.predict_proba(before_predict_df)[:,1]
    merged_df['proba'] = proba

    df_p=pd.merge(left=merged_df, right=df[['sigun_nm','sigun_code']], how='inner',left_on='지점명',right_on='sigun_nm')
    df_p['일시_x'] = df_p['일시_x'].map(lambda x: x.strftime('%Y-%m-%d %H:%M')) 
    df_p.to_csv('temp_predicted.csv')
    print(str(n)+' updated')
    time.sleep(20)
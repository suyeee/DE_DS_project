import pandas as pd
import json


import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import math

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 인공지능 부분
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import VotingClassifier
# import joblib
# from lightgbm import early_stopping, LGBMClassifier

# HOST = "ec2-35-77-169-139.ap-northeast-1.compute.amazonaws.com"
# DB_USER   = "yjy"
# DB_PASSWD = "1111"
# DB_NAME = "wildfire"
# conn = f"mysql://{DB_USER}:{DB_PASSWD}@{HOST}/{DB_NAME}?charset=utf8mb4"
# engine = create_engine(conn)
# Base = declarative_base()
# class Weather_Info(Base):
    
#     __tablename__ = "weather_info"
    
#     weather_his_id = Column(Integer, primary_key=True)
#     tm = Column(DateTime)
#     rnum = Column(Integer)
#     stnId = Column(Integer)
#     stnNm = Column(String(6))
#     ta = Column(Float)
#     taQcflg = Column(Float)
#     rn = Column(Float)
#     rnQcflg = Column(Float)
#     ws = Column(Float)
#     wsQcFlg = Column(Float)
#     wd = Column(Float)
#     wdQcFlg = Column(Float)
#     hm = Column(Float)
#     hmQcFlg = Column(Float)
#     pv = Column(Float)
#     td = Column(Float)
#     pa = Column(Float)
#     paQcFlg = Column(Float)
#     ps = Column(Float)
#     psQcFlg = Column(Float)
#     ss = Column(Float)
#     ssQcFlg = Column(Float)
#     icsr = Column(Float)
#     dsnw = Column(Float)
#     hr3Fhsc = Column(Float)
#     dc10Tca = Column(Float)
#     dc10LmcsCa = Column(Float)
#     clfmAbbrCd = Column(String(6))
#     lcsCh = Column(Float)
#     vs = Column(Float)
#     gndSttCd = Column(Float)
#     dmstMtphNo = Column(Float)
#     ts = Column(Float)
#     tsQcflg = Column(Float)
#     m005Te = Column(Float)
#     m01Te = Column(Float)
#     m02Te = Column(Float)
#     m03Te = Column(Float)
    
#     def __init__(self, tm, rnum, stnId, stnNm, ta, taQcflg, rn, rnQcflg, ws, wsQcflg, wd, wdQcflg, hm, hmQcflg, pv, td, pa, paQcflg, ps, psQcflg, ss, ssQcflg, icsr, dsnw, hr3Fhsc, dc10Tca, dc10LmcsCa, clfmAbbrCd, lcsCh, vs, gndSttCd, dmstMtphNo, ts, tsQcflg, m005Te, m01Te, m02Te, m03Te):
#         self.tm = tm
#         self.rnum = rnum
#         self.stnId = stnId
#         self.stnNm = stnNm
#         self.ta = ta
#         self.taQcflg = taQcflg
#         self.rn = rn
#         self.rnQcflg = rnQcflg
#         self.ws = ws
#         self.wsQcFlg = wsQcflg
#         self.wd = wd
#         self.wdQcFlg = wdQcflg
#         self.hm = hm
#         self.hmQcFlg = hmQcflg
#         self.pv = pv
#         self.td = td
#         self.pa = pa
#         self.paQcFlg = paQcflg
#         self.ps = ps
#         self.psQcFlg = psQcflg
#         self.ss = ss
#         self.ssQcFlg = ssQcflg
#         self.icsr = icsr
#         self.dsnw = dsnw
#         self.hr3Fhsc = hr3Fhsc
#         self.dc10Tca = dc10Tca
#         self.dc10LmcsCa = dc10LmcsCa
#         self.clfmAbbrCd = clfmAbbrCd
#         self.lcsCh = lcsCh
#         self.vs = vs
#         self.gndSttCd = gndSttCd
#         self.dmstMtphNo = dmstMtphNo
#         self.ts = ts
#         self.tsQcflg = tsQcflg
#         self.m005Te = m005Te
#         self.m01Te = m01Te
#         self.m02Te = m02Te
#         self.m03Te = m03Te
        
#     def __repr__(self):
#         return "<{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}>".format(self.tm, self.rnum, self.stnId, self.stnNm, self.ta, self.taQcflg, self.rn, self.rnQcflg, self.ws, self.wsQcFlg, self.wd, self.wdQcFlg, self.hm, self.hmQcFlg, self.pv, self.td, self.pa, self.paQcFlg, self.ps, self.psQcFlg, self.ss, self.ssQcFlg, self.icsr, self.dsnw, self.hr3Fhsc, self.dc10Tca, self.dc10LmcsCa, self.clfmAbbrCd, self.lcsCh, self.vs, self.gndSttCd, self.dmstMtphNo, self.ts, self.tsQcflg, self.m005Te, self.m01Te, self.m02Te, self.m03Te)

# class Effective_Humidity(Base):
    
#     __tablename__ = "Humidity_info" # 수정 필요
    
#     prId = Column(Integer,primary_key=True)
#     stnId = Column(Integer)
#     stnNm = Column(String(12))
#     tm = Column(DateTime)
#     humidcurr = Column(Float)
    
#     def __init__(self, stnId, stnNm, tm, humidcurr):
#         self.stnId = stnId
#         self.stnNm = stnNm
#         self.tm = tm
#         self.humidcurr = humidcurr
        
#     def __repr__(self):
#         return "{}, {}, {}, {}".format(self.stnId, self.stnNm, self.tm, self.humidcurr)
    
# Base.metadata.create_all(engine)
# Session = sessionmaker(engine) # python-mysql 연결 작업.
# sess = Session()


    # # callback 할때마다 필요한 프로세스
    # weatherInfo = sess.query(Weather_Info).filter(func.substr(Weather_Info.tm,1,10)=='2022-07-24').all()
    # effHm = sess.query(Effective_Humidity).filter(func.substr(Effective_Humidity.tm,1,10)=='2022-07-24').all()


    # weather_df_list = []
    # effHm_df_list = []
    # for i in weatherInfo:
    #     weather_df_list.append([i.tm, i.stnNm, i.ta, i.rn, i.ws, i.wd, i.hm])
    # for i in effHm:
    #     effHm_df_list.append([i.stnId, i.stnNm, i.tm, i.humidcurr])
        

    # weather_df = pd.DataFrame(data=weather_df_list, columns=['일시','지점명','기온','강수량','풍속','풍향','습도'])
    # effHm_df = pd.DataFrame(data=effHm_df_list, columns=['지점번호','지점명','일시','실효습도'])
    # effHm_df.loc[effHm_df['지점번호']==115,'지점명'] = '울릉도'
    # effHm_df.loc[effHm_df['지점번호']==185, '지점명'] = '고산'
    # #print(weather_df)

    # #print()
    # before_predict_df = pd.merge(left = weather_df, right = effHm_df, how = "inner", on='지점명')
    # before_predict_df = before_predict_df.fillna(0)
    # before_predict_df['day_name'] = before_predict_df['일시_x'].dt.day_name()
    # before_predict_df['Month'] = before_predict_df['일시_x'].dt.month
    # print(before_predict_df)
# before_predict_df_copy = before_predict_df.copy()
# before_predict_df_copy['Month'] = before_predict_df_copy['Month'].astype(str)
# before_predict_df_copy.drop(['일시_x','일시_y', '지점명','풍향','지점번호'], axis=1, inplace=True)

# scaler = StandardScaler()
# scaled1 = scaler.fit_transform(before_predict_df_copy['기온'].values.reshape(-1, 1))
# before_predict_df_copy.insert(0,'scaled1',scaled1)
# before_predict_df_copy.drop(['기온'], axis=1, inplace=True)

# scaled2 = scaler.fit_transform(before_predict_df_copy['강수량'].values.reshape(-1, 1))
# before_predict_df_copy.insert(1,'scaled2',scaled2)
# before_predict_df_copy.drop(['강수량'], axis=1, inplace=True)

# scaled3 = scaler.fit_transform(before_predict_df_copy['풍속'].values.reshape(-1, 1))
# before_predict_df_copy.insert(2,'scaled3',scaled3)
# before_predict_df_copy.drop(['풍속'], axis=1, inplace=True)

# scaled4 = scaler.fit_transform(before_predict_df_copy['습도'].values.reshape(-1, 1))
# before_predict_df_copy.insert(3,'scaled4',scaled4)
# before_predict_df_copy.drop(['습도'], axis=1, inplace=True)

# scaled5 = scaler.fit_transform(before_predict_df_copy['실효습도'].values.reshape(-1, 1))
# before_predict_df_copy.insert(4,'scaled5',scaled5)
# before_predict_df_copy.drop(['실효습도'], axis=1, inplace=True)

# before_predict_df_copy = pd.get_dummies(before_predict_df_copy)

    # before_predict_df['Month'] = before_predict_df['Month'].astype(str)
    # before_predict_df.drop(['일시_x','일시_y', '지점명','풍향','지점번호'], axis=1, inplace=True)

    # scaler = StandardScaler()
    # scaled1 = scaler.fit_transform(before_predict_df['기온'].values.reshape(-1, 1))
    # before_predict_df.insert(0,'scaled1',scaled1)
    # before_predict_df.drop(['기온'], axis=1, inplace=True)

    # scaled2 = scaler.fit_transform(before_predict_df['강수량'].values.reshape(-1, 1))
    # before_predict_df.insert(1,'scaled2',scaled2)
    # before_predict_df.drop(['강수량'], axis=1, inplace=True)

    # scaled3 = scaler.fit_transform(before_predict_df['풍속'].values.reshape(-1, 1))
    # before_predict_df.insert(2,'scaled3',scaled3)
    # before_predict_df.drop(['풍속'], axis=1, inplace=True)

    # scaled4 = scaler.fit_transform(before_predict_df['습도'].values.reshape(-1, 1))
    # before_predict_df.insert(3,'scaled4',scaled4)
    # before_predict_df.drop(['습도'], axis=1, inplace=True)

    # scaled5 = scaler.fit_transform(before_predict_df['실효습도'].values.reshape(-1, 1))
    # before_predict_df.insert(4,'scaled5',scaled5)
    # before_predict_df.drop(['실효습도'], axis=1, inplace=True)

    # before_predict_df = pd.get_dummies(before_predict_df)

    # for i in ['day_name_Sunday','day_name_Monday','day_name_Tuesday','day_name_Wednesday','day_name_Thursday','day_name_Friday','day_name_Saturday']:
    #     if before_predict_df.columns[5] != i:
    #         before_predict_df[i]=0.0
    # for i in [f'Month_{k}' for k in range(1,13)]:
    #     if before_predict_df.columns[6] != i:
    #         before_predict_df[i]=0.0

    # print(before_predict_df)

    # # one = pd.concat([before_predict_df_copy, before_predict_df])
    # # print(one.columns)
    # # test = one

    # model = joblib.load('./ensemble_model.pkl')
    # proba = model.predict_proba(before_predict_df)[:,1]
    # before_predict_df['proba'] = proba
    # print(before_predict_df)

    # print(before_predict_df.info())
# end


state_geo1 = json.load(open('map (7).zip.geojson', encoding='utf-8'))
df = pd.read_csv('one_day.csv', encoding='utf-8')
df_p = pd.read_csv('one_day_predicted.csv', encoding='utf-8')
df['sigun_code'] = df['sigun_code'].astype(str)

latitude = 35.565
longitude = 127.986

token = open(".mapbox_token").read()



suburbs = df['stnNm'].str.title().tolist()
suburbs_p = df_p['지점명'].str.title().tolist()

# trace_left = []
# trace_left.append(go.Choroplethmapbox(
#     geojson=state_geo1,
#     locations = df['sigun_code'].tolist(),
#     z=df['ta'].tolist(),
#     text=suburbs,
#     featureidkey='properties.merged',
#     zmin = min(df['ta'].tolist())-0.5,
#     zmax = max(df['ta'].tolist())+0.5,
#     visible=True,
#     subplot='mapbox',
#     colorbar=dict(x=0.7),
#     colorscale='Blackbody',
    
#     hovertemplate="<b>%{text}</b><br><br>" +
#                     "value: %{z}<br>" +
#                     "<extra></extra>"
    
# ))

# trace_right = []
# trace_right.append(go.Bar(
#     x=df.sort_values(['ta'],ascending=False).head(10)['ta'],
#     y=df.sort_values(['ta'],ascending=False).head(10)['stnNm'].str.title().tolist(),
#     xaxis = 'x2',
#     yaxis = 'y2',
#     marker = dict(
#         color='blue',
        
#     ),
#     visible=True,
#     orientation='h',
# ))
# weatherInfo = sess.query(Weather_Info).filter(func.substr(Weather_Info.tm,1,13)==('2022-07-24 00')).all()
# effHm = sess.query(Effective_Humidity).filter(func.substr(Effective_Humidity.tm,1,13)==('2022-07-24 00')).all()
# print(weatherInfo)

# weather_df_list = []
# effHm_df_list = []
# for i in weatherInfo:
#     weather_df_list.append([i.tm, i.stnNm, i.ta, i.rn, i.ws, i.wd, i.hm])
# for i in effHm:
#     effHm_df_list.append([i.stnId, i.stnNm, i.tm, i.humidcurr])
    

# weather_df = pd.DataFrame(data=weather_df_list, columns=['일시','지점명','기온','강수량','풍속','풍향','습도'])
# effHm_df = pd.DataFrame(data=effHm_df_list, columns=['지점번호','지점명','일시','실효습도'])
# effHm_df.loc[effHm_df['지점번호']==115,'지점명'] = '울릉도'
# effHm_df.loc[effHm_df['지점번호']==185, '지점명'] = '고산'

# before_predict_df = pd.merge(left = weather_df, right = effHm_df, how = "inner", on='지점명')
# merged_df = before_predict_df.copy()
# before_predict_df = before_predict_df.fillna(0)
# before_predict_df['day_name'] = before_predict_df['일시_x'].dt.day_name()
# before_predict_df['Month'] = before_predict_df['일시_x'].dt.month

# before_predict_df['Month'] = before_predict_df['Month'].astype(str)
# before_predict_df.drop(['일시_x','일시_y', '지점명','풍향','지점번호'], axis=1, inplace=True)

# scaler = StandardScaler()
# scaled1 = scaler.fit_transform(before_predict_df['기온'].values.reshape(-1, 1))
# before_predict_df.insert(0,'scaled1',scaled1)
# before_predict_df.drop(['기온'], axis=1, inplace=True)

# scaled2 = scaler.fit_transform(before_predict_df['강수량'].values.reshape(-1, 1))
# before_predict_df.insert(1,'scaled2',scaled2)
# before_predict_df.drop(['강수량'], axis=1, inplace=True)

# scaled3 = scaler.fit_transform(before_predict_df['풍속'].values.reshape(-1, 1))
# before_predict_df.insert(2,'scaled3',scaled3)
# before_predict_df.drop(['풍속'], axis=1, inplace=True)

# scaled4 = scaler.fit_transform(before_predict_df['습도'].values.reshape(-1, 1))
# before_predict_df.insert(3,'scaled4',scaled4)
# before_predict_df.drop(['습도'], axis=1, inplace=True)

# scaled5 = scaler.fit_transform(before_predict_df['실효습도'].values.reshape(-1, 1))
# before_predict_df.insert(4,'scaled5',scaled5)
# before_predict_df.drop(['실효습도'], axis=1, inplace=True)

# before_predict_df = pd.get_dummies(before_predict_df)

# for i in ['day_name_Sunday','day_name_Monday','day_name_Tuesday','day_name_Wednesday','day_name_Thursday','day_name_Friday','day_name_Saturday']:
#     if before_predict_df.columns[5] != i:
#         before_predict_df[i]=0.0
# for i in [f'Month_{k}' for k in range(1,13)]:
#     if before_predict_df.columns[6] != i:
#         before_predict_df[i]=0.0


# proba = model.predict_proba(before_predict_df)[:,1]
# merged_df['proba'] = proba

# df_p=pd.merge(left=merged_df, right=df[['sigun_nm','sigun_code']], how='inner',left_on='지점명',right_on='sigun_nm')
# suburbs = df_p['지점명'].str.title().tolist()

layout = go.Layout(
    autosize=True,
    mapbox=dict(
        domain={'x':[0,0.7], 'y':[0,1]},
        center=dict(lat=latitude, lon=longitude),
        style="open-street-map",
        zoom=5
    ),
    xaxis2={
        'domain':[0.77,1],
        'side':'right',
        'anchor':'x2',
    },
    yaxis2={
        'domain':[0,1],
        'anchor':'y2',
        'autorange':'reversed',
    },
    margin=dict(l=80,r=20,t=70,b=70),
    
)
# fig = go.Figure(data=trace_left+trace_right, layout=layout)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#,dbc.themes.BOOTSTRAP

app =Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1('Interactive dashboard for wildfire prediction and weather info'),
    dcc.Dropdown(['WEATHER','WILDFIRE'], 'WEATHER', id = 'map-dropdown',style={"width": 200}),
    dcc.Graph(id="graph"),
    dcc.Interval(
        id = 'interval-component',
        interval=1*20000,
        n_intervals=0
    ),
    
    html.Div([
        html.Div([
        html.H6('산불 통계 확인',style=dict(textAlign='center')),
        html.Button(html.A('바로가기',href='https://public.tableau.com/views/_16588290457790/1_2?:language=ko-KR&:display_count=n&:origin=viz_share_link', title='link'),style={'marginBottom':50, 'align':'center'}),
        html.Div(id='container')
        ], style=dict(textAlign='center')),
        html.Div(id='container2'),
        # html.Div([
        #     dash_table.DataTable(
                
        #         data = df_p.to_dict('records'),
        #         columns=[
        #             {'name' : i, 'id' : i, 'deletable': False, "selectable":False} for i in df_p.columns
        #         ],
        #         editable=False,
        #         filter_action="native",
        #         sort_action="native",
        #         sort_mode="multi",
        #         row_selectable="multi",
        #         row_deletable=False,
        #         selected_rows=[],
        #         page_action="native",
        #         page_current=0,
        #         page_size=6,

        #         style_cell_conditional=[
        #             {
        #                 'if': {'column_id': c},
        #                 'textAlign': 'left'
        #             } for c in ['Date', 'Region']
        #         ],
        #         style_data_conditional=[
        #             {
        #                 'if': {'row_index': 'odd'},
        #                 'backgroundColor': 'rgb(248, 248, 248)'
        #             }
        #         ],
        #         style_header={
        #             'backgroundColor': 'rgb(230, 230, 230)',
        #             'fontWeight': 'bold'
        #         },
                
        #     )
        
        # ])
    ], className='row')

])

@app.callback(
    Output('graph', 'figure'),
    Input('map-dropdown','value'),
    Input('interval-component','n_intervals')
)
def display_choropleth(map_kind, n):
    
    # if (n%24) < 10:
    #     cond_hour = '0'+str(n%4)
    # else:
    #     cond_hour = str(n%24)
    # # callback 할때마다 필요한 프로세스
    # weatherInfo = sess.query(Weather_Info).filter(func.substr(Weather_Info.tm,1,13)==('2022-07-24 00')).all()
    # effHm = sess.query(Effective_Humidity).filter(func.substr(Effective_Humidity.tm,1,13)==('2022-07-24 00')).all()
    # print(weatherInfo)
    
    # weather_df_list = []
    # effHm_df_list = []
    # for i in weatherInfo:
    #     weather_df_list.append([i.tm, i.stnNm, i.ta, i.rn, i.ws, i.wd, i.hm])
    # for i in effHm:
    #     effHm_df_list.append([i.stnId, i.stnNm, i.tm, i.humidcurr])
        

    # weather_df = pd.DataFrame(data=weather_df_list, columns=['일시','지점명','기온','강수량','풍속','풍향','습도'])
    # effHm_df = pd.DataFrame(data=effHm_df_list, columns=['지점번호','지점명','일시','실효습도'])
    # effHm_df.loc[effHm_df['지점번호']==115,'지점명'] = '울릉도'
    # effHm_df.loc[effHm_df['지점번호']==185, '지점명'] = '고산'
    
    # before_predict_df = pd.merge(left = weather_df, right = effHm_df, how = "inner", on='지점명')
    # merged_df = before_predict_df.copy()
    # before_predict_df = before_predict_df.fillna(0)
    # before_predict_df['day_name'] = before_predict_df['일시_x'].dt.day_name()
    # before_predict_df['Month'] = before_predict_df['일시_x'].dt.month
    
    # before_predict_df['Month'] = before_predict_df['Month'].astype(str)
    # before_predict_df.drop(['일시_x','일시_y', '지점명','풍향','지점번호'], axis=1, inplace=True)

    # scaler = StandardScaler()
    # scaled1 = scaler.fit_transform(before_predict_df['기온'].values.reshape(-1, 1))
    # before_predict_df.insert(0,'scaled1',scaled1)
    # before_predict_df.drop(['기온'], axis=1, inplace=True)

    # scaled2 = scaler.fit_transform(before_predict_df['강수량'].values.reshape(-1, 1))
    # before_predict_df.insert(1,'scaled2',scaled2)
    # before_predict_df.drop(['강수량'], axis=1, inplace=True)

    # scaled3 = scaler.fit_transform(before_predict_df['풍속'].values.reshape(-1, 1))
    # before_predict_df.insert(2,'scaled3',scaled3)
    # before_predict_df.drop(['풍속'], axis=1, inplace=True)

    # scaled4 = scaler.fit_transform(before_predict_df['습도'].values.reshape(-1, 1))
    # before_predict_df.insert(3,'scaled4',scaled4)
    # before_predict_df.drop(['습도'], axis=1, inplace=True)

    # scaled5 = scaler.fit_transform(before_predict_df['실효습도'].values.reshape(-1, 1))
    # before_predict_df.insert(4,'scaled5',scaled5)
    # before_predict_df.drop(['실효습도'], axis=1, inplace=True)

    # before_predict_df = pd.get_dummies(before_predict_df)

    # for i in ['day_name_Sunday','day_name_Monday','day_name_Tuesday','day_name_Wednesday','day_name_Thursday','day_name_Friday','day_name_Saturday']:
    #     if before_predict_df.columns[5] != i:
    #         before_predict_df[i]=0.0
    # for i in [f'Month_{k}' for k in range(1,13)]:
    #     if before_predict_df.columns[6] != i:
    #         before_predict_df[i]=0.0
    
    
    # proba = model.predict_proba(before_predict_df)[:,1]
    # merged_df['proba'] = proba
    
    # df_p=pd.merge(left=merged_df, right=df[['sigun_nm','sigun_code']], how='inner',left_on='지점명',right_on='sigun_nm')
    # suburbs = df_p['지점명'].str.title().tolist()
    
    df_p = pd.read_csv('temp_predicted.csv', encoding='utf-8')
    if map_kind=='WEATHER':
        trace_left = []
        trace_left.append(go.Choroplethmapbox(
            geojson=state_geo1,
            locations = df_p['sigun_code'].tolist(),
            z=df_p['기온'].tolist(),
            text=suburbs,
            featureidkey='properties.merged',
            zmin = min(df_p['기온'].tolist())-0.5,
            zmax = max(df_p['기온'].tolist())+0.5,
            visible=True,
            subplot='mapbox',
            colorbar=dict(x=0.7),
            colorscale='bluered',
            
            hovertemplate="<b>%{text}</b><br><br>" +
                            "value: %{z}<br>" +
                            "<extra></extra>"
            
        ))

        trace_right = []
        trace_right.append(go.Bar(
            x=df_p.sort_values(['기온'],ascending=False).head(10)['기온'],
            y=df_p.sort_values(['기온'],ascending=False).head(10)['지점명'].str.title().tolist(),
            xaxis = 'x2',
            yaxis = 'y2',
            marker = dict(
                color='blue',
                
            ),
            visible=True,
            orientation='h',
        ))
    else:
        trace_left = []
        trace_left.append(go.Choroplethmapbox(
            geojson=state_geo1,
            locations = df_p['sigun_code'].tolist(),
            z=df_p['proba'].map(lambda x:x*100).tolist(),
            text=suburbs,
            featureidkey='properties.merged',
            zmin = min(df_p['proba'].map(lambda x:x*100).tolist())-0.5,
            zmax = max(df_p['proba'].map(lambda x:x*100).tolist())+0.5,
            visible=True,
            subplot='mapbox',
            colorbar=dict(x=0.7),
            colorscale='bluered',
            
            hovertemplate="<b>%{text}</b><br><br>" +
                            "value: %{z}<br>" +
                            "<extra></extra>"
            
        ))

        trace_right = []
        trace_right.append(go.Bar(
            x=df_p.sort_values(['proba'],ascending=False).head(10)['proba'],
            y=df_p.sort_values(['proba'],ascending=False).head(10)['지점명'].str.title().tolist(),
            xaxis = 'x2',
            yaxis = 'y2',
            marker = dict(
                color='blue',
                
            ),
            visible=True,
            orientation='h',
        ))
    fig = go.Figure(data=trace_left+trace_right, layout=layout)
    return fig

@app.callback(
    Output('container', 'children'),
    Input('interval-component','n_intervals')
)
def display_proba(n):
    # if (n%24) < 10:
    #     cond_hour = '0'+str(n%24)
    # else:
    #     cond_hour = str(n%24)
    # weatherInfo = sess.query(Weather_Info).filter(func.substr(Weather_Info.tm,1,13)=='2022-07-24 00').all()
    # effHm = sess.query(Effective_Humidity).filter(func.substr(Effective_Humidity.tm,1,13)=='2022-07-24 00').all()

    
    # weather_df_list = []
    # effHm_df_list = []
    # for i in weatherInfo:
    #     weather_df_list.append([i.tm, i.stnNm, i.ta, i.rn, i.ws, i.wd, i.hm])
    # for i in effHm:
    #     effHm_df_list.append([i.stnId, i.stnNm, i.tm, i.humidcurr])
        

    # weather_df = pd.DataFrame(data=weather_df_list, columns=['일시','지점명','기온','강수량','풍속','풍향','습도'])
    # effHm_df = pd.DataFrame(data=effHm_df_list, columns=['지점번호','지점명','일시','실효습도'])
    # effHm_df.loc[effHm_df['지점번호']==115,'지점명'] = '울릉도'
    # effHm_df.loc[effHm_df['지점번호']==185, '지점명'] = '고산'
    
    # before_predict_df = pd.merge(left = weather_df, right = effHm_df, how = "inner", on='지점명')
    # merged_df = before_predict_df.copy()
    # before_predict_df = before_predict_df.fillna(0)
    # before_predict_df['day_name'] = before_predict_df['일시_x'].dt.day_name()
    # before_predict_df['Month'] = before_predict_df['일시_x'].dt.month
    
    # before_predict_df['Month'] = before_predict_df['Month'].astype(str)
    # before_predict_df.drop(['일시_x','일시_y', '지점명','풍향','지점번호'], axis=1, inplace=True)

    # scaler = StandardScaler()
    # scaled1 = scaler.fit_transform(before_predict_df['기온'].values.reshape(-1, 1))
    # before_predict_df.insert(0,'scaled1',scaled1)
    # before_predict_df.drop(['기온'], axis=1, inplace=True)

    # scaled2 = scaler.fit_transform(before_predict_df['강수량'].values.reshape(-1, 1))
    # before_predict_df.insert(1,'scaled2',scaled2)
    # before_predict_df.drop(['강수량'], axis=1, inplace=True)

    # scaled3 = scaler.fit_transform(before_predict_df['풍속'].values.reshape(-1, 1))
    # before_predict_df.insert(2,'scaled3',scaled3)
    # before_predict_df.drop(['풍속'], axis=1, inplace=True)

    # scaled4 = scaler.fit_transform(before_predict_df['습도'].values.reshape(-1, 1))
    # before_predict_df.insert(3,'scaled4',scaled4)
    # before_predict_df.drop(['습도'], axis=1, inplace=True)

    # scaled5 = scaler.fit_transform(before_predict_df['실효습도'].values.reshape(-1, 1))
    # before_predict_df.insert(4,'scaled5',scaled5)
    # before_predict_df.drop(['실효습도'], axis=1, inplace=True)

    # before_predict_df = pd.get_dummies(before_predict_df)

    # for i in ['day_name_Sunday','day_name_Monday','day_name_Tuesday','day_name_Wednesday','day_name_Thursday','day_name_Friday','day_name_Saturday']:
    #     if before_predict_df.columns[5] != i:
    #         before_predict_df[i]=0.0
    # for i in [f'Month_{k}' for k in range(1,13)]:
    #     if before_predict_df.columns[6] != i:
    #         before_predict_df[i]=0.0
    
    
    # proba = model.predict_proba(before_predict_df)[:,1]
    # merged_df['proba'] = proba
    
    # df_p=pd.merge(left=merged_df, right=df[['sigun_nm','sigun_code']], how='inner',left_on='지점명',right_on='sigun_nm')
    
    
    
    df_p = pd.read_csv('temp_predicted.csv', encoding='utf-8')
    return html.Div([
        html.H6('산불 발생 위험 지역 상위 10 지역'),
        html.Div([
            html.Tr([html.Th(i) for i in df_p.sort_values(['proba'],ascending=False).head(10)['지점명'].str.title().tolist()]),
            html.Tr([html.Td(str(round(k*100))+'%') for k in df_p.sort_values(['proba'],ascending=False).head(10)['proba'].tolist()])
        ],style=dict(display='inline-block')),
        
    ],style=dict(textAlign='center'))
    
@app.callback(
    Output('container2', 'children'),
    Input('interval-component', 'n_intervals')
)
def display_table(n):
    # if (n%24) < 10:
    #     cond_hour = '0'+str(n%4)
    # else:
    #     cond_hour = str(n%24)
    # weatherInfo = sess.query(Weather_Info).filter(func.substr(Weather_Info.tm,1,13)=='2022-07-24 00').all()
    # effHm = sess.query(Effective_Humidity).filter(func.substr(Effective_Humidity.tm,1,13)=='2022-07-24 00').all()

    
    # weather_df_list = []
    # effHm_df_list = []
    # for i in weatherInfo:
    #     weather_df_list.append([i.tm, i.stnNm, i.ta, i.rn, i.ws, i.wd, i.hm])
    # for i in effHm:
    #     effHm_df_list.append([i.stnId, i.stnNm, i.tm, i.humidcurr])
        

    # weather_df = pd.DataFrame(data=weather_df_list, columns=['일시','지점명','기온','강수량','풍속','풍향','습도'])
    # effHm_df = pd.DataFrame(data=effHm_df_list, columns=['지점번호','지점명','일시','실효습도'])
    # effHm_df.loc[effHm_df['지점번호']==115,'지점명'] = '울릉도'
    # effHm_df.loc[effHm_df['지점번호']==185, '지점명'] = '고산'
    
    # before_predict_df = pd.merge(left = weather_df, right = effHm_df, how = "inner", on='지점명')
    # merged_df = before_predict_df.copy()
    # before_predict_df = before_predict_df.fillna(0)
    # before_predict_df['day_name'] = before_predict_df['일시_x'].dt.day_name()
    # before_predict_df['Month'] = before_predict_df['일시_x'].dt.month
    
    # before_predict_df['Month'] = before_predict_df['Month'].astype(str)
    # before_predict_df.drop(['일시_x','일시_y', '지점명','풍향','지점번호'], axis=1, inplace=True)

    # scaler = StandardScaler()
    # scaled1 = scaler.fit_transform(before_predict_df['기온'].values.reshape(-1, 1))
    # before_predict_df.insert(0,'scaled1',scaled1)
    # before_predict_df.drop(['기온'], axis=1, inplace=True)

    # scaled2 = scaler.fit_transform(before_predict_df['강수량'].values.reshape(-1, 1))
    # before_predict_df.insert(1,'scaled2',scaled2)
    # before_predict_df.drop(['강수량'], axis=1, inplace=True)

    # scaled3 = scaler.fit_transform(before_predict_df['풍속'].values.reshape(-1, 1))
    # before_predict_df.insert(2,'scaled3',scaled3)
    # before_predict_df.drop(['풍속'], axis=1, inplace=True)

    # scaled4 = scaler.fit_transform(before_predict_df['습도'].values.reshape(-1, 1))
    # before_predict_df.insert(3,'scaled4',scaled4)
    # before_predict_df.drop(['습도'], axis=1, inplace=True)

    # scaled5 = scaler.fit_transform(before_predict_df['실효습도'].values.reshape(-1, 1))
    # before_predict_df.insert(4,'scaled5',scaled5)
    # before_predict_df.drop(['실효습도'], axis=1, inplace=True)

    # before_predict_df = pd.get_dummies(before_predict_df)

    # for i in ['day_name_Sunday','day_name_Monday','day_name_Tuesday','day_name_Wednesday','day_name_Thursday','day_name_Friday','day_name_Saturday']:
    #     if before_predict_df.columns[5] != i:
    #         before_predict_df[i]=0.0
    # for i in [f'Month_{k}' for k in range(1,13)]:
    #     if before_predict_df.columns[6] != i:
    #         before_predict_df[i]=0.0
    
    
    # proba = model.predict_proba(before_predict_df)[:,1]
    # merged_df['proba'] = proba
    
    # df_p=pd.merge(left=merged_df, right=df[['sigun_nm','sigun_code']], how='inner',left_on='지점명',right_on='sigun_nm')
    df_p = pd.read_csv('temp_predicted.csv', encoding='utf-8')
    df_p = df_p[['일시_x', '지점명','기온', '강수량','풍속','풍향','습도','지점번호','실효습도','proba']]
    df_p = df_p.rename(columns={'일시_x':'일시'})
    return dash_table.DataTable(
                
                data = df_p.to_dict('records'),
                columns=[
                    {'name' : i, 'id' : i, 'deletable': False, "selectable":False} for i in df_p.columns
                ],
                editable=False,
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                row_selectable="multi",
                row_deletable=False,
                selected_rows=[],
                page_action="native",
                page_current=0,
                page_size=6,

                style_cell_conditional=[
                    {
                        'if': {'column_id': c},
                        'textAlign': 'left'
                    } for c in ['Date', 'Region']
                ],
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ],
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                
            )






app.run_server(debug=True)
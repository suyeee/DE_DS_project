import pandas as pd

df = pd.read_csv('기상데이터_2차(0707).csv')

values_list = []

for a in list(df['지점번호'].unique()):

  for i in range(len(df.loc[df['지점번호'] == a, '일시'].to_list())):

    b = df.loc[df['지점번호'] == a, '지점명'].values[i]
    c = df.loc[df['지점번호'] == a, '일시'].values[i]
    d = df.loc[df['지점번호'] == a, '기온'].values[i]
    e = df.loc[df['지점번호'] == a, '강수량'].values[i]
    f = df.loc[df['지점번호'] == a, '풍속'].values[i]
    g = df.loc[df['지점번호'] == a, '풍향'].values[i]
    h = df.loc[df['지점번호'] == a, '습도'].values[i]

    values_dict = {'stnld' : a, 'stnNm' : b, 'tm' : c, 'ta' : d, 'rn' : e, 'ws' : f, 'wd' : g, 'hm' : h}
    values_list.append(values_dict)
 
# 리스트 저장하기
import pickle

f = open('climate_lst.pickle', 'wb')
pickle.dump(values_list, f)
f.close()
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score 
from sklearn.metrics import roc_auc_score 
from sklearn.model_selection import train_test_split 
from lightgbm import LGBMClassifier 
from imblearn.under_sampling import OneSidedSelection 
from imblearn.combine import SMOTEENN 
from collections import Counter 
import seaborn as sns 
import matplotlib.pyplot as plt 
import warnings 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import VotingClassifier 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier 
from xgboost import XGBClassifier 
from lightgbm import LGBMClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import plot_tree 
from sklearn.model_selection import cross_validate 
from sklearn.model_selection import KFold 
from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import VotingClassifier 
import joblib


#python 3.8에서 작동
#source activate 8

df = pd.read_csv('/home/lab20/airflow/dags/data/processed_data.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('hour', axis=1, inplace=True)
df0 = df[df['label']==0].sample(n=80000)
df1 = df[df['label']==1]
df = pd.concat([df0,df1])

# 정규화 함수 
def get_preprocessed_df(df=None): 
    df_copy = df.copy() 
    # print(df.keys())
    df_copy['Month'] = df_copy['Month'].astype(str) 
    # df_copy['hour'] = df_copy['hour']
    df_copy.drop(['일시','지점명','풍향'], axis=1, inplace=True) 
    scaler = StandardScaler() 
    scaled1 = scaler.fit_transform(df_copy['기온'].values.reshape(-1, 1)) 
    df_copy.insert(0, 'scaled1', scaled1) 
    df_copy.drop(['기온'], axis=1, inplace=True) 
    scaled2 = scaler.fit_transform(df_copy['강수량'].values.reshape(-1, 1)) 
    df_copy.insert(1, 'scaled2', scaled2) 
    df_copy.drop(['강수량'], axis=1, inplace=True) 
    scaled3 = scaler.fit_transform(df_copy['풍속'].values.reshape(-1, 1)) 
    df_copy.insert(2, 'scaled3', scaled3) 
    df_copy.drop(['풍속'], axis=1, inplace=True) 
    scaled4 = scaler.fit_transform(df_copy['습도'].values.reshape(-1, 1))

    df_copy.insert(3, 'scaled4', scaled4) 
    df_copy.drop(['습도'], axis=1, inplace=True) 
    scaled5 = scaler.fit_transform(df_copy['실효습도'].values.reshape(-1, 1)) 
    df_copy.insert(4, 'scaled5', scaled5) 
    df_copy.drop(['실효습도'], axis=1, inplace=True) 
    # 정규화한 후 카테고리형 
    df_copy = pd.get_dummies(df_copy) 
    return df_copy 


# 사전 데이터 가공 후 학습과 테스트 데이터 세트를 반환하는 함수. 
def get_train_test_dataset(df=None): 
    # 인자로 입력된 DataFrame의 사전 데이터 가공이 완료된 복사 DataFrame 반환 
    df_copy = get_preprocessed_df(df) 
    # DataFrame의 맨 마지막 컬럼이 레이블, 나머지는 피처들 
    X_features = df_copy.drop('label',axis = 1) 
    y_target = df['label'] 
    # train_test_split( )으로 학습과 테스트 데이터 분할. 
    # stratify=y_target으로 Stratified 기반 분할 
    X_train, X_test, y_train, y_test = train_test_split(X_features, y_target, test_size=0.3, random_state=111, stratify=y_target) 
    # 학습과 테스트 데이터 세트 반환 
    return X_train, X_test, y_train, y_test 

# 검증 수치 표시 함수 
def get_clf_eval(y_test, pred=None, pred_proba=None): 
    confusion = confusion_matrix( y_test, pred) 
    accuracy = accuracy_score(y_test , pred) 
    precision = precision_score(y_test , pred) 
    recall = recall_score(y_test , pred) 
    f1 = f1_score(y_test,pred) 
    # ROC-AUC 추가 
    roc_auc = roc_auc_score(y_test, pred_proba) 
    print('오차 행렬') 
    print(confusion) 
    # ROC-AUC print 추가 
    print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f},F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc)) 

# 인자로 사이킷런의 Estimator객체와, 학습/테스트 데이터 세트를 입력 받아서 
# 학습/예측/평가 수행. 
def get_model_train_eval(model, ftr_train=None, ftr_test=None, 
    tgt_train=None, tgt_test=None): 
    model.fit(ftr_train, tgt_train) 
    pred = model.predict(ftr_test) 
    pred_proba = model.predict_proba(ftr_test)[:, 1] 
    get_clf_eval(tgt_test, pred, pred_proba) 

# 학습 데이터셋 구성 
X_train, X_test, y_train, y_test = get_train_test_dataset(df) 

#모델 로드 코드
model = joblib.load('/home/lab20/airflow/dags/data/model/final_model.pkl')
model.fit(X_train,y_train)

# # # 모델 저장 코드
joblib.dump(model, '/home/lab20/airflow/dags/data/model/final_model.pkl')
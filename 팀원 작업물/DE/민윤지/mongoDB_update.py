# 파이썬으로 MongoDB에 데이터 저장하기

from pymongo import MongoClient   #mongodb 모듈 지정
import datetime
import pprint

from bson.objectid import ObjectId  #objectid 모듈 지정

# mongodb 연결객체 생성
client = MongoClient()  #접속IP, 포트
client = MongoClient('mongodb://35.77.169.139:27017/')

# 데이터베이스 개체 가져오기
# db = client['------']
db = client.dbMYJ

# 데이터베이스에 앞서 생성한 리스트 넣기
db.users.insert_many(row)

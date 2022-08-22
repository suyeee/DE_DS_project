from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from kafka import KafkaConsumer

import json

from datetime import datetime
import pymysql
pymysql.install_as_MySQLdb()

BROKERS = ['localhost:9092']
TOPIC_NAME = "effective_humidity_topic"

# sqlalchemy variables
HOST = "ec2-35-77-169-139.ap-northeast-1.compute.amazonaws.com"
DB_USER   = "yjy"
DB_PASSWD = "1111"
DB_NAME = "wildfire"
conn = f"mysql://{DB_USER}:{DB_PASSWD}@{HOST}/{DB_NAME}?charset=utf8mb4"

engine = create_engine(conn)

Base = declarative_base()

# 실효습도 테이블
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
Session = sessionmaker(engine)
sess = Session()



# Consumer 생성
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BROKERS)

# 들어오는 데이터는 모두 데이터베이스에 저장
for message in consumer:
    row = json.loads(message.value.decode())
    print(row)
    # row_list = row.split(',')
    effHm = Effective_Humidity(str(row['stnId']), row['stnNm'], row['tmHh'], row['he'].strip())
    print(effHm)

    sess.add(effHm)
    sess.commit()
    print(row)
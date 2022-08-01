from kafka import KafkaConsumer, KafkaProducer
import json
import MySQLdb
from sqlalchemy import *

HOST = "ec2-35-77-169-139.ap-northeast-1.compute.amazonaws.com"
DB_USER   = "hsy"
DB_PASSWD = "1111"
DB_NAME = "wildfire"
conn = f"mysql://{DB_USER}:{DB_PASSWD}@{HOST}/{DB_NAME}?charset=utf8"

engine = create_engine(conn, encoding='utf-8')

connection = engine.connect()
metadata = MetaData()
table = Table('weather_info', metadata, autoload=True, autoload_with=engine)

CLIMATE_TOPIC = "climate_topic"

BROKER_SERVER = ["localhost:2121"]

consumer = KafkaConsumer(CLIMATE_TOPIC, bootstrap_servers=BROKERS)

for message in consumer:
    msg = json,loads(message.value.decode())


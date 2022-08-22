from kafka import KafkaProducer

BROKER_SERVER = ["localhost:9092"]
TOPIC_NAME = 'first_tutor_topic'

producer = KafkaProducer(bootstrap_servers=BROKER_SERVER)
producer.send(TOPIC_NAME, b'hello world')
producer.flush()
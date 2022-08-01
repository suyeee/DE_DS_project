from kafka import KafkaConsumer

BROKER_SERVER = ["localhost:2121"]
TOPIC_NAME = "climate_topic"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BROKER_SERVER)


for message in consumer:
    print(message)
    







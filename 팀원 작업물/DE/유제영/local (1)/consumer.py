from kafka import KafkaConsumer

BROKER_SERVER = ['localhost:9092']
TOPIC_NAME = 'first_tutor_topic'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BROKER_SERVER)
print('Wait....')

for message in consumer:
    print(message)

print("Done....")
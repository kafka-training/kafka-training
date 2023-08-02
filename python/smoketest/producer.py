from kafka import KafkaProducer
import time

# Initialize the Kafka producer 
producer = KafkaProducer(bootstrap_servers='10.35.125.xxx:9092')

# Topic to which messages will be sent
topic = 'my-topic'

# Sending messages to the topic
for i in range(5):
    message = f"Message {i}"
    producer.send(topic, value=message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)  # Sleep for 1 second between each message

# Flush the producer to ensure all messages are sent
producer.flush()

# Close the producer
producer.close()

# Tips:
# check server, what topics are there:
# $ kafka-topics.sh --list --bootstrap-server <broker_list>
# check topic:
# $ kafka-topics.sh --describe --bootstrap-server <broker_list> --topic <topic_name>


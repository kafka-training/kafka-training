from kafka import KafkaProducer
import time

# Initialize the Kafka producer 
producer = KafkaProducer(bootstrap_servers='10.35.125.101:9092')

# Topic to which messages will be sent
topic = 'my-topic'

# Sending messages to the topic
for i in range(5):
    message = f"Message {i+10}"
    producer.send(topic, value=message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)  # Sleep for 1 second between each message

# Flush the producer to ensure all messages are sent
producer.flush()

# Close the producer
producer.close()

from kafka import KafkaConsumer

# Initialize the Kafka consumer 
consumer = KafkaConsumer( 
    bootstrap_servers='10.35.125.xxx:9092',
    auto_offset_reset="earliest"
  )

consumer.subscribe(['my-topic'])


# Consume messages from the topic
try:
    for messages in consumer:
        print(f"Received: {messages.value.decode('utf-8')}")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    consumer.close()
from kafka import KafkaConsumer

# Initialize the Kafka consumer
consumer = KafkaConsumer( 
    bootstrap_servers='10.35.125.xxx:9092',
    group_id="python-consumer-group2",
    # enable_auto_commit=True,
    # group_id=os.environ["CONSUMER_GROUP"],
    # key_deserializer=lambda x: json.loads(x.decode("utf-8")),
    # value_deserializer=lambda x: json.loads(x.decode("utf-8"))
  )
consumer.subscribe(['my-topic'])

# Consume messages from the topic
try:
    for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    consumer.close()


# check what consumer groups are there:
# $ kafka-consumer-groups.sh --list --bootstrap-server <broker_list>    
# check consumer group:
# $ kafka-consumer-groups.sh --describe --bootstrap-server <broker_list> --group <consumer_group_name>
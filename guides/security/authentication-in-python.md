# Authentication in Python  

Step 1: Install the Required Libraries Make sure you have `confluent-kafka-python` installed. You can install it using pip:

```
pip install confluent-kafka

```

Step 2: Configure SCRAM Credentials As described in the previous steps, you need to create SCRAM credentials for the user on the Kafka broker using the `kafka-configs.sh` tool.

Step 3: Write the Python Producer/Consumer Code For the producer:

```
from confluent_kafka import Producer

# Kafka broker properties
bootstrap_servers = 'your_broker_hostname:9092'

# SASL properties
sasl_mechanism = 'SCRAM-SHA-256'
security_protocol = 'SASL_PLAINTEXT'
sasl_plain_username = 'your_username'
sasl_plain_password = 'your_password'

# Kafka topic to produce messages to
topic = 'your_topic_name'

# Producer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'security.protocol': security_protocol,
    'sasl.mechanisms': sasl_mechanism,
    'sasl.username': sasl_plain_username,
    'sasl.password': sasl_plain_password
}

# Create the Kafka producer
producer = Producer(conf)

# Produce a message
message = "Hello, Kafka!"
producer.produce(topic, message.encode('utf-8'))
producer.flush()

```

For the consumer:

```
from confluent_kafka import Consumer, KafkaError

# Kafka broker properties
bootstrap_servers = 'your_broker_hostname:9092'

# SASL properties
sasl_mechanism = 'SCRAM-SHA-256'
security_protocol = 'SASL_PLAINTEXT'
sasl_plain_username = 'your_username'
sasl_plain_password = 'your_password'

# Kafka topic to consume messages from
topic = 'your_topic_name'

# Consumer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'your_consumer_group',
    'security.protocol': security_protocol,
    'sasl.mechanisms': sasl_mechanism,
    'sasl.username': sasl_plain_username,
    'sasl.password': sasl_plain_password
}

# Create the Kafka consumer
consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe([topic])

# Consume messages
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Reached end of partition.')
            else:
                print('Error occurred: {}'.format(msg.error().str()))
        else:
            print('Received message: {}'.format(msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

```

Replace `your_broker_hostname`, `your_topic_name`, `your_username`, and `your_password` with appropriate values.
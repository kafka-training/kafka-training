# SCRAM Authentication without JAAS

Step 1: Enable SASL in Kafka Broker Configuration Edit the Kafka broker configuration file (server.properties) and add/modify the following properties:

```
listeners=SASL_PLAINTEXT://your_broker_hostname:9092
security.inter.broker.protocol=SASL_PLAINTEXT
sasl.mechanism.inter.broker.protocol=SCRAM-SHA-256

```

Step 2: Configure SCRAM Users on Kafka Broker Generate SCRAM credentials for the users who will be allowed to authenticate to the Kafka broker. Use the `kafka-configs.sh` tool as explained in the previous response:

```
bin/kafka-configs.sh --zookeeper your_zookeeper_connect_string --alter --add-config 'SCRAM-SHA-256=[iterations=<iterations>,password=<user_password>]' --entity-type users --entity-name <username>

```

Replace the following placeholders in the command:

-   `<iterations>`: The number of iterations to be used in the SCRAM algorithm (e.g., 8192).
-   `<user_password>`: The password for the user.
-   `<username>`: The username for which you want to create SCRAM credentials.

Step 3: Start Kafka Broker Start the Kafka broker as you would normally do without any additional JAAS configuration:

```
bin/kafka-server-start.sh -daemon server.properties

```

Step 4: Produce or Consume Data with SCRAM Authentication When starting the Kafka producer or consumer, provide the necessary SASL properties directly without using a JAAS configuration file:

For the producer:

```
bin/kafka-console-producer.sh --broker-list your_broker_hostname:9092 --topic your_topic_name --producer-property security.protocol=SASL_PLAINTEXT --producer-property sasl.mechanism=SCRAM-SHA-256 --producer-property sasl.jaas.config="org.apache.kafka.common.security.scram.ScramLoginModule required username=<username> password=<user_password>;"

```

For the consumer:

```
bin/kafka-console-consumer.sh --bootstrap-server your_broker_hostname:9092 --topic your_topic_name --consumer-property security.protocol=SASL_PLAINTEXT --consumer-property sasl.mechanism=SCRAM-SHA-256 --consumer-property sasl.jaas.config="org.apache.kafka.common.security.scram.ScramLoginModule required username=<username> password=<user_password>;"

```

Replace `your_broker_hostname`, `your_topic_name`, `<username>`, and `<user_password>` with appropriate values.
# SCRAM with JAAS (Both Sides)  

Configuring SASL (Simple Authentication and Security Layer) using SCRAM (Salted Challenge Response Authentication Mechanism) in Kafka involves several steps. SCRAM is a secure authentication mechanism that helps protect your Kafka cluster from unauthorized access. Below are the step-by-step instructions, along with command examples and configuration file examples:

Step 1: Enable SASL in Kafka Broker Configuration Edit the Kafka broker configuration file (server.properties) and add/modify the following properties:

```
listeners=SASL_PLAINTEXT://your_broker_hostname:9092
security.inter.broker.protocol=SASL_PLAINTEXT
sasl.mechanism.inter.broker.protocol=SCRAM-SHA-256

```

Step 2: Configure SCRAM Users on Kafka Broker Generate SCRAM credentials for the users who will be allowed to authenticate to the Kafka broker.

```
# Use kafka-configs.sh tool to add SCRAM credentials for users
bin/kafka-configs.sh --zookeeper your_zookeeper_connect_string --alter --add-config 'SCRAM-SHA-256=[iterations=<iterations>,password=<user_password>]' --entity-type users --entity-name <username>

```

Replace the following placeholders in the command:

-   `<iterations>`: The number of iterations to be used in the SCRAM algorithm (e.g., 8192).
-   `<user_password>`: The password for the user.
-   `<username>`: The username for which you want to create SCRAM credentials.

Step 3: Configure Kafka Server JAAS (Java Authentication and Authorization Service) Configuration Create a JAAS configuration file (kafka\_server\_jaas.conf) and add the following content:

```
KafkaServer {
    org.apache.kafka.common.security.scram.ScramLoginModule required
    username="<username>"
    password="<user_password>";
};

```

Replace `<username>` and `<user_password>` with the actual username and password created in Step 2.

Step 4: Start Kafka Broker with JAAS Configuration Start the Kafka broker with the JAAS configuration file specified:

```
bin/kafka-server-start.sh -daemon server.properties --override security.inter.broker.protocol=SASL_PLAINTEXT --override sasl.mechanism.inter.broker.protocol=SCRAM-SHA-256 --override sasl.jaas.config=your_path/kafka_server_jaas.conf

```

Replace `your_path` with the path to the directory containing kafka\_server\_jaas.conf.

Step 5: Configure Kafka Client JAAS Configuration Create a JAAS configuration file (kafka\_client\_jaas.conf) and add the following content:

```
KafkaClient {
    org.apache.kafka.common.security.scram.ScramLoginModule required
    username="<username>"
    password="<user_password>";
};

```

Replace `<username>` and `<user_password>` with the actual username and password created in Step 2.

Step 6: Produce or Consume Data with SCRAM Authentication Start a Kafka producer or consumer with the JAAS configuration file specified:

```
bin/kafka-console-producer.sh --broker-list your_broker_hostname:9092 --topic your_topic_name --producer.config your_path/kafka_client_jaas.conf

```

Or for the consumer:

```
bin/kafka-console-consumer.sh --bootstrap-server your_broker_hostname:9092 --topic your_topic_name --consumer.config your_path/kafka_client_jaas.conf --from-beginning

```

Replace `your_path`, `your_broker_hostname`, and `your_topic_name` with appropriate values.
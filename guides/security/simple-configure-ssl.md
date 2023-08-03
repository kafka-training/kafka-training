# Simple SSL Configuration

**Step 1: Generate SSL Certificates**

1.  Generate a private key and self-signed certificate for the broker:

```
keytool -genkeypair -v -keystore broker-keystore.jks -keyalg RSA -keysize 2048 -alias broker -validity 365

```

You will be prompted to set a password for the keystore and the private key. Use the same password for simplicity.

2.  Export the broker's certificate from the keystore:

```
keytool -exportcert -v -keystore broker-keystore.jks -alias broker -file broker-cert.pem

```

**Step 2: Create the Truststore**

1.  Import the broker's certificate into the truststore:

```
keytool -importcert -v -keystore truststore.jks -alias broker -file broker-cert.pem

```

You will be prompted to set a password for the truststore. Use a secure password and remember it as you'll need it later.

**Step 3: Configure Kafka Broker**

Create a `server.properties` file for the Kafka broker and add the following SSL-related configurations:

```
propertiesCopy codelisteners=SSL://<broker-hostname>:9093
security.inter.broker.protocol=SSL
ssl.keystore.location=/path/to/broker-keystore.jks
ssl.keystore.password=<keystore-password>
ssl.key.password=<key-password>

```

Replace `<broker-hostname>` with the actual hostname of your Kafka broker, and `<keystore-password>` and `<key-password>` with the passwords you set during the keystore generation.

**Step 4: Configure Kafka Clients (Producer and Consumer)**

For each Kafka client (producer and consumer), you need to configure SSL settings in the respective properties file.

1.  **Producer Configuration (`producer.properties`)**

```
propertiesCopy codebootstrap.servers=<broker-hostname>:9093
security.protocol=SSL
ssl.truststore.location=/path/to/truststore.jks
ssl.truststore.password=<truststore-password>

```

Replace `<broker-hostname>` with the actual hostname of your Kafka broker, and `<truststore-password>` with the password you set for the truststore.

2.  **Consumer Configuration (`consumer.properties`)**

```
propertiesCopy codebootstrap.servers=<broker-hostname>:9093
security.protocol=SSL
ssl.truststore.location=/path/to/truststore.jks
ssl.truststore.password=<truststore-password>

```

Replace `<broker-hostname>` with the actual hostname of your Kafka broker, and `<truststore-password>` with the password you set for the truststore.

**Step 5: Start Kafka Broker**

Run the Kafka broker with the `server.properties` file:

```
bin/kafka-server-start.sh config/server.properties

```

**Step 6: Start Kafka Producer**

Run the Kafka producer with the `producer.properties` file:

```
bin/kafka-console-producer.sh --topic <topic-name> --broker-list <broker-hostname>:9093 --producer.config config/producer.properties

```

**Step 7: Start Kafka Consumer**

Run the Kafka consumer with the `consumer.properties` file:

```
bin/kafka-console-consumer.sh --topic <topic-name> --bootstrap-server <broker-hostname>:9093 --consumer.config config/consumer.properties

```

Replace `<topic-name>` with the name of the Kafka topic you want to produce/consume messages to/from, and `<broker-hostname>` with the actual hostname of your Kafka broker.
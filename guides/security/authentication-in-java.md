# Authentication in Java

Step 1: Add Kafka Client Library Dependency Ensure that you have the Kafka client library added to your Java project's dependencies. If you are using Maven, add the following to your `pom.xml`:

```
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>2.8.0</version> <!-- Replace with the desired version -->
</dependency>

```

Step 2: Write the Java Producer/Consumer Code For the producer:

```
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;
import java.util.Properties;

public class KafkaProducerExample {
    public static void main(String[] args) {
        // Kafka broker properties
        String bootstrapServers = "your_broker_hostname:9092";

        // SASL properties
        String saslMechanism = "SCRAM-SHA-256";
        String securityProtocol = "SASL_PLAINTEXT";
        String saslPlainUsername = "your_username";
        String saslPlainPassword = "your_password";

        // Kafka topic to produce messages to
        String topic = "your_topic_name";

        // Producer configuration
        Properties props = new Properties();
        props.put("bootstrap.servers", bootstrapServers);
        props.put("key.serializer", StringSerializer.class.getName());
        props.put("value.serializer", StringSerializer.class.getName());
        props.put("security.protocol", securityProtocol);
        props.put("sasl.mechanism", saslMechanism);
        props.put("sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"" + saslPlainUsername + "\" password=\"" + saslPlainPassword + "\";");

        // Create the Kafka producer
        Producer<String, String> producer = new org.apache.kafka.clients.producer.KafkaProducer<>(props);

        // Produce a message
        String message = "Hello, Kafka!";
        producer.send(new ProducerRecord<>(topic, message));

        // Close the producer
        producer.close();
    }
}

```

For the consumer:

```
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import java.util.Collections;
import java.util.Properties;

public class KafkaConsumerExample {
    public static void main(String[] args) {
        // Kafka broker properties
        String bootstrapServers = "your_broker_hostname:9092";

        // SASL properties
        String saslMechanism = "SCRAM-SHA-256";
        String securityProtocol = "SASL_PLAINTEXT";
        String saslPlainUsername = "your_username";
        String saslPlainPassword = "your_password";

        // Kafka topic to consume messages from
        String topic = "your_topic_name";

        // Consumer configuration
        Properties props = new Properties();
        props.put("bootstrap.servers", bootstrapServers);
        props.put("key.deserializer", StringDeserializer.class.getName());
        props.put("value.deserializer", StringDeserializer.class.getName());
        props.put("group.id", "your_consumer_group");
        props.put("security.protocol", securityProtocol);
        props.put("sasl.mechanism", saslMechanism);
        props.put("sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"" + saslPlainUsername + "\" password=\"" + saslPlainPassword + "\";");

        // Create the Kafka consumer
        Consumer<String, String> consumer = new KafkaConsumer<>(props);

        // Subscribe to the topic
        consumer.subscribe(Collections.singletonList(topic));

        // Consume messages
        try {
            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(100);
                records.forEach(record -> {
                    System.out.println("Received message: " + record.value());
                });
            }
        } finally {
            // Close the consumer
            consumer.close();
        }
    }
}

```

Replace `your_broker_hostname`, `your_topic_name`, `your_username`, and `your_password` with appropriate values.
package com.igjb;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import java.util.Properties;

public class KafkaProducerDemo {
    public static void main(String[] args) {
        String topicName = "demo-topic";
        String bootstrapServers = "10.35.125.102:9092";

        Properties props = new Properties();
        props.put("bootstrap.servers", bootstrapServers);
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        try (KafkaProducer<String, String> producer = new KafkaProducer<>(props)) {
            String message = "Hello, Kafka! x";
            ProducerRecord<String, String> record = new ProducerRecord<>(topicName, message);
            producer.send(record);
            System.out.println("Message sent: " + message);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

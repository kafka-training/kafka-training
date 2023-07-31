package com.igjb;

import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.TopicPartition;

import java.util.Collections;
import java.util.Properties;
import java.time.Duration;

public class KafkaConsumerDemo {
    public static void main(String[] args) {
        String topicName = "demo-topic";
        String bootstrapServers = "10.35.125.101:9092";

        Properties props = new Properties();
        props.put("bootstrap.servers", bootstrapServers);
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        try (Consumer<String, String> consumer = new KafkaConsumer<>(props)) {
            // You don't need to subscribe to a specific topic when not using consumer groups
            // consumer.subscribe(Collections.singletonList(topicName));

            // Instead, manually assign the partitions you want to consume from
            consumer.assign(Collections.singleton(new TopicPartition(topicName, 0))); // Assuming partition 0
            consumer.seekToBeginning(Collections.singleton(new TopicPartition(topicName, 0)));

            while (true) {
                Duration timeout = Duration.ofMillis(100);
                ConsumerRecords<String, String> records = consumer.poll(timeout);
                records.forEach(record -> {
                    System.out.println("Received message: " + record.value());
                });
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

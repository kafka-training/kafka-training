1 / 1

Sure! Here are some of the most useful Kafka command-line interface (CLI) commands:

1.  **Create a Topic:**

```
kafka-topics.sh --create --topic <topic_name> --bootstrap-server <broker_list> --partitions <num_partitions> --replication-factor <replication_factor>

```

2.  **List Topics:**

```
kafka-topics.sh --list --bootstrap-server <broker_list>

```

3.  **Describe Topic:**

```
kafka-topics.sh --describe --topic <topic_name> --bootstrap-server <broker_list>

```

4.  **Produce Messages:**

```
kafka-console-producer.sh --topic <topic_name> --bootstrap-server <broker_list>

```

(Note: Use Ctrl+C to exit the producer console.)

5.  **Consume Messages:**

```
kafka-console-consumer.sh --topic <topic_name> --bootstrap-server <broker_list> [--from-beginning]

```

6.  **Consumer Group Listing:**

```
kafka-consumer-groups.sh --list --bootstrap-server <broker_list>

```

7.  **Consumer Group Description:**

```
kafka-consumer-groups.sh --describe --group <group_name> --bootstrap-server <broker_list>

```

8.  **Alter Configurations:**

```
kafka-configs.sh --zookeeper <zookeeper_host:port> --alter --entity-type topics --entity-name <topic_name> --add-config <config_key>=<config_value>

```

9.  **View Broker List:**

```
zookeeper-shell.sh <zookeeper_host:port> ls /brokers/ids

```

10.  **View Kafka Broker Configuration:**

```
kafka-configs.sh --describe --entity-type brokers --entity-name <broker_id> --bootstrap-server <broker_list>

```

Remember to replace `<topic_name>`, `<broker_list>`, `<num_partitions>`, `<replication_factor>`, `<group_name>`, and `<broker_id>` with the appropriate values specific to your Kafka cluster.

These commands are commonly used for managing and interacting with Kafka topics, messages, consumers, and brokers from the command-line interface. The Kafka CLI offers various options and functionalities for managing Kafka clusters efficiently. Always refer to the official Kafka documentation for the most up-to-date and comprehensive list of available commands and their usages.
# Add kafka to cluster

To add an existing single-node Kafka instance to another Kafka cluster, you need to follow these steps:

1.  **Optionally Backup Existing Kafka Configuration:** Before making any changes, create a backup of the existing Kafka configuration on the single-node instance. This ensures that you can revert to the original state if needed.
    
2.  **Stop the Single-Node Kafka Instance:** Stop the Kafka service on the single-node instance to prevent any conflicts during the configuration process.
    
3.  **Configure the New Kafka Cluster:** Obtain the configuration details of the new Kafka cluster, including the broker list, ZooKeeper connection string, and any security settings (if applicable).
    
4.  **Update Kafka Configuration:** Update the configuration file (`server.properties`) of the single-node Kafka instance to match the configuration of the new Kafka cluster. Make sure to adjust the following properties:
    
    -   `broker.id`: Ensure that the `broker.id` is unique within the new Kafka cluster. You may need to change this value to avoid conflicts with existing brokers in the cluster.
    -   `listeners`: Update the `listeners` property to listen on the appropriate interface and port based on the new cluster's requirements.
    -   `advertised.listeners`: Set the advertised listeners to the publicly accessible address and port of the single-node Kafka instance. This should be reachable from other brokers and clients in the new cluster.
    -   `log.dirs`: Update the `log.dirs` property to specify the directory where Kafka stores its data (e.g., topics and partitions). Make sure this directory exists and is accessible by the Kafka process.
5.  **Join ZooKeeper Ensemble:** Ensure that the ZooKeeper ensemble used by the single-node Kafka instance matches the ZooKeeper ensemble used by the new Kafka cluster. Update the ZooKeeper connection string in the Kafka configuration (`zookeeper.connect`) to point to the correct ZooKeeper quorum used by the new Kafka cluster.
    
6.  **Start the Single-Node Kafka Instance:** After updating the Kafka configuration, start the Kafka service on the single-node instance.
    
7.  **Monitor Kafka Logs:** Monitor the Kafka logs for any issues or errors during the startup process. Ensure that the Kafka instance successfully connects to the new Kafka cluster and becomes part of the cluster.
    
8.  **Test Connectivity:** Test connectivity between the single-node Kafka instance and the brokers in the new Kafka cluster. Use Kafka command-line tools (`kafka-topics`, `kafka-console-producer`, `kafka-console-consumer`, etc.) to create topics and produce/consume messages.
    
9.  **Rebalance and Replication:** As the single-node Kafka instance joins the new cluster, ensure that the topic partitions are properly distributed across the brokers and the replication factor is set correctly.


## Appendix A: Sample Kafka Configurations

**Single-Node Kafka Instance Configuration (`server.properties`):**

```
propertiesCopy code# Single-Node Kafka Configuration

# Broker ID for the single-node Kafka instance
broker.id=0

# Listeners to accept client connections (adjust the IP and port as needed)
listeners=PLAINTEXT://10.10.10.1:9092

# Advertised listeners for clients to connect to this broker (adjust the IP and port as needed)
advertised.listeners=PLAINTEXT://10.10.10.1:9092

# Directory where Kafka stores its data (topics and partitions)
log.dirs=/path/to/single_node_kafka_data

# ZooKeeper connection string for the single-node Kafka instance
zookeeper.connect=10.30.30.1:2181

# Other Kafka configuration properties (adjust as needed)

```

**New Kafka Cluster Configuration (`server.properties`):**

For each broker in the new Kafka cluster (`server.properties` on each node):

**Broker 1 (`server.properties`):**

```
propertiesCopy code# New Kafka Cluster - Broker 1 Configuration

# Broker ID for this broker (should be unique within the cluster)
broker.id=1

# Listeners to accept client connections (adjust the IP and port as needed)
listeners=PLAINTEXT://10.20.20.1:9092

# Advertised listeners for clients to connect to this broker (adjust the IP and port as needed)
advertised.listeners=PLAINTEXT://10.20.20.1:9092

# Directory where Kafka stores its data (topics and partitions)
log.dirs=/path/to/kafka_data_1

# ZooKeeper connection string for the new Kafka cluster
zookeeper.connect=10.30.30.1:2181,10.30.30.2:2181,10.30.30.3:2181

# Other Kafka configuration properties (adjust as needed)

```

**Broker 2 (`server.properties`):**

```
propertiesCopy code# New Kafka Cluster - Broker 2 Configuration

# Broker ID for this broker (should be unique within the cluster)
broker.id=2

# Listeners to accept client connections (adjust the IP and port as needed)
listeners=PLAINTEXT://10.20.20.2:9092

# Advertised listeners for clients to connect to this broker (adjust the IP and port as needed)
advertised.listeners=PLAINTEXT://10.20.20.2:9092

# Directory where Kafka stores its data (topics and partitions)
log.dirs=/path/to/kafka_data_2

# ZooKeeper connection string for the new Kafka cluster
zookeeper.connect=10.30.30.1:2181,10.30.30.2:2181,10.30.30.3:2181

# Other Kafka configuration properties (adjust as needed)

```

**Broker 3 (`server.properties`):**

```
propertiesCopy code# New Kafka Cluster - Broker 3 Configuration

# Broker ID for this broker (should be unique within the cluster)
broker.id=3

# Listeners to accept client connections (adjust the IP and port as needed)
listeners=PLAINTEXT://10.20.20.3:9092

# Advertised listeners for clients to connect to this broker (adjust the IP and port as needed)
advertised.listeners=PLAINTEXT://10.20.20.3:9092

# Directory where Kafka stores its data (topics and partitions)
log.dirs=/path/to/kafka_data_3

# ZooKeeper connection string for the new Kafka cluster
zookeeper.connect=10.30.30.1:2181,10.30.30.2:2181,10.30.30.3:2181

# Other Kafka configuration properties (adjust as needed)

```

Make sure to replace `/path/to/single_node_kafka_data`, `/path/to/kafka_data_1`, `/path/to/kafka_data_2`, and `/path/to/kafka_data_3` with the actual paths for data storage on each node.

## Appendix B: Smoke Test

```
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create \
                      --topic my_topic \
                      --partitions 3 \
                      --replication-factor 3
```

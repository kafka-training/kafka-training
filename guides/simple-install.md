## Simple install and smoke test


This guide assumes that you are running a relatively recent version of Ubuntu and you have `sudo` privileges.

**Step 1: Update System**

Open Terminal and update your Ubuntu system to have the latest packages.

```
sudo apt-get update
sudo apt-get upgrade

```

**Step 2: Install Java**

Kafka needs Java to run. You can install Java (OpenJDK 8) using the following commands:

```
sudo apt-get install openjdk-8-jdk

```

Verify the installation:

```
java -version

```

**Step 3: Download Kafka**

You can download Kafka from the official Apache website. At the time of writing this, the latest Kafka version is 2.8.0 (Please check the latest version on the official Apache Kafka site).

```
wget http://apache.mirrors.hoobly.com/kafka/2.8.0/kafka_2.13-2.8.0.tgz

```

**Step 4: Extract Kafka**

Next, extract the downloaded Kafka archive file:

```
tar xzf kafka_2.13-2.8.0.tgz

```

**Step 5: Move Kafka**

Optionally, you can move the Kafka directory to a location of your choice. Here, we'll move it to the `/usr/local/kafka` directory:

```
sudo mv kafka_2.13-2.8.0 /usr/local/kafka

```

**Step 6: Start Zookeeper Service**

Before starting Kafka, you need to start the Zookeeper service. Kafka uses Zookeeper to store metadata about the Kafka cluster, as well as consumer client details.

```
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties

```

You should keep this terminal open and running. Alternatively, you can start the Zookeeper service in the background by appending `&` at the end of the command.

**Step 7: Start Kafka Server**

Open a new terminal and navigate to the Kafka directory (unless you started Zookeeper in the background). Now, you can start the Kafka server:

```
cd /usr/local/kafka
bin/kafka-server-start.sh config/server.properties

```

**Step 8: Test Kafka**

You can test the Kafka installation by creating a topic, producing some messages, and consuming them.

-   Create a topic:

```
bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

```

-   List topics to verify the creation:

```
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

```

-   Start a message producer:

```
bin/kafka-console-producer.sh --topic test --broker-list localhost:9092

```

You can then type some messages in this terminal. Press `Ctrl+C` to stop the producer.

-   Start a message consumer in a new terminal:

```
bin/kafka-console-consumer.sh --topic test --from-beginning --bootstrap-server localhost:9092

```

You should see the messages produced earlier in this terminal.

And that's it! You have set up a single-node Kafka on your Ubuntu system. Note that this setup is only suitable for development and testing purposes. For a production setup, you need a multi-node Kafka cluster and possibly a separate Zookeeper ensemble for improved reliability and performance.
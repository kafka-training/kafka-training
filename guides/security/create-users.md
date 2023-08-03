# Create Users

Step 1: Start ZooKeeper and Kafka Server Before creating users, ensure that ZooKeeper and Kafka are up and running.

Step 2: Create the Users Open a terminal or command prompt and execute the following commands to create three users:

User 1:

```
bin/kafka-configs.sh --zookeeper your_zookeeper_connect_string --alter --add-config 'SCRAM-SHA-256=[iterations=8192,password=user1_password]' --entity-type users --entity-name user1

```

User 2:

```
bin/kafka-configs.sh --zookeeper your_zookeeper_connect_string --alter --add-config 'SCRAM-SHA-256=[iterations=8192,password=user2_password]' --entity-type users --entity-name user2

```

User 3:

```
bin/kafka-configs.sh --zookeeper your_zookeeper_connect_string --alter --add-config 'SCRAM-SHA-256=[iterations=8192,password=user3_password]' --entity-type users --entity-name user3

```

Replace `your_zookeeper_connect_string` with the connection string of your ZooKeeper ensemble (e.g., localhost:2181) and set the passwords (e.g., `user1_password`, `user2_password`, `user3_password`) accordingly for each user.

Each command creates a new user with a unique username and password and enables SCRAM-SHA-256 authentication for them.

After executing these commands, you should have three users (`user1`, `user2`, and `user3`) in your Kafka cluster, ready to use SASL with SCRAM for authentication.
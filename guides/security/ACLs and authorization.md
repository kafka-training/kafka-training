# ACLs and authorization


To grant specific permissions to users for a topic and restrict their access to certain actions in Kafka, you can use Access Control Lists (ACLs). Kafka provides fine-grained access control using ACLs to manage read, write, and other operations on topics. Here are the steps to achieve the desired permissions:

Step 1: Grant Permissions to Topic "my-topic"

Assuming you have already created the three users (`user1`, `user2`, and `user3`) with SCRAM authentication as described in the previous steps, you can grant them the necessary permissions on the topic "my-topic" using the `kafka-acls.sh` tool:

User 1 (Read and Write):

```
bin/kafka-acls.sh --authorizer-properties zookeeper.connect=your_zookeeper_connect_string --add --allow-principal User:user1 --operation Read --operation Write --topic my-topic

```

User 2 (Read-only):

```
bin/kafka-acls.sh --authorizer-properties zookeeper.connect=your_zookeeper_connect_string --add --allow-principal User:user2 --operation Read --topic my-topic

```

User 3 (Full Control):

```
bin/kafka-acls.sh --authorizer-properties zookeeper.connect=your_zookeeper_connect_string --add --allow-principal User:user3 --operation All --topic my-topic

```

Replace `your_zookeeper_connect_string` with the connection string of your ZooKeeper ensemble (e.g., localhost:2181).

Step 2: Restrict Topic Creation

By default, all users have permission to create new topics in Kafka. To restrict topic creation for `user1` and `user2`, you need to set the appropriate ACLs:

```
# Deny topic creation for user1 and user2
bin/kafka-acls.sh --authorizer-properties zookeeper.connect=your_zookeeper_connect_string --add --deny-principal User:user1 --operation Create --topic '*'
bin/kafka-acls.sh --authorizer-properties zookeeper.connect=your_zookeeper_connect_string --add --deny-principal User:user2 --operation Create --topic '*'

```

To allow topic creation for `user3`:

```
# Allow topic creation for user3
bin/kafka-acls.sh --authorizer-properties zookeeper.connect=your_zookeeper_connect_string --add --allow-principal User:user3 --operation Create --topic '*'

```

Now, `user1` and `user2` will not be able to create new topics, while `user3` will have permission to create new topics.
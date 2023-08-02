# Add ZooKeeper to an Ensemble

To reset a standalone ZooKeeper installation and join it to an existing one-node ensemble, you'll need to perform a series of steps. Please note that this process assumes you have administrative access to the server running ZooKeeper and are familiar with managing ZooKeeper instances. It's essential to take backups of your data before proceeding, as resetting ZooKeeper will result in data loss.

Here are the general steps to reset and join the standalone ZooKeeper node to an existing ensemble:

Step 1: Stop the ZooKeeper service Make sure to stop the standalone ZooKeeper service before proceeding. You can use the following command to stop it:

```
$ bin/zkServer.sh stop

```

...in case of our systemd service:

```
$ systemctl stop kafka-zookeeper

```

Step 2: Remove data directory Remove the data directory (or specific data files) associated with the standalone ZooKeeper instance. For example:

```
$ rm -rf /path/to/zookeeper/dataDir/*


Step 3: Edit the configuration Open the ZooKeeper configuration file (`zoo.cfg`) in an editor and ensure the following settings are correct: (note in a kafka installation the zookeeper configuration file is located at `config/zookeeper.properties`)

```
server.1=existing_zk_server_ip:port
server.2=new_zk_server_ip:port
```

Replace `existing_zk_server_ip` and `port` with the IP address and port of the existing ZooKeeper server in the ensemble. If you are unsure about the server number (`server.1`), you can check the `myid` file in the `dataDir` directory to find the server number associated with the standalone instance.

Step 4: Do the same on the existing ZooKeeper server. Edit the configuration file on the existing ZooKeeper server in the ensemble and add the following line:

```
$ systemctl stop kafka-zookeeper
```

```
server.1=existing_zk_server_ip:port
server.2=new_zk_server_ip:port
```


Step 5: Start ZooKeepers After editing the configuration, start the ZooKeeper service on both the new and existing ZooKeeper servers:

```
$ bin/zkServer.sh start

```
...in case of our systemd service:

```
$ systemctl start kafka-zookeeper

```


Step 6: Verify status Check the status of the ZooKeeper ensemble to ensure that the standalone node has successfully joined the existing one-node ensemble:

```
$ bin/zkServer.sh status

```

...in case of our systemd service:

```
$ systemctl status kafka-zookeeper

```

If everything is set up correctly, you should see both the new and the existing node listed as part of the ensemble.


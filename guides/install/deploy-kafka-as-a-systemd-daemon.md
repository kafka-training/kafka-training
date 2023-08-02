# Kafka installation with systemd
**Create kafka user:**
```
sudo adduser kafka
sudo adduser kafka sudo
su -l kafka
```

**Download and Install kafka archive:**
```bash
cd /opt                                                              # go to /opt folder

sudo wget https://downloads.apache.org/kafka/3.5.0/kafka_2.13-3.5.0.tgz   # download archive to folder
sudo tar -zxvf kafka*.tgz                                                 # extract archive 
sudo chown -R kafka:kafka /opt/kafka_2.13-3.5.0/                          # change owner of the folder
sudo rm kafka*.tgz                                                        # remove archive 
sudo ln -s kafka_2.13-3.5.0/ kafka                                        # create symbolic link  
sudo chown -R kafka:kafka /opt/kafka                                      # change owner of the folder
```

**Create zookeeper service file:**


```bash
sudo touch /etc/systemd/system/kafka-zookeeper.service
sudo chown kafka:kafka /etc/systemd/system/kafka-zookeeper.service
sudo chmod 664 /etc/systemd/system/kafka-zookeeper.service
nano /etc/systemd/system/kafka-zookeeper.service
```

**Add content to file:**

```
[Unit]
Description=Apache Zookeeper server (Kafka)
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
User=kafka
Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ExecStart=/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
ExecStop=/opt/kafka/bin/zookeeper-server-stop.sh

[Install]
WantedBy=multi-user.target
```


**Create kafka service file:**

```bash
sudo touch /etc/systemd/system/kafka.service
sudo chown kafka:kafka /etc/systemd/system/kafka.service
sudo chmod 664 /etc/systemd/system/kafka.service
nano /etc/systemd/system/kafka.service
```

**Add content to file:**

```
[Unit]
Description=Apache Kafka server (broker)
Documentation=http://kafka.apache.org/documentation.html
Requires=network.target remote-fs.target
After=network.target remote-fs.target kafka-zookeeper.service

[Service]
Type=simple
User=kafka
Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ExecStart=/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
ExecStop=/opt/kafka/bin/kafka-server-stop.sh

[Install]
WantedBy=multi-user.target
```

**Edit service files:**

``` bash
nano /etc/systemd/system/kafka-zookeeper.service
nano /etc/systemd/system/kafka.service
```

**Edit kafka settings:**
``` bash
nano /opt/kafka/config/server.properties
listeners=PLAINTEXT://0.0.0.0:9092
advertised.listeners=PLAINTEXT://10.35.125.xxx:9092
```

**Reload and start the systemd services:**

``` bash
sudo systemctl daemon-reload
sudo systemctl enable kafka-zookeeper.service
sudo systemctl enable kafka.service
sudo systemctl start kafka-zookeeper.service
sudo systemctl start kafka.service
```


**Check services state:**
``` bash
sudo systemctl status kafka-zookeeper.service
sudo systemctl status kafka.service
```
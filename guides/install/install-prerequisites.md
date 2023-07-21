## install-prerequisites.md

To install Kafka 3.5, you will need to install Java 8, 11, or 17. Kafka is built and tested with these Java versions. However, please note that Java 8 support has been deprecated since Kafka 3.0 and will be removed in Kafka 4.0. Similarly, Scala 2.12 support has been deprecated since Kafka 3.0 and will be removed in Kafka 4.0.

Here are the steps to install Kafka:

1.  Download the Kafka binary distribution from the Apache Kafka website.
    -   For example, you can download Kafka 3.5.0 from [here](https://kafka.apache.org/downloads).

2.  Install Java on your machine if you haven't already done so.
    -   Kafka supports Java 8, 11, and 17.
    -   Follow the instructions provided by your operating system to install Java.

3.  Extract the Kafka binary distribution that you downloaded in step 1 to a directory of your choice.

4.  Set the `JAVA_HOME` environment variable to the path of your Java installation.
    -   This step ensures that Kafka uses the correct Java version.
    -   The process for setting the `JAVA_HOME` variable varies depending on your operating system.
    -   You can refer to the documentation specific to your operating system for instructions on setting environment variables.

5.  You can now start using Kafka by running the appropriate scripts or commands.
    -   For example, you can start a Kafka broker by running the following command from the Kafka directory:

```
     bin/kafka-server-start.sh config/server.properties
     ```

```

-   Make sure to update the `config/server.properties` file with the necessary configurations for your setup.

Please note that the above steps are a general guide for installing Kafka. It's always recommended to refer to the official Kafka documentation and the documentation specific to your operating system for more detailed installation instructions and any additional requirements.

Sources:

-   [Apache Kafka Downloads](https://kafka.apache.org/downloads)
-   [Apache Kafka Installation Steps - Tutorialspoint](https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm)
-   [Apache Kafka - Index Scala](https://index.scala-lang.org/apache/kafka)
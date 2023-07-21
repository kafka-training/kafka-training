## intstall java openjdk 11

To install Java 11 (OpenJDK 11) on Ubuntu 22.04, you can follow these steps:

**Step 1: Update Your System**

First, update your package index using the following command:

```
sudo apt update

```

**Step 2: Check Available OpenJDK Packages**

You can check if OpenJDK 11 is available in the package repository with this command:

```
sudo apt search openjdk

```

This will list all the available OpenJDK packages. Look for OpenJDK 11 in this list.

**Step 3: Install OpenJDK 11**

If OpenJDK 11 is available, you can install it with the following command:

```
sudo apt install openjdk-11-jdk

```

This will install OpenJDK 11 and the associated JDK.

**Step 4: Verify the Installation**

After the installation is complete, you can verify it by running the following command:

```
java -version

```

If OpenJDK 11 is installed successfully, you will see output similar to this:

```
javaCopy codeopenjdk version "11.0.11" 2021-04-20
OpenJDK Runtime Environment (build 11.0.11+9-Ubuntu-0ubuntu2.22.04)
OpenJDK 64-Bit Server VM (build 11.0.11+9-Ubuntu-0ubuntu2.22.04, mixed mode, sharing)

```

**Step 5: Configure JAVA\_HOME Variable**

Lastly, you may want to set the `JAVA_HOME` environment variable. It's often used by other applications to know the location of Java. Here's how to do it:

```
echo 'JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"' | sudo tee -a /etc/environment

```

Load the environment variable into the current session:

```
source /etc/environment

```

You can verify `JAVA_HOME` has been set correctly with this command:

```
echo $JAVA_HOME

```

This should return:

```
/usr/lib/jvm/java-11-openjdk-amd64

```

That's it. You have installed OpenJDK 11 on your Ubuntu 22.04 system and configured the `JAVA_HOME` environment variable.
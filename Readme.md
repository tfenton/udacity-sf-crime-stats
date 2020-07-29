# Kafka and Spark Streaming Integration

## Overview

In this project, we provide a statistical analyses of the data using Apache Spark Structured Streaming. We created a Kafka server to produce data, a test Kafka Consumer to consume data and ingest data through Spark Structured Streaming. Then we applied Spark Streaming windowing and filtering to aggregate the data and extract count on hourly basis.

### Environment

 - Java 1.8.x
 - Python 3.6 or above
 - Zookeeper
 - Kafka
 - Scala 2.11.x
 - Spark 2.4.x


### Running this project...
#### Start Zookeeper and Kafka Server 
```
/usr/bin/zookeeper-server-start config/zookeeper.properties
/usr/bin/kafka-server-start config/server.properties
```
#### Run Kafka Producer server
`python kafka_server.py`

#### Run the kafka Consumer server 
`python kafka_consumer.py`

#### Submit Spark Streaming Job
`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`

### kafka consumer output
![Kafka console output](https://github.com/tfenton/udacity-sf-crime-stats/blob/master/Screen Shot - kafka topic.png)


### Streaming progress submission
![Streaming submission](https://github.com/tfenton/udacity-sf-crime-stats/blob/master/Screen Shot - spark job submitted.png)

### Streaming progress running
![Streaming running](https://github.com/tfenton/udacity-sf-crime-stats/blob/master/Screen Shot - spark job streaming.png)






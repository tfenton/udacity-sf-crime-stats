# Kafka and Spark Streaming Integration

## Overview
This project is for the Udacity Streaming Data course. It takes data found in the file `police-department-calls-for_service.json` and puts that data info a kafka topics. This data is then streamed into spark.

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
![Kafka console output](https://github.com/tfenton/udacity-sf-crime-stats/blob/master/screen_shot_kafka_topic.png)


### Streaming progress submission
![Streaming submission](https://github.com/tfenton/udacity-sf-crime-stats/blob/master/screen_shot_spark_submitted.png)

### Streaming progress running
![Streaming running](https://github.com/tfenton/udacity-sf-crime-stats/blob/master/screen_shot_spark_running.png)

### Questions
1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
> Changing `processedRowsPerSecond` increases/decreases throughput.
2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
>I monitored `processedRowsPerSecond` and saw values north of 300
```
spark.sql.shuffle.partitions                10
spark.streaming.kafka.maxRatePerPartition   10
spark.default.parallelism                   10000
```





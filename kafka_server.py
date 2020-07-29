import producer_server


def run_kafka_server():
    """
    creates the kafka producer object
    params - None
    returns - kafka producer
    """
	# TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="calls",
        bootstrap_servers="localhost:9092",
        client_id=None
    )

    return producer


def feed():
    """
    starts consuming from the kafka producer
    
    params - None
    returns - None
    """
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()

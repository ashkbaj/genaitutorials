import datetime
import time

from confluent_kafka import Producer, Consumer
import time

def readconfig():
    config = {}
    with open("client.properties") as config_file:
        for line in config_file:
            line_stripped = line.strip()
            if len(line_stripped)>0 and line_stripped[0] != "#":
                line_data = line_stripped.split("=", maxsplit=1)
                config[line_data[0]] = line_data[1]
    return config


def producer(config, topic):
    producr = Producer(config)

    key = int(time.time_ns()).to_bytes()
    value = f"Messege published at {time.time()}"

    producr.produce(topic=topic, key=key, value=value)
    producer.flush()



config = readconfig()

topic ="first_topic"

producer(config=config, topic=topic)
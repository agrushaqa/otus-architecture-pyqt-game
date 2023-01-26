import json
import time

from fake_data import get_first_operation_first_object, get_operation_info
from kafka import KafkaProducer


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        # operation_info = get_operation_info()
        operation_info = get_first_operation_first_object()
        print(operation_info)
        producer.send("operation_info", operation_info)
        time.sleep(4)

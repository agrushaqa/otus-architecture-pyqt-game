import json

from kafka import KafkaConsumer


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "operation_info",
        bootstrap_servers='127.0.0.1:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        json_dict = json.loads(msg.value)
        print(json_dict)

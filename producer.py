import json
import time

from kafka import KafkaProducer
import generate_ship

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        generate_ship.generate_ships_list()
        source_data = json_serializer(generate_ship.generate_enemy_ships())
        print(source_data)
        producer.send("operation_info", source_data)
        time.sleep(4)

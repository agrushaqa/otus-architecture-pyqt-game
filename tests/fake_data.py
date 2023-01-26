import random
import time
from datetime import datetime

from faker import Faker

fake = Faker()


def get_operation_info():
    return {
        "game_id": random.randint(0, 20),
        "object_id": random.randint(0, 20),
        "operation_id": random.randint(0, 20),
        "args": {"name": fake.name(),
                 "address": fake.address()
                 },
        "data": datetime.now(),
        "json_version": 1
    }


def get_first_operation_first_object():
    return {"game_id": 1, "object_id": 1, "operation_id": 1,
            "args": {"x": 5, "y": 7},
            # "data": datetime.now(),
            "json_version": 1
            }


if __name__ == "__main__":
    print(get_operation_info())

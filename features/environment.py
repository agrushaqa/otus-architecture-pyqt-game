# before every scenario
from unittest.mock import MagicMock

import numpy as np

from features.steps.src.commands.fuel import Fuel
from features.steps.src.commands.move import Movable
from features.steps.src.commands.rotate import Rotable


class MockPosition:
    def __init__(self):
        self.coord = None

    def get_position(self):
        return self.coord

    def set_position(self, new_value):
        self.coord = new_value


def mock_add(x, y):
    return np.add(x, y).tolist()


class MockRotable(Rotable):
    def __init__(self):
        self.direction = 0
        self.directions_number = 0

    def get_direction(self):
        return self.direction

    def get_angular_velocity(self):
        pass

    def set_direction(self, new_value):
        self.direction = new_value

    def get_directions_number(self):
        return self.directions_number

    def set_directions_number(self, value):
        self.directions_number = value


def before_feature(context, feature):
    mock_position = MockPosition()
    context.mock = MagicMock(spec=Movable)
    context.mock.add = mock_add
    context.mock.set_position = mock_position.set_position
    context.mock.get_position = mock_position.get_position

    context.fuel = Fuel()
    context.rotable = MockRotable()

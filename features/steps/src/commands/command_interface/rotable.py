from abc import ABC, abstractmethod


class Rotable(ABC):

    @abstractmethod
    def get_direction(self):
        pass

    @abstractmethod
    def get_angular_velocity(self):
        pass

    @abstractmethod
    def set_angular_velocity(self, new_value):
        pass

    @abstractmethod
    def set_direction(self, new_value):
        pass

    @abstractmethod
    def get_directions_number(self):
        pass

    @abstractmethod
    def set_directions_number(self, new_value):
        pass

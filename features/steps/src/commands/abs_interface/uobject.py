from abc import ABC, abstractmethod


class UObject(ABC):
    @abstractmethod
    def get_property(self, key: str):
        pass

    @abstractmethod
    def set_property(self, key: str, new_value):
        pass

from abc import ABC, abstractmethod


class TankOperationsIMovable(ABC):

    @abstractmethod
    def getPosition(self):
        pass

    @abstractmethod
    def setPosition(self, value):
        pass

    @abstractmethod
    def getVelocity(self):
        pass

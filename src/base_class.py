from abc import ABC, abstractmethod


class Shop(ABC):
    @abstractmethod
    def __repr__(self):
        pass

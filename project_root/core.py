
from abc import ABC, abstractmethod

class AbstractX(ABC):

    @abstractmethod
    def add(a, b):
        pass




class Xclass(AbstractX):

    def add(self, a, b):
        return a + b
    

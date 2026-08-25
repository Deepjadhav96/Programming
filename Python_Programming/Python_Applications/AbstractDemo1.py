from abc import ABC, abstractmethod  #ABC=> Abstract base class

class Base(ABC):                #its compulsory to add ABC when creating abstract method inside class
    @abstractmethod
    def Addition(self, No1, No2):
        pass

class Derived(Base):
    pass
dobj = Derived()                #error due to 
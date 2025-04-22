from abc import ABC, abstractmethod

class Abclass(ABC):
    def print(self,x):
        print("value is:",x)

    @abstractmethod
    def task(self):
        print("i am inside abstractless")


class tclass(Abclass):
    def task(self):
        print("i am inside test class")

obj=tclass()
obj.task()
obj.print(100)

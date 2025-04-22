from abc import ABC, abstractmethod

class animal(ABC):
    def move (self):
        pass

class human(animal):
    def move(self):
        print("Humans can walk.")

class snake(animal):
    def move(self):
        print("Snakes can slither.")

class fish(animal):
    def move(self):
        print("Fishes can swim.")

santosh=human()
santosh.move()
leo=snake()
leo.move()
nero=fish()
nero.move()
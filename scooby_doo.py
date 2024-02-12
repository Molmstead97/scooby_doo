from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name: str, location: str, mood: str):
        self.name = name
        self.location = location
        self.mood = mood

    @abstractmethod
    def take_action(self):
        pass

class Fred(Player):
    def __init__(self)-> str:
        super().__init__(name="Fred", location="entrance", mood="confident")
        print(self.name, self.location, self.mood)
  
    def take_action(self):
        print("Fred: Alright Gang, let's split up and look for clues. Daphne, Velma, you're with me. ")

class Daphne(Player):
    def __init__(self, name, location, mood):
        super().__init__(name="Daphne", location="entrance", mood="curious")
        print()

    def take_action(self):
        print("Daphne: I'll search the gravesites for any signs of the ghost. ")

class Velma(Player):
    def __init__(self, name: str, location: str, mood: str):
        super().__init__("Velma", "entrance", "analytical")
        print()

    def take_action(self):
        print("Velma: I'll investigate the mausoleum for any clues.")

class Shaggy(Player):
    def __init__(self, name: str, location: str, mood: str):
        super().__init__("Shaggy", "gravesite", "hungry")
        print()

    def take_action(self):
        print("Shaggy: Like, I'll check out the entrance area. Maybe there's some food around. ")

class Scooby(Player):
    def __init__(self, name: str, location: str, mood: str):
        super().__init__("Scooby", "gravesite", "nervous")
        print()

    def take_action(self):
        print("Scooby: Ruh-roh! I'll join Shaggy in the entrance. ")

class Ghost(Player):
    def __init__(self, name: str, location: str, mood: str):
        super().__init__("Ghost", "mausoleum", "upset")

    def take_action(self):
        "Ghost: Wooooo! You meddling kids will never solve the mystery! "

fred = Fred()

print(fred)
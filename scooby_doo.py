from abc import ABC, abstractmethod

class ClueFinder:
    def __init__(self, location: str):
        self.location = location

    def find_clues(self):
        # Simulate finding clues based on the location
        if self.location == "entrance":
            print("You found some footprints near the entrance.")
        elif self.location == "gravesite":
            print("You found a torn piece of cloth near a gravesite.")
        elif self.location == "mausoleum":
            print("You found a mysterious symbol carved on the wall of the mausoleum.")

class Player(ABC):
    def __init__(self, name: str, mood: str):
        self.name = name
        self.mood = mood

    @abstractmethod
    def take_action(self):
        pass

    def __str__(self):
        return f"Name: {self.name}\nMood: {self.mood}\n"

class Fred(Player):
    def __init__(self):
        super().__init__(name="Fred", mood="confident")
  
    def take_action(self):
        print("Fred: Alright Gang, let's split up and look for clues. Daphne, Velma, you're with me. ")
    

class Daphne(Player):
    def __init__(self):
        super().__init__(name="Daphne", mood="curious")
  
    def take_action(self):
        print("Daphne: I'll search the gravesites for any signs of the ghost. ")
        

class Velma(Player):
    def __init__(self):
        super().__init__(name="Velma", mood="analytical")
  
    def take_action(self):
        print("Velma: I'll investigate the mausoleum for any clues.")


class Shaggy(Player):
    def __init__(self):
        super().__init__(name="Shaggy", mood="hungry")
  
    def take_action(self):
        print("Shaggy: Like, I'll check out the entrance area. Maybe there's some food around. ")


class Scooby(Player):
    def __init__(self):
        super().__init__(name="Scooby", mood="nervous")
  
    def take_action(self):
        print("Scooby: Ruh-roh! I'll join Shaggy in the entrance. ")


class Ghost(Player):
    def __init__(self):
        super().__init__(name="Ghost", mood="upset")

    def take_action(self):
        print("Ghost: Wooooo! You meddling kids will never solve the mystery! ")


characters = {
    "Fred": Fred(),
    "Daphne": Daphne(),
    "Velma": Velma(),
    "Shaggy": Shaggy(),
    "Scooby": Scooby(),
    "Ghost": Ghost()
}

def main():
    # Introduction
    print() 
    print("""
        The Scooby Doo gang is out on another mystery. 
        While visiting a small town, they stumbled upon a legend of the 'Ghost in the Graveyard'. 
        It is your job to help the gang solve the mystery before the ghost gets them.
        Daphne added you to the group chat that shows the current location of each gang member 
        and what they plan to do. """)
    print()
    
    # Print character name, location, mood, and take action
for character_name, character in characters.items():
        print(f"{character_name}:\n{str(character)}")
        character.take_action()
        print()


if __name__ == "__main__":
    main()

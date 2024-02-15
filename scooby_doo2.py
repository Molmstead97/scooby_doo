from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name: str, mood: str):
        self.name = name
        self.mood = mood

    @abstractmethod
    def take_action(self):
        pass

    def __str__(self):
        return f"Name: {self.name}\nMood: {self.mood}\n"
    
    def move_location(user_location, turn_count):
        valid_input = False
        turn_count += 1

        while not valid_input:
            move = input("\nWhere would you like to move? Gravesite (g), Mausoleum (m), Chapel (c), Gardens (gd), Entrance (e): ").lower()

            if move == user_location:
                print("You're already here.")
            
            elif move in locations:
                user_location = locations[move]
                valid_input = True
            
            else:
                print("You can't go there. Try somewhere else.")
            
        return user_location, turn_count
    
    def find_clues(self):
        # Simulate finding clues based on the location
        if self.location == "entrance":
            player_clues.append[clues[2]]
            print("You found some footprints near the entrance.")
        elif self.location == "gravesite":
            player_clues.append[clues[4]]
            print("You found a torn piece of cloth near a gravesite.")
        elif self.location == "mausoleum":
            player_clues.append[clues[3]]
            print("You found a mysterious symbol carved on the wall of the mausoleum.")
        elif self.location == "chapel":
            player_clues.append[clues[0]]
            print("You found a strange note in the chapel.")
        elif self.location == "gardens":
            player_clues.append[clues[1]]
            print("You found a shovel in the gardens.")

    
    def search_location(user_location, player_clues, turn_count):
        turn_count += 1
        user_search = random.randint(1, 3)
        if user_search == 3:
            print("You see nothing out of the ordinary.")
        else:
            player_clues.append(clue_locations.get(user_location, ""))
    

class Fred(Player):
    def __init__(self):
        super().__init__(name="Fred", mood="confident")
  
    def take_action(self):
        print("Fred: Alright Gang, let's split up and look for clues. ")
    

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
        It was a crisp autumn evening, and the gang—Fred, Daphne, Velma, Shaggy, and, of course, Scooby-Doo—found themselves parked outside the gates of Graveyard Grove.
        
        The old cemetery was rumored to be haunted by the ghost of Old Man Jenkins, a local legend who was said to roam the grounds every Halloween.
          
        "Like, I don't know about this, Scoob," Shaggy said nervously, his voice trembling as he glanced at the darkened graveyard.
          
        Rearing up onto his hind legs, Scooby-Doo whimpered, his large puppy-dog eyes reflecting the moonlight.
          
        But as scared as they were, the Mystery Inc. gang knew that they had a job to do—unravel the mystery of the ghostly sightings and put an end to the rumors once and for all.
          
        As they crept through the eerie graveyard, Velma consulted her flashlight and map, leading the way with confidence.
          
        "According to my research, the legend of Old Man Jenkins dates back over a hundred years.
          
        He was a recluse who lived on the outskirts of town, and when he died, his spirit supposedly returned to haunt this graveyard.
          """)
    print()
    for character_name, character in characters.items():
        print(f"{character_name}:\n{str(character)}")
        character.take_action()
        print()

if __name__ == "__main__":
    main()
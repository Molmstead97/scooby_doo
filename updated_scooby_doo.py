from abc import ABC, abstractmethod

import random

# Location info
locations = {
    "gravesite": 0,
    "g": 0,
    "masoleum": 1,
    "m": 1,
    "chapel": 2,
    "c": 2,
    "gardens": 3,
    "gd": 3,
    "entrance": 4,
    "e": 4
}
user_location = locations["entrance"]
mystery_gang_location = locations["entrance"]
# Clue info
player_clues = []
clues = ["Strange Note", "Shovel", "Footprints", "Broken headstone", "Torn Cloth"]
clue_locations = {
    locations["gravesite"]: clues[3],
    locations["masoleum"]: clues[4],
    locations["chapel"]: clues[0],
    locations["gardens"]: clues[1],
    locations["entrance"]: clues[2]
}
turn_count = 0

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
    
    def find_clues(user_location, player_clues, turn_count):
        # Simulate finding clues based on the location
        turn_count += 1
        user_search = random.randint(1, 3)
        if user_search == 3:
            print("You see nothing out of the ordinary.")
        else:
            player_clues.append(clue_locations.get(user_location, ""))
    
    def search_location(user_location):
        interactive_objects = {}

        for location, object in locations.items():
            # Define interactive objects based on location code
            if object == 0:  # Gravesite
                interactive_objects[location] = ["headstone", "funeral urn", "dead flowers", "lantern"]
            elif object == 1:  # Mausoleum
                interactive_objects[location] = ["crypt", "statue", "torch", "cobwebs"]
            elif object == 2:  # Chapel
                interactive_objects[location] = ["pew", "altar", "stained glass window"]
            elif object == 3:  # Gardens
                interactive_objects[location] = ["fountain", "decrepit bench", "flower bed", "bird feeder"]
            elif object == 4:  # Entrance
                interactive_objects[location] = ["gate", "signboard", "gargoyle statue", "lamp post"]

        return interactive_objects
    
    def look_at_clues():
        for clue in player_clues:
            print(f"\nCurrent clues: {clue}")
        
        
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
    
    
    #Introduction
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
    while turn_count < 15:
        print(f"\nCurrent location: {user_location}. Mystery gang locations: {mystery_gang_locations}")
        try:
            user_input = input("\nWhat would you like to do? Move location: (m), Search current location: (s), Interact with object: (i), Look for clues: (c), Look at your list of clues: (l): ").lower
            if user_input == "m" or user_input == "move":
                player.move_location()
            elif user_input == "s":
                player.search_location()            
            elif user_input == "i":
                player.interact_with_object
            elif user_input == "c":
                player.find_clues()
            elif user_input == "l":
                player.look_at_clues()

# Location info
locations = {
    "gravesite": 0,
    "g": 0,
    "masoleum": 1,
    "m": 1,
    "chapel": 2,
    "c": 2,
    "gardens": 3,
    "gd": 3,
    "entrance": 4,
    "e": 4
}
user_location = locations["entrance"]
mystery_gang_location = locations["entrance"]
# Clue info
player_clues = []
clues = ["Strange Note", "Shovel", "Footprints", "Broken headstone", "Torn Cloth"]
clue_locations = {
    locations["gravesite"]: clues[3],
    locations["masoleum"]: clues[4],
    locations["chapel"]: clues[0],
    locations["gardens"]: clues[1],
    locations["entrance"]: clues[2]
}
turn_count = 0

if __name__ == "__main__":
    main()
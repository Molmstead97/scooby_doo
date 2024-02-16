from abc import ABC, abstractmethod

import random

import time


class NPC(ABC):
    def __init__(self, name: str, mood: str):
        self.name = name
        self.mood = mood
    
    @abstractmethod
    
    def take_action(self):
        pass
    
    def __str__(self):
        return f"\nMood: {self.mood}\n"
    

class Player:
    
    
    def move_location(self, user_location: str) -> str:
        valid_input = False
        
        while not valid_input:
            move = input("\nWhere would you like to move? Gravesite (g): Mausoleum (m): Chapel (c): Gardens (gd): Entrance (e): ").lower()
            if move == user_location:
                print("You're already here.")
            elif move in locations:
                user_location = locations[move]
                print(f"\nYou decide to go to the {user_location}.")
                valid_input = True
                
        return user_location

    
    def search_location(self, user_location):
        interactive_objects = locations[user_location]
        for location, object in locations.items():
            # Define interactive objects based on location code
            if object == 0:  # Gravesite
                interactive_objects[location] = ["headstone", "funeral urn", "dead flowers", "lantern"]
                print("")
            elif object == 1:  # Mausoleum
                interactive_objects[location] = ["crypt", "statue", "torch", "cobwebs"]
                print("")
            elif object == 2:  # Chapel
                interactive_objects[location] = ["pew", "altar", "stained glass window"]
                print("")
            elif object == 3:  # Gardens
                interactive_objects[location] = ["fountain", "decrepit bench", "flower bed", "bird feeder"]
                print("")
            elif object == 4:  # Entrance
                interactive_objects[location] = ["gate", "signboard", "gargoyle statue", "lamp post"]
                print("")

        return interactive_objects, turn_count
        
        
    def interact_with_object(self, user_location):
        pass    
    
    
    def look_at_clues(self, player_clues):
        if not player_clues:
            print("You don't have any clues yet.")
        for clue in player_clues:
            print(f"- {clue}")
            
        
class Fred(NPC):
    def __init__(self):
        super().__init__(name="Fred", mood="confident")
    def take_action(self):
        print("\nAlright Gang, let's split up and look for clues. Daphne, Velma, you're with me. ")


class Daphne(NPC):
    def __init__(self):
        super().__init__(name="Daphne", mood="curious")
    def take_action(self):
        print("\nI'll search the gravesites for any signs of the ghost. ")


class Velma(NPC):
    def __init__(self):
        super().__init__(name="Velma", mood="analytical")
    def take_action(self):
        print("\nI'll investigate the mausoleum for any clues.")


class Shaggy(NPC):
    def __init__(self):
        super().__init__(name="Shaggy", mood="hungry")
    def take_action(self):
        print("\nLike, I'll check out the entrance area. Maybe there's some food around. ")


class Scooby(NPC):
    def __init__(self):
        super().__init__(name="Scooby", mood="nervous")
    def take_action(self):
        print("\nRuh-roh! I'll join Shaggy in the entrance. ")


class Ghost(NPC):
    def __init__(self):
        super().__init__(name="Ghost", mood="upset")
    def take_action(self):
        print("\nWooooo! You meddling kids will never solve the mystery! ")


# Game info
locations = {
    "g": "gravesite",
    "m": "mausoleum",
    "c": "chapel",
    "gd": "gardens",
    "e": "entrance"
}

user_location = "entrance"

clue_locations = {
    "gravesite": [("headstone", "broken headstone")],
    "mausoleum": [("crypt", "torn cloth")],
    "chapel": [("altar", "strange note")],
    "gardens": [("flower bed", "shovel")],
    "entrance": [("dirt pathway", "footprints")]
}

player_clues = []

turn_count = 0

characters = {
    "Fred": Fred(),
    "Daphne": Daphne(),
    "Velma": Velma(),
    "Shaggy": Shaggy(),
    "Scooby": Scooby(),
    "Ghost": Ghost()
}

def main():
    player = Player()
    
    #Introduction
    print()
    print("""
        The Scooby Doo gang is out on another mystery.
        While visiting a small town, they stumbled upon a legend of the 'Ghost in the Graveyard'.
        It is your job to help the gang solve the mystery before the ghost gets them.
        Daphne added you to the group chat that shows the current location of each gang member
        and what they plan to do. """)
    print()
    #time.sleep(5)
    
    # Print character name, location, mood, and take action
    for character_name, character in characters.items():
        #time.sleep(5)
        print(f"\n{character_name}:") 
        character.take_action()
        print(f"{str(character)}")
        
    turn_count = 0
    while turn_count < 15:
        turn_count += 1
        
        print(f"\nYou are currently in the {user_location}.")
        try:
            user_input = input("\nWhat would you like to do? Move location: (m), Search current location: (s), Interact with object: (i), Look at your list of clues: (l): ").lower()
            if user_input == "m" or user_input == "move":
                player.move_location(user_location)
            elif user_input == "s" or user_input == "search":
                player.search_location()            
            elif user_input == "i" or user_input == "interact":
                player.interact_with_object()
            elif user_input == "l":
                player.look_at_clues()
                
        except ValueError:
            print("\nThat's not valid input.")


if __name__ == "__main__":
    main()
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
    locations = {
        "g": "gravesite",
        "m": "mausoleum",
        "c": "chapel",
        "gd": "gardens",
        "e": "entrance"
    }
    
    def __init__(self, user_location="entrance", player_clues=[]):
        self.user_location = user_location
        self.player_clues = player_clues
    def move_location(self, user_location: str) -> str:
        valid_input = False
        
        while not valid_input:
            move = input("\nWhere would you like to move? Gravesite (g): Mausoleum (m): Chapel (c): Gardens (gd): Entrance (e): ").lower()
            if move == user_location:
                print("You're already here.")
            elif move in self.locations:
                user_location = move  # Update user_location directly with the key
                print(f"\nYou decide to go to the {self.locations[user_location]}.")
                valid_input = True
                
        return user_location

    def search_location(self, user_location):
        location_name = self.locations[user_location]  # Get the name of the location
          # Initialize an empty dictionary for interactive objects
        # Define interactive objects based on location name
        if location_name == "gravesite":
            while True:
                try:
                    user_choice = input("\nYou enter the gravesite and you see a headstone(h), funeral urn(f), dead flowers(d), and a lantern(l). Which object would you like to examine further(or return to main menu(m)? ")
                    if user_choice == "m":
                        main()
                    elif user_choice == "h":
                        print("A headstone is normal in a graveyard, ya silly. ")
                    elif user_choice == "f":
                        print("It is normal to see an urn around a graveyard full of dead people. Try using your brain. ")
                    elif user_choice == "d":
                        print("These dead people don't have anyone that loves them enough to bring them fresh flowers. ")
                    elif user_choice == "l":
                        print("You found a clue: There is a single lantern by this grave. ")
                        self.player_clues.append("lantern")
                    elif user_choice == "m":
                        break
                except ValueError:
                    print("\nThat's not valid input.")

        elif location_name == "mausoleum":
            while True:
                try:
                    user_choice = input("\nYou enter the mausoleum and you see a crypt(c), statue(s), and torch(t). Which object would you like to examine further(or return to main menu(m)? ")
                    if user_choice == "c":
                        print("You found a clue: The crypt looks like it has been damaged by somethig sharp. ")
                        self.player_clues.append("damaged crypt")
                    elif user_choice == "s":
                        print("It looks like there is a statue of someone that was buried here. ")
                    elif user_choice == "t":
                        print("Like this place is too old to have a lightswitch so I guess the torch makes sense. But who lit it?? ")
                    elif user_choice == "m":
                        break
                except ValueError:
                    print("\nThat's not valid input.")
        elif location_name == "chapel":
            while True:
                try:
                    user_choice = input("\nYou enter the chapel and see a shovel(s), altar(a), and a stained glass window(g). Which object would you like to examine further(or return to main menu(m)? ")
                    if user_choice == "s":
                        print("You found a clue: Gang, like why is there a shovel in a church? The edge looks like it has been chipped. ")
                        self.player_clues.append("shovel")
                    elif user_choice == "a":
                        print("Jeepers! This place gives me the creeps. ")
                    elif user_choice == "g":
                        print("Jinkies! The stained glass window looks like Scooby. ")
                    elif user_choice == "m":
                        break
                except ValueError:
                    print("\nThat's not valid input.")
                    
        elif location_name == "gardens":
            while True:
                try:
                    user_choice = input("\nYou enter the gardens and see a fountain(f), large holes(h), and a flower bed(b). Which object would you like to examine further(or return to main menu(m)? ")
                    if user_choice == "f":
                        print("That sure is a pretty fountain. Maybe we should get one in the mystery machine? ")
                    elif user_choice == "h":
                        print("You found a clue: Like zoinkes Scoob! There are large holes all over this garden that seem to be too large for plants. ")
                        self.player_clues.append("large holes")
                    elif user_choice == "b":
                        print("What did you expect? Zombies in the flower bed? ")
                    elif user_choice == "m":
                        break
                except ValueError:
                    print("\nThat's not valid input.")
        elif location_name == "entrance":
            while True:
                try:
                    user_choice = input("\nYou are at the entrance and see a gate(g), signboard(s), gargoyle statue(gs). Which object would you like to examine further(or return to main menu(m)? ")
                    if user_choice == "g":
                        print("Hold the phone. This gate has a lock on it that appears to have been cut")
                        self.player_clues.append("gate")
                    elif user_choice == "s":
                        print("It says 'Welcome to Graveyard Grove'. ")
                    elif user_choice == "gs":
                        print("Ruh-roh! A gargoyle statue. ")
                    elif user_choice == "m":
                        break
                except ValueError:
                    print("\nThat's not valid input.")

    
    def look_at_clues(self):
        if not self.player_clues:
            print("You don't have any clues yet. ")
        for clue in self.player_clues:
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

player = Player()
def main():
    
    user_location = "e"
    
    # Introduction
    print("""
        It was a crisp autumn evening, and the gang—Fred, Daphne, Velma, Shaggy, and, of course, Scooby-Doo—found themselves parked outside the gates of Graveyard Grove.
        
        The old cemetery was rumored to be haunted by the ghost of Old Man Jenkins, a local legend who was said to roam the grounds every Halloween.
          
        "Like, I don't know about this, Scoob," Shaggy said nervously, his voice trembling as he glanced at the darkened graveyard.
          
        Rearing up onto his hind legs, Scooby-Doo whimpered, his large puppy-dog eyes reflecting the moonlight.
          
        But as scared as they were, the Mystery Inc. gang knew that they had a job to do—unravel the mystery of the ghostly sightings and put an end to the rumors once and for all.
          
        As they crept through the eerie graveyard, Velma consulted her flashlight and map, leading the way with confidence.
          
        "According to my research, the legend of Old Man Jenkins dates back over a hundred years.
          
        He was a recluse who lived on the outskirts of town, and when he died, his spirit supposedly returned to haunt this graveyard.
        
        You are currently at the entrance to the graveyard.
            """)
    print()
    #time.sleep(5)
    
    # Print character name, location, mood, and take action
    characters = {
        "Fred": Fred(),
        "Daphne": Daphne(),
        "Velma": Velma(),
        "Shaggy": Shaggy(),
        "Scooby": Scooby(),
        "Ghost": Ghost()
    }
    
    for character_name, character in characters.items():
        #time.sleep(5)
        print(f"\n{character_name}:") 
        character.take_action()
        print(f"{str(character)}")
        
    turn_count = 0
    while turn_count < 15:
        turn_count += 1

        try:
            user_input = input("\nWhat would you like to do? Move location: (m), Search current location: (s), Interact with object: (i), Look at your list of clues: (l): ").lower()
            if user_input == "m" or user_input == "move":
                user_location = player.move_location(user_location)
            elif user_input == "s" or user_input == "search":
                player.search_location(user_location)            
            elif user_input == "l":
                player.look_at_clues()
                
        except ValueError:
            print("\nThat's not valid input.")


if __name__ == "__main__":
    main()

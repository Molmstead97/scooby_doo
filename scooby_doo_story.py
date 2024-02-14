#Make some clues for the players to interact with
#Make a menu of some sort that asks for user input
#Allow characters to move around the graveyard
#Make a ghost class that attacks every so often

import random

class Game:
    
    
    
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
    
    
    def search_location(user_location, player_clues, turn_count):
        turn_count += 1
        user_search = random.randint(1, 3)
        if user_search == 3:
            print("You see nothing out of the ordinary.")
        else:
            player_clues.append(clue_locations.get(user_location, ""))
    

class Ghost:
    
    def __init__(self):
        pass

def main(player: Player):
    
    while turn_count < 15:
        print(f"\nCurrent location: {user_location}. Mystery gang locations: {mystery_gang_locations}")
        
        try:
            user_input = input("\nWhat would you like to do? Move location: (m), Search current location: (s), Interact with object: (i), Look at clues: (c): ").lower
            
            if user_input == "m" or user_input == "move":
                move_location(player)
               
            elif user_input == "s":
                search_location(player)
                    
            elif user_input == "i":
                interact_with_object(player)
            
            elif user_input == "c":
                player_inventory(player)

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
clues = ["Disturbed soil", "Shovel", "Footprints", "Broken headstone", "Mysterious note"]
clue_locations = {
    locations["gravesite"]: clues[3],
    locations["masoleum"]: clues[2],
    locations["chapel"]: clues[4],
    locations["gardens"]: clues[1],
    locations["entrance"]: clues[0]
}

turn_count = 0



    







                
        
        
        
    
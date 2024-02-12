#Make some clues for the players to interact with
#Make a menu of some sort that asks for user input
#Allow characters to move around the graveyard
#Make a ghost class that attacks every so often

import random

locations = ["Gravesite", "Masoleum", "Chapel", "Gardens", "Entrance"]

clues = ["Disturbed soil", "Shovel", "Footprints", "Broken headstone", "Mysterious note"]

user_location = locations[4]

def move_location():
    valid_input = False
    turn_count += 1
    
    
    while valid_input == False:
        move_location = input("\nWhere would you like to move? Gravesite (g), Masoleum (m), Chapel (c), Gardens (gd), Entrance (e): ").lower
    
        if move_location == user_location:
            print("You're already here.")
            
        elif move_location == "gravesite" or move_location == "g":
            user_location = locations[0]
            valid_input == True

        elif move_location == "masoleum" or move_location == "m":
            user_location = locations[1]
            valid_input == True
        
        elif move_location == "chapel" or move_location == "c":
            user_location = locations[2]
        
        elif move_location == "gardens" or move_location == "gd":
            user_location = locations[3]
            valid_input == True
        
        elif move_location == "entrance" or move_location == "e":
            user_location = locations[4]
            valid_input == True
        
        else:
            print("You can't go there. Try somewhere else.")
            
        
    
    
    

    
    """def look_at_clues():
        clues_list = []
        clues_list.append(player_clues)"""
    
    

        
class Ghost:
    
    """def ghost_attack(self):
        ghost_attack = random.randint(1, 5)
        if ghost_attack == 1:
            
        elif ghost_attack == 2:
            
        elif ghost_attack == 3:
            
        elif ghost_attack == 4:
            
        else:"""
            
def main():
    
    user_location = locations[2]
    mystery_gang_locations = locations[2]
    
    while turn_count < 15 and mystery_gang > 0:
        try:
            user_input = input("\nWhat would you like to do? Move location: (m), Search current location: (s), Interact with object: (i), Look at clues: (c): ").lower
            
            if user_input == "m":
                move_location()
                user_move = input("Where would you like to move? ")
                if user_input ==
                
                elif user_input ==
                
                
            elif user_input == "s":
                search_location()
                current_location = ""
                user_search = random.randint(1, 3)
                if user_search != 3:
                    print("\nYou see nothing out of the ordinary.")
                    
                elif current_location == "":
                    print()
                    
                    
                elif user_input == "i":
                    interact_with_object()
                    
                elif user_input == "c":
                    player_inventory()
                
        
        
        
    
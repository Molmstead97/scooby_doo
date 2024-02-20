from abc import ABC, abstractmethod
import random
import time
import sys

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
    
    def __init__(self, user_location="entrance", player_clues=[], first_g_encounter=True, first_m_encounter=True, first_c_encounter=True, first_gd_encounter=True, clue_count=0):
        self.user_location = user_location
        self.player_clues = player_clues
        self.first_g_encounter = first_g_encounter
        self.first_m_encounter= first_m_encounter
        self.first_c_encounter = first_c_encounter
        self.first_gd_encounter = first_gd_encounter
        self.clue_count = clue_count
    
    def move_location(self, user_location: str) -> str:
        valid_input = False
        
        while not valid_input:
            move = input("\nWhere would you like to move? Gravesite (g): Mausoleum (m): Chapel (c): Gardens (gd): Entrance (e): ").lower()
            
            if move == user_location:
                print("\nYou're already here.")
            
            elif move in self.locations:
                user_location = move  # Update user_location directly with the key
                if user_location == "g" and self.first_g_encounter:
                    time.sleep(2)
                    print("""
    As the moon cast eerie shadows upon the graveyard, you cautiously step through the rusted iron gate, 
    your footsteps echoing ominously against the crumbling headstones. 
                          
    The air is thick with a haunting silence, broken only by the sound of Shaggy and Scooby hunting for food, 
    while the dim moonlight reveals the gravesite's macabre scenery: broken headstones, overgrown with moss and flowers adorning burial mounds.""")
                    self.first_g_encounter = False 
                
                elif user_location == "m" and self.first_m_encounter:
                    time.sleep(2)
                    print("""
    With trepidation gnawing at your insides, you push open the heavy wooden door of the decrepit mausoleum.
            
    Inside, a suffocating mustiness envelops you, mingling with the faint scent of decay 
    that lingerers in the stagnant air.""")
                    self.first_m_encounter = False
                    
                elif user_location == "c" and self.first_c_encounter:
                    time.sleep(2)
                    print("""
    You step into the dimly lit chapel. The stained glass windows cast eerie shadows on the stone walls 
    adorned with fading murals depicting scenes of saints and sinners.""")
                    self.first_c_encounter = False
                    
                elif user_location == "gd" and self.first_gd_encounter:
                    time.sleep(2)
                    print("""
    You venture into the gardens, the tangled vines seeming to reach out like skeletal fingers. 
    The once vibrant flower beds are now overrun with weeds, 
    reflected in murky puddles that splash beneath your feet.""")
                    self.first_gd_encounter = False
                    
                    
                else:
                    print(f"\nYou decide to go to the {self.locations[user_location]}.")
                
                valid_input = True
                
        return user_location

    def search_location(self, user_location, turn_count: int) -> int:
        location_name = self.locations[user_location]  # Get the name of the location
        # Initialize an empty dictionary for interactive objects
        # Define interactive objects based on location name
        if location_name == "gravesite":
            while True:
                try:
                    user_choice = input("""\nYou look around the gravesite and you see a suspicious headstone (h), funeral urn (f), dead flowers (d), and a lantern (l). 
Do you want to examine an object further, or do something else (m)? """)
                    
                    if user_choice == "h":
                        turn_count += 1
                        print("\nA headstone is normal in a graveyard, ya silly.")
                    
                    elif user_choice == "f":
                        turn_count += 1
                        print("\nIt is normal to see an urn around a graveyard full of dead people. Try using your brain.")
                    
                    elif user_choice == "d":
                        turn_count += 1
                        print("\nThese dead people don't have anyone that loves them enough to bring them fresh flowers.")
                    
                    elif user_choice == "l":
                        turn_count += 1
                        print("\nYou found a clue: A single lantern rests by this grave.")
                        
                        if "lantern" not in self.player_clues:
                            self.player_clues.append("lantern")
                            self.clue_count += 1
                            
                        elif self.clue_count >= 5:
                            player.solve_mystery()
                        
                    elif user_choice == "m":
                        break
                    
                except ValueError:
                    print("\nThat's not valid input.")

        elif location_name == "mausoleum":
            while True:
                try:
                    user_choice = input("""\nYou look around the mausoleum and you see a crypt (c), a statue (s), and a torch (t). 
Do you want to examine an object further, or do something else (m)? """)
                    
                    if user_choice == "c":
                        turn_count += 1
                        print("\nYou found a clue: The crypt looks like it has been damaged by somethig sharp. ")
                        if "damaged crypt" not in self.player_clues:
                            self.player_clues.append("damaged crypt")
                            self.clue_count += 1
                        
                        elif self.clue_count >= 5:
                            player.solve_mystery()
                    
                    elif user_choice == "s":
                        turn_count += 1
                        print("\nIt looks like there is a statue of someone that was buried here. ")
                    
                    elif user_choice == "t":
                        turn_count += 1
                        print("\nLike this place is too old to have a lightswitch so I guess the torch makes sense. But who lit it?? ")
                    
                    elif user_choice == "m":
                        break
                
                except ValueError:
                    print("\nThat's not valid input.")
        
        elif location_name == "chapel":
            while True:
                try:
                    user_choice = input("""\nYou look around the chapel and see a shovel (s), an altar (a), and a stained glass window (g). 
Do you want to examine an object further, or do something else (m)? """)
                    
                    if user_choice == "s":
                        turn_count += 1
                        print("\nYou found a clue: Gang, like why is there a shovel in a church? The edge looks like it has been chipped. ")
                        if "shovel" not in self.player_clues:
                            self.player_clues.append("shovel")
                            self.clue_count += 1
                        
                        elif self.clue_count >= 5:
                            player.solve_mystery()
                    
                    elif user_choice == "a":
                        turn_count += 1
                        print("\nYou look behind the altar but see nothing. Jeepers! This place gives me the creeps. ")
                    
                    elif user_choice == "g":
                        turn_count += 1
                        print("\nJinkies! The stained glass window looks like Scooby. ")
                    
                    elif user_choice == "m":
                        break
                
                except ValueError:
                    print("\nThat's not valid input.")
                    
        elif location_name == "gardens":
            while True:
                try:
                    user_choice = input("""\nYou look around the gardens and see a fountain (f), large holes (h), and a flower bed (b). 
Do you want to examine an object further, or do something else (m)? """)
                    
                    if user_choice == "f":
                        turn_count += 1
                        print("\nThat sure is a pretty fountain. Maybe we should get one in the mystery machine? ")
                    
                    elif user_choice == "h":
                        turn_count += 1
                        print("\nYou found a clue: Like zoinkes Scoob! There are large holes all over this garden that seem to be too large for plants. ")
                        if "large holes" not in self.player_clues:
                            self.player_clues.append("large holes")
                            self.clue_count += 1
                        
                        elif self.clue_count >= 5:
                            player.solve_mystery()
                    
                    elif user_choice == "b":
                        turn_count += 1
                        print("\nThere's nothing there, what did you expect? Zombies in the flower bed? ")
                    
                    elif user_choice == "m":
                        break
                
                except ValueError:
                    print("\nThat's not valid input.")
        
        elif location_name == "entrance":
            while True:
                try:
                    user_choice = input("""\nYou are at the entrance and see a gate (g), a signboard (s), and a couple gargoyle statue (gs). 
Do you want to examine an object further, or do something else (m)? """)
                    
                    if user_choice == "g":
                        turn_count += 1
                        print("\nYou found a clue: Hold the phone. This gate has a lock on it that appears to have been cut.")
                        if "gate" not in self.player_clues:
                            self.player_clues.append("gate")
                            self.clue_count += 1
                        
                        elif self.clue_count >= 5:
                            player.solve_mystery()
                    
                    elif user_choice == "s":
                        turn_count += 1
                        print("\nIt says 'Welcome to Graveyard Grove'.")
                    
                    elif user_choice == "gs":
                        turn_count += 1
                        print("\nRuh-roh! A gargoyle statue. ")
                    
                    elif user_choice == "m":
                        break
                
                except ValueError:
                    print("\nThat's not valid input.")
                    
        

    def look_at_clues(self):
        if not self.player_clues:
            print("\nYou don't have any clues yet. ")
        for clue in self.player_clues:
            print(f"\n- {clue}")
            
    def solve_mystery(self):
        time.sleep(2)
        print("""
            The groundskeeper approaches you and says that he noticed that you and the gang have been trying to solve the mystery.
            He hands you a map of the graveyard with several circles drawn on it 
            and tells you that there is said to be treasure buried on the grounds of the graveyard.
            He believes that the story of the ghost of Old Man Jenkins was created to keep people away
            so someone could look for the buried treasure without being disturbed.
            He suspects that the so called ghost is Randy Roughington who has a gambling problem. """)
        
        try:
            
            user_choice = input("\nWho do you think the is the ghost? Randy Roughington (rr), a real ghost (rg), or the groundskeeper (gk)? ")
                
            if user_choice == "rr":
                time.sleep(2)
                print("""
                      The groundskeeper tells that Randy visits the gravyard every night around 8pm.
                      It is 7pm so now is the perfect time to capture him.
                      You agree that you should be the bait.
                      The groundskeeper stands by with a net. 
                      You hear rustling and as you turn your head to investigate, a net is thrown of your head.
                      Through the holes in the net, you can see that the groundskeeper was the one that caught you.
                      He takes you to an underground cave where the rest of the gang is.
                      You are screwed. It is game over for you and the gang. """)
                sys.exit()
            
            elif user_choice == "rg":
                time.sleep(2)
                print("""
                      You decide to leave the gang and go home because you are too scared of ghosts.
                      You are the best friend ever known to man. Whether or not you made the right choice, you will never know.""")
                sys.exit()
                
            elif user_choice == "gk":
                time.sleep(2)
                print("""
                You don't trust a word that the groundskeeper says, so you thank him for his input and pretend to help him capture Randy.
                While the groundskeeper is getting the net ready, you pull out the net in your bag and throw it on him
                (you're part of the gang and would never come unprepared). The groundskeeper is suprised that you knew it was him.
                You call the sheriff who takes the man into custody, but not before you bribe the man with a scooby snack.
                He reveals that the gang is in the loft of the church. The man states that several years ago, 
                he created the legend of Old Man Jenkins when he buried a years supply of scooby snacks in 
                the graveyard during the pandemic. 
                He buried the treasure when there was a large storm so the neighbors wouldn't know what he was doing.
                You knew that there was no such thing as ghosts. """)
                sys.exit()
                
        except ValueError:
            print("\nThat's not valid input.")
                    
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
        
        self.available_targets = ["Fred", "Daphne", "Velma", "Shaggy", "Scooby"]
        
        self.captured_dialogue = {
            "Fred": "\nFred yells for help as the ghost drags him away!",
            "Daphne": "\nDaphne tries to run but trips over a trap Fred set! She is captured by the ghost!",
            "Velma": "\nThe ghost fogs up Velma's glasses enough to snatch her away while she can't see!",
            "Shaggy": "\nThe ghost manages to sneak up on Shaggy while he's busy shoveling a sandwich into his mouth.",
            "Scooby": "\nThe ghost pulls out a Scooby-Snack from his back pocket and captures Scooby while he's distracted!"
        }
        
        self.dialogue = {
            "Fred": "\nFred is able to lead the ghost into a trap and get away!",
            "Daphne": "\nDaphne runs fast enough the ghost gives up almost immediately.",
            "Velma": "\nVelma isn't afraid of the ghost and it walks away in shame.",
            "Shaggy": "\nShaggy manages to beat the ghost over the head with his sandwich until it backs off!",
            "Scooby": "\nScooby uses a Scooby-Snack to distract the ghost long enough until he escapes!"
        }
    
    def take_action(self):
        print("\nWooooo! You meddling kids will never solve the mystery! ")
        
    def ghost_attack(self):
        
        if self.available_targets:
            target = random.choice(self.available_targets)
            time.sleep(2)
            print(f"\nThe ghost of Old Man Jenkins suddenly attacks {target}!")
            if random.randint == 1:
                time.sleep(1)
                print(self.captured_dialogue[target])
                self.available_targets.remove(target)
                if not self.available_targets:
                    time.sleep(3)
                    print("\nThe ghost has captured the entire mystery gang! You were unable to solve the mystery in time.")
                    sys.exit()
            else:
                time.sleep(1)
                print(self.dialogue[target])
        
player = Player()
ghost = Ghost()

def main():
    
    user_location = "e"
    
    # Introduction
    print("""
        It was a crisp autumn evening and Fred, Daphne, Velma, Shaggy, and of course Scooby-Doo—found themselves parked outside the gates of Graveyard Grove.
        
        The old cemetery was rumored to be haunted by the ghost of Old Man Jenkins, a local legend who was said to roam the grounds every Halloween.
          
        "Like, I don't know about this, Scoob," Shaggy said nervously, his voice trembling as he glanced at the darkened graveyard.
          
        Rearing up onto his hind legs, Scooby-Doo whimpered, his large puppy-dog eyes reflecting the moonlight.
          
        But as scared as they were, the Mystery Inc. gang knew that they had a job to do—unravel the mystery of the ghostly sightings and put an end to the rumors once and for all.
          
        As they crept through the eerie graveyard, Velma consulted her flashlight and map, leading the way with confidence.
          
        "According to my research, the legend of Old Man Jenkins dates back over a hundred years.
          
        He was a recluse who lived on the outskirts of town, and when he died, his spirit supposedly returned to haunt this graveyard. Let's take a look."
        
        You are currently at the entrance to the graveyard.
            """)
    print()
    #time.sleep(10)
    
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
    
    while turn_count <= 20:
        
        if turn_count >= 20:
            print("""
                  As the morning draws nearer you realize you missed your best opportunity
                  to solve the puzzle of Graveyard Grove! You are completely stumped by the ghost,
                  and together with the Mystery Gang you head home with an unresolved case.""")
            sys.exit()
        
        
        elif turn_count % 3 == 0:
            
            ghost.ghost_attack()
            
        user_input = input("\nWhat would you like to do? Move location: (m), Search current location: (s), Look at your list of clues: (l): ").lower()
        
        if user_input == "m" or user_input == "move":
                turn_count += 1
                user_location = player.move_location(user_location)
        elif user_input == "s" or user_input == "search":
                turn_count += 1
                player.search_location(user_location)            
        elif user_input == "l":
                player.look_at_clues()
        
        else:
            print("\nThat's not valid input.")


if __name__ == "__main__":
    main()






    







                
        
        
        
    
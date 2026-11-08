
import os
import random
import time

_system = os.system
def _portable_system(command):
    if command == "cls" and os.name != "nt":
        command = "clear"                    
    return _system(command)
os.system = _portable_system

#used ai for type_print function , and for msvcrt
try:
    import msvcrt
except ImportError:
    msvcrt = None 
    
def type_print(text, delay = 0.03):
    for i, letter in enumerate(text):
        if msvcrt is not None and msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                print(text[i:], end="", flush=True)
                break
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()
    while msvcrt is not None and msvcrt.kbhit():
        key = msvcrt.getch()


def input_type(text, delay=0.03):
    for i, letter in enumerate(text):
        if msvcrt is not None and msvcrt.kbhit(): 
            key = msvcrt.getch()

            if key == b'\r':
                print(text[i:], end="", flush=True)
                break

        print(letter, end="", flush=True)
        time.sleep(delay)

    return input()


type_print("\n\nWelcome to my text based Adventure Game!")
type_print("\n\nI hope you enjoy!\n\n")
    

def get_name():
    player_name = input_type("What would you like to be called Adventurer? ").strip()
    if len(player_name) < 4:
        type_print("Name must be atleast 4 characters :)")
        os.system('cls')
        return get_name()
    print("\n")
    type_print("Ah " + player_name + ", What an excellent name.")
    return player_name


def play_beginning():
    print("\n")
    type_print("Choose your difficulty.")
    difficulty = input_type("Enter one. Easy, Medium, Or Hard? ").lower().strip()
    if difficulty == "medium":
        type_print("Indeed the path you chosen is a simple one.")
        health = 150
        damage = 7
    elif difficulty == "easy":
        type_print("\nIndeed the path you have chosen is a forgiving one.")
        health = 200
        damage = 10
    elif difficulty == "hard":
        type_print("Indeed the path you have chosen is a hard one.")
        health = 75
        damage = 5
    else:
        os.system('cls')
        type_print("Please enter a proper difficulty.")
        return play_beginning()
    input_type("\nPress ENTER to continue")
    os.system('cls')
    return health, damage

def choose_a_path(player):
    path = input_type("\nNow, where would you like to go? A: A shimmering city. B: A dark forest. C: Through the swamp. I: Inventory P: Drink a health pot ").upper().strip()
    if path == "A":
        os.system('cls')
        return shimmering_city(player)
    elif path == "B":
        os.system('cls')
        return dark_forest(player)
    elif path == "C":
        os.system('cls')
        return swamp(player)
    elif path == "I":
        os.system('cls')
        show_inventory(player)
        return choose_a_path(player)
    elif path == "P":
        os.system('cls')
        use_potion(player)
        return choose_a_path(player)
    else:
        os.system('cls')
        type_print("Please choose A, B, or C, I, or P")
        
        return choose_a_path(player)


def shimmering_city(player):
    os.system('cls')
    type_print("You make your way down to the city... unfortunately you somehow get stopped by the guard for not having any ID.")
    guards = input_type("Do you A. Turn back to the crossroads. B: Say you'll turn back and try to sneak past them. C: Fight ").upper().strip()
    if guards == "A":
        os.system('cls')
        return choose_a_path(player)
    elif guards == "B":
        os.system('cls')
        type_print("This managed to work. You are now inside the city.")
        return inside_city(player)
    elif guards == "C":
        os.system('cls')
        return combat(player, 30, 5, "guard", "city")
    else:
        type_print("Please enter A. B. or C.")
        input_type("Press enter to continue")
        return shimmering_city(player)

def dark_forest(player):
    encounter = random.randint(1, 10)
    if 1 <= encounter <= 6:
        type_print("A wolf approaches you!")
        return combat(player, 25, 5, "wolf")
    elif 7 <= encounter <= 9:
        type_print("A goblin approaches you!")
        return combat(player, 50, 8, "goblin")
    else:
        type_print("You discover a treasure chest! How rare!")
        open_chest(player)
        input_type("Press enter to continue")
        return choose_a_path(player)

def swamp(player):
    path = input_type("You trek your way through the swamp. There you see two things, which do you go to? A.) A Witches hut. B.) A seperate secret enterence to the city.").upper().strip()
    if path == "A":
        witch = input_type("You make your way into the witches hut. Inside you see the witch sleeping. Do you A. Kill her. or B. Wake her up? or C. Leave (recommended)").upper().strip()
        if witch == "A":
            type_print("You tried to kill her, but failed as she suddenly rolled over. This woke her up.")
            return combat(player, 40, 10, "Witch")
        elif witch == "B":
            type_print("You really scared her. She's enraged.")
            return combat(player, 50, 12, "Witch")
        elif witch == "C":
            type_print("You decided to leave (very smart)")
            input_type("Press enter to continue")
            return choose_a_path(player)
        else:
            type_print("Please type A,  B or C.")
            return swamp(player)
    elif path == "B":
        type_print("You find a hidden enterence into the city")
        input_type("Press enter to continue")
        return inside_city(player)
    else:
        type_print("Please choose A or B")
        return swamp(player)

def inside_city(player):
    os.system('cls')
    type_print("You now sneak past the gates into the shimmering city")
    type_print("It is beautiful, unlike any city you have ever seen.")
    choice = input_type("What do you do? A.) Look for the blacksmith. B.) Wander around. C.) Look at the giant grate D. Leave").upper().strip()
    if choice == "A":
        os.system('cls')
        return shop(player)
    elif choice == "B":
        os.system('cls')
        return wander_streets(player)
    elif choice == "C":
        os.system('cls')
        return dungeon(player)
    elif choice == "D":
        os.system('cls')
        return choose_a_path(player)
    else:
        type_print("Please enter A, B, C, or D")
        os.system('cls')
        return inside_city(player)

def shop(player):
    os.system('cls')
    type_print("An exhausted looking blacksmith looks up from this anvil? 'What'll it be' he says")
    type_print(f"You have {player['gold']} gold (earn more from fighting).")
    choice = input_type("A: A health potion (10g). B: A Gold Scythe (+3 dmg, 30g) Or C: Iron Dagger (+1 dmg, 15g) D: War Axe (+5 dmg, 60g) E: Leave ").upper().strip()
    if choice == "A":
        if player["gold"] >= 10:
            player["gold"] -= 10
            pickup(player, "Health Potion")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You don't have enough gold.")
            input_type("Press enter to continue")
            os.system('cls')
            return shop(player)
    elif choice == "B":
        if "Gold Scythe" in player["inventory"]:
            type_print("You cant buy another")
            input_type("Press enter to continue")
            return shop(player)
        if player["gold"] >= 30:
            player["gold"] -= 30
            player["damage"] += 3
            type_print(f"Congrats! Your damage is now {player['damage']}")
            pickup(player, "Gold Scythe")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You don't have enough gold :(")
            input_type("Press enter to continue")
            return shop(player)
    elif choice == "C":
        if "Iron Dagger" in player["inventory"]:
            type_print("You already have one")
            input_type("Press enter to continue")
            return shop(player)
        if player ["gold"] >= 15:
            player["gold"] -= 15
            player["damage"] += 1
            type_print(f"Your damage is now {player['damage']}")
            pickup(player, "Iron Dagger")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You don't have enough gold :(")
            input_type("Press enter to continue")
            os.system('cls')
            return shop(player)
    elif choice == "D":
        if "War Axe" in player["inventory"]:
            type_print("You cant buy another")
            input_type("Press enter to continue")
            return shop(player)
        if player["gold"] >= 60:
            player["gold"] -= 60
            player["damage"] += 5
            type_print(f"Your damage is now {player['damage']}")
            pickup(player, "War Axe")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You don't have enough gold :(")
            input_type("Press enter to continue")
            return shop(player)
    elif choice == "E":
        return inside_city(player)
    else:
        type_print("Please choose A, B, C, D, or E")
        input_type("Press enter to continue")
        return shop(player)

def wander_streets(player):
    os.system('cls')
    roll = random.randint(1, 10)
    if roll <= 4:
        gold_found = random.randint(10, 30)
        player["gold"] += gold_found
        type_print(f"You spot a wallet on the floor +{gold_found} gold")
        input_type("Press enter to continue")
        return inside_city(player)
    elif roll <= 7:
        type_print("An angry dude thinks you stole his wallet!")
        return combat(player, 40, 10, "angry dude", "city")
    else:
        type_print("Nothing worthwhile here")
        input_type("Press enter to continue")
        return inside_city(player)

def combat(player, enemy_health, enemy_damage, enemy_name, next = "crossroads"):
    type_print(f"You encounter a {enemy_name}.")
    type_print(f"It has {enemy_health} health!")
    while enemy_health > 0 and player["health"] > 0:
        choice = input_type("Would you like to A.) Attack or B.) Flee C.) Use a Potion ").strip().upper()
        if choice == "A":
            enemy_health = max(0, enemy_health - player["damage"])
            type_print(f"You did {player['damage']} damage!")
            type_print(f"It has {enemy_health} health left!")
            damage_dealt = random.randint(enemy_damage - 2, enemy_damage + 2)
            if enemy_health > 0:
                player["health"] = max(0, player["health"] - damage_dealt)
                type_print(f"The {enemy_name} did {damage_dealt} damage! You have {player['health']} health left!" )
        elif choice == "B":
            type_print("You scream and run away")
            if next == "city":
                return inside_city(player)
            elif next == "Dungeon":
                return dungeon(player)
            elif next == "HiddenCity":
                return far_underground(player)
            return choose_a_path(player)
        elif choice == "C":
            if use_potion(player) == False:
                type_print("You fumble in your pack and waste your turn :sob:")
            damage_dealt = random.randint(enemy_damage -2, enemy_damage +2)
            player["health"] = max(0, player["health"] - damage_dealt)
            type_print(f"The {enemy_name} did {damage_dealt} damage while you were fooling around! you have {player['health']} health left! ")
        else:
            type_print("Please choose A, B or C")
    if enemy_health <= 0:
        type_print("YOU WON!")
        if enemy_name == "Warden":
            player["warden_dead"] = True
            player["damage"] += 7
            pickup(player, "Warden's spear")
            type_print("The warden collapses. The gold door grinds open behind it.")
            input_type("Press enter to continue")
            player["dungeon_floor"] = 6
            return village(player)
        if enemy_name == "The Sealed One":
            player["sealed_one_dead"] = True
            input_type("Press enter to continue")
            return sealed_ending(player)
        enemy_drop(player, enemy_name)
        input_type("Press enter to continue")
        if next == "city":
            return inside_city(player)
        elif next == "Dungeon":
            player["dungeon_floor"] += 1
            return dungeon(player)
        elif next == "HiddenCity":
            return far_underground(player)
        return choose_a_path(player)
    elif player["health"] <= 0:
        type_print("You lost LOL")
        type_print("You wake up at the crossroads. Your bag feels lighter.")
        player["health"] = player["max_health"] // 2
        player["gold"] = player["gold"] // 2
        player["dungeon_floor"] = 0
        input_type("Press enter to continue")
        return choose_a_path(player)

def village(player):
    os.system('cls')
    type_print("The tunnel opens into a street...?")
    type_print("Above you, far above, you can hear the ground shake above you.")
    choice = input_type("What do you do? A.) Visit the market B.) Talk to a local C.) Keep walking D.) Try to go back up").strip().upper()
    if choice == "A":
        os.system('cls')
        return merchant(player)
    elif choice == "B":
        os.system('cls')
        return local(player)
    elif choice == "C":
        os.system('cls')
        return far_underground(player)
    elif choice == "D":
        player["dungeon_floor"] = 0
        os.system('cls')
        return inside_city(player)
    else:
        type_print("Please choose A, B, C, or D" )
        input_type("Press enter to continue")
        return village(player)

def merchant(player):
    os.system('cls')
    type_print("An old woman sits behind a counter. Her eyes are pale, she looks tired.")
    type_print("'You came from up there' she says. Haven't seen one of yem since the 3rd epoch.")
    type_print(f"You have {player['gold']} gold.")
    choice = input_type("A.) Health potion(8g). B.) Whetstone(+2 dmg, 40g) C.) Iron Heart(+25 max health, 50g) D.) Leave").strip().upper()
    if choice == "A":
        if player["gold"] >= 8:
            player["gold"] -= 8
            pickup(player, "Health Potion")
            input_type("Press enter to continue")
            return merchant(player)
        else:
            type_print("You don't have enough gold")
            input_type("Press enter to continue")
            return merchant(player)
    elif choice == "B":
        if player ["whetstone_bought"]:
            type_print("'I've already used the whetstone for you' says the merchant.")
            input_type("Press enter to continue")
            return merchant(player)
        if player["gold"] >= 40:
            player["whetstone_bought"] = True
            player["gold"] -= 40
            player["damage"] += 2
            type_print(f"She sharpens your weapon. Your damage is now {player['damage']}")
            input_type("Press enter to continue")
            return merchant(player)
        else:
            type_print("You don't have enough gold")
            input_type("Press enter to continue")
            return merchant(player)
    elif choice == "C":
        if player["iron_heart_bought"]:
            type_print("'You've already bought one' she says")
            input_type("Press enter to continue")
            return merchant(player)
        if player["gold"] >= 50:
            player["iron_heart_bought"] = True
            player["gold"] -= 50
            player["max_health"] += 25
            player["health"] += 25
            type_print(f"She hands you some mercury in a bottle and tells you to drink up. Your max health is now {player['max_health']}")
            input_type("Press enter to continue")
            return merchant(player)
        else:
            type_print("You don't have enough gold")
            input_type("Press enter to continue")
            return merchant(player)

    elif choice == "D":
        os.system('cls')
        return village(player)
    else:
        type_print("Please choose A, B, C, or D.")
        input_type("Press enter to continue")
        return merchant(player)

def local(player):
    os.system('cls')
    type_print("A thin man leans against a wall. He looks like he hasnt slept in a while...")
    type_print("'You killed the warden' he says 'we heard it fall from here'.")
    type_print("'Do you know how much it did for us?'")
    choice = input_type("A.) It was guarding this place B.) It was keeping something out. C.) Say nothing").upper().strip()
    if choice == "A":
        type_print("'No,' he says. 'it was keeping something in'")
    elif choice == "B":
        type_print("'Wrong way round' he says 'it was keeping it from getting out'")
    else:
        type_print("Dont matter, he says 'You should know either way'")
    type_print("'When the old city was sealed, the warden was used as a lock to keep it out. The sealed one is what the lock was for'")
    type_print("'Now the lock is broken. It will awaken soon.'")
    input_type("Press enter to continue")
    return village(player)

def far_underground(player):
    os.system('cls')
    type_print("The streets narrow.")
    choice = input_type("A.) Walk deeper. B.) Approach the sealed gate. C.) go back.").upper().strip()
    if choice == "A":
        os.system('cls')
        roll = random.randint(1, 10)
        if roll <= 2:
            type_print("A pale figure steps out of a doorway.")
            return combat(player, 40, 12, "sealed child", "HiddenCity")
        elif roll <= 4:
            type_print("Something flys through the walls.")
            return combat(player, 55, 16, "ghoul", "HiddenCity")
        elif roll <= 6:
            type_print("A child-shaped shadow runs past you.")
            return combat(player, 50, 15, "Pale Child", "HiddenCity")
        elif roll <= 7:
            type_print("A watcher in armor approaches")
            return combat(player, 80, 14, "Watcher", "HiddenCity")
        elif roll <= 8:
            type_print("A small thing crawls over.")
            return combat(player, 70, 12, "better crawler", "HiddenCity")
        else:
            type_print("A hunched thing crawls over.")
            return combat(player, 80, 13, "elder crawler", "HiddenCity")
    elif choice == "B":
        os.system('cls')
        return sealed_gate(player)
    elif choice == "C":
        os.system('cls')
        return village(player)
    else:
        type_print("Please choose A, B, or C.")
        input_type("Press enter to continue")
        return far_underground(player)

def sealed_gate(player):
    os.system('cls')
    if player["sealed_one_dead"]:
        type_print("The gate is broken open. Nothing is inside...")
        input_type("Press enter to continue")
        return far_underground(player)
    type_print("An enormous stone gate stands here.")
    type_print(" Many chains lay snapped on the floor. A couple remain.")
    type_print("You hear something breathe.")
    choice = input_type("A.) Break the last chains. B.) Leave").upper().strip()
    if choice == "A":
        os.system('cls')
        type_print("The last chain falls. The gate opens")
        type_print("A shape appears, it has too many arms.")
        type_print("It speaks")
        type_print("'You freed me, an unwise decision.'")
        return combat(player, 200, 16, "The Sealed One", "HiddenCity")
    elif choice == "B":
        os.system('cls')
        return far_underground(player)
    else:
        type_print("Please choose A or B")
        input_type("Press enter to continue")
        return sealed_gate(player)
    
    
def sealed_ending(player):
    os.system('cls')
    type_print("The sealed one falls. The lanterns go out one by one.")
    type_print("The village is quiet for the first time in a long time.")
    type_print("You climb back up to the surface.")
    type_print("Congratulations! You have completed the game!")
    type_print("\nTHE END\n")
    choice = input_type("A.) Play again. B.) Close").upper().strip()
    if choice == "A":
        os.system('cls')
        return start_game()
    elif choice == "B":
        os.system('cls')
        type_print("THANKS FOR PLAYING!!")
        return
    else:
        type_print("Please choose A or B")
        input_type("Press enter to continue")
        return sealed_ending(player)
    
def dungeon(player):
    os.system('cls')
    floor = player["dungeon_floor"]
    if player["warden_dead"] and floor == 0:
        type_print("The tunnel is quiet, the tunnel to the Sealed Village is Open")
        choice = input_type("A.) Walk straight to the village. B.) Fight your way down again. C.) Leave").strip().upper()
        if choice == "A":
            os.system('cls')
            return village(player)
        elif choice == "B":
            os.system('cls')
        elif choice == "C":
            return inside_city(player)
        else:
            type_print("Please choose A, B, or C.")
            input_type("Press enter to continue")
            return dungeon(player)
    if floor >= 6:
        return village(player)
    if floor == 5:
        if player["warden_dead"]:
            player["dungeon_floor"] = 6
            return village(player)
        return boss_fight(player)
    if floor > 0:
        type_print(f"You stand in the tunnel, {floor} floor(s) under the city.")
        choice = input_type("A.) Fight whats ahead. B: Climb back up (lose all dungeon progress)").upper().strip()
        if choice == "B":
            player["dungeon_floor"] = 0
            type_print("You climb back up. Losing all your progress.")
            input_type("Press enter to continue")
            os.system('cls')
            return inside_city(player)
        elif choice != "A":
            type_print("Please choose A or B.")
            input_type("Press enter to continue")
            return dungeon(player)
    os.system('cls')
        
    if floor == 0 :
            type_print("something scurries past your feet")
            return combat(player, 20, 5, "crawler", "Dungeon")
    elif floor == 1:
            type_print("A figure stumbles out")
            return combat(player, 35, 7, "Shanker", "Dungeon")
    elif floor == 2:
            type_print("Something drags itself to you")
            return combat(player, 45, 6, "trash thing", "Dungeon")
    elif floor == 3:
            type_print("Something drops from above")
            return combat(player, 55, 10, "haunter", "Dungeon")
    else:
            type_print("two shankers step out side by side")
            return combat(player, 70, 12, "twin shankers", "Dungeon")
        
def boss_fight(player):
    if player["warden_dead"] == True:
        type_print("The gold door stands silent. Nothing is behind it now.")
        input_type("Press enter to continue")
        return dungeon(player)
    os.system('cls')
    type_print("The door slides open, the ground rumbles as the thing behind it awakens...")
    type_print("The warden RISES")
    return combat(player, 100, 12, "Warden", "Dungeon")        

def enemy_drop(player, enemy_name):
    roll = random.randint(1, 100)
    if roll <= 30:
        type_print(f"The {enemy_name} was holding something...")
        pickup(player, "Health Potion")
    elif roll <= 60:
        gold_found = random.randint(10, 20)
        player["gold"] += gold_found
        type_print(f"You got {gold_found} gold from that corpse!")

def show_inventory(player):
    type_print("\n --- INVENTORY ---")
    if player["inventory"] == []:
        type_print("Your pack is empty.")
    else:
        for item in player["inventory"]:
            type_print(" -" + item)
    type_print(f"\n Gold: {player['gold']}")
    type_print(f"Health: {player['health']}/{player['max_health']}")
    type_print(f"Damage: {player['damage']}")
    input_type("Press Enter to continue")
    os.system('cls')

def use_potion(player):
    if "Health Potion" not in player["inventory"]:
        type_print("You dig around in your pack... No potions. :(")
        return False
    if player["health"] >= player["max_health"]:
        type_print("You're already at full health.")
        return False
    player["inventory"].remove("Health Potion")
    old_health = player["health"]
    player["health"] += 50
    if player["health"] > player["max_health"]:  # noqa: PLR1730
        player["health"] = player["max_health"]
    type_print(f"You heal {player['health'] - old_health} health")
    type_print(f"Health: {player['health']}/{player['max_health']}")
    return True    
    
def pickup(player, item):
    player["inventory"].append(item)
    type_print("you got a " + item + "!")
    
def silver_scythe(player):
    if "Silver Scythe" in player["inventory"]:
        return False
    player["damage"] += 2
    pickup(player, "Silver Scythe")
    type_print(f"Your damage now is {player['damage']}")
    return True

def open_chest(player):
    type_print("you open the chest")    
    gold_found = random.randint(5, 20)
    player["gold"] += gold_found
    type_print(f"You find {gold_found} gold!")
    roll = random.randint(1, 100)
    if roll <= 55:
        pickup(player, "Health Potion")
    elif roll <= 80:
        if silver_scythe(player) == False:
            gold_found = random.randint(10, 25)
            player["gold"] += gold_found
            type_print(f"you leave the scythe and grab {gold_found} gold instead ")        
    elif roll <= 90:
        if silver_scythe(player) == False:
             gold_found = random.randint(10, 25)
             player["gold"] += gold_found
             type_print(f"You leave the scythe and grab {gold_found} gold instead")
        pickup(player, "Health Potion")
        type_print("WOW")
    else:
        type_print("... and nothing else. Somebody else got here first!")
    
def start_game():
    player_name = get_name()
    player_health, player_damage = play_beginning()
    player = {
    "name": player_name,
    "warden_dead": False,
    "sealed_one_dead": False,
    "whetstone_bought": False,
    "iron_heart_bought": False,
    "dungeon_floor": 0,
    "damage": player_damage,
    "health": player_health,
    "max_health": player_health,
    "inventory": [],
    "gold": 0,
    }   
    type_print(f"\nWelcome {player_name}!")
    type_print(f"Your starting health is {player_health} and your starting damage is {player_damage}.")
    choose_a_path(player)
if __name__ == "__main__":
    start_game()

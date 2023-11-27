import random
import keywords
import compendium_rooms

rooms = compendium_rooms.compendium_rooms
room_list = compendium_rooms.room_names_dict
actions = keywords.action_keywords


### ROLLING DICE ###


def roll_dice(num_of_dice: int, size_of_dice: int) -> list:
    """
    Roll a set number of dice according to the number of dice and the size of the dice. Saves all rolls in a list.

    Args:
        num_of_dice (int): The number of dice rolled
        size_of_dice (int): The size of the dice rolled

    Returns:
        dice_rolls (list): All of the dice rolled
    """
    dice_rolls = []
    for i in range(num_of_dice):
        dice_rolls.append(random.randint(1, size_of_dice))

    # PRINT TESTS
    # print("roll_dice", dice_rolls)
    return (dice_rolls)


def roll_ability_check(modifier: int = 5, char_level: int = 10) -> tuple:
    """
    Roll for an ability check. Also, saves if a nat 1 or nat 20 was rolled.

    Arguments:
        modifier (int): rolled ability modifier
        char_level (int): level of the character

    Returns:
        tuple: A tuple with base roll[0], total roll[1], nat 1 bool[2], and nat 20 bool[3].
    """
    roll = roll_dice(1, 20)[0]  # base dice roll
    # calculate total roll with modifier & char level
    total_roll = roll + modifier + char_level

    # print(
    #     f"rolled: {roll}, nat 1: {nat_one(roll)}, nat 20: {nat_twenty(roll)},\n{roll}+{modifier}+{char_level}={total_roll}")
    return (roll, total_roll, nat_one(roll), nat_twenty(roll))


def roll_ability_save(modifier: int = 14) -> tuple:
    """
    Roll for an ability save. Also, saves if a nat 1 or nat 20 was rolled.

    Arguments:
        ability (str): the ability we are checking.

    Returns:
        tuple: A tuple with base roll[0], total roll[1], nat 1 bool[2], and nat 20 bool[3].
    """
    roll = roll_dice(1, 20)[0]  # base dice roll
    total_roll = roll + modifier  # calculate total roll with modifier

    print(
        f"rolled: {roll}, nat 1: {nat_one(roll)}, nat 20: {nat_twenty(roll)},\n{roll}+{modifier}={total_roll}")
    return (roll, total_roll, nat_one(roll), nat_twenty(roll))


def roll_attack_or_spell(modifier: int = 15) -> tuple:
    """
    Roll attack or spell roll. Also, saves if a nat 1 or nat 20 was rolled.

    Arguments:
        modifier (int): character attack roll modifier

    Returns:
        tuple: A tuple with base roll[0], total roll[1], nat 1 bool[2], and nat 20 bool[3].
    """
    roll = roll_dice(1, 20)[0]  # base dice roll
    total_roll = roll + modifier  # calculate total roll with modifier

    print(
        f"rolled: {roll}, nat 1: {nat_one(roll)}, nat 20: {nat_twenty(roll)},\n{roll}+{modifier}={total_roll}")
    return (roll, total_roll, nat_one(roll), nat_twenty(roll))


def nat_one(roll: int) -> bool:
    """
    Determine if the dice roll was a natural one aka an automatic critical failure

    Args:
        roll (int): The dice number rolled

    Returns: 
        bool: True if it's a natural 1 and false for otherwise
    """
    return roll == 1


def nat_twenty(roll: int) -> bool:
    """
    Determine if the dice roll was a natural twenty aka an automatic critical success

    Args:
        roll (int): The dice number rolled

    Returns: 
        bool: True if it's a natural 20 and false for otherwise
    """
    return roll == 20


def calculate_damage_dealt(rolls: list = [1, 2, 3], modifier: int = 0) -> int:
    """
    Sum total damage rolled and add any modifiers

    Arguments:
        rolls (list): the value of the rolled dice.
        modifier (int): additional base damage added to roll.

    Returns:
        total (int): the total sum of a given rolls and modifiers.
    """
    total = sum(rolls) + modifier
    # print(f"calculate_damage_dealt... {rolls}+{modifier}={total}")
    return total


def calculate_hazard_damage_dealt(num_of_dice: int = 1, dice_size: int = 4, modifier: int = 0, char_result=1) -> int:
    """
    Calculate how much damage a hazard dealt. Rolls the dice, adds the modifier, and calculates dmg based on player's degree of success.

    Arguments:
        num_of_dice (int): The number of dice rolled
        size_of_dice (int): The size of the dice rolled
        modifier (int): additional base damage added to roll.
        char_result (int): character's degree of success (-1=crit fail, 0= fail, 1=pass, 2=crit pass)

    Returns:
        total_damage (int): total damage a character will recieve (based on their degree of success)
    """
    modifer_based_on_success = {-1: 2, 0: 1, 1: 0, 2: 0}

    rolled_dice = roll_dice(num_of_dice, dice_size)
    total_damage = calculate_damage_dealt(
        rolled_dice, modifier) * modifer_based_on_success[char_result]

    # print(
    #     f"calculate_hazard_damage_dealt... ({rolled_dice}+{modifier})*{modifer_based_on_success[char_result]}={total_damage}")
    return total_damage

# FIX PLEASE


def calculate_enemy_damage_dealt(num_of_dice: int = 1, dice_size: int = 4, dmg_modifier: int = 0, atk_modifier: int = 18, char_ac=28) -> int:
    modifer_based_on_success = {-1: 0, 0: 0, 1: 1, 2: 2}

    enemy_atk_roll = roll_attack_or_spell(atk_modifier)
    enemy_result = degree_of_success(
        char_ac, enemy_atk_roll[1], enemy_atk_roll[2], enemy_atk_roll[3])
    rolled_dice = roll_dice(num_of_dice, dice_size)
    total_damage = calculate_damage_dealt(
        rolled_dice, dmg_modifier) * modifer_based_on_success[enemy_result]

    print(
        f"calculate_enemy_damage_dealt... ({rolled_dice}+{dmg_modifier})*{modifer_based_on_success[enemy_result]}={total_damage}")
    return total_damage


calculate_enemy_damage_dealt(3, 12, 4)
# DEGREE OF SUCCESS
# Did the thing pass the check? Also account for crits


def degree_of_success(dc: int, total_roll: int, nat_one: bool = False, nat_twenty: bool = False) -> int:
    """
    Determine the degree of success of a certain roll. Success is determined by a dc or difficulty check.

    If the player rolls a natural one, then it is an automatic critical failure. 
    If the player rolls a natural twenty, then the degree of success is increased by one level.
    Anything 10 or higher than the dc is a critical success. Anything higher than the dc is a success.
    Anything lower than the dc is a failure. And anything 10 or lower than the dc is a critical failure.

    Args:
        dc (int): The difficulty check
        total_roll (int): The total roll of the player, includes the dice roll and any modifiers added.
        nat_one (bool): Was a nat 1 rolled?
        nat_twenty (bool): Was a nat 20 rolled?

    Returns:
        int: integer representing degrees of success (-1=crit fail, 0= fail, 1=pass, 2=crit pass).
    """
    if nat_one:
        print("you rolled a Nat One")
        return -1

    if nat_twenty:
        print("you rolled a Nat Twenty")
        dc -= 10  # Decrease DC by 10 for a nat twenty

    if total_roll >= dc + 10:
        # print("you rolled a crit success... 2")
        return 2
    elif total_roll >= dc:
        # print("you rolled a success... 1")
        return 1
    elif total_roll < dc - 10:
        # print("you rolled a crit fail... -1")
        return -1
    else:
        # print("you rolled a fail... 0")
        return 0


def print_degree_of_success_result(result: int) -> str:
    """
    Will print out the degree of success of a roll

    Arguments:
        result (int): character's degree of success (-1=crit fail, 0= fail, 1=pass, 2=crit pass)
    """
    degree_of_success = {-1: "Critical Failure",
                         0: "Failure", 1: "Success", 2: "Critical Success"}
    return degree_of_success.get(result, "Invalid Result")

### ACTUAL RESULTS ###


def ability_roll_and_text_result(category: str, ability: str, dc: int, crit_success_text="", success_text="", fail_text="", crit_fail_text=""):
    """
    Determines the roll for an ability score, and whether you passed the dc for the following scenario. 
    Your degree of success determines the text of the scenario you get.

    Arguments:
        category (str): type of action you're rolling for.
        ability (str): which ability modifier you roll for.
        dc (int): difficulty check, the parameter for a pass or fail.
        crit_success_text (str): critical success text.
        success_text (str): standard success text.
        fail_text (str): standard failure text.
        crit_fail_text (str): critical failure text.

    Returns:
        text_result (tuple): the result (-1 through 2), total roll, final text result
    """
    print(f"\nYou must roll for action: {category}")

    # our actual rolls and result
    rolled = ability_check_or_save(ability)
    result = degree_of_success(
        dc, rolled[1], rolled[2], rolled[3])

    # is the inserted text a binary pass or fail? Do the following
    text_result = ""
    if crit_success_text and result == 2:
        text_result = crit_success_text
    elif result == 1 or result == 2:
        text_result = success_text
    elif result == 0:
        text_result = fail_text
    elif result == -1:
        text_result = crit_fail_text
    else:
        text_result = fail_text

    return (result, rolled[1], text_result)


def calculate_attack_and_dmg(num_of_dice: int, dice_sides: int, atk_type: str, modifier: int = 0, target_ac: int = 10) -> int:
    """
    Determines the roll for an attack, whether you beat the targets ac and how much you hit for.

    Arguments:
        num_of_dice (int): the number of attack dice rolled
        dice_sides (int): the damage size of the attack dice
        atk_type (string): physical or spell attack
        modifier (int): additional damage modifier
        target_ac (int): target ac or armor class

    Returns:
        int: the amount of damage you dealt to the target, will be 0 if you missed.
    """
    all_rolls = roll_dice(num_of_dice, dice_sides)
    atk_rolled = attack_or_spell_roll(atk_type)
    result = degree_of_success(
        target_ac, atk_rolled[1], atk_rolled[2], atk_rolled[3])
    if result <= 0:
        return 0
    else:
        return damage_dealt(all_rolls, modifier, atk_rolled[3])

## PLAYER ACTIONS ###


# def current_room_data(current_room, action):
#     id = room_list[current_room]

#     print("BASIC INFORMATION")
#     print("Room ID:\n", rooms[id].room_id)
#     print("Event:\n", rooms[id].event)
#     print("Room Entry Description:\n", rooms[id].description)
#     print("Secret Solved Leads To:\n", rooms[id].secret)

#     print("Keyword Action:\n", action)
#     print("DC", rooms[id].actions[0][action]["DC"])
#     print(rooms[id].actions[0][action]["skill_success"][0])
#     print(rooms[id].actions[0][action]["skill_success"][1])
#     print(rooms[id].actions[0][action]["skill_fail"])

#     print("Completed Room:\n", rooms[id].room_cleared)

def enter_a_command() -> str:
    """
    Command to simply get the user input.
    """
    command = input("Please enter a command: ").strip().lower()
    return command


def player_input_category(word: str) -> str:
    """
    Determine player input and if it is correlated with a specific category or keyword available.

    Arguments:
        word (str): users inputted words

    Returns:
        str: keyword category determined by user input, otherwise None is provided.
    """
    action = None

    # Iterate through each action category and its associated keywords
    for category, keywords in actions.items():
        for keyword in keywords:
            if word == keyword:  # Check for exact match
                action = category
                break  # Match is found break the loop
        if action:
            break  # Action is found break the loop

    # If no exact match is found, check for partial matches
    if not action:
        for category, keywords in actions.items():
            for keyword in keywords:
                if keyword in word:
                    action = category
                    break  # keyword is found break the loop
            if action:
                break

    # PRINT TESTS
    if action is not None:
        print(f"The input word corresponds to the action: {action}")
    else:
        print("No matching action found.")

    return action  # Return the matched action or None if there's no match


def get_player_input(command: str) -> str:
    """
     Will make sure that player has inputted a proper command. This includes navigational commands.

    Arguments:
        command (str): the direct input given by the player

    Returns:
        str: will give the verified keyword category given by the player
    """
    while True:
        try:
            player_inputed = player_input_category(command)

            # Checking for navigation specifically first
            if player_inputed == "navigation":
                command = command.split()
                if len(command) > 1:
                    direction = command[1]
                    if direction in ["north", "up", "forward", "ahead", "south", "down", "back", "backward", "behind", "east", "right", "west", "left"]:
                        return player_input_category(direction)
                    else:
                        print(
                            "Invalid direction. Please enter 'north', 'south', 'east', or 'west'.")
                else:
                    print("Invalid navigation command. Please specify a direction.")
            elif player_inputed is None:
                print("Invalid command, please try again")
            else:
                return player_inputed
        except ValueError or TypeError:
            print("Invalid command, please try again")


class Test_Chara:
    lvl = 10

    expertise = {
        "trained": 2,
        "expert": 4,
        "master": 6,
        "legendary": 8,
        "potency": 2
    }
    ability = {
        "str": 5,
        "dex": 3,
        "con": 4,
        "int": 0,
        "wis": 2,
        "cha": 1
    }
    saves = {
        "perception": lvl + ability["wis"] + expertise["master"],
        "fortitude": lvl + ability["con"] + expertise["master"],
        "reflex": lvl + ability["dex"] + expertise["expert"],
        "will": lvl + ability["wis"] + expertise["expert"]
    }
    phys_or_spell_atk = {
        "attack": lvl + ability["str"] + expertise["master"] + expertise["potency"],
        "spell": 0
    }


# if __name__ == "__main__":
    # inputted = input("Pick your alignment: ")
    # player_input_category(inputted)
    # print("")

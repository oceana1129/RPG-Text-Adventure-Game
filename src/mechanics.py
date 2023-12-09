import random
import sys
import time
import os
import keywords

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

    # print(
    #     f"rolled: {roll}, nat 1: {nat_one(roll)}, nat 20: {nat_twenty(roll)},\n{roll}+{modifier}={total_roll}")
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

    # print(
    #     f"ROLL_ATTACK_OR_SPELL:\nrolled: {roll}, nat 1: {nat_one(roll)}, nat 20: {nat_twenty(roll)},\n{roll}+{modifier}={total_roll}")
    return (roll, total_roll, nat_one(roll), nat_twenty(roll))


def nat_one(roll: int) -> bool:
    """
    Determine if the dice roll was a natural one aka an automatic critical failure

    Args:
        roll (int): The dice number rolled

    Returns: 
        bool: True if it's a natural 1 and false for otherwise
    """
    if roll == 1:
        print_text(f"\033[1m\033[91mRolled a NAT 1\033[0m")
    return roll == 1


def nat_twenty(roll: int) -> bool:
    """
    Determine if the dice roll was a natural twenty aka an automatic critical success

    Args:
        roll (int): The dice number rolled

    Returns: 
        bool: True if it's a natural 20 and false for otherwise
    """
    if roll == 20:
        print_text(f"\033[1m\033[38;5;28mRolled a NAT 20\033[0m")
    return roll == 20


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
    # print(f"total roll...{total_roll}")
    # print(f"dc... {dc}")
    if nat_one:
        return -1

    if nat_twenty:
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

### ENEMY RESULTS ###


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


def calculate_enemy_attack_damage_dealt(num_of_dice: int = 1, dice_size: int = 4, dmg_modifier: int = 5,
                                        atk_modifier: int = 18, char_ac=28) -> int:
    modifer_based_on_success = {-1: 0, 0: 0, 1: 1, 2: 2}

    enemy_atk_roll = roll_attack_or_spell(atk_modifier)
    print_text(f"They rolled a {BOLD}{enemy_atk_roll[1]}{RESET}")
    enemy_result = degree_of_success(
        char_ac, enemy_atk_roll[1], enemy_atk_roll[2], enemy_atk_roll[3])
    damage_dice = roll_dice(num_of_dice, dice_size)
    total_damage = calculate_damage_dealt(
        damage_dice, dmg_modifier) * modifer_based_on_success[enemy_result]

    # print(
    #     f"calculate_enemy_damage_dealt... ({damage_dice}+{dmg_modifier})*{modifer_based_on_success[enemy_result]}={total_damage}")
    return total_damage


def calculate_enemy_saving_throw_damage(num_of_dice: int = 2, dice_size: int = 4, dmg_modifier:
                                        int = 5, atk_modifier: int = 18, dc=22, char_roll=21,
                                        nat_one=False, nat_twenty=False):
    modifer_based_on_success = {-1: 2, 0: 1, 1: 0.5, 2: 0}

    char_degree_of_success = degree_of_success(
        dc, char_roll, nat_one, nat_twenty)

    damage_dice = roll_dice(num_of_dice, dice_size)
    total_damage = round(calculate_damage_dealt(
        damage_dice, dmg_modifier) * modifer_based_on_success[char_degree_of_success])

    # print(
    #     f"calculate_enemy_saving_throw_damage... ({damage_dice}+{dmg_modifier})*"
    #     f"{modifer_based_on_success[char_degree_of_success]}={total_damage}")
    return total_damage


def enemy_text_result(damage=7, hit_text="Enemy hit", miss_text="Enemy miss"):
    if damage == 0:
        return miss_text
    else:
        return hit_text


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


def ability_save_and_text_result(modifier: int = 10, dc: int = 20, crit_success_text="", success_text="", fail_text="", crit_fail_text=""):
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
    # our actual rolls and result
    rolled = roll_ability_save(modifier)
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

    rolled = roll_ability_check(ability)
    result = degree_of_success(
        dc, rolled[1], rolled[2], rolled[3])

    # is the inserted text a binary pass or fail? Do the following
    text_result = ""
    if crit_success_text and result == 2:
        text_result = crit_success_text
    elif result >= 1:
        text_result = success_text
    elif crit_fail_text and result == -1:
        text_result = crit_fail_text
    else:
        text_result = fail_text

    return (result, rolled[1], text_result)

## PLAYER ACTIONS ###


# def current_room_data(current_room, action):
#     pass

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
        print(f"Corresponding Input: {action}\n")
    else:
        print("No matching action found.\n")

    return action  # Return the matched action or None if there's no match


def player_input(command: str) -> str:
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
                command = input("Enter a direction: ").lower()
                if command in ["north", "up", "forward", "ahead", "south", "down", "back", "backward", "behind", "east", "right", "west", "left"]:
                    player_inputed = player_input_category(command)
                    return player_inputed
                else:
                    print(
                        "Invalid direction. Please enter 'north', 'south', 'east', or 'west'.")
            elif player_inputed is None:
                print("Invalid command, please try again\n")
                command = input("Enter a valid command: ")
            else:
                return player_inputed
        except (ValueError, TypeError):
            print("Invalid command, please try again\n")
            command = input("Enter a valid command: ")


# text printed like typing function
# ANSI escape codes for text color
BOLD = '\033[1m'
RESET = '\033[0m'  # Reset color to default


def print_text(message: str = "", text_speed="default"):
    print("")
    line_speed_settings = {"default": 0.1, "slow": 0.9, "normal": 0.7,
                           "fast": 0.3, "extra fast": 0.1}
    speed_settings = {"default": 0.009, "slow": 0.09,
                      "normal": 0.02, "fast": 0.01, "extra fast": 0.009}
    # Default to "normal" speed if speed is not provided
    speed = speed_settings.get(text_speed, 0.1)
    line_speed = line_speed_settings.get(text_speed, 0.009)
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(speed)
        else:
            time.sleep(line_speed)
    print("")


def style_damage(name="player", damage=10, current_hp=100):
    RED = '\033[91m'
    FIREBRICK = '\033[38;5;196m'
    DARK_SALMON = '\033[38;5;210m'
    PALE_VIOLET_RED = '\033[38;5;211m'
    RESET = '\033[0m'
    if damage >= 40:
        return (f"{FIREBRICK}{BOLD}{name} take's {damage} damage{RESET}"
                f"\n{BOLD}{name} currently has {current_hp} HP{RESET}")
    elif damage >= 20:
        return (f"{RED}{BOLD}{name} take's {damage} damage{RESET}"
                f"\n{BOLD}{name} currently has {current_hp} HP{RESET}")
    elif damage > 0:
        return (f"{DARK_SALMON}{BOLD}{name} take's {damage} damage{RESET}"
                f"\n{BOLD}{name} currently has {current_hp} HP{RESET}")
    else:
        return (f"{PALE_VIOLET_RED}{BOLD}{name} take's {damage} damage{RESET}"
                f"\n{BOLD}{name} currently has {current_hp} HP{RESET}")


def style_heal(name="player", heal=10):
    SEA_GREEN = '\033[38;5;28m'
    LIGHT_GREEN = '\033[38;5;83m'
    PALE_GREEN = '\033[38;5;114m'
    RESET = '\033[0m'
    if heal >= 25:
        return (f"{SEA_GREEN}{BOLD}{name} heal's for {heal} HP{RESET}")
    elif heal >= 15:
        return (f"{LIGHT_GREEN}{BOLD}{name} heal's for {heal} HP{RESET}")
    elif heal > 0:
        return (f"{PALE_GREEN}{BOLD}{name} heal's for {heal} HP{RESET}")
    else:
        return ("")


def style_mana(mana=2, current_mana=50):
    ROYAL_BLUE = '\033[38;5;69m'
    if current_mana == 0:
        return (f"{ROYAL_BLUE}{BOLD}Not enough mana to cast this spell.\nYou have {current_mana} MP left{RESET}")
    return (f"{ROYAL_BLUE}{BOLD}You used {mana} MP\nYou have {current_mana} MP left{RESET}")


def style_restore_mana(restored=2, current_mana=50):
    ROYAL_BLUE = '\033[38;5;69m'
    return (f"{ROYAL_BLUE}{BOLD}You restore {restored} MP, you have {current_mana} left{RESET}")


def style_error(message):
    RED = '\033[38;5;88m'

    error_message = f"{RED}ERROR: {message}{RESET}"
    return (error_message)


# print("""
# Red (Default): \033[91mError: Something went wrong\033[0m
# Bright Red: \033[91;1mError: Something went wrong\033[0m
# Light Red: \033[31mError: Something went wrong\033[0m
# Dark Red: \033[38;5;88mError: Something went wrong\033[0m
# Maroon: \033[38;5;52mError: Something went wrong\033[0m
# Crimson: \033[38;5;160mError: Something went wrong\033[0m
# FireBrick: \033[38;5;196mError: Something went wrong\033[0m
# IndianRed: \033[38;5;131mError: Something went wrong\033[0m
# Salmon: \033[38;5;208mError: Something went wrong\033[0m
# LightCoral: \033[38;5;203mError: Something went wrong\033[0m
# """)

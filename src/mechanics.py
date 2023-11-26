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
        nat_one (bool): Whether the players original roll was a natural one.
        nat_twenty (bool): Whether the players original roll was a natural twenty.

    Returns:
        int: An integer representing a crit success (2), a success (1), a failure (0), a crit failure (-1).
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


def print_pass_fail_or_crit(result):
    """
    Will print out the degree of success of a roll
    """
    degree_of_success = {-1: "Critical Failure",
                         0: "Failure", 1: "Success", 2: "Critical Success"}
    return degree_of_success.get(result, "Invalid Result")


def ability_check_or_save(ability: str) -> tuple:
    """
    Configure the value of a roll for either an ability check or an ability save. Also save the values of a nat one or nat twenty.

    Arguments:
        ability (str): the ability we are checking.

    Returns:
        tuple: A tuple containing the final roll, modified roll, nat one check, and nat twenty check.
    """
    roll = roll_dice(1, 20)[0]  # base dice roll

    # determine if the roll is for an ability check or save
    if ability in Test_Chara.ability:
        modifier = Test_Chara.ability[ability] + Test_Chara.lvl
    elif ability in Test_Chara.saves:
        modifier = Test_Chara.saves[ability]

    total_roll = roll + modifier  # calculate total roll with modifier

    # nat one and twenty results
    nat_twenty_result = nat_twenty(roll)
    nat_one_result = nat_one(roll)
    # print(f"rolls: {roll}, nat 1: {nat_one_result}, nat 20: {nat_twenty_result}, ability: {ability}, modifier: {modifier}, total: {total_roll}")
    return (roll, total_roll, nat_one_result, nat_twenty_result)


def attack_or_spell_roll(attack_type: str) -> tuple:
    """
    Configure the value of a roll for a physical or spell attack roll. Also save the values of a nat one or nat twenty.

    Arguments:
        attack_type (str): determine whether we are rolling for a physical or spell attack

    Returns:
        tuple: A tuple containing the final roll, modified roll, nat one check, and nat twenty check.
    """
    roll = roll_dice(1, 20)[0]
    modifier = Test_Chara.phys_or_spell_atk[attack_type]

    total_roll = roll + modifier

    nat_twenty_result = nat_twenty(roll)
    nat_one_result = nat_one(roll)
    print(f"\nrolls: {roll}, nat 1: {nat_one_result}, nat 20: {nat_twenty_result}, type: {attack_type}, modifier: {modifier}, total: {total_roll}")
    return (roll, total_roll, nat_one_result, nat_twenty_result)


def damage_dealt(rolls: list = [0], modifier: int = 0, nat_twenty: bool = False) -> int:
    """
    Sums up the total damage rolled from a set of dice along with any additional damage modifiers.
    This function is used primarily for damage rolls from spells and attacks.
    If a natural 20 is rolled on the attack dice, then the total damage is doubled.

    Arguments:
        rolls (list): the value of the rolled dice.
        modifier (int): additional base damage added to roll.
        nat_twenty (bool): Used to determine if a critical roll was made.

    Returns:
        total (int): the total sum of a given roll and modifiers.
    """
    total = sum(rolls) + modifier
    print(f"Rolled dice: {rolls} + {modifier}")
    if nat_twenty:
        total *= 2
        print("Critical Hit! All damage is doubled")
    print(f"Total Damage: {total}")
    return total


def hazard_damage(num_of_dice, dice_size, modifier, result) -> int:
    damage_dealt = 0
    if result == 0:
        rolled_dice = roll_dice(num_of_dice, dice_size)
        damage_dealt = sum(rolled_dice) + modifier
    elif result == -1:
        rolled_dice = roll_dice(num_of_dice, dice_size)
        damage_dealt = (sum(rolled_dice) + modifier) * 2
    else:
        damage_dealt = 0
    return damage_dealt


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
    # if action is not None:
    #     print(f"The input word corresponds to the action: {action}")
    # else:
    #     print("No matching action found.")

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
#     # inputted = input("Pick your alignment: ")
#     # player_input_action(inputted)
#     print("")

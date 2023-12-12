"""
This is the main program that will run the game.
"""

import mechanics
import character_creator
import keywords
import sys
import os
import a0
import s1
import s2
import s3
import a1
import a2
import a3
import b1
import b2
import c2

screen_width = 200

CHARACTER = character_creator.Character(character_creator.Bard())
CURRENT_ROOM = a0.room
CURRENT_EVENT = a1.event

DIRECTIONS = ["north", "south", "east", "west"]
ROOMS = {"entrance": a0.room,
         "s1": s1.room,
         "s2": s2.room,
         "s3": s3.room,
         "a1": a1.room,
         "a2": a2.room,
         "a3": a3.room,
         "b1": b1.room,
         "b2": b2.room,
         "c2": c2.room,
         }
EVENTS = {"entrance": None,
          "s1": None,
          "s2": s2.event,
          "s3": s3.event,
          "a1": a1.event,
          "a2": a2.event,
          "a3": a3.event,
          "b1": b1.event,
          "b2": b2.event,
          "c2": c2.event,
          }


def option(message="") -> str:
    """
    Have the user type in an input. All messages are lowered and stripped.

    Args:
        message (str): dislayed message or prompt for the user

    Return:
        input (str): the input the user typed in
    """
    return input(f"{message} > ").lower().strip()


def option_title_screen() -> str:
    """
    Have the user type in an input. All messages are lowered and stripped.

    Return:
        input (str): the input the user typed in
    """
    return input(">>> ").lower().strip()


def press_enter_to_continue() -> str:
    """
    A simple function that prompts the user to press Enter.
    Used to simulate a 'next' button.
    """
    input("\033[38;5;241mPress Enter to continue...\033[0m")


def end_demo():
    """
    A text that's displayed when the user reaches the end of the demo.
    Will quit the game after it's done displaying.
    """
    mechanics.print_text("You've reached the end of the demo!\n"
                         "I really hope you've enjoyed the game so far! \n"
                         "Please check out my GitHub for more future updates\n"
                         "https://github.com/oceana1129")
    quit_game()


def game_over_screen():
    """
    Text that is displayed when the player character has died. 
    Quits the game after it's done displaying.
    """
    mechanics.print_text(keywords.text_game_over_death)

    mechanics.print_text("Thanks for playing!")
    exit()  # Quit the game

#### MOVING AROUND ####


def transition_room(current_room: str, next_room: str, navigation_text: str) -> str:
    """
    Will determine which room the player has moved into. Will change the global
    variables for CURRENT_ROOM and CURRENT_EVENT based on the new room inputted.
    If next_room is not applicable, then return current_room

    Args:
        current_room (str): the name of the current room player is in
        next_room (str): the name of the new prompted room
        navigation_text (str): the description for moving into the next room

    Return:
        input (str): the input the user typed in
    """
    global CURRENT_ROOM, CURRENT_EVENT, CHARACTER, ROOMS
    if next_room == "end":
        end_demo()
    if next_room in ROOMS:
        print(f"{navigation_text}... into room {next_room}!\n")
        CURRENT_ROOM = ROOMS[next_room]
        CURRENT_EVENT = EVENTS[next_room]
        CHARACTER.reset_attack_bonus()
        CHARACTER.reset_conditions()

        press_enter_to_continue()
        mechanics.print_text("...", "slow")
        mechanics.print_text(CURRENT_ROOM.get_description())
    else:
        mechanics.style_error("Invalid room name")
        return current_room


def hazard_activated():
    """
    Runs when a hazard is activated. Will read the hazard event description.
    Will have the user make a saving throw, and take damage if they failed.
    Depending on if they survived or failed, it will toggle the room state
    and it will display that current room state.
    """
    if CURRENT_EVENT.read_description() != "":
        print(CURRENT_EVENT.read_description())

    requirements = CURRENT_EVENT.hazard_saving_throw()
    player_mod = CHARACTER.get_ability_mod(requirements)
    damage = CURRENT_EVENT.calculate_damage(player_mod)
    CHARACTER.take_damage(damage)

    if damage == 0:
        CURRENT_ROOM.player_clear_room()
    else:
        CURRENT_ROOM.player_fail_room()
    mechanics.print_text(CURRENT_ROOM.get_description())


def monster_attack():
    """
    Goes through the monsters turn, it will randomly select one of its moves.
    If the monster rolls over the player ac, then they damage them...
    or if the player fails their saving thow, then they damage them.
    If the ability can heal the monster, then it will also heal them.
    """
    global CHARACTER, CURRENT_EVENT
    selected_move = CURRENT_EVENT.select_move()
    selected_move = CURRENT_EVENT.attack_list[selected_move[0]]
    if selected_move.dc > 0:
        saving_throw_mod = CHARACTER.get_ability_mod(selected_move.dc_type)
        roll = mechanics.roll_ability_save(saving_throw_mod)
        mechanics.print_text(f"You must pass \033[1mDC {selected_move.dc}\033[0m\n"
                             f"Crit succeed roll to take 0 damage\n")
        press_enter_to_continue()
        mechanics.print_text(f"\033[1m... You rolled {roll[1]}\033[0m")
        damage = selected_move.saving_throw_damage_roll(CURRENT_EVENT,
                                                        roll[1], roll[2], roll[3])
        CHARACTER.take_damage(damage)
    else:
        mechanics.print_text(
            f"\033[1m{CURRENT_EVENT.name}\033[0m must roll over your\033[1m AC "
            f"{CHARACTER.ac}\033[0m")
        damage = selected_move.standard_damage_roll(
            monster=CURRENT_EVENT, char_ac=CHARACTER.ac)
        CHARACTER.take_damage(damage)
    if selected_move.can_heal():
        selected_move.apply_healing(CURRENT_EVENT)


def player_attack():
    """
    Will prompt the user to select an action from their class list.
    Once an action is picked, they will roll to see if they hit over
    the monsters ac. If they do then they damage the monster. 
    If the action costs mana, then it will reduce their mana.
    If the action has a cooldown, then it will do the cooldown mechanic.
    If the user enters an attack incorrectly, then will prompt the user
    to enter a proper attack.
    """
    while True:

        fighting_actions = CHARACTER.get_fighting_actions()
        mechanics.print_text(
            "\033[1mYou can take these current actions:\033[0m", "normal")
        for action in fighting_actions:
            mechanics.print_text(f"- \033[1m{action}\033[0m")
        print("")
        attack_selected = input("Which action will you take? ")
        if attack_selected == "quit":
            quit_game()
        elif attack_selected == "help":
            help_menu(asked_from_where="room")
        # Check if the attack_selected is a valid action
        if attack_selected in fighting_actions:
            attack = CHARACTER.actions[attack_selected]

            # Check if the attack can be used (considering cooldown, mana, etc.)
            can_use = attack.can_use(CHARACTER)

            if can_use:
                mechanics.print_text(attack.attempt())
                press_enter_to_continue()

                if attack.name == "magic missile":
                    CURRENT_EVENT.take_damage(
                        attack.damage_roll(enemy=CURRENT_EVENT.name))
                    break
                elif attack.heals:
                    attack.apply_healing(CHARACTER)
                    if attack.mana_cost > 0:
                        attack.consume_mana(CHARACTER)
                    break
                else:
                    if attack.mana_cost > 0:
                        attack.consume_mana(CHARACTER)
                    attack_roll = CHARACTER.attack_roll()
                    result = CHARACTER.did_it_hit(
                        attack_roll, CURRENT_EVENT.ac)
                    damage = attack.damage_roll(result, CURRENT_EVENT.name)
                    press_enter_to_continue()
                    CURRENT_EVENT.take_damage(damage)

                    if attack.cooldown_duration > 0:
                        if attack.cooldown_counter == 0:
                            attack.start_cooldown()
                    break
            else:
                mechanics.print_text(
                    f"You can't use the action {attack_selected} right now.")
        else:
            mechanics.style_error("That is not an action you can take.")


def start_combat():
    """
    Function will run when combat has been triggered. As long as the character
    and monster are still alive, then it will play. If either monster or
    character dies, it will bounce back and forth between player_attack() and
    monster_attack(). If the monster dies, then it will display the fail text
    of the monster. Otherwise, it will display the win text of the monster and
    the player will go through a game over screen.
    """
    global CHARACTER, CURRENT_EVENT
    mechanics.print_text(
        f"The {CURRENT_EVENT.name} is prepared to fight.")
    while CHARACTER.current_health > 0 and CURRENT_EVENT.current_hp > 0:
        CHARACTER.start_round_of_combat()
        # PLAYER'S TURN
        mechanics.print_text(".\n.\n.", "slow")
        mechanics.print_text(
            f"{CHARACTER.character_name}, it's your turn to attack", "normal")
        player_attack()

        if CURRENT_EVENT.is_alive():
            mechanics.print_text(
                f"{CURRENT_EVENT.name} is readying to attack", "normal")
            press_enter_to_continue()
        else:
            break  # Exit the loop immediately when the monster dies

        # MONSTER'S TURN
        mechanics.print_text(".\n.\n.", "slow")
        monster_attack()
        press_enter_to_continue()

    if CHARACTER.current_health > 0:
        mechanics.print_text(f"{CHARACTER.character_name} survived!")
        if CURRENT_EVENT.loot:
            CHARACTER.add_loot_to_inventory(CURRENT_EVENT.loot)
            mechanics.print_text(f"You earned loot from this encounter...")
            CHARACTER.view_inventory()
        CURRENT_ROOM.room_failed = True
        mechanics.print_text(CURRENT_ROOM.get_description())
    else:
        mechanics.print_text(CURRENT_EVENT.win_text)
        game_over_screen()


def run_trigger_event():
    """
    Determines if the current room trigger event is a hazard or combat.
    Will run the appropriate hazard_actuivated() or start_combat().
    """
    # event was triggered, make sure it results in either combat or hazard as necessary
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT
    if CURRENT_EVENT.event_type() == "hazard":
        hazard_activated()
    elif CURRENT_EVENT.event_type() == "combat":
        start_combat()
    else:
        mechanics.style_error("An error has occured to trigger event")


def room_is_cleared(command):
    """
    Actions available if the room is currently cleared.

    Args:
        command (str): the command the user had previously entered
    """
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT
    CURRENT_ROOM.get_description()
    # ROOM IS CLEARED
    # VALID ACTION USED FOR EXPLORATION?
    if command in CURRENT_ROOM.action_cleared:
        selected_action = CURRENT_ROOM.action_cleared[command]
        # VALID ACTION WAS USED?
        if not selected_action.used:
            # Read description + apply bonus (if applicable) + mark as used
            mechanics.print_text(selected_action.text)
            CHARACTER.apply_cleared_bonus(selected_action.bonus)

            selected_action.use_action()
        # ACTION ALREADY USED
        else:
            mechanics.print_text(selected_action.was_used())
    # VALID ACTION FOR NAVIGATION?
    elif command in CURRENT_ROOM.actions_cleared_navigation:
        # Navigate to next room
        selected_action = CURRENT_ROOM.actions_cleared_navigation[command]
        transition_room(
            CURRENT_ROOM, selected_action.next_room, selected_action.navigation_text)
    # NOT A VALID ACTION FOR NAVIGATION?
    else:
        print("This action is not available")


def room_not_cleared(command):
    """
    Actions available if the room is currently not cleared.

    Args:
        command (str): the command the user had previously entered
    """
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT

    # ROOM NOT CLEARED ACTIONS
    if command in CURRENT_ROOM.actions_not_cleared:
        selected_action = CURRENT_ROOM.actions_not_cleared[command]

        # VALID ACTION WAS USED?
        if not selected_action.used:
            action_stats = selected_action.get_dc_and_text()
            # No need to roll
            if action_stats[0] == 0:
                # print text + update action + apply room state
                mechanics.print_text(action_stats[1])
                selected_action.use_action()
                CURRENT_ROOM.apply_room_state(
                    selected_action.success_effect, selected_action.fail_effect, 2)
            # need to roll for action
            else:
                # roll for action + print text + update action + apply room state
                mod = CHARACTER.get_ability_mod(
                    selected_action.ability[0])
                result = mechanics.ability_roll_and_text_result(
                    command, mod, action_stats[0], success_text=action_stats[1], fail_text=action_stats[2])

                # resulting actions
                mechanics.print_text(
                    f"You rolled a {result[1]}\n{result[2]}")
                selected_action.use_action()
                CHARACTER.apply_bonus(selected_action.bonus)
                # print(CHARACTER.atk_roll_bonus)
                CURRENT_ROOM.apply_room_state(
                    selected_action.success_effect, selected_action.fail_effect, result[0])

            # after rolling for action, if trigger then run room event
            if CURRENT_ROOM.trigger_event:
                press_enter_to_continue()
                run_trigger_event()
                if CHARACTER.current_health < 0:
                    game_over_screen()

        # ACTION ALREADY USED
        else:
            print(selected_action.was_used())

    # ROOM NOT CLEARED NAVIGATION
    elif command in DIRECTIONS:
        # Navigation command applicable
        if command in CURRENT_ROOM.actions_not_cleared_navigation:
            selected_action = CURRENT_ROOM.actions_not_cleared_navigation[command]
            # some navigation leads to event triggers
            if selected_action.trigger_event == "trigger event":
                run_trigger_event()
            # does not trigger event, move as normal
            else:
                transition_room(
                    CURRENT_ROOM, selected_action.next_room, selected_action.navigation_text)
        # navigation command not applicable
        else:
            mechanics.print_text("You can't move that way")

    # ACTION NOT AVAILABLE AS STANDARD ACTION OR NAVIGATION
    else:
        mechanics.style_error(
            "Invalid action. Please choose a valid action.")


def run_secret_event():
    """
    Runs if the player encounters a secret. Will gain loot from the room.
    """
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT
    if CURRENT_ROOM.loot:
        press_enter_to_continue()
        mechanics.print_text(f"You earned loot from this encounter...")
        mechanics.print_text(f"...", "slow")
        CHARACTER.add_loot_to_inventory(CURRENT_ROOM.loot)
    if CURRENT_ROOM.name == "s3":
        mechanics.print_text("As you put on the amulet granted by the Fey Queen, "
                             "You feel an odd and warming sensation overcome you. You "
                             "feel a surge of invigoration. As every part of you "
                             "feels greatly improved.")
        CHARACTER.ac += 1
        CHARACTER.str += 1
        CHARACTER.dex += 1
        CHARACTER.con += 1
        CHARACTER.wis += 1
        CHARACTER.intell += 1
        CHARACTER.cha += 1
        CHARACTER.perception += 1
        CHARACTER.fortitude += 1
        CHARACTER.reflex += 1
        CHARACTER.will += 1
    CURRENT_ROOM.room_cleared = True
    press_enter_to_continue()
    mechanics.print_text(CURRENT_ROOM.get_description())


def room_is_failed(command):
    """
    Actions available if the room is currently failed.

    Args:
        command (str): the command the user had previously entered
    """
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT

    # player can't explore further since they failed the room
    # ROOM IS FAILED
    # VALID ACTION FOR NAVIGATION?
    if command in CURRENT_ROOM.actions_cleared_navigation:
        # Navigate to next room
        selected_action = CURRENT_ROOM.actions_cleared_navigation[command]
        transition_room(
            CURRENT_ROOM, selected_action.next_room, selected_action.navigation_text)
    # NOT A VALID ACTION FOR NAVIGATION?
    else:
        print("This action is not available")


def navigate_room():
    """
    Will look at the current state of the room. Depending on the current state
    the function will either allow the player to use actions from room_is_cleared(),
    room_not_cleared(), run_secret_event(), or room_is_failed().
    """
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT  # Use the global variables

    # RESET CHARACTER CONDITIONS AND BONUSES
    CHARACTER.reset_attack_bonus()
    CHARACTER.reset_conditions()

    mechanics.print_text(CURRENT_ROOM.get_description())  # ROOM DESCRIPTION

    # ASK PLAYER FOR COMMAND
    while True:
        command = mechanics.player_input(
            option("...\nWhat would you like to do?"), CHARACTER)
        if command == "quit":
            quit_game()
        elif command == "help":
            help_menu(asked_from_where="room")
        # ROOM CLEARED # ROOM CLEARED # ROOM CLEARED # ROOM CLEARED
        # ROOM IS CLEARED --player can pick from cleared actions or navigation
        if CURRENT_ROOM.room_cleared:
            room_is_cleared(command)
        elif CURRENT_ROOM.room_secret:
            run_secret_event()
        # ROOM FAILED # ROOM FAILED # ROOM FAILED # ROOM FAILED
        elif CURRENT_ROOM.room_failed:
            room_is_failed(command)

        # ROOM UNCLEARED # ROOM UNCLEARED # ROOM UNCLEARED # ROOM UNCLEARED
        else:
            room_not_cleared(command)

            if CURRENT_ROOM.room_secret:
                run_secret_event()


def start_game():
    """
    Function that displays when the user confirms to start the game.
    Will bring them to navigate the first playable room.
    """
    mechanics.print_text(
        f"Welcome, {CHARACTER.character_name}\nYou've started the game..")
    mechanics.print_text("Remember to explore and have fun!")
    press_enter_to_continue()
    navigate_room()


def help_menu(asked_from_where):
    """
    Will help the user learn information about various parts of the game.
    When user enters a response from the menu, it will display that information.
    Runs until the user prompts to leave the help menu.
    Will return user to the appropriate spot they left.

    Args:
        asked_from_where (str): where the help menu was asked from
    """
    mechanics.print_text("✦ .          ⁺      . ✦ .     ⁺           . ✦\n"
                         "                   HELP MENU\n"
                         "✦ .          ⁺      . ✦ .     ⁺           . ✦\n")
    mechanics.print_text("\033[38;5;241mNote: You may access this menu at any "
                         "time for help\033[0m")
    while True:
        mechanics.print_text("Read more about:\n"
                             "1. Navigation\n"
                             "2. Exploration\n"
                             "3. Inventory\n"
                             "4. Combat\n"
                             "5. Exit\n")
        user_input = option("Select one of the following options: ")
        if user_input == "1" or user_input == "navigation":
            mechanics.print_text("To navigate use the following commands:\n"
                                 "- north, east, west, south\n"
                                 "- up, down, left, right\n"
                                 "- (front/forward or back/backward)\n")
            press_enter_to_continue()
        elif user_input == "2" or user_input == "exploration":
            mechanics.print_text("To explore, you may use the following commands (and many more):\n"
                                 "- recall knowledge, perception\n"
                                 "- interaction, manipulate\n"
                                 "- animal handling\n"
                                 "- attacking, brute forcing, punch\n"
                                 "- cast spell, detect magic\n"
                                 "- throw, jump\n"
                                 "- disable, stealth\n"
                                 "- diplomacy, intimidate, charm\n"
                                 "- deception, play dead\n"
                                 "- perform\n")
            press_enter_to_continue()
        elif user_input == "3" or user_input == "inventory":
            mechanics.print_text("During exploration, type 'inventory' to access your items.\n"
                                 "If an item is consumable, you will drink it to restore MP/HP.\n"
                                 "Otherwise, it will read the item description.")
            press_enter_to_continue()
        elif user_input == "4" or user_input == "combat":
            mechanics.print_text("If you are a melee class, your strongest actions have cooldowns.\n"
                                 "Cooldowns start when you use that action and go down by 1 each round of combat.\n"
                                 "All cooldowns reset upon entering combat.\n\n"
                                 "If you are a spellcaster class, your strongest actions cost mana.\n"
                                 "Be careful not to expend all of your mana, otherwise, you may only be able to use your basic actions.")
        elif user_input == "5" or user_input == "exit":
            if asked_from_where == "title":
                mechanics.print_text(keywords.text_title_screen)
                title_screen_options()
            if asked_from_where == "room":
                break
        else:
            mechanics.print_text(
                "Invalid choice. Please select a valid option.")


def about_game():
    """
    Will display information about the game, then return the user
    to the title_screen_options()
    """
    mechanics.print_text(keywords.text_about)
    press_enter_to_continue()
    mechanics.print_text(keywords.text_title_screen)
    title_screen_options()


def quit_game():
    """
    Will display the quit game text, and then stop the program.
    """
    mechanics.print_text(keywords.text_quit)
    sys.exit()


def title_screen():
    """
    Display the initial title screen and prompt the user to enter commands
    from title_screen_options().
    """
    os.system("clear")
    mechanics.print_text(keywords.text_title_screen)
    title_screen_options()


def title_screen_options():
    """
    Options available when user first starts the game.
    Depending on the input, it will run the appropriate function.
    Otherwise, it will display an error message.
    """
    while True:
        try:
            command = mechanics.player_input_category(
                option_title_screen(), CHARACTER)
            if command == "play":
                mechanics.print_text("Starting the game...", "normal")
                setup_game()
            elif command == "about":
                about_game()
                mechanics.print_text(keywords.text_title_screen)
            elif command == "help":
                help_menu("title")
            elif command == "quit":
                quit_game()
            else:
                mechanics.style_error(keywords.text_error)
        except ValueError:
            mechanics.style_error(keywords.text_error)


def setup_game():
    """
    Function to help set up the game. Will determine the name for the 
    player character, and the class/job the character will have.
    Will assign the appropriate class and name to the player CHARACTER.
    """
    global CHARACTER
    mechanics.print_text(keywords.text_ask_name)
    name = option()
    print("")

    while True:
        print(keywords.text_select_class)
        current_class_list = ["fighter", "wizard", "bard", "rogue"]

        job = option()
        if job in current_class_list:
            break
        else:
            print(keywords.text_class_error)

    while True:
        mechanics.print_text(
            f"\nDo you confirm the following?\nName: {name}\nClass: {job}")
        choice = option()
        if choice == "yes":
            mechanics.print_text("Let's start the game...", "normal")
            if job == "fighter":
                chosen_class = character_creator.Fighter()
            elif job == "wizard":
                chosen_class = character_creator.Wizard()
            elif job == "bard":
                chosen_class = character_creator.Bard()
            elif job == "rogue":
                chosen_class = character_creator.Rogue()

            CHARACTER = character_creator.Character(chosen_class)
            CHARACTER.character_name = name

            start_game()
            break
        elif choice == "no":
            setup_game()
            break
        else:
            mechanics.print_text("Invalid choice. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    title_screen()

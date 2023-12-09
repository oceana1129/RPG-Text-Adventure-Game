"""
This is the main program that will run the game.
Loading Screen
"""

import mechanics
import character_creator
import keywords
import game_state
import compendium_hazards
import compendium_monster
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

CHARACTER = character_creator.Character(character_creator.Rogue())
CURRENT_ROOM = a0.room
CURRENT_EVENT = b2.event

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
          }

#### OPTIONS ####


def option(message=""):
    return input(f"{message} > ").lower().strip()


def option_title_screen():
    return input(">>> ").lower().strip()


def press_enter_to_continue():
    input("\033[38;5;241mPress Enter to continue...\033[0m")


def game_over_screen():
    mechanics.print_text(keywords.text_game_over_death)

    while True:
        choice = input("Do you want to play again? (yes/no): ")

        if choice == "yes":
            mechanics.print_text("Restarting the game...", "slow")
            break
        elif choice == "no":
            mechanics.print_text("Thanks for playing!")
            exit()  # Quit the game
        else:
            mechanics.style_error(
                "Please enter 'yes' or 'no'.")

#### MOVING AROUND ####


def transition_room(current_room: str, next_room: str, navigation_text: str):
    # Have this call from the global CURRENT_ROOM variable
    # Go from current_room to next_room if next_room is a room that
    # you can transition to from current_room
    global CURRENT_ROOM, CURRENT_EVENT, CHARACTER, ROOMS

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
    if CURRENT_EVENT.read_description() != "":
        print(CURRENT_EVENT.read_description())

    requirements = CURRENT_EVENT.hazard_saving_throw()
    player_mod = CHARACTER.get_ability_mod(requirements)
    damage = CURRENT_EVENT.calculate_damage(player_mod)
    CHARACTER.take_damage(damage)

    if damage == 0:
        return CURRENT_ROOM.player_clear_room()
    else:
        return CURRENT_ROOM.player_fail_room()


def monster_attack():
    """
    Goes through the monsters turn, different things occur depending on it's attack
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
    while True:

        fighting_actions = CHARACTER.get_fighting_actions()
        mechanics.print_text(
            "\033[1mYou can take these current actions:\033[0m", "normal")
        for action in fighting_actions:
            mechanics.print_text(f"- \033[1m{action}\033[0m")
        print("")
        attack_selected = input("Which action will you take? ")

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
    global CHARACTER, CURRENT_EVENT
    mechanics.print_text(
        f"The {CURRENT_EVENT.name} is prepared to fight.")
    while CHARACTER.is_alive() and CURRENT_EVENT.current_hp > 0:
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
    else:
        mechanics.print_text(CURRENT_EVENT.win_text)
        game_over_screen()


# start_combat()


def run_trigger_event():
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
                CURRENT_ROOM.apply_room_state(
                    selected_action.success_effect, selected_action.fail_effect, result[0])
                CURRENT_ROOM.get_room_state()

            # after rolling for action, if trigger then run room event
            if CURRENT_ROOM.trigger_event:
                press_enter_to_continue()
                print("trigger 2")
                run_trigger_event()

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
                print("trigger 3")
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
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT
    if CURRENT_ROOM.loot:
        press_enter_to_continue()
        mechanics.print_text(f"You earned loot from this encounter...")
        mechanics.print_text(f"...", "slow")
        CHARACTER.add_loot_to_inventory(CURRENT_ROOM.loot)
    if CURRENT_ROOM.name == "s3":
        mechanics.print_text("As you put on the amulet granted by the Fey Queen, "
                             "You feel an odd and warming sensation overcome you. Every part "
                             "of your body feels a surge of invigoration. Every part of you, "
                             "shockingly, feels greatly improved.")
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


def room_is_failed(command):
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
    global CURRENT_ROOM, CHARACTER, CURRENT_EVENT  # Use the global variables

    # RESET CHARACTER CONDITIONS AND BONUSES
    CHARACTER.reset_attack_bonus()
    CHARACTER.reset_conditions()

    mechanics.print_text(CURRENT_ROOM.get_description())  # ROOM DESCRIPTION

    # ASK PLAYER FOR COMMAND
    while True:
        command = mechanics.player_input(
            option("...\nWhat would you like to do?"))
        if command == "quit":
            quit_game()
        elif command == "restart":
            restart_game()
        elif command == "help":
            help()
        # ROOM CLEARED # ROOM CLEARED # ROOM CLEARED # ROOM CLEARED
        # ROOM CLEARED # ROOM CLEARED # ROOM CLEARED # ROOM CLEARED
        # ROOM IS CLEARED --player can pick from cleared actions or navigation
        if CURRENT_ROOM.room_cleared:
            room_is_cleared(command)
        elif CURRENT_ROOM.room_secret:
            run_secret_event()
        # ROOM FAILED # ROOM FAILED # ROOM FAILED # ROOM FAILED
        # ROOM FAILED # ROOM FAILED # ROOM FAILED # ROOM FAILED
        elif CURRENT_ROOM.room_failed:
            room_is_failed(command)

        # ROOM UNCLEARED # ROOM UNCLEARED # ROOM UNCLEARED # ROOM UNCLEARED
        # ROOM UNCLEARED # ROOM UNCLEARED # ROOM UNCLEARED # ROOM UNCLEARED
        else:
            room_not_cleared(command)
            if CURRENT_ROOM.trigger_event:
                # if CURRENT_ROOM.event == "combat":
                print("trigger 4")
                run_trigger_event()

            elif CURRENT_ROOM.room_secret:
                run_secret_event()


def start_game():
    mechanics.print_text(
        f"Welcome, {CHARACTER.character_name}\nYou've started the game..")
    mechanics.print_text("Remember to explore and have fun!")
    press_enter_to_continue()
    navigate_room()


def restart_game():
    game_state.reset_game_state()
    title_screen()


def help_menu():
    mechanics.print_text(keywords.text_help_base)
    title_screen_options()


def about_game():
    mechanics.print_text(keywords.text_about)
    title_screen_options()


def quit_game():
    mechanics.print_text(keywords.text_quit)
    sys.exit()


def title_screen():
    os.system("clear")
    mechanics.print_text(keywords.text_title_screen)
    title_screen_options()


def title_screen_options():
    while True:
        try:
            command = mechanics.player_input_category(option_title_screen())
            if command == "play":
                mechanics.print_text("Starting the game...", "normal")
                setup_game()
            elif command == "about":
                about_game()
            elif command == "help":
                help_menu()
            elif command == "quit":
                quit_game()
            else:
                mechanics.style_error(keywords.text_error)
        except ValueError:
            mechanics.style_error(keywords.text_error)


def setup_game():
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

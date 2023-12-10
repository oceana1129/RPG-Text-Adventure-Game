import mechanics


class Room:
    def __init__(self, name, event, description, room_cleared, room_failed, room_secret, trigger_event,
                 trigger_name, description_cleared, description_failed, loot, action_cleared,
                 actions_cleared_navigation, actions_not_cleared, actions_not_cleared_navigation):
        self.name = name
        self.event = event
        self.description = description
        self.room_cleared = room_cleared
        self.room_failed = room_failed
        self.room_secret = room_secret
        self.trigger_event = trigger_event
        self.trigger_name = trigger_name
        self.description_cleared = description_cleared
        self.description_failed = description_failed
        self.loot = loot

        ### ACTIONS SPECIFIC TO THE ROOM ###
        self.action_cleared = action_cleared
        self.actions_cleared_navigation = actions_cleared_navigation
        self.actions_not_cleared = actions_not_cleared
        self.actions_not_cleared_navigation = actions_not_cleared_navigation

    def player_clear_room(self):
        self.room_cleared = True

    def player_fail_room(self):
        self.room_failed = True

    def player_find_secret(self):
        self.room_secret = True

    def player_trigger_event(self):
        self.trigger_event = True

    def apply_room_state(self, success_effect, fail_effect, result):
        if result >= 1:
            if success_effect == "room cleared":
                self.player_clear_room()
                mechanics.print_text(self.get_description())
            elif success_effect == "room secret":
                self.player_find_secret()
            elif success_effect == "trigger event":
                self.player_trigger_event()
        else:
            if fail_effect == "trigger event":
                self.player_trigger_event()
            elif fail_effect == "room failed":
                self.player_fail_room()
                mechanics.print_text(self.get_description())

    def get_room_state(self):
        print("Room Cleared:", self.room_cleared)
        print("Room Failed: ", self.room_failed)
        print("Room Secret: ", self.room_secret)
        print("Triggered Event: ", self.trigger_event)

    def get_available_actions(self):
        actions = {}
        if self.room_cleared:
            actions.update(self.actions_cleared_navigation)
        else:
            actions.update(self.actions_not_cleared_navigation)
        print(actions)

    def get_description(self):
        if self.room_cleared == False and self.room_failed == False:
            return self.description
        elif self.room_cleared:
            return self.description_cleared
        else:
            return self.description_failed

    def get_current_room_directions(self):
        # loop through the current rooms you can travel to
        current_directions = []
        if self.room_cleared:
            for action in self.actions_cleared_navigation:
                current_directions.append(action)
        else:
            for action in self.actions_not_cleared_navigation:
                current_directions.append(action)
        return current_directions

    def get_loot(self):
        return self.loot

    def get_trigger_name(self):
        return self.trigger_name


class Action_Cleared(Room):
    def __init__(self, used, bonus, text):
        self.used = used
        self.bonus = bonus
        self.text = text

    def use_action(self):
        """
        If player has selected for this action, we modify the action to say that it has been used.
        """
        self.used = True

    def was_used(self) -> str:
        """
        If the user has already selected this action, ask player to do a new action.
        """
        if self.used:
            return ("You've already used this action, try a new one or continue navigating.")
        else:
            pass

    def get_bonus(self) -> str:
        """
        Get the name of the bonus the action would provide
        """
        return self.bonus

    def get_success_text(self) -> str:
        """
        Get the text this action should display
        """
        return self.text


class Action_Not_Cleared(Room):
    def __init__(self, used, DC, ability, bonus, success_effect, success_bonus, fail_effect, success_text,
                 fail_text):
        self.used = used
        self.DC = DC
        self.ability = ability,
        self.bonus = bonus
        self.success_effect = success_effect
        self.success_bonus = success_bonus
        self.fail_effect = fail_effect
        self.success_text = success_text
        self.fail_text = fail_text

    def use_action(self):
        """
        If player has selected for this action, we modify the action to say that it has been used.
        """
        self.used = True

    def get_success_text(self) -> str:
        """
        Will return success text for the specified action type.
        """
        return self.success_text

    def get_fail_text(self) -> str:
        """
        Will return fail text for the specified action type.
        """
        return self.fail_text

    def was_used(self) -> str:
        """
        If the user has already selected this action, ask player to do a new action.
        """
        if self.used:
            return ("You've already used this action, try a new one or continue navigating.")
        else:
            pass

    def get_bonus(self) -> str:
        """
        Get the name of the bonus the action would provide
        """
        return self.bonus

    def get_dc_and_text(self):
        return (self.DC, self.success_text, self.fail_text)


class Action_Cleared_Navigation(Room):
    def __init__(self, navigation_text, next_room):
        self.navigation_text = navigation_text
        self.next_room = next_room

    def get_next_room(self) -> str:
        """
        Get the name of the next room player is navigating to
        """
        return self.next_room

    def get_navigation_text(self) -> str:
        """
        Get the navigational text for moving in a certain direction
        """
        return self.navigation_text


class Action_Not_Cleared_Navigation(Room):
    def __init__(self, navigation_text, next_room, trigger_event):
        self.navigation_text = navigation_text
        self.next_room = next_room
        self.trigger_event = trigger_event

    def get_next_room(self) -> str:
        """
        Get the name of the triggered effect moving will cause
        """
        return self.trigger_event

    def get_navigation_text(self) -> str:
        """
        Get the navigational text for moving in a certain direction
        """
        return self.navigation_text


test_room_1 = Room(
    name="Test Room",
    event="Exploration",
    description="This is the basic description of the room",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name=False,
    description_cleared="You cleared the room",
    description_failed="You failed the room",
    loot={},
    action_cleared={
        "diplomacy": Action_Cleared(
            used=False,
            bonus="",
            text=""
        )
    },
    actions_cleared_navigation={
        "north": Action_Cleared_Navigation(
            navigation_text="move north.",
            next_room="test_room_2"
        ),
        "south": Action_Cleared_Navigation(
            navigation_text="move south.",
            next_room="test_room_3"
        ),
    },
    actions_not_cleared={
        "perception": Action_Not_Cleared(
            used=False,
            DC=30,
            ability="int",
            bonus="",
            success_effect=False,
            success_bonus=0,
            fail_effect=False,
            success_text="You notice some strange markings on the wall...",
            fail_text="You see nothing out of the ordinary...",
        ),
        "intimidation": Action_Not_Cleared(
            used=False,
            DC=30,
            ability="int",
            bonus="",
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="grr on the wall...",
            fail_text="grr nothing out of the ordinary...",
        )
    },
    actions_not_cleared_navigation={
        "north": Action_Not_Cleared_Navigation(
            navigation_text="You can't move that way",
            next_room="",
            trigger_event=""
        )
    }
)


# print(test_room_1.actions_not_cleared["perception"].get_success_text())
# test_room_1.actions_not_cleared["perception"].use_action()
# print(test_room_1.actions_not_cleared["perception"].used)  # should print true
# test_room_1.player_clear_room()
# test_room_1.get_loot()
# print(test_room_1.get_room_state())

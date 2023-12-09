class Room:
    def __init__(self, name, event, description, room_cleared, room_failed, room_secret, trigger_effect,
                 trigger_name, description_cleared, description_failed, loot, action_cleared,
                 actions_cleared_navigation, actions_not_cleared, actions_not_cleared_navigation):
        self.name = name
        self.event = event
        self.description = description
        self.room_cleared = room_cleared
        self.room_failed = room_failed
        self.room_secret = room_secret
        self.trigger_effect = trigger_effect
        self.trigger_name = trigger_name
        self.description_cleared = description_cleared
        self.description_failed = description_failed
        self.loot = loot
        self.action_cleared = action_cleared
        self.actions_cleared_navigation = actions_cleared_navigation
        self.actions_not_cleared = actions_not_cleared
        self.actions_not_cleared_navigation = actions_not_cleared_navigation


class Action_Cleared(Room):
    def __init__(self, used, bonus, text):
        self.used = used
        self.bonus = bonus
        self.text = text


class Action_Not_Cleared(Room):
    def __init__(self, used, DC, player_result, bonus, success_effect, success_effect_2, fail_effect, success_text,
                 fail_text):
        self.used = used
        self.DC = DC
        self.player_result = player_result
        self.bonus = bonus
        self.success_effect = success_effect
        self.success_effect_2 = success_effect_2
        self.fail_effect = fail_effect
        self.success_text = success_text
        self.fail_text = fail_text


class Action_Cleared_Navigation(Room):
    def __init__(self, navigation_text, next_room):
        self.navigation_text = navigation_text
        self.next_room = next_room


class Action_Not_Cleared_Navigation(Room):
    def __init__(self, navigation_text, trigger_effect):
        self.navigation_text = navigation_text
        self.trigger_effect = trigger_effect


test_room_1 = Room(
    name="Test Room",
    event="Exploration",
    description="This is the basic description of the room",  # standard description
    ###
    room_cleared=False,  # if player cleared the room
    room_failed=False,  # if player failed the room
    room_secret=False,  # if player found the room secret
    trigger_effect=False,  # did player trigger either combat or hazard
    trigger_name=False,  # name of combat or hazard
    description_cleared="You cleared the room",  # if player cleared description
    description_failed="You failed the room",  # if player failed description
    loot={},  # included from monster or room secret
    ###
    action_cleared={
        "diplomacy": {
            "used": False,
            "bonus": "",
            "text": ""
        }
    },  # actions you can take once room is cleared
    actions_cleared_navigation={
        "north": ["move north.", "test_room_2"],
        "south": ["move south.", "test_room_3"],
    },  # navigation you can take once room is cleared
    ###
    actions_not_cleared={
        "perception": {  # name of action
            "used": False,  # did player use this
            "DC": 30,  # difficulty check
            # the player result [-1 through 2 degree of success]
            "player result": None,
            "bonus": "",  # any bonuses a success grants
            "success effect": False,  # what does a success do?
            "success effect 2": False,  # if success also triggers combat
            "fail effect": False,
            "success text":
                "You notice some strange markings on the wall to the east. Their glow "
                "is faint and bright. You swear these markings weren't there previously.",
            "fail text":
                "You see nothing out of the ordinary. Steel your wits; it’s time to go in!",
        },
        "boop": {  # name of action
            "used": False,  # did player use this
            "DC": 30,  # difficulty check
            # the player result [-1 through 2 degree of success]
            "player result": None,
            "bonus": "",  # any bonuses a success grants
            "success effect": False,  # what does a success do?
            "success effect 2": False,  # if success also triggers combat
            "fail effect": False,
            "success text":
                "You notice some strange markings on the wall to the east. Their glow "
                "is faint and bright. You swear these markings weren't there previously.",
            "fail text":
                "You see nothing out of the ordinary. Steel your wits; it’s time to go in!",
        },
        "beep": {  # name of action
            "used": False,  # did player use this
            "DC": 30,  # difficulty check
            # the player result [-1 through 2 degree of success]
            "player result": None,
            "bonus": "",  # any bonuses a success grants
            "success effect": False,  # what does a success do?
            "success effect 2": False,  # if success also triggers combat
            "fail effect": False,
            "success text":
                "You notice some strange markings on the wall to the east. Their glow "
                "is faint and bright. You swear these markings weren't there previously.",
            "fail text":
                "You see nothing out of the ordinary. Steel your wits; it’s time to go in!",
        }
    },
    actions_not_cleared_navigation={
        "north": ["You can't move that way", "trigger effect"]

    }
)


class Room:
    pass


class Action_Cleared(Room):
    pass


class Action_Not_Cleared(Room):
    pass


class Action_Cleared_Navigation(Room):
    pass


class Action_Not_Cleared_Navigation(Room):
    pass

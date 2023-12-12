"""
Entrance room of the game.
"""

import create_room

room = create_room.Room(
    name="entrance",
    event="exploration",
    description="You stand at the entrance of a dark cave.\n\nThe air is "
                "thick with an uneasy stillness. "
                "The faint rustling of the ground beneath your feet echoes in "
                "the cavernous darkness. This may be your very "
                "last breath of fresh air for all you know. You grip your weapon and "
                "prepare for your journey ahead.",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name=False,
    description_cleared="Continue north to the main entrance or examine the wall "
    "further east?",
    description_failed="No time to dwaddle, the only way forward is up ahead.",
    loot={},
    action_cleared={
        "": create_room.Action_Cleared(
            used=False,
            bonus="",
            text=""
        )
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the entrance and move north.",
            next_room="a1"
        ),
        "east": create_room.Action_Cleared_Navigation(
            navigation_text="Walk over and investigate the east wall.",
            next_room="s1"
        ),
    },
    actions_not_cleared={
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=32,
            ability="perception",
            bonus=0,
            success_effect="room cleared",
            success_bonus=0,
            fail_effect="room failed",
            success_text="You notice some strange markings on the wall to the east. Their glow "
            "is faint and bright. You swear these markings weren't there previously.",
            fail_text="You see nothing out of the ordinary. Steel your wits; it’s time to go in!",
        )
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="Continue and move north.",
            next_room="a1",
            trigger_event=""
        )
    }
)

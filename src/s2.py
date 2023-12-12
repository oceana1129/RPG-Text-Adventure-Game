"""
Room that leads to beauty of a god hazard. Can lead to main secret room.
"""

import create_room
import compendium_hazards

room = create_room.Room(
    name="s2",
    event="hazard",
    description="You step into the concealed room, and an enchanting radiance surrounds you. "
    "The air hums with a mysterious magic, as your heart tenses with "
    "anticipation at whatever lies ahead.\n"
    "However, seconds turn to minutes as minutes turn to hours. You feel like you've begun "
    "to lose all track of time. The warm light burning your eyes as the corridor seems to "
    "stretch for an infinite amount of time.\n\n\n"
    "Finally, after what feels like an eternity, you are greeted with breathless feeling.\n"
    "At the end of the tunnel, you see a bright, almost blinding illuminating light. It bathes "
    "you with a sense of otherwordly brilliance.\nAnd as you move closer to the light, "
    "you sense an absolutely overwhelming and foreboding presence. An aura of dominance and beauty.\n"
    "Before you can move another inch, you feel an overwhelming urge to flee wash over you.\n\n"
    "Will you try to keep moving forward?",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="hazard_beauty_of_a_god",
    description_cleared="...",
    description_failed="You must turn back.",
    loot={},
    action_cleared={
        "detect magic": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="You can tell that whatever up ahead is exuding powerful magical energy. "
            "You may have just faced a minor challenge made by them."
        ),
        "perception": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="It's hard to see much of anything over this bright light. You can't tell "
            "from who or where the sensation to run was cast from."
        ),
        "perform": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="You play a soft tune that slowly eases your worries."
        ),
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="You continue to follow the light up ahead.",
            next_room="s3"
        ),
        "south": create_room.Action_Cleared_Navigation(
            navigation_text="You run all the way back to the entrance.\nWhatever is ahead, you don't want "
            "to face it.",
            next_room="a1"
        ),
        "west": create_room.Action_Cleared_Navigation(
            navigation_text="You run all the way back to the entrance.\nWhatever is ahead, you don't want "
            "to face it.",
            next_room="a1"
        ),
    },
    actions_not_cleared={
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="perception",
            bonus="",
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="Your senses become blinded as the need to run overwhelms you.",
            fail_text="",
        )
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You try to move forward, but your feet won't let you move ahead.",
            next_room="",
            trigger_event="trigger event"
        ),
        "south": create_room.Action_Not_Cleared_Navigation(
            navigation_text="This is far too much for you to handle.\n"
            "You find yourself back at the entrance, out of breath and feeling more tired than "
            "before. You take a moment and rest before you walk into the main entrance.",
            next_room="a1",
            trigger_event=""
        ),
        "west": create_room.Action_Not_Cleared_Navigation(
            navigation_text="This is far too much for you to handle.\n"
            "You find yourself back at the entrance, out of breath and feeling more tired than "
            "before. You take a moment and rest before you walk into the main entrance.",
            next_room="a1",
            trigger_event=""
        ),
        "yes": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You try to move forward, but your feet won't let you move ahead.",
            next_room="",
            trigger_event="trigger event"
        ),
    }
)

event = compendium_hazards.Hazard(
    name="Beauty of a God",
    dc=32,
    saving_throw="will",
    description="",
    skill_crit_success="",
    skill_success="You keep your resolve as you muster the courage to keep moving forward. "
    "You get the feeling that you should act carefully from here on out. You’ve come "
    "this far.\n\nShould you keep moving forward or head back?",
    skill_fail="It feels like whatever uneasiness you had before is even ten thousand "
    "times more unnerving. You can't force yourself to keep moving forward. Whatever "
    "is up ahead can easily put a stop to your adventure. \n\n"
    "You can't stop the urge to turn tail and run away.",
    skill_crit_fail="",
    damage_dice=0,
    damage_size=0,
    modifier=15
)

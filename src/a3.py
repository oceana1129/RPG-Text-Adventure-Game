"""
Room that contains a miasma hazard.
"""

import create_room
import compendium_hazards

room = create_room.Room(
    name="a3",
    event="hazard",
    description="You walk down the dimly lit tunnel as the darkness grows deeper. "
    "The silence envelops you. The walls, damp and uneven, seem to close in around "
    "you with every step. Strange, otherworldly markings and symbols are etched "
    "into the stone, their meaning lost to time. The air is heavy with an earthy scent, "
    "and the distant echoes of water dripping create an eerie backdrop.\n"
    "As you continue, a thick fog begins seeps through the air. It swirls through the "
    "tunnel as your breathing becomes labored. The dim light from your torch dances "
    "through the mist. As you move through, it doesn't seem to get any thinner, and "
    "is in fact becoming dangerously thick. You can see a passageway up ahead towards "
    "the north.",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="hazard_miasma",
    description_cleared="You can see up ahead that there is a corridor that leads either "
    "north or west.",
    description_failed="The miasma in the room makes you naseous, but at least it's cleared "
    "up significantly more. You can see a corridor that leads either north or west.",
    loot={},
    action_cleared={
        "perception": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="There is nothing of note to see."
        ),
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move north.",
            next_room="b2"
        ),
        "west": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move west.",
            next_room="a2"
        ),
    },
    actions_not_cleared={
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=24,
            ability="int",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You think back to previous adventures and books you've read. The "
            "thickening air and sickly hue... This is a miasma. If you don't "
            "protect yourself properly, then inhaling too much of this fog will "
            "cause lethal damage. You recognize that if you cover up your mouth "
            "in some way or create a clean pocket of air, then you'll likely "
            "make it through just fine.",
            fail_text="You can't really think of anything that explains the fog in the air.",
        ),
        "mask": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="wis",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect=False,
            success_text="You think fast and create a makeshift mask out of some cloth. "
            "You're able to walk through the fog with little to no problem.",
            fail_text="",
        ),
        "attacking": create_room.Action_Not_Cleared(
            used=False,
            DC=30,
            ability="str",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="A strange idea pops in your head. You take out your weapon and "
                        "begin to spin it in the air rapidly. By spinning it around at "
                        "such a fast speed, you are able to make a pocket of air around "
                        "you. You are able to pass through the fog with little trouble.\n"
                        "You see a passage up north.",
            fail_text="You have your weapon out, but there is nothing really to attack.",
        ),
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=27,
            ability="perception",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You search your way through the fog and end up finding areas in "
            "the tunnel with a thin amount of fog. You are able to walk through "
            "the fog safely by utilizing this weakness.",
            fail_text="You peer through the fog but you can't find anything that will help you.",
        ),
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=24,
            ability="wis",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You look around you and begin to chant a spell to yourself. Gesturing "
            "your arms you create a makeshift bubble around you. You are able to "
            "purify the air around you as you walk through the tunnel.",
            fail_text="You think of various different spells in your arsenal. You think of any "
            "that could help in this situation.",
        ),
        "jump": create_room.Action_Not_Cleared(
            used=False,
            DC=28,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="With a running start, you aim towards the end of the corridor with a "
                        "glorious vault. Tumbling through air, you land on your feet gracefully "
                        "at the other end of the tunnel. You can now continue to move north.",
            fail_text="With a running start, you vault through the corridor; trying to make it "
            "through the end. However, your jump ends short and you're still in the "
            "thick of the fog.",
        ),
        "disable": create_room.Action_Not_Cleared(
            used=False,
            DC=29,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You peer all over the room, shining your light on the walls. You "
            "miraculously find a portion of the wall with some vents in it. You take "
            "out some items from your belt as you finagle with the vents. With a "
            "click, the vents stop pushing out air. The fog begins to thin and you "
            "can now make it through the other side at the north wall.",
            fail_text="You peer all over the room, looking for a way to reduce the fog. You "
            "can't find anthing of note.",
        ),
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk through the room.",
            next_room="",
            trigger_event="trigger event"
        ),
        "west": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk through the room.",
            next_room="",
            trigger_event=""
        ),
    }
)

event = compendium_hazards.Hazard(
    name="Miasma Trap",
    dc=23,
    saving_throw="fortitude",
    description="The fog continues to grow becoming thick and dangerous. A thick and deadly miasma begins to seep through the air.",
    skill_crit_success="",
    skill_success="With a massive inhale of clean air, you hold your breath as you sprint "
    "across the room. The miasma barely effects you as you effortlessly walk through.",
    skill_fail="With a massive inhale, you steal yourself and walk across the room. Your "
    "lungs give out and you make your last stretch with some miasma filling them.",
    skill_crit_fail="You can’t properly prepare yourself as miasma completely fills "
    "up your lungs. Your find yourself coughing all the way through the corridor.",
    damage_dice=1,
    damage_size=6,
    modifier=5
)

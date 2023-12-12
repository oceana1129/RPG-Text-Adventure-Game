"""
Room that is just exploration. Can unlock a hidden secret room.
"""
import create_room

room = create_room.Room(
    name="s1",
    event="Exploration",
    description="Your curiosity gets the better of you. As you walk your way over to the "
                "east wall, a sense of wonder and anticipation fills your heart. The runes "
                "etched on the wall emit a warm, enchanting radiance, reminiscent of a vibrant sunset.\n"
                "Gazing at the runes, you find them incomprehensible. More reminiscent of an ancient tongue. "
                "Upon further inspection, you note that the wall underneath the carvings "
                "looks... off. As if concealing a hidden truth.\n\nDo you wish to investigate "
                "further or walk back west to the main entrance?",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name=False,
    description_cleared="You've uncovered the illusion behind the runes as a new entrance opens.\n\n"
                "Do you dare explore further north, or head back west to the main entrance?",
    description_failed="The strange runes baffle you. You really out to start your adventure "
    "and head back west.",
    loot={},
    action_cleared={
        "perception": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="The wall is completely gone, you can't find any traces of it left behind."
        )
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="You decide to move through the once hidden wall",
            next_room="s2"
        ),
        "south": create_room.Action_Cleared_Navigation(
            navigation_text="Ignore the markings and move back to the main entrance.",
            next_room="a0"
        ),
        "west": create_room.Action_Cleared_Navigation(
            navigation_text="Ignore the markings and move back to the main entrance.",
            next_room="a0"
        )
    },
    actions_not_cleared={
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="perception",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You've already investigated the markings...\nTry something else instead.",
            fail_text="",
        ),
        "detect magic": create_room.Action_Not_Cleared(
            used=False,
            DC=25,
            ability="int",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect=False,
            success_text="You identify the carvings as a seal for some kind of illusion spell. "
            "You trace over the carvings and undo the magical seal. You can now proceed east.",
            fail_text="The carvings are magical, but you aren't sure from which magic school "
            "they're from. Best to tread carefully.",
        ),
        "throw": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="dex",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You grab a rock and throw it at the wall. Congrats, you just threw a "
            "rock at a wall.",
            fail_text="",
        ),
        "attacking": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You hit the wall, as your weapon phases through it. You try to walk "
            "forward but bounce off the wall. You wonder if there's another angle you can "
            "take or if you're just wasting your time.",
            fail_text="",
        ),
        "punch": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You hit the wall, as your fist phases through it. You try to walk "
            "forward but bounce off the wall. You wonder if there's another angle you can "
            "take or if you're just wasting your time.",
            fail_text="",
        ),
        "cast spell": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You cast a spell at the wall. The carvings glow as they absorb "
            "your magic harmlessly. You wonder if there's another approach you can take "
            "or if you should even bother.",
            fail_text="",
        ),
        "manipulate": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect=False,
            success_text="You touch the carvings and find your finger tracing along "
            "the symbols. They grow bright and dissipate. Soon the illusion of a wall "
            "begins to disappear. Now you can traverse into this unconventional opening.",
            fail_text="",
        ),
        "interaction": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect=False,
            success_text="You touch the carvings and find your finger tracing along "
            "the symbols. They grow bright and dissipate. Soon the illusion of a wall "
            "begins to disappear. Now you can traverse into this unconventional opening.",
            fail_text="",
        ),
    },
    actions_not_cleared_navigation={
        "south": create_room.Action_Not_Cleared_Navigation(
            navigation_text="Ignore the markings and move back to the main entrance.",
            next_room="a1",
            trigger_event=""
        ),
        "west": create_room.Action_Not_Cleared_Navigation(
            navigation_text="Ignore the markings and move back to the main entrance.",
            next_room="a1",
            trigger_event=""
        )
    }
)

"""
Room that contains a tile room trap hazard.
"""
import create_room
import compendium_hazards

room = create_room.Room(
    name="a1",
    event="hazard",
    description="As you cautiously step into the cave's entrance, an otherworldly "
    "stillness envelopes you. A hushed silence fills the air. The dim light filtering "
    "in from the outside barely penetrates the cavern's depths. What little light "
    "there is casts eeries shadows that dance along the rocky walls.\n"
    "Beneath your feet, you discover a tangled mosaic of peculiar tiles, each carved "
    "with intricate patterns emenating with energy. The air carries a faint hymm, "
    "daring you to venture further. Each step uncovering more about the secrets "
    "of this dungeon.\nAs you move deeper along the corridor, your torchlight reveals "
    "the walls and floor adorned with these mysterious designs. The patterns intertwine "
    "and shift, as you're still unsure of their origin. Call it your sense of "
    "experience, paranoia begins to gnaw at you as you feel every step further may "
    "lead you to peril. There's something odd about these tiles.",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="hazard_tiles",
    description_cleared="You can see up ahead that there is a corridor that leads either "
    "north or east. \nWhich direction would you like to take?",
    description_failed="The arrows scattered on the floor remind you that you at least "
    "made it out of the room alive. You can see up ahead that there is a corridor that "
    "leads either north or east. \nWhich direction would you like to take?",
    loot={},
    action_cleared={
        "perception": create_room.Action_Cleared(
            used=False,
            bonus=0,
            text="The room has already been cleared, there's nothing left for you to explore."
        )
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move north.",
            next_room="b1"
        ),
        "east": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move east.",
            next_room="a2"
        )
    },
    actions_not_cleared={
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=22,
            ability="perception",
            bonus=0,
            success_effect=False,
            success_bonus=0,
            fail_effect="trigger event",
            success_text="You've seen something like this before. You think this room may "
            "be some kind of trigger trap. You best be careful not to trigger it.",
            fail_text="You don't seem to notice anything odd. But while investigating, you "
            "accidentally trigger one of the pressure plates.\nBrace yourself!"
        ),
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=22,
            ability="int",
            bonus=0,
            success_effect=False,
            success_bonus=0,
            fail_effect="trigger event",
            success_text="Noting the markings on the floor, and the strange material they are "
            "made of, you note that this is a trigger trap. You might be able to disable it, jump over it,"
            "or activate it safely using other means.",
            fail_text="You don't seem to notice anything odd. But while investigating, you "
            "accidentally trigger one of the pressure plates.\nBrace yourself!"
        ),
        "disable": create_room.Action_Not_Cleared(
            used=False,
            DC=24,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=0,
            fail_effect="trigger event",
            success_text="You safely disarm the trap with your Lockpick. Good thing you've "
            "been practicing. The tiles shift down harmlessly.",
            fail_text="You trigger the trap, as arrows shoot across the room.\nBrace yourself!",
        ),
        "jump": create_room.Action_Not_Cleared(
            used=False,
            DC=23,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=0,
            fail_effect="trigger event",
            success_text="With a running start, you leap over the tiles without triggering it.",
            fail_text="You misjudge your jump, triggering the trap as arrows shoot across the "
            "room.\nBrace yourself!",
        ),
        "throw": create_room.Action_Not_Cleared(
            used=False,
            DC=40,  # fix to 26
            ability="str",
            bonus=0,
            success_effect="room cleared",
            success_bonus=0,
            fail_effect="trigger event",
            success_text="You pick up a loose stone and toss it onto the tiles. You safely "
            "trigger the trap as arrows shoot across the room.",
            fail_text="You throw an item onto the pressure plate, but it isn't heavy enough "
            "to activate it. You confidently walk over it and trigger the trap, "
            "as arrows shoot across the room.\nBrace yourself!",
        ),
        "attack": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=0,
            fail_effect="trigger event",
            success_text="With precision, you strike the pressure plate with your weapon, "
            "triggering the trap from a safe distance. Arrows fly across the room as "
            "you narrowly dodge them.",
            fail_text="You attempt to hit the pressure plate from a safe distance. However, "
            "when you hit the plate, you were too close. You get caught in a flurry "
            "of arrows across the room.\nBrace yourself!",
        ),
        "brute forcing": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="str",
            bonus=0,
            success_effect="room cleared",
            success_bonus=0,
            fail_effect="trigger event",
            success_text="With precision, you strike the pressure plate with your weapon, "
            "triggering the trap from a safe distance. Arrows fly across the room as "
            "you narrowly dodge them.",
            fail_text="You attempt to hit the pressure plate from a safe distance. However, "
            "when you hit the plate, you were too close. You get caught in a flurry "
            "of arrows across the room.\nBrace yourself!",
        ),
        "cast spell": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="int",
            bonus=0,
            success_effect="room cleared",
            success_bonus=0,
            fail_effect="trigger event",
            success_text="Using your wits, you cast a spell from a safe distance. You "
            "trigger the trap as arrows fly across the room.",
            fail_text="Thinking you're clever, you cast a spell from a safe distance "
            "at the tiles. You didn't realize how weak your spell was as "
            "you walked across the tiles that triggered a flurry of arrows."
            "\nBrace yourself!",
        ),
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You go to move ahead, but end up triggering a trap.",
            next_room="",
            trigger_event="trigger event"
        ),
        "east": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You go to move ahead, but end up triggering a trap.",
            next_room="",
            trigger_event="trigger event"
        )
    }
)

event = compendium_hazards.Hazard(
    name="Tile Arrow Trap",
    dc=26,
    saving_throw="reflex",
    description="The tiles shift down as a mechanism is triggered. The walls surrounding "
    "you suddenly come to life, shifting and opening with a sinister creak. "
    "In an instant, a relentless flurry of arrows is unleashed, filling the "
    "narrow corridor with deadly projectiles",
    skill_crit_success="",
    skill_success="With remarkable agility, you gracefully evade the oncoming barrage "
    "of arrows. Your movements are like a carefully choreographed dance, and you "
    "emerge from the hail of projectiles completely unscathed, your heart pounding"
    " with adrenaline.",
    skill_fail="You valiantly attempt to dodge the relentless assault of arrows, "
    "but despite your efforts, some of the projectiles find their mark. The impact "
    "is painful, and you bear the brunt of the attack as you stagger through the "
    "other side, wounded but determined.",
    skill_crit_fail="In your desperate bid to avoid the arrows, you stumble and "
    "falter. The arrows seem to find you with uncanny accuracy, striking "
    "you with piercing force. \nYou endure the pain, as you finally make it through the storm.",
    damage_dice=2,
    damage_size=4,
    modifier=2
)

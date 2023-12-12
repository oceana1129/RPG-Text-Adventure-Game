"""
Room that contains a Giant Rat for combat. Also contains a secret.
"""
import create_room
import compendium_monster


room = create_room.Room(
    name="a2",
    event="combat",
    description="You walk down the tunnel as the darkness grows deeper. The narrow "
    "passage is damp, and the air feels heavy with moisture. The faint echoes of your "
    "footsteps bounce off the cold, stone walls. As you continue, you hear a "
    "scampering on the floor, followed by sharp screeches. After being through many "
    "dark caves before, you instantly recognize the sounds. It's a Giant Rat."
    "\nYou take a moment to assess the situation. The tunnel extends ahead, and you "
    "can't see the end of it. The rat could be coming from anywhere within the "
    "darkness. It steps sound even closer as you wait, till it nears closer in "
    "sight.\nThink quickly; your next steps could be crucial.",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="trigger event",
    description_cleared="The rat scampers around happy to see you again. When you get"
    "close to it, it runs away.\nYou can move either west or east.",
    description_failed="You can move either east or west.",
    loot={"healing potion lesser": 1, "gold": 50, "rope": 1, "letter": 1},
    action_cleared={
        "animal handling": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="You pet the Giant Rat. He squeaks with pure joy."
        ),
        "throw": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="You throw a pebble across the room. The Giant Rat runs with glee as he"
            "catches the pebble in middair, bringing it back to you."
        )
    },
    actions_cleared_navigation={
        "west": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move west.",
            next_room="a1"
        ),
        "east": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move west.",
            next_room="a3"
        ),
    },
    actions_not_cleared={
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="perception",
            bonus=2,
            success_effect=False,
            success_bonus=0,
            fail_effect=False,
            success_text="You notice the Giant Rat has a limp on its back left paw, you can "
            "use this to your advantage in combat.",
            fail_text="You don't notice anything peculiar about this rat, other than him "
            "being a giant rat.",
        ),
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=21,
            ability="wis",
            bonus=2,
            success_effect=False,
            success_bonus=0,
            fail_effect=False,
            success_text="Giant rats are enormous versions of the common vermin. They mostly "
            "live in sewers or damp places where they can scavenge. Though their bite is not "
            "lethal, you'd do your best not to get bit by once, since they typically carry diseases.",
            fail_text="This is a Giant Rat and that's there is to it.",
        ),
        "stealth": create_room.Action_Not_Cleared(
            used=False,
            DC=24,
            ability="dex",
            bonus=2,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="Like a shadow, you slink into the darkest crevices in the cavern. "
            "Slowing your breath and obscuring your presence. When the rat "
            "comes near, you will be ready to attack with utmost precision",
            fail_text="You attempt to hide and loudly kick a loose rock. Its movement "
            "ricochets in the tunnel as the rat turns to face you, ready for combat.",
        ),
        "diplomacy": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="cha",
            bonus=0,
            success_effect="room secret",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="With a kind hand and gentle voice, you manage to soothe the rats anxious heart. "
            "Perhaps its old days of being a smaller rat resurface in its mind. It now acts "
            "very friendly and docile with you, deciding to befriend you. To show its "
            "gratitude, it uncovers a hidden treasure buried in the ground.",
            fail_text="Your attempts to communicate or pet the rat fall flat, aggravating it "
            "further. The Giant Rat grows even more hostile. It bares its teeth "
            "and is ready for combat.",
        ),
        "animal handling": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="wis",
            bonus=0,
            success_effect="room secret",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="With a kind hand and gentle voice, you manage to soothe the rats anxious heart. "
            "Perhaps its old days of being a smaller rat resurface in its mind. It now acts "
            "very friendly and docile with you, deciding to befriend you. To show its "
            "gratitude, it uncovers a hidden treasure buried in the ground.",
            fail_text="Your attempts to communicate or pet the rat fall flat, aggravating it "
            "further. The Giant Rat grows even more hostile. It bares its teeth "
            "and is ready for combat.",
        ),
        "throw": create_room.Action_Not_Cleared(
            used=False,
            DC=25,
            ability="dex",
            bonus=2,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You hurl a loose pebble, distracting the Giant Rat momentarily and giving "
            "you an advantage in combat.",
            fail_text="You throw a loose pebble attempting to distract the rat, instead you only "
            "draw attention to yourself. The rat turns towards you and bares its teeth "
            "ready for combat.",
        ),
        "intimidate": create_room.Action_Not_Cleared(
            used=False,
            DC=27,
            ability="cha",
            bonus=4,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="With an intimidating glare, you strike fear into the Giant Rat. In cowers "
            "in fear, unable to move.",
            fail_text="The rat can't even tell you were trying to intimidate it. It lowers "
            "its stance, ready to attack.",
        ),
        "play dead": create_room.Action_Not_Cleared(
            used=False,
            DC=27,
            ability="cha",
            bonus=4,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You collapse to the ground, feigning death. The rat comes over to sniff "
            "you, and once it assumes you're dead it turns to leave. You have the "
            "opportunity to strike while its guard is down.",
            fail_text="You try to play dead, but it's not very convincing. The Giant Rat still "
            "thinks you're a threat and is ready to attack.",
        ),
        "perform": create_room.Action_Not_Cleared(
            used=False,
            DC=24,
            ability="cha",
            bonus=0,
            success_effect="room secret",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="Your melody fills the cavern. The Giant Rat lowers its guard, completely "
            "enamored with your song. It seems friendly and no longer interested in "
            "attacking you. To show its gratitude, it uncovers a hidden treasure "
            "buried in the ground.",
            fail_text="Your melody falls flat and the Giant Rat, in its irritation, bares its "
            "teeth ready to fight you.",
        ),
        "attacking": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="Without hesitation, you draw your weapon and prepare to strike.\n"
            "Adrenaline courses through your veins as you prepare for the upcoming battle.",
            fail_text="",
        ),
        "cast spell": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You focus your energy, drawing upon your magical powers. With a series of "
            "gestures the air around you crackles.\nYou prepare to cast a spell for the "
            "upcoming battle.",
            fail_text="",
        )

    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You try to move ahead but are caught by the Giant Rat.",
            next_room="",
            trigger_event="trigger event"
        )
    }
)


event = compendium_monster.Monster(
    name="Giant Rat",
    ac=16,
    max_hp=16,
    current_hp=16,
    level=1,
    lore_dc=11,
    lore_mod="wis",
    loot={"rope": 1, "gold": 5},
    defeat_text="The rat slumps over in defeat.",
    win_text="Completely shocked at it's victory, it simply scuries away in victory.",
    attack_list={
        "jaws": compendium_monster.Attacks(
            name="jaws",
            frequency=[0, 1],
            atk_roll=6,
            dc=0,
            dc_type=None,
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=1,
            dice_size=6,
            add_dmg=0,
            success_text="The Giant Rat lunges out at you with a vicious bite, sinking "
            "its teeth into you.",
            fail_text="The Giant Rat lunges out at you, missing. As it ferociously snaps "
            "at the air.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        )
    }
)

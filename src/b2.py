"""
Room that contains a Shadow for combat.
"""

import create_room
import compendium_monster

room = create_room.Room(
    name="b2",
    event="combat",
    description="You find yourself walking further, and as you walk, the walls "
    "begin to narrow into a claustrophobic corridor. Dimly lit by the flickering "
    "light of your torch. You can see strange encryptions on the walls as you "
    "continue to walk. Each step brings you into an ever encroaching darkness.\n"
    "You cautiously proceed as you feel the hair on your body begin to prickle. "
    "You exhale as your breath turns into frosty plumes. You begin to shiver as "
    "you begin to feel an unsettling presence looming. You turn with your torch "
    "in hand as the shadows around you begin to twist and distort. And from "
    "above you, the shadows begin to form dripping onto the cavern floor. A "
    "shapeless malevolent entity emerges from the tendrils of darkness on the floor. "
    "Made of pure darkness, its very presence seems to drain warmth and light from "
    "the surrounded. A cold shroud intensifies as the creature draws nearer."
    "\n\nThink fast!",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="shadow",
    description_cleared="The room is now empty, you may go either north or south.",
    description_failed="The room is now empty, you may go either north or south.",
    loot={},
    action_cleared={
        "perception": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="There is an unsettling black ooze left on the floor. A remnant of "
            "the shadow that was once here."
        )
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move north.",
            next_room="c2"
        ),
        "south": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move south.",
            next_room="a3"
        ),
    },
    actions_not_cleared={
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=27,
            ability="int",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You wrack you brain and recall the type of creature this is. "
            "It’s a Shadow, an undead creature made of darkness. They lurk in dark "
            "places and attack those who stray from the light. If you parlay with a "
            "shadow, you remember that you can keep them at bay with a strong light...",
            fail_text="You can’t seem to recall what kind of creature this is other than "
            "some kind of shadow.",
        ),
        "attacking": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="You grip your weapon, prepared to strike the shadowed fiend.",
            fail_text="",
        ),
        "cast spell": create_room.Action_Not_Cleared(
            used=False,
            DC=24,
            ability="int",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger combat",
            success_text="You think quickly on your feet. Thinking of the current spells "
            "in your arsenal, you are reminded of one of the most common "
            "cantrip spells… ‘Light’. You cast it as radiant light blooms "
            "in the narrow corridor. The creature of darkness recoils in "
            "the bright light. The shadows around you seem to scurry into "
            "the depths of the cave. The flash-bomb you’ve magically created "
            "seems to have deterred the shadow from making an enemy of you. "
            "You may continue moving north.",
            fail_text="You conjure magical energy around you, prepared to blast the "
            "shadowed fiend.",
        ),
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=24,
            ability="perception",
            bonus=2,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You notice that the shadow is sulking in the darkest parts of "
                        "the room. As long as you fight him in the lightest parts, it "
                        "will at least give you a small advantage in combat.",
            fail_text="The shadow is large and imposing, sending shivers coursing through "
            "your body. You can’t tell anything peculiar about it that will "
            "help you in combat.",
        ),
        "punch": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="You throw a big punch at the fiend, but it seems to phase "
            "right through it. The shadowy creature arches its back and "
            "howls, sending shivers coursing through your body.",
            fail_text="",
        ),
        "throw": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="You take a lose rock from the floor and toss it at the shadow. "
            "It simply phases right through it. The shadowy creature lets "
            "out a hiss resembling a laugh. It lurches forward at you with "
            "its claws.",
            fail_text="",
        ),
        "detect magic": create_room.Action_Not_Cleared(
            used=False,
            DC=25,
            ability="int",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You quickly decipher through your mind, studying the magic in "
            "the room. You detect some sort of illusion spell throughout "
            "the small corridor. Without moments hesitation, you counteract "
            "the illusion. The darkness begins to dissipate around you as "
            "the torches you’d become accustomed to seeing throughout this "
            "dungeon relight. The bright light pours through the corridor as "
            "the shadow reals in discomfort. It holds its claws to its eyes "
            "disoriented by the change of scenery. It begins to dissipate "
            "as the light tears through its body.",
            fail_text="You try to detect if there’s any magic in the room. You get the "
            "sense that some powerful magic is at work in the room. But you "
            "can’t distinguish if it’s from the shadow itself or the corridor. "
            "In your confusion, the shadow takes the opportunity to strike.",
        ),
        "stealth": create_room.Action_Not_Cleared(
            used=False,
            DC=32,
            ability="dex",
            bonus=4,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You grab your torch and put it up to its face, it recoils as "
            "you use the instance to slip into a small crevice. The shadow "
            "shakes its head in disbelief, losing sight of you. Now you "
            "have the perfect opportunity to strike back at it with great force.",
            fail_text="It shocking that you even thought you could slip away from an "
            "actual shadow seeing as you were standing right in front of it. "
            "It sees through your ruse quite clearly and readies its claws.",
        ),
        "intimidate": create_room.Action_Not_Cleared(
            used=False,
            DC=28,
            ability="cha",
            bonus=2,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="The shadows begins to lurch out at you as you grab onto your "
            "blade and unleash the deadliest insult to its face. It recoils "
            "at your ferocity and shudders. Your display has granted you "
            "the upper hand.",
            fail_text="You muster up a pathetic roar at the shadow. It is unimpressed "
            "as it lets out a hiss like laughter. Reading its claws, it "
            "prepares for combat.",
        ),
        "play dead": create_room.Action_Not_Cleared(
            used=False,
            DC=31,
            ability="cha",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="With the most impressive acting of your life, you clench your "
            "chest and hold your breath. Feigning death as if you were "
            "struck by the fear of fear itself. The shadow creeps over "
            "your body confused at first. But then becomes most pleased "
            "with itself, letting out a hiss resembling laughter. It "
            "coaches back into the shadows and slips away.",
            fail_text="You grab your chest and lean backwards. You let out a pathetic "
            "groan as if you were keeling over. However, the shadow is not "
            "very impressed with your lackluster performance. It lets out a "
            "roar as it readies its claws.",
        ),
        "perform": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="cha",
            bonus=4,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="You perform a small song in the thick of the moment. The "
            "shadow recoils with anger as the melody trickles within the "
            "small corridor. It flails its claws over its face as if "
            "shielding itself from the harmony of your tune.",
            fail_text="",
        ),
        "light": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect=False,
            success_text="An idea comes into your head. If this creature is made of "
            "darkness, then the best way to counteract it is to use light. "
            "You quickly take some cloth from inside your bag and light it "
            "on fire with your torch. The flames grow readily as you toss "
            "it on the floor. The light causes the corridor to feel "
            "completely alight. The shadow recoils in agony, screeching "
            "as it flails on the floor. As the light grows, the shadow seems "
            "to dissipate and disappear.",
            fail_text="",
        ),
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You try to walk ahead with the shadow looming over you. \n\n"
            "He won't let you escape.",
            next_room="",
            trigger_event="trigger event"
        ),
        "south": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You try to walk ahead with the shadow looming over you. \n\n"
            "He won't let you escape.",
            next_room="",
            trigger_event="trigger event"
        ),
    }
)


event = compendium_monster.Monster(
    name="Shadow",
    ac=25,
    max_hp=75,
    current_hp=75,
    level=6,
    lore_dc=17,
    lore_mod="wis",
    loot={},
    defeat_text="The shadow convulses, falling to the floor and leaving behind a black ooze.",
    win_text="The Shadow shakes with glee as a shrill laughter escapes from it.",
    attack_list={
        "shadow claws": compendium_monster.Attacks(
            name="Shadow Claws",
            frequency=[0, 0.2],
            atk_roll=16,
            dc=0,
            dc_type=None,
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=2,
            dice_size=6,
            add_dmg=4,
            success_text="The Shadow swipes at you with its Shadow Claws. "
            "Tendrils phase through your skin as you take damage.",
            fail_text="You shudder as the Shadow reaches out for you with its Shadow Claws. "
            "It overestimates and misses.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        ),
        "steal shadow": compendium_monster.Attacks(
            name="Steal Shadow",
            frequency=[0.21, 1],
            atk_roll=0,
            dc=24,
            dc_type="reflex",
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=3,
            dice_size=4,
            add_dmg=4,
            success_text="The Shadow grasps a sliver of your shadow and steals it.",
            fail_text="You shudder as the Shadow reaches out for your shadow as you "
            "adeptly dodge it.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        )
    }
)

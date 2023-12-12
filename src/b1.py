"""
Room that contains a Kobold for combat.
"""

import create_room
import compendium_monster

room = create_room.Room(
    name="b1",
    event="combat",
    description="You cautiously walk through the corridor, dimly lit and long. The "
    "silence is disrupted by faint sounds of scuttling feet and muted chattering. "
    "You swivel your head around. Paranoia gnaws at your senses.\nYou strain your "
    "ears and listen more closely, trying to discern the noises. You get the feeling "
    "that you are not alone in this tunnel. You swear you could hear a faint "
    "chuckling from behind the walls.\nA sense of danger pricks your skin. From "
    "the corner of your eye, you catch a fleeting moment of a dim light, darting "
    "along the tunnel walls. Something is following you, stalking you through the "
    "darkness.\n\nThink fast.",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="trigger event",
    description_cleared="The room is now empty, you may go either north or south.",
    description_failed="The room is now empty, you may go either north or south.",
    loot={"playing cards": 1, "gold": 20},
    action_cleared={
        "perception": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="You can go over and inspect the Kobold was investigating. It looks "
            "like some plain rocks and nothing of interest."
        )
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move north.",
            next_room="c2"
        ),
        "south": create_room.Action_Cleared_Navigation(
            navigation_text="Continue through the tunnel and move south.",
            next_room="a1"
        ),
    },
    actions_not_cleared={
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=20,
            ability="int",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="Piecing together the clues, you can guess that the creature "
            "stalking you is a Kobold, a cunning and opportunistic creature. The "
            "like to burrow in tunnels and are generally peaceful as long as you "
            "don't trespass in their territory. You know that as long as you can "
            "avoid it or convince it to go away, it will probably just ignore you.",
            fail_text="There aren't enough clues for you to piece together what kind "
            "of creature is stalking you.",
        ),
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="perception",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You lay low and wait for a bit. You hone in on your senses and "
            "adjust to the darkness. The faint lights you saw flicker and form into the "
            "shadow of the creature. It appears to be a Kobold, minding its own business "
            "and looking for crevices to squeeze into.",
            fail_text="You don't seem to notice anything other than the Kobold inspecting "
            "a wall. You start getting anxious. You rush out and begin combat.",
        ),
        "attacking": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="Without hesitation, you draw your blade and prepare to strike "
            "whatever it is that’s following you. With bated breath, "
            "adrenaline courses through your veins as you wait.",
            fail_text="",
        ),
        "cast spell": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="You channel your magical energies, preparing to unleash a "
            "spell at your shadowed stalker.",
            fail_text="",
        ),
        "throw": create_room.Action_Not_Cleared(
            used=False,
            DC=27,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="In a moment of quick thinking, you grab a trusted loose pebble "
            "on the floor. You wait with bated breath as you wait for your "
            "shadowed follower. A kobold steps out of the shadows, inspecting "
            "the tunnel walls and unassuming. You hurl the loose rock and nail "
            "it right at the kobold’s head. It’s a direct hit, knocking him at "
            "the temple. With a teeter, the kobold rocks as it falls onto the "
            "floor, completely incapacitated.",
            fail_text="You grab a loose pebble from the floor. And wait with bated breath "
            "as you wait for your shadowed follower. A kobold steps out of the "
            "shadows, inspecting the tunnel walls and unassuming. You hurl the "
            "pebble and it hits its mark. However, the force of impact was so "
            "minimal that it simply directs the kobold to your location.",
        ),
        "stealth": create_room.Action_Not_Cleared(
            used=False,
            DC=26,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You move quickly and blend into the shadows. Hugging the tunnel "
                        "walls in the crevice of darkness. You hold your breath as you "
                        "watch the shadow of a kobold creep into sight. It appears to be "
                        "inspecting one of the tunnel walls. It grabs something from the "
                        "wall and then creeps back into the shadows, scurrying into a "
                        "tunnel in the floor. You let go of the wall. It doesn’t look "
                        "like it’s coming back. You see a tunnel up ahead to the north.",
            fail_text="You move quickly and walk into the shadows. You hug the tunnel "
            "walls as a kobold appears to creep into sight. You can’t get a "
            "good look at it and what it’s doing. So you move closer into sight. "
            "However, you snag a loose pebble under your foot as it bounces "
            "clumsily and loudly towards the kobold. Alerted, it turns around "
            "and looks straight at you.",
        ),
        "intimidate": create_room.Action_Not_Cleared(
            used=False,
            DC=27,
            ability="cha",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You wait for whatever it is following you through the tunnel. "
            "You hold onto your weapon with great resolve and puff your "
            "chest. From the shadows, you see a creature come out of the "
            "shadows, a small kobold. You charge towards it with your weapon "
            "in hand, letting out a most ferocious roar. The kobolds eyes "
            "grow large as its heart leaps out. It falls to the floor and "
            "then quickly gets back up to run away. As you partly chase it, "
            "it scampers and squeezes into a hidden tunnel in the floor; one "
            "that is far too small for you to get into. It likely won’t be "
            "coming back out any time soon. You see up ahead a northern tunnel.",
            fail_text="You wait for the creature to come out of the shadows, ready to "
            "scare it away with your might. A small kobold appears from the "
            "light, carrying a small weapon and some tools. You move towards "
            "it and yell at him. Confused, it looks at you with an angry look "
            "on its face. It sees your signs of aggression and is ready for combat.",
        ),
        "diplomacy": create_room.Action_Not_Cleared(
            used=False,
            DC=20,
            ability="cha",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You think the best way to get out of this is to reason your "
                        "way out of it. You gently call out at the shadow scampered "
                        "along the tunnel walls. You reason that you’re here peacefully "
                        "and simply wish to move through. The kobold scurries out of "
                        "the shadows, fearful at first, but quickly relieved. It looks "
                        "at you and tells you how it’s just here to check one of the walls "
                        "for the lady of the caves. Before you could ask anything else, "
                        "it does exactly as it says. Checking the wall and then "
                        "scampering away into a tunnel in the floor. It doesn’t look "
                        "like it’s coming back. You see a tunnel ahead that leads north.",
            fail_text="You call out to the shadows, thinking reasoning may be better than "
            "just fighting. You say that you do not wish to harm whatever he "
            "is.\nA kobold scurries out of the shadows, but it looks at you "
            "with fear. It looks at your gear and doesn’t seem to trust you "
            "despite your words.",
        ),
        "perform": create_room.Action_Not_Cleared(
            used=False,
            DC=22,
            ability="cha",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger combat",
            success_text="You begin to play a tune, playing a beautiful progression of "
                        "cords. The sound is reminiscent of a warm winter day, filling "
                        "the tunnel with a harmonious tune. From the shadows appears a "
                        "kobold. It seems completely mesmerized and curious by what "
                        "you’re doing. You pay no mind to it as it begins to sway with "
                        "the tempo. It hums to itself as it walks over to the tunnel "
                        "wall it was intending to work on. It taps the tunnel wall with "
                        "inspiration carrying its steps. It turns around and waves at you "
                        "goodbye as it disappears in a kobold sized tunnel in the floor. "
                        "You don’t think it’ll be coming back any time soon. You see the "
                        "northern tunnel up ahead.",
            fail_text="You begin to play a tune, but it is completely discordant and out "
            "of tune. A kobold runs out of the shadows mad and upset. It seems "
            "to be completely irritated with your disharmonious tune ready to "
            "stop the source.",
        ),
        "play dead": create_room.Action_Not_Cleared(
            used=False,
            DC=30,
            ability="cha",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You press yourself up against the tunnel wall, feigning death; "
                        "losing weight from your limbs and going limp. You don’t even "
                        "stir as you hear small scuffling from a creature in the distance. "
                        "You don’t know if has noticed you or not but seems to not care "
                        "or notice your presence. It seems to walk towards a tunnel wall "
                        "as it disappears into the ground. You wait a few minutes, until "
                        "you’re sure it won’t come back again. You get up and brush "
                        "yourself off. You see a northern tunnel up ahead.",
            fail_text="You fall limply to the floor but fail to conceal yourself in a "
            "convincing manner. You wait with your heart beating through your "
            "chest as you hear faint footsteps in the distance. But then, the "
            "footsteps grow even louder as it begins to approach closer. You "
            "try not to move as you feel something small walk right next to you. "
            "You can feel moist breath as it sniffs your ‘corpse’. It screeches "
            "and you stir to life startled. Your cover is blown, and it has its "
            "weapon at the ready.",
        ),
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk through the room and move up ahead.",
            next_room="",
            trigger_event="trigger event"
        )
    }
)

event = compendium_monster.Monster(
    name="Kobold",
    ac=18,
    max_hp=20,
    current_hp=20,
    level=1,
    lore_dc=13,
    lore_mod="int",
    loot={"playing cards": 1, "gold": 25, "lockpick": 1, "torch": 1},
    defeat_text="The Kobold slumps to the floor in defeat",
    win_text="Completely shocked at it's victory, it simply runs away in confusion.",
    attack_list={
        "shortsword": compendium_monster.Attacks(
            name="Shortsword",
            frequency=[0, 1],
            atk_roll=12,
            dc=0,
            dc_type=None,
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=1,
            dice_size=8,
            add_dmg=2,
            success_text="The Kobold swings its shortsword with precision, "
            "landing a solid blow.",
            fail_text="The Kobold's attack misses as it barely grazes your body.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        )
    }
)

"""
Room that holds major secret event. If player fails, then they trigger instant death.
"""

import create_room
import compendium_hazards

room = create_room.Room(
    name="s3",
    event="hazard",
    description="You muster the courage to continue onward, fighting the relentless urge to flee. "
    "Each step you take brings you closer to the radiant light at the end of the tunnel.\n\n"
    "Emerging from the incandescent brilliance, you behold a beautiful and breathtaking sight. A "
    "magnificent Fey, regally seated upon an adorned throne. Ethereal light dances around her, "
    "as small pixies, with luminscent wings shimmering like firefies, dance around her. Her presence "
    "is chiseled with wisom and power shining with luminescence.\n\n"
    "Her eyes betray either amusement or curiosity, with their gaze fixed upon you. An aura of enchantment "
    "envelopes the throne room, drawing you in deeper.\n\n"
    "In her presence, what do you do?",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="hazard_instant_death",
    description_cleared="The Fey Queen looks pleased, she'll help you move forward if you'd like.",
    description_failed="You find yourself in a bright void that stretches on endlessly.",
    loot={"healing potion greater": 1, "amulet": 1},
    action_cleared={
        "diplomacy": create_room.Action_Cleared(
            used=False,
            bonus="1 intell",
            text="You continue to talk with her and she bestows a little bit more knowledge to you."
        ),
        "perform": create_room.Action_Cleared(
            used=False,
            bonus="1 cha",
            text="You continue to entertain and she bestows a little bit more warmth to you."
        ),
        "charm": create_room.Action_Cleared(
            used=False,
            bonus="1 str",
            text="You give her some compliments and she is pleased. You feel like you've become"
            " a little stronger."
        ),
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="Bathed in a bright light, she summons you away.\nYou find yourself back"
            " at the entrance of the cave. The eastern wall you came through "
            "appears to be missing. You walk through the entrance, beginng your quest.",
            next_room="a1"
        ),
        "south": create_room.Action_Cleared_Navigation(
            navigation_text="Bathed in a bright light, she summons you away.\nYou find yourself back"
            " at the entrance of the cave. The eastern wall you came through "
            "appears to be missing. You walk through the entrance, beginng your quest.",
            next_room="a1"
        ),
        "west": create_room.Action_Cleared_Navigation(
            navigation_text="Bathed in a bright light, she summons you away.\nYou find yourself back"
            " at the entrance of the cave. The eastern wall you came through "
            "appears to be missing. You walk through the entrance, beginng your quest.",
            next_room="a1"
        ),
    },
    actions_not_cleared={
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=25,
            ability="perception",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="She seems to be rather intrigued by your presence. She doesn't appear to want "
            "to hurt you in any way. However, you still sense an unnerving amount of power "
            "emanating from her. It'd be best to stay on her good side.",
            fail_text="The bright light is too bright for your eyes. It's hard to discern anything peculiar about her.",
        ),
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=32,
            ability="int",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You recall how Fey came from the Feywilds. They are synonymous with the supernatural. "
            "They are often found near specific natural locations imbued with magic. Their nature "
            "can vary from playful and mischievous to outright selfish.\n"
            "This particular Fey is a Lampesperid Queen which rules over isolated regions soaked "
            "in light. They guard countless treasures and secrets, though, for those who approach "
            "them with respect, they're willing to part with knowledge or items.",
            fail_text="You can't recognize what kind of creature she is other than some kind of Fey.",
        ),
        "diplomacy": create_room.Action_Not_Cleared(
            used=False,
            DC=28,
            ability="cha",
            bonus=0,
            success_effect="room secret",
            success_bonus="5 damage",
            fail_effect="room failed",
            success_text="She is pleased and has a conversation with you. You share stories of your "
                        "previous adventures and secrets you've uncovered before. In return, she warns "
                        "you about the cave ahead filled with traps and monsters. She also gives you an "
                        "amulet that will boost your stats. As well as a Greater Potion of Healing.",
            fail_text="Although the Queen is normally one for good company, she finds your presence rather "
            "annoying. While you are mid-sentence, she waves her hand at you as you feel bathed "
            "in a bright light.",
        ),
        "intimidate": create_room.Action_Not_Cleared(
            used=False,
            DC=35,
            ability="cha",
            bonus=0,
            success_effect="room failed",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You somehow manage to intimidate the Fey Queen. She shivers in repulsion as she "
            "hastily waves at you to go away.",
            fail_text="You let out a pathetic roar or mumble under your breath. It's evident you "
            "were trying to intimidate the Fey Queen. No matter, she laughs in your face.\n"
            "And then a cheeky look creeps upon her face. She begins to move her hands around "
            "and whispers something in Fey's tongue. A warm light begins to envelop you as "
            "you feel your very being begin to burn. Everything around you seems to grow "
            "bigger as you shrink into the floor.\nBefore you come to, you find yourself the "
            "size of a sprite with wings upon your back. And you feel an overwhelming urge "
            "to fly towards the queen and worship her for the rest of your life. \n\n"
            "Hope you like a life of eternal servitude!",
        ),
        "perform": create_room.Action_Not_Cleared(
            used=False,
            DC=30,
            ability="cha",
            bonus=0,
            success_effect="room secret",
            success_bonus=False,
            fail_effect="room failed",
            success_text="You reach for your instrument and begin to play a soothing melody.\n"
            "The ethereal music fills the air, and the Fey Queen's eyes sparkle "
            "with delight. She leans in closer, entranced by your performance and "
            "humming to the tune. In appreciation for your beautiful serenade, she "
            "bestows upon you an amulet and Greater Healing Potion.",
            fail_text="Your music falls flat, and the notes seem discordant in this "
            "otherworldly realm. The Fey Queen winces at the cacophony and abruptly "
            "waves her hand. You are submerged in a bright light.",
        ),
        "charm": create_room.Action_Not_Cleared(
            used=False,
            DC=31,
            ability="cha",
            bonus=0,
            success_effect="room secret",
            success_bonus=False,
            fail_effect="room failed",
            success_text="Your charm and wit catch the Fey Queen off guard. She bursts into laughter, "
            "thoroughly entertained by your advances. In appreciation, she bestows upon "
            "you an amulet that enhances your prowess and a Potion of Greater Healing.",
            fail_text="Instead of being flattered, she becomes annoyed. Annoyance replaces "
            "her mirth as she promptly ushers you away. She waves her hand as you are "
            "bathed in a bright light.",
        ),
        "attacking": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus="",
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You ready an attack, immediately wary of her presence. The Fey Queen "
                        "frowns and looks at you with disappointment. Before you can so much as think, "
                        "she lifts her finger as you are enveloped in a white light. You feel your body "
                        "begin to burn as each molecule of your being begins to erupt.",
            fail_text="",
        ),
        "cast spell": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus="",
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You ready an attack, immediately wary of her presence. The Fey Queen "
            "frowns and looks at you with disappointment. Before you can so much as think, "
            "she lifts her finger as you are enveloped in a white light. You feel your body "
            "begin to burn as each molecule of your being begins to erupt.",
            fail_text="",
        ),
        "manipulate": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="dex",
            bonus="",
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You seem drawn to her... like a moth to a flame. And as you reach out your "
            "hand to touch the Fey Queen. \nShe begins to move her hands around and "
            "whispers something in Fey's tongue. A warm light begins to envelop you "
            "as you feel your very being begin to burn. Everything around you seems to "
            "grow bigger as you shrink into the floor. \nBefore you come to, you find "
            "yourself the size of a sprite with wings upon your back. And you feel an "
            "overwhelming urge to fly towards the queen and worship her for the "
            "rest of your life. \n\nHope you like a life of eternal servitude!",
            fail_text="",
        ),
        "throw": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="dex",
            bonus="",
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="In a panic, you grab a rock on the floor and chuck it at the Fey Queen. "
            "She frowns in annoyance. One of the pixies catches the pebble in midair.\n"
            "With a flick of the wrist, the Fey Queen ushers you away as you are submerged "
            "in a glowing light.\n\nWhy did you think that was a good idea?",
            fail_text="",
        ),

    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk a single step. The bright light around you flashes. "
            "You blink and find yourself back at the cave entrance. That could've gone"
            "much worse...",
            next_room="a1",
            trigger_event=""
        ),
        "south": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk a single step. The bright light around you flashes. "
            "You blink and find yourself back at the cave entrance. That could've gone"
            "much worse...",
            next_room="a1",
            trigger_event=""
        ),
        "east": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk a single step. The bright light around you flashes. "
            "You blink and find yourself back at the cave entrance. That could've gone"
            "much worse...",
            next_room="a1",
            trigger_event=""
        ),
        "west": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk a single step. The bright light around you flashes. "
            "You blink and find yourself back at the cave entrance. That could've gone"
            "much worse...",
            next_room="a1",
            trigger_event=""
        ),
    }
)

event = compendium_hazards.Hazard(
    name="Instant Death",
    dc=100,
    saving_throw="will",
    description="",
    skill_crit_success="",
    skill_success="",
    skill_fail="You can't feel anything over the overwhelming sense of pain and doom.",
    skill_crit_fail="Everything crumbles apart...",
    damage_dice=100,
    damage_size=6,
    modifier=50
)

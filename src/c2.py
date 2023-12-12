"""
Room that contains a Dragon for combat. The final demo room.
"""

import create_room
import compendium_monster

room = create_room.Room(
    name="c2",
    event="combat",
    description="As you step into the room, a chilling gust of wind greets you. The "
    "sight before you is brilliantly breathtaking. The walls seem to shimmer with "
    "a scattered ethereal blue glow as crystal shards jut out from the frozen rocks. "
    "Trinkets of all kinds are lavishly scattered across the chamber, from ornate "
    "goblets to glittering gems, casting prismatic reflections that dance on the "
    "icy walls.\nAnd in the center of the room is a Frost Drake sat regally atop "
    "a pile of gold and bones. Its scales gleam with an otherworldly luster, "
    "glistening in the gentle caress of your torchlight. The Drake's massive chest "
    "rises and falls in a hypnotic rhythm, each breath accompanied by a soft mist "
    "of frigid vapor that escapes its mouth like a spectral sigh.\n Thankfully, "
    "it appears to be sleeping... for now.\nThere is a bright room behind it to "
    "the north of the room.",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name="frost_drake",
    description_cleared="There is a passageway up ahead, north.",
    description_failed="The drake is felled, there is a passageway to the north.",
    loot={},
    action_cleared={
        "perception": create_room.Action_Cleared(
            used=False,
            bonus="",
            text="A pile of gold rests underneath the Drake. He'll let you "
            "pass for now, try anything else and he might snap."
        )
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="The room ahead is clear and bright. Happiness fills your being.",
            next_room="end"
        ),
        "east": create_room.Action_Cleared_Navigation(
            navigation_text="You walk back east.",
            next_room="b1"
        ),
        "west": create_room.Action_Cleared_Navigation(
            navigation_text="You walk back west",
            next_room="b2"
        )
    },
    actions_not_cleared={
        "recall knowledge": create_room.Action_Not_Cleared(
            used=False,
            DC=25,
            ability="int",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="You think back, and remember some information this kind of drake. "
            "\nFrost drakes pose an immense danger in the frozen reaches they "
            "call home. Frost drakes are among the most depraved and openly malicious "
            "of the drakes.",
            fail_text="",
        ),
        "perception": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="perception",
            bonus=0,
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="Nothing in particular catches your attention.",
            fail_text="",
        ),
        "animal handling": create_room.Action_Not_Cleared(
            used=False,
            DC=39,
            ability="wis",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You figure, that even though this creature is a dragon, it "
            "still is an animal nonetheless. You go up to the dragon with baited breath. "
            "It hears you faintly and stirs just a bit. However, you come up close to "
            "it and begin to sooth it with some gentle strokes of its scales. It seems "
            "pleased and continues to rest. Perhaps feeling like he's just had a pleasant "
            "dream.",
            fail_text="You figure, that even though this creature is a dragon, it still "
            "is an animal nonetheless. You go up to the dragon with baited breath. It "
            "hears you faintly and stirs, opening its eyes. It watches you, and you "
            "feel helpless in its presence. Instead of soothing it, you've made "
            "yourself out to be prey. The dragons nostrils flare as it gets up. It licks "
            "its lips, looks like another meal has come directly to it.",
        ),
        "attacking": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="You grab your weapon, and bring courage to yourself. No point "
            "waisting any time, you have the upper hand. It's asleep. And it's time to "
            "go in and attack.",
            fail_text="",
        ),
        "punch": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="str",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="You go up to the dragon, figuring you have the upper hand. "
            "You take your fist and land a solid punch. However, the dragon seems the "
            "list bit fazed by it as your hand begins to sting with the sensation of "
            "hitting a solid block of ice. The Drake snarls at you. It's nostril flare "
            "as its gets up. This prey thinks itself bold doesn't it?",
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
            success_text="You ready yourself, whispering softly and moving your hands "
            "as magical energy begins to emenate around you. The Drake quickly stirs "
            "awake, sensing your magical presence. As it gets up, it arches its back "
            "in pride, seemingly looking down at you. This prey thinks itself bold "
            "doesn't it?",
            fail_text="",
        ),
        "detect magic": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect=False,
            success_text="There doesn't seem to be anything of note. There are a few "
            "items in the room that could be interesting to inspect later... If you're "
            "able to grab them succesfully.",
            fail_text="",
        ),
        "throw": create_room.Action_Not_Cleared(
            used=False,
            DC=30,
            ability="dex",
            bonus=2,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You take a gem from the floor and fling it across the "
            "room. The Drake bolts awake, one of its precious items has been touched. "
            "It runs to chase after it. And as it runs, you come from behind to attack "
            "it, granted the upper hand.",
            fail_text="You take a loose gem from the floor and fling it across the "
            "room. The Drake bols awake, aware of your presence. It looks down upon "
            "you with furious anger, arching its back and snarling. It does not take "
            "too kindly to you touching its treasures. Icy pride fills its eyes. This "
            "prey looks weak and foolish doesn't it?",
        ),
        "stealth": create_room.Action_Not_Cleared(
            used=False,
            DC=34,
            ability="dex",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You hold your breath and tip toe forward. Expertly, you "
            "saunter through the room, as silence continues to fill the room. You "
            "walk forward, and the Drake seems to either not notice or mind.",
            fail_text="You walk forward, careful to take each step as silently as "
            "possible. You inch nearer and nearer to the Drake until you are about "
            "an arms reach away. You continue to walk past him... and accidentally "
            "kick one of the loose goblets on the floor. It clammers, dancing "
            "across the room. As the Drake stirs. It turns to face your direction. "
            "Guilt is written all over your face. He looks down at you and gets up. "
            "Looks like its first meal of the day has arrived.",
        ),
        "play dead": create_room.Action_Not_Cleared(
            used=False,
            DC=35,
            ability="cha",
            bonus=0,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You stumble onto the floor, feighning death. It was a "
            "convincing performance, however, it causes the Drake to stir. It shakes "
            "its head and flares its nostrils, approaching you. As you lie still on "
            "the floor, you wait with baited breath. Its icy breath tickles your "
            "skin as you do your best to stay still. You don't dare to move though."
            "\n...\nWhat feels like forever is disturbed by a horrifying sound. You "
            "hear the Drakes mouth begin to hinge. Even though it thinks you are dead, "
            "it couldn't possibly pass up on a meal, could it? You jump away with your "
            "weapon in hand, as its jaws clamp together. It looks at you with anger. "
            "How dare you just trick him?!",
            fail_text="You stumble onto the floor, feighning death. It was a "
            "convincing performance, however, it causes the Drake to stir. It shakes "
            "its head and flares its nostrils, approaching you. As you lie still on "
            "the floor, you wait with baited breath. Its icy breath tickles your "
            "skin as you do your best to stay still. Despite your best attempt, "
            "you heart begins to pound violently and your skin prickles. You let "
            "out a small whimper.The Drake laughs, deep and gutteral. It knows "
            "you're alive. Unhinging its mouth, you scurry away just in time as its "
            "jaw clamps shut.\nPrepare yourself.",
        ),
        "charm": create_room.Action_Not_Cleared(
            used=False,
            DC=38,
            ability="cha",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You've heard tales of adventurers wooing dragons before. "
            "So why not try it yourself. You clear your throat as the Drake stirs "
            "awake. You begin to spin a wonderful impromtu poem about the power, glory, "
            "and beauty of the Drake. You don't believe a word of it yourself, but "
            "the Drake seems most pleased by your presence. It lays back down, and "
            "gives you a look as if to say- you'd make a tastey meal... but you "
            "understand my glory and for that I'll let you pass.",
            fail_text="You've heard tales of adventurers wooing dragons before. So "
            "why not try it yourself. You clear your throat as the Drake stirs "
            "awake. You think on your feet, and try to come up with an impromtu "
            "poem to speak of the Drakes glory and beauty. However, you slip up "
            "and accidentally insult it. It looks down upon you, clearly angered. "
            "This prey dares to insult him?",
        ),
        "perform": create_room.Action_Not_Cleared(
            used=False,
            DC=35,
            ability="cha",
            bonus=0,
            success_effect="room cleared",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You do what you do best, and you begin to play a song. "
            "The Drake stirs awake, it's large eyes afixed onto you. You don't "
            "let his presence scare you, however, and continue to play your song. "
            "The melody begins to fill the room. It is as beautiful and etheral "
            "and the lights bouncing off the walls of this room. The notes carry "
            "a high pitch that inspire calmness and peace, like the beginning of "
            "a silent winter day. The Drake is pleased. It lowers its guard as "
            "it allows you to walk around, seeming more pleased by the though of "
            "listening to your melody than eating you.",
            fail_text="You do what you do best, and you begin to play a song. "
            "The Drake stirs awake, it's large eyes afixed onto you. You don't "
            "let his presence scare you, however, and continue to play your song. "
            "All seems to be going well as you play a melody of your childhood. "
            "However, the Drake seems to be growing restless- like a cat ready "
            "to pounce. This causes anxiety to fill your heart as your next chord "
            "rings out in a discordant screech. And in an instance, the Drake "
            "gets to its feet ready to attack.",
        ),
        "intimidate": create_room.Action_Not_Cleared(
            used=False,
            DC=38,
            ability="cha",
            bonus=4,
            success_effect="trigger event",
            success_bonus=False,
            fail_effect="trigger event",
            success_text="You run up to the Drake, with weapon in hand. And you "
            "let out the mightiest and most ferocious roar of your life. The "
            "Drake stirs awake, restless and frightened. Your sound reminiscent "
            "of perhaps a mightier and more ferocious Drake than he. You have "
            "the upper hand.",
            fail_text="You run up to the Drake, with weapon in hand, and let "
            "out a roar. He hears you come up close and as he awakens, he lets "
            "out an even more impressive display. It's roar echoes throughout "
            "the room, causing some of the shards on the walls to break. You "
            "stop in your tracks ready to fight.",
        ),
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text="The room ahead is clear and bright. Happiness "
            "fills your being.",
            next_room="end",
            trigger_event="trigger event"
        ),
        "east": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk back east.",
            next_room="b2",
            trigger_event="trigger event"
        ),
        "west": create_room.Action_Not_Cleared_Navigation(
            navigation_text="You walk back west.",
            next_room="b1",
            trigger_event=""
        )
    }
)

event = compendium_monster.Monster(
    name="Frost Drake",
    ac=29,
    max_hp=145,
    current_hp=145,
    level=8,
    lore_dc=21,
    lore_mod="int",
    loot={"gold": 150, "glacial amulet": 1,
          "healing potion greater": 1, "mana potion moderate": 1},
    defeat_text="The Frost Drake reels backwards on it's hind legs, shocked "
    "by the pain you've inflicted. It flaps its wings in a desperate big to keep "
    "itself up. And as the light in it's eyes dims, it slams to the floor in defeat.",
    win_text="The Frost Drake laughs in utter triamph, it walks over to "
    "it's mound of gold with a smile on it's face.",
    attack_list={
        "fangs": compendium_monster.Attacks(
            name="Fangs",
            frequency=[0, 0.35],
            atk_roll=17,
            dc=0,
            dc_type=None,
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=3,
            dice_size=8,
            add_dmg=4,
            success_text="The Frost Drake sinks its fangs into you, dealing a heavy blow.",
            fail_text="The Frost Drake lunges forward with its fangs, but you manage to evade.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        ),
        "tail whip": compendium_monster.Attacks(
            name="Tail Whip",
            frequency=[0.36, 0.79],
            atk_roll=18,
            dc=0,
            dc_type=None,
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=2,
            dice_size=12,
            add_dmg=6,
            success_text="The Frost Drake shifts its weight and lashes out at you with "
            "its heavy tail, hitting you with great force.",
            fail_text="The Frost Drake whips its tail through the air. You "
            "sidestep and avoid the blow.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        ),
        "frost breath": compendium_monster.Attacks(
            name="Frost Breath",
            frequency=[0.8, 1],
            atk_roll=0,
            dc=30,
            dc_type="fortitude",
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=6,
            dice_size=6,
            add_dmg=0,
            success_text="The Frost Drake breathes in a heavy breath, as swirling "
            "cold fills its lungs. The Frost Drake breathes out as a chilling "
            "frost engulfs you, freezing you down to your core as you take damage.",
            fail_text="The Frost Drake breathes in a heavy breath, as swirling cold "
            "fills its lungs. You narrowly dodge the Frost Drake's icy frost breath "
            "by the skin of your teeth.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        )
    }
)


class Room:
    def __init__(self, name, event, description, room_cleared, room_failed, trigger_hazard,
                 hazard_name, trigger_combat, combat_name, description_cleared,
                 description_failed, actions_cleared, actions):
        self.name = name
        self.event = event
        self.description = description
        self.room_cleared = room_cleared
        self.room_failed = room_failed
        self.trigger_hazard = trigger_hazard
        self.hazard_name = hazard_name
        self.trigger_combat = trigger_combat,
        self.combat_name = combat_name,
        self.description_cleared = description_cleared
        self.description_failed = description_failed
        self.actions_cleared = actions_cleared
        self.actions = actions

    def get_description(self):
        return self.description

    def is_cleared(self):
        return self.room_cleared

    def set_cleared(self, value):
        self.room_cleared = value

    def get_actions(self):
        return self.actions

    def perform_action(self, action):
        if action in self.actions:
            return self.actions[action]


# Create an instance of the Room class
a0 = Room(
    name="Entrance",
    event="Exploration",
    description="You stand at the entrance of a dark cave.\n\nThe air is "
                "thick with an uneasy stillness."
                "The faint rustling of the ground beneath your feet echoes in "
                "the cavernous darkness. This may be your very "
                "last breath of fresh air for all you know. You grip your weapon and "
                "prepare for your journey ahead.",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=None,
    hazard_name=None,
    trigger_combat=False,
    combat_name=None,
    description_cleared="Continue north to the main entrance or examine the wall further east?",
    description_failed="No time to dwaddle, the only way forward is up ahead.",
    ###
    actions_cleared={
        "north": ["Continue through the entrance and move north.", "A1"],
        "east": ["Walk over and investigate the east wall.", "S1"],
    },
    ###
    actions={
        "perception": {
            "used": False,
            "DC": 30,
            "success": [
                "You notice some strange markings on the wall to the east. Their glow "
                "is faint and bright. You swear these markings weren't there previously.",
                "room cleared"
            ],
            "fail": [
                "You see nothing out of the ordinary. Steel your wits; it’s time to go in!",
                "room failed"
            ],
        },
        "navigation": {
            "north": ["Continue and move north.", "A1"]
        }
    }
)

s1 = Room(
    name="Secret Entrance",
    event="Exploration",
    description="Your curiosity gets the better of you. As you walk your way over to the "
                "east wall, a sense of wonder and anticipation fills your heart. The runes "
                "etched on the wall emit a warm, enchanting radiance, reminiscent of a vibrant sunset.\n"
                "Gazing at the runes, you find them incomprehensible. More reminiscent of an ancient tongue."
                "Upon further inspection, you note that the wall underneath the carvings "
                "looks... off. As if concealing a hidden truth\n\nDo you wish to investigate "
                "further or walk back west to the main entrance?",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=None,
    hazard_name=None,
    trigger_combat=False,
    combat_name=None,
    description_cleared="You've uncovered the illusion behind the runes as a new entrance opens.\n\n"
                "Do you dare explore further north, or head back west to the main entrance?",
    description_failed="The strange runes baffle you. You really out to start your adventure and head back west.",
    actions_cleared={
        "south": ["Ignore the markings and move back to the main entrance.", "A0"],
        "west": ["Ignore the markings and move back to the main entrance.", "A0"],
        "north": ["You decide to move through the once hidden wall", "S2"],
    },
    actions={
        "perception": {
            "DC": 0,
            "success": "You've already investigated the markings...\nTry something else instead.",
        },
        "detect magic": {
            "DC": 25,
            "skill_success": [
                "You identify the carvings as a seal for some kind of illusion spell. "
                "You trace over the carvings and undo the magical seal. You can now proceed east.",
                "room cleared"],
            "skill_fail": "The carvings are magical, but you aren't sure from which magic school "
            "they're from. Best to tread carefully."
        },
        "throw": {
            "DC": 0,
            "skill_success": "You grab a rock and throw it at the wall. Congrats, you just threw a "
            "rock at a wall."
        },
        "brute forcing": {
            "DC": 0,
            "skill_success": "You hit the wall, as your weapon phases through it. You try to walk "
            "forward but bounce off the wall. You wonder if there's another angle you can "
            "take or if you're just wasting your time."
        },
        "cast spell": {
            "DC": 0,
            "skill_success": "You cast a spell at the wall. The carvings glow as they absorb "
            "your magic harmlessly. You wonder if there's another approach you can take."
            "or if you should even bother."
        },
        "manipulate": {
            "DC": 0,
            "skill_success": ["You touch the carvings and find your finger tracing along "
                              "the symbols. They grow bright and dissipate. Soon the illusion of a wall "
                              "begins to disappear. Now you can traverse into this unconventional opening.",
                              "room cleared"]
        },
        "interaction": {
            "DC": 0,
            "skill_success": ["You touch the carvings and find your finger tracing along "
                              "the symbols. They grow bright and dissipate. Soon the illusion of a wall "
                              "begins to disappear. Now you can traverse into this unconventional opening.",
                              "room cleared"]
        },
        "navigate": {
            "south": ["Ignore the markings and move back to the main entrance.", "A1"],
            "west": ["Ignore the markings and move back to the main entrance.", "A1"]
        }
    }
)

s2 = Room(
    name="Secret Hallway",
    event="Hazard",
    description="You step into the concealed room, and an enchanting radiance surrounds you. "
    "Th air hums with a mysterious magic, as your heart tenses with "
    "anticipation at whatever lies ahead.\n"
    "However, seconds turn to minutes as minutes turn to hours. You feel like you've begun"
    "to lose all track of time. The warm light burning your eyes as the corridor seems to "
    "stretch for an infinite amount of time.\n\n\n"
    "Finally, after what feels like an eternity, you are greeted with breathless feeling.\n"
    "At the end of the tunnel, you see a bright, almost blinding illuminating light. It bathes "
    "you with a sense of otherwordly brilliance.\nAnd as you move closer to the light, "
    "you sense an absolutely overwhelming and foreboding presence. An aura of dominance and beauty.\n"
    "Before you can move another inch, you feel an overwhelming urge to flee wash over you.\n\n"
    "Will you try to keep moving forward?",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=False,
    hazard_name="hazard_beauty_of_a_god",
    trigger_combat=False,
    combat_name=None,
    description_cleared="",
    description_failed="",
    actions_cleared={
        "west": ["You run all the way back to the entrance.\nWhatever is ahead, you don't want "
                 "to face it.", "A1"],
        "south": ["You run all the way back to the entrance.\nWhatever is ahead, you don't want "
                  "to face it.", "A1"],
        "north": ["You continue to follow the light up ahead.", "S3"],
    },
    actions={
        "navigate": {
            "west": ["This is far too much for you to handle.\n"
                     "You find yourself back at the entrance, out of breath and feeling more tired than "
                     "before. You take a moment and rest before you walk into the main entrance.", "A1"],
            "south": ["This is far too much for you to handle.\n"
                      "You find yourself back at the entrance, out of breath and feeling more tired than "
                      "before. You take a moment and rest before you walk into the main entrance.", "A1"],
            "north": ["You try to move forward, but your feet won't let you move ahead.", "trigger hazard"]
        },
    }
)

s3 = Room(
    name="Fey Queen",
    event="Exploration",
    description="You muster the courage to continue onward, fighting the relentless urge to flee. "
    "Each step you take brings you closer to the radiant light at the end of the tunnel.\n\n"
    "Emerging from the incandescent brilliance, you behold a beautiful and breathtaking sight. A "
    "magnificent Fey, regally seated upon an adorned throne. Ethereal light dances around her, "
    "as small pixies, with luminscent wings shimmering like firefies, dance around her. Her presence "
    "is chiseled with wisom and power shining with luminescence.\n\n"
    "Her eyes betray either amusement or curiosity, with their gaze fixed upon you. An aura of enchantment "
    "envelopes the throne room, drawing you in deeper.\n\n"
    "In her presence, what do you do?",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=False,
    hazard_name=None,
    trigger_combat=False,
    combat_name=None,
    description_cleared="",
    description_failed="",
    actions_cleared={
        "diplomacy": "You continue to talk with her and she bestows a little bit more knowledge to you."
        "[Gain +1 permanently to intelligence]",
        "perform": "You continue to entertain and she bestows a little bit more warmth to you."
        "[Gain +1 permanently to charisma]",
        "charm": "You try to charm her, she is pleased and you begin to feel a little stronger."
        "[Gain +1 permanently to strength]",
        "south": ["You make your way back to the cave entrance, enlightened and relieved.", "A1"],
        "west": ["You make your way back to the cave entrance, enlightened and relieved.", "A1"],
    },
    actions={
        "perception": {
            "DC": 25,
            "success":
            "She seems to be rather intrigued by your presence. She doesn't appear to want "
            "to hurt you in any way. However, you still sense an unnerving amount of power "
            "emanating from her. It'd be best to stay on her good side.",
            "fail": [
                "The bright light is too bright for your eyes. It's hard to discern anything peculiar about her.",
            ]
        },
        "recall knowledge": {
            "DC": 32,
            "success":
            "You recall how Fey came from the Feywilds. They are synonymous with the supernatural. "
            "They are often found near specific natural locations imbued with magic. Their nature "
            "can vary from playful and mischievous to outright selfish.\n"
            "This particular Fey is a Lampesperid Queen which rules over isolated regions soaked "
            "in light. They guard countless treasures and secrets, though, for those who approach "
            "them with respect, they're willing to part with knowledge or items.",
            "fail":
            "You can't recognize what kind of creature she is other than some kind of Fey or Fairy.",
        },
        "diplomacy": {
            "DC": 28,
            "success": ["She is pleased and has a conversation with you. You share stories of your "
                        "previous adventures and secrets you've uncovered before. In return, she warns "
                        "you about the cave ahead filled with traps and monsters. She also gives you an "
                        "amulet that will give you +5 to all damage rolls. As well as a Greater Potion of Healing. "
                        "Bathed in a warm light, she summons you away.\n",
                        "You find yourself back at the entrance of the cave. The eastern wall you came through "
                        "appears to be missing.",
                        "room cleared"],
            "fail": ["Although the Queen is normally one for good company, she finds your presence rather "
                     "annoying. While you are mid-sentence, she waves her hand at you as you feel bathed "
                     "in a warm light. Before your next breath, you find yourself back at the entrance of "
                     "the cave.\nThe eastern wall you came through appears to be missing.",
                     "room failed"]
        },
        "intimidate": {
            "DC": 35,
            "success": ["You somehow manage to intimidate the Fey Queen. She shivers in repulsion as she "
                        "hastily gives you a Potion of Greater Healing and summons you away.\n",
                        "You find yourself back at the entrance of the cave. The eastern wall you came "
                        "through appears to be missing.",
                        "room cleared"],
            "fail": ["You let out a pathetic roar or mumble under your breath. It's evident you "
                     "were trying to intimidate the Fey Queen. No matter, she laughs in your face.\n\n"
                     "And then a cheeky look creeps upon her face. She begins to move her hands around "
                     "and whispers something in Fey's tongue. A warm light begins to envelop you as "
                     "you feel your very being begin to burn. Everything around you seems to grow "
                     "bigger as you shrink into the floor.\nBefore you come to, you find yourself the "
                     "size of a sprite with wings upon your back. And you feel an overwhelming urge "
                     "to fly towards the queen and worship her for the rest of your life. \n\n"
                     "Hope you like a life of eternal servitude!",
                     "trigger hazard"]
        },
        "perform": {
            "DC": 28,
            "success": ["You reach for your instrument and begin to play a soothing melody.\n"
                        "The ethereal music fills the air, and the Fey Queen's eyes sparkle "
                        "with delight. She leans in closer, entranced by your performance and "
                        "humming to the tune. In appreciation for your beautiful serenade, she "
                        "bestows upon you an amulet. [+5 bonus to all damage rolls].",
                        "room cleared"],
            "fail": ["Your music falls flat, and the notes seem discordant in this "
                     "otherworldly realm. The Fey Queen winces at the cacophony and abruptly "
                     "waves her hand. You are bathed in a bright light and find yourself back "
                     "at the entrance of the cave. The eastern wall you came through appears "
                     "to be missing.",
                     "room failed"]
        },
        "charm": {
            "DC": 31,
            "success": [
                "Your charm and wit catch the Fey Queen off guard. She bursts into laughter, "
                "thoroughly entertained by your advances. In appreciation, she bestows upon "
                "you an amulet that enhances your prowess, granting you a +5 bonus to all damage rolls.",
                "room cleared"
            ],
            "fail": [
                "Instead of being flattered, she becomes annoyed. Annoyance replaces "
                "her mirth as she promptly ushers you away. She waves her hand as you are "
                "bathed in a bright light.\n\n",
                "You find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.",
                "room failed"
            ]
        },
        "attack": {
            "DC": 0,
            "success": ["You ready an attack, immediately wary of her presence. The Fey Queen "
                        "frowns and looks at you with disappointment. Before you can so much as think, "
                        "she lifts her finger as you are enveloped in a white light. You feel your body "
                        "begin to burn as each molecule of your being begins to erupt. And before you "
                        "know it, you're dead.",
                        "trigger hazard"]
        },
        "cast spell": {
            "DC": 0,
            "success": ["You ready an attack, immediately wary of her presence. The Fey Queen "
                        "frowns and looks at you with disappointment. Before you can so much as think, "
                        "she lifts her finger as you are enveloped in a white light. You feel your body "
                        "begin to burn as each molecule of your being begins to erupt. And before you "
                        "know it, you're dead.",
                        "trigger hazard"]
        },
        "manipulate": {
            "DC": 0,
            "success": ["You seem drawn to her... like a moth to a flame. And as you reach out your "
                        "hand to touch the Fey Queen. \nShe begins to move her hands around and "
                        "whispers something in Fey's tongue. A warm light begins to envelop you "
                        "as you feel your very being begin to burn. Everything around you seems to "
                        "grow bigger as you shrink into the floor. \nBefore you come to, you find "
                        "yourself the size of a sprite with wings upon your back. And you feel an "
                        "overwhelming urge to fly towards the queen and worship her for the "
                        "rest of your life. \n\nHope you like a life of eternal servitude!",
                        "trigger hazard"]
        },
        "throw": {
            "DC": 0,
            "success": ["In a panic, you grab a rock on the floor and chuck it at the Fey Queen. "
                        "She frowns in annoyance. One of the pixies catches the pebble in midair.\n"
                        "With a flick of the wrist, the Fey Queen ushers you away as you are bathed "
                        "in a glowing light. You find yourself at the entrance of the cave again. "
                        "\n\nWhy did you think that was a good idea?",
                        "room failed"]
        }
    }
)

a1 = Room(
    name="Tile Room Trap",
    event="Hazard",
    description="As you cautiously step into the cave's entrance, an otherworldly "
    "stillness envelopes you. A hushed silence fills the air. The dim light filtering "
    "in from the outside barely penetrates the cavern's depths. What little light "
    "there is casts eeries shadows that dance along the rocky walls.\n\n"
    "Beneath your feet, you discover a tangled mosaic of peculiar tiles, each carved "
    "with intricate patterns emenating with energy. The air carries a faint hymm, "
    "daring you to venture further. Each step uncovering more about the secrets "
    "of this dungeon.\n\nAs you move deeper along the corridor, your torchlight reveals "
    "the walls and floor adorned with these mysterious designs. The patterns intertwine "
    "and shift, as you're still unsure of their origin. Call it your sense of "
    "experience, paranoia begins to gnaw at you as you feel every step further may "
    "lead you to peril. There's something odd about these tiles."
    "\n\nWhat would you like to do?",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=False,
    hazard_name="hazard_tiles",
    trigger_combat=False,
    combat_name=None,
    description_cleared="You can see up ahead that there is a corridor that leads either "
    "north or east. \n\nWhich direction would you like to take?",
    description_failed="The arrows scattered on the floor remind you that you at least "
    "made it out of the room alive. You can see up ahead that there is a corridor that "
    "leads either north or east. \n\nWhich direction would you like to take?",
    actions_cleared={
        "north": ["Continue through the tunnel and move north.", "B1"],
        "east": ["Continue through the tunnel and move east.", "A2"],
    },
    actions={
        "perception": {
            "DC": 22,
            "success": "You've seen something like this before. You think this room may "
            "be some kind of trigger trap. You best be careful not to trigger the trap.",
            "fail": ["You don't seem to notice anything odd. But while investigating, you "
                     "accidentally trigger one of the pressure plates.\nBrace yourself!",
                     "trigger hazard"]
        },
        "disable": {
            "DC": 24,
            "success": "You safely disarm the trap with your Lockpick. Good thing you've "
            "been practicing. The tiles shift down harmlessly.",
            "fail": ["You trigger the trap, as arrows shoot across the room.\nBrace yourself!",
                     "trigger hazard"]
        },
        "jump": {
            "DC": 23,
            "success": "With a running start, you leap over the tiles without triggering it.",
            "fail": ["You misjudge your jump, triggering the trap as arrows shoot across the "
                     "room.\nBrace yourself!",
                     "trigger hazard"]
        },
        "throw": {
            "DC": 26,
            "success": "You pick up a loose stone and toss it onto the tiles. You safely "
            "trigger the trap as arrows shoot across the room.",
            "fail": ["You throw an item onto the pressure plate, but it isn't heavy enough "
                     "to activate it. You confidently walk over it and trigger the trap, "
                     "as arrows shoot across the room.\nBrace yourself!",
                     "trigger hazard"]
        },
        "attack": {
            "DC": 26,
            "success": "With precision, you strike the pressure plate with your weapon, "
            "triggering the trap from a safe distance. Arrows fly across the room as "
            "you narrowly dodge them.",
            "fail": ["You attempt to hit the pressure plate from a safe distance. However, "
                     "when you hit the plate, you were too close. You get caught in a flurry "
                     "of arrows across the room.\nBrace yourself!",
                     "trigger hazard"]
        },
        "brute forcing": {
            "DC": 26,
            "success": "With precision, you strike the pressure plate with your weapon, "
            "triggering the trap from a safe distance. Arrows fly across the room as "
            "you narrowly dodge them.",
            "fail": ["You attempt to hit the pressure plate from a safe distance. However, "
                     "when you hit the plate, you were too close. You get caught in a flurry "
                     "of arrows across the room.\nBrace yourself!",
                     "trigger hazard"]
        },
        "cast spell": {
            "DC": 26,
            "success": "Using your wits, you cast a spell from a safe distance. You "
            "trigger the trap as arrows fly across the room.",
            "fail": ["Thinking you're clever, you cast a spell from a safe distance "
                     "at the tiles. You didn't realize how weak your spell was as "
                     "you walked across the tiles that triggered a flurry of arrows."
                     "\nBrace yourself!",
                     "trigger hazard"]
        },
        "navigate": "You should investigate the room first, before you move ahead.",
    }
)

a2 = Room(
    name="Giant Rat Room",
    event="Combat",
    description=" You walk down the tunnel as the darkness grows deeper. The narrow "
    "passage is damp, and the air feels heavy with moisture. The faint echoes of your "
    "footsteps bounce off the cold, stone walls. As you continue, you hear a "
    "scampering on the floor, followed by sharp screeches. After being through many "
    "dark caves before, you instantly recognize the sounds. It's a Giant Rat."
    "\n\nYou take a moment to assess the situation. The tunnel extends ahead, and you "
    "can't see the end of it. The rats could be coming from anywhere within the "
    "darkness. It steps sound even closer as you wait, till it nears closer in "
    "sight.\n\nThink quickly; your next steps could be crucial.",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=None,
    hazard_name=None,
    trigger_combat=False,
    combat_name="Giant Rat",
    description_cleared="The rat scampers around happy to see you again. When you get"
    "close to it, it runs away.\nYou can move either west or east.",
    description_failed="You've already been through this room.\nYou can move either "
    "west or east.",
    ###
    actions_cleared={
        "west": ["Continue through the tunnel and move west.", "A1"],
        "east": ["Continue through the tunnel and move east.", "S1"],
    },
    ###
    actions={
        "perception": {
            "DC": 22,
            "success": [
                "You notice the Giant Rat has a limp on its back left paw, you can "
                "use this to your advantage in combat.",
                "attack roll bonus small"
            ],
            "fail": [
                "You don't notice anything peculiar about this rat, other than him "
                "being a giant rat.",
                "room cleared"
            ],
        },
        "stealth": {
            "DC": 24,
            "success": [
                "Like a shadow, you slink into the darkest crevices in the cavern. "
                "Slowing your breath and obscuring your presence. When the rat "
                "comes near, you will be ready to attack with utmost precision",
                "attack roll bonus small"
            ],
            "fail": [
                "You attempt to hide and loudly kick a loose rock. Its movement "
                "ricochets in the tunnel as the rat turns to face you, ready for combat.",
                "trigger combat"
            ],
        },
        "diplomacy": {
            "DC": 26,
            "success": [
                "With a kind hand and gentle voice, you manage to soothe the rats anxious heart. "
                "Perhaps its old days of being a smaller rat resurface in its mind. It now acts "
                "very friendly and docile with you, deciding to befriend you. To show its "
                "gratitude, it uncovers a hidden treasure buried in the ground.",
                "room cleared"
            ],
            "fail": [
                "Your attempts to communicate or pet the rat fall flat, aggravating it "
                "further. The Giant Rat grows even more hostile. It bares its teeth "
                "and is ready for combat.",
                "trigger combat"
            ],
        },
        "animal handling": {
            "DC": 22,
            "success": [
                "With a kind hand and gentle voice, you manage to soothe the rats anxious heart. "
                "Perhaps its old days of being a smaller rat resurface in its mind. It now acts "
                "very friendly and docile with you, deciding to befriend you. To show its "
                "gratitude, it uncovers a hidden treasure buried in the ground.",
                "room cleared"
            ],
            "fail": [
                "Your attempts to communicate or pet the rat fall flat, aggravating it "
                "further. The Giant Rat grows even more hostile. It bares its teeth "
                "and is ready for combat.",
                "trigger combat"
            ],
        },
        "throw": {
            "DC": 25,
            "success": [
                "You hurl a loose pebble, distracting the Giant Rat momentarily and giving "
                "you an advantage in combat.",
                "attack roll bonus small"
            ],
            "fail": [
                "You throw a loose pebble attempting to distract the rat, instead you only "
                "draw attention to yourself. The rat turns towards you and bares its teeth "
                "ready for combat.",
                "trigger combat"
            ],
        },
        "intimidate": {
            "DC": 27,
            "success": [
                "With an intimidating glare, you strike fear into the Giant Rat. In cowers "
                "in fear, unable to move.",
                "attack roll bonus big"
            ],
            "fail": [
                "The rat can't even tell you were trying to intimidate it. It lowers "
                "its stance, ready to attack.",
                "trigger combat"
            ],
        },
        "play dead": {
            "DC": 27,
            "success": [
                "You collapse to the ground, feigning death. The rat comes over to sniff "
                "you, and once it assumes you're dead it turns to leave. You have the "
                "opportunity to strike while its guard is down.",
                "attack roll bonus big"
            ],
            "fail": [
                "You try to play dead, but it's not very convincing. The Giant Rat still "
                "thinks you're a threat and is ready to attack.",
                "trigger combat"
            ],
        },
        "perform": {
            "DC": 24,
            "success": [
                "Your melody fills the cavern. The Giant Rat lowers its guard, completely "
                "enamored with your song. It seems friendly and no longer interested in "
                "attacking you. To show its gratitude, it uncovers a hidden treasure "
                "buried in the ground.",
                "room cleared"
            ],
            "fail": [
                "Your melody falls flat and the Giant Rat, in its irritation, bares its "
                "teeth ready to fight you.",
                "trigger combat"
            ],
        },
        "attacking": {
            "DC": 0,
            "success": [
                "Without hesitation, you draw your weapon and prepare to strike.\n\n"
                "Adrenaline courses through your veins as you prepare for the upcoming battle.",
                "trigger combat"
            ]
        },
        "cast spell": {
            "DC": 0,
            "success": [
                "You focus your energy, drawing upon your magical powers. With a series of "
                "gestures the air around you crackles.\n\nYou prepare to cast a spell for the "
                "upcoming battle.",
                "trigger combat"
            ]
        },
        "navigate": "You need to deal with the giant rat before you move ahead.",
    }
)

a3 = Room(
    name="Miasma",
    event="Hazard",
    description="You walk down the dimly lit tunnel as the darkness grows deeper. "
    "The silence envelops you. The walls, damp and uneven, seem to close in around "
    "you with every step. Strange, otherworldly markings and symbols are etched "
    "into the stone, their meaning lost to time. The air is heavy with an earthy scent, "
    "and the distant echoes of water dripping create an eerie backdrop.\n"
    "As you continue, a thick fog begins seeps through the air. It swirls through the "
    "tunnel as your breathing becomes labored. The dim light from your torch dances "
    "through the mist. As you move through, it doesn't seem to get any thinner, and "
    "is in fact becoming dangerously thick. You can see a passageway up ahead towards "
    "the north.\n\nWhat do you do?",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=False,
    hazard_name="hazard_miasma",
    trigger_combat=False,
    combat_name=None,
    description_cleared="You can see up ahead that there is a corridor that leads either "
    "north or east. \n\nWhich direction would you like to take?",
    description_failed="The arrows scattered on the floor remind you that you at least "
    "made it out of the room alive. You can see up ahead that there is a corridor that "
    "leads either north or east. \n\nWhich direction would you like to take?",
    actions_cleared={
        "north": ["Continue through the tunnel and move north.", "B1"],
        "east": ["Continue through the tunnel and move east.", "A2"],
    },
    actions={
        "recall knowledge": {
            "DC": 24,
            "success": "You think back to previous adventures and books you've read. The "
            "thickening air and sickly hue... This is a miasma. If you don't "
            "protect yourself properly, then inhaling too much of this fog will "
            "cause lethal damage. You recognize that if you cover up your mouth "
            "in some way or create a clean pocket of air, then you'll likely "
            "make it through just fine.",
            "fail": "You can't really think of anything that explains the fog in the air."
        },
        "mask": {
            "DC": 0,
            "success": ["You think fast and create a makeshift mask out of some cloth. "
                        "You're able to walk through the fog with little to no problem.",
                        "room cleared"],
        },
        "attacking": {
            "DC": 30,
            "success": ["A strange idea pops in your head. You take out your weapon and "
                        "begin to spin it in the air rapidly. By spinning it around at "
                        "such a fast speed, you are able to make a pocket of air around "
                        "you. You are able to pass through the fog with little trouble.\n"
                        "You see a passage up north.",
                        "room cleared"],
            "fail": ["You have your weapon out, but there is nothing really to attack.",
                     "trigger hazard"]
        },
        "perception": {
            "DC": 27,
            "success": "You search your way through the fog and end up finding areas in "
            "the tunnel with a thin amount of fog. You are able to walk through "
            "the fog safely by utilizing this weakness.",
            "fail": ["You peer through the fog but you can't find anything that will help you.",
                     "trigger hazard"]
        },
        "recall knowledge": {
            "DC": 24,
            "success": ["You look around you and begin to chant a spell to yourself. Gesturing "
                        "your arms you create a makeshift bubble around you. You are able to "
                        "purify the air around you as you walk through the tunnel.",
                        "room cleared"],
            "fail": ["You think of various different spells in your arsenal. You think of any "
                     "that could help in this situation.",
                     "trigger hazard"]
        },
        "jump": {
            "DC": 28,
            "success": ["With a running start, you aim towards the end of the corridor with a "
                        "glorious vault. Tumbling through air, you land on your feet gracefully "
                        "at the other end of the tunnel. You can now continue to move north.",
                        "room cleared"],
            "fail": ["With a running start, you vault through the corridor; trying to make it "
                     "through the end. However, your jump ends short and you're still in the "
                     "thick of the fog.",
                     "trigger hazard"]
        },
        "disable": {
            "DC": 29,
            "success": "You peer all over the room, shining your light on the walls. You "
            "miraculously find a portion of the wall with some vents in it. You take "
            "out some items from your belt as you finagle with the vents. With a "
            "click, the vents stop pushing out air. The fog begins to thin and you "
            "can now make it through the other side at the north wall.",
            "fail": ["You peer all over the room, looking for a way to reduce the fog. You can't "
                     "find anthing of note.",
                     "trigger hazard"]
        },
        "navigate": ["You walk through the room and move up ahead.", "trigger hazard"],
    }
)

b1 = Room(
    name="Kobold",
    event="Combat",
    description="You cautiously walk through the corridor, dimly lit and long. The "
    "silence is disrupted by faint sounds of scuttling feet and muted chattering. "
    "You swivel your head around. Paranoia gnaws at your senses.\nYou strain your "
    "ears and listen more closely, trying to discern the noises. You get the feeling "
    "that you are not alone in this tunnel. You swear you could hear a faint "
    "chuckling from behind the walls.\nA sense of danger pricks your skin. From "
    "the corner of your eye, you catch a fleeting moment of a dim light, darting "
    "along the tunnel walls. Somethingn is following you, stalking you through the "
    "darkness.\n\nThink fast.",
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=False,
    hazard_name=None,
    trigger_combat=False,
    combat_name="kobold",
    description_cleared="The room is now empty, you may go either north or south.",
    description_failed="The room is now empty, you may go either north or south.",
    actions_cleared={
        "north": ["Continue through the tunnel and move north.", "C2"],
        "south": ["Continue through the tunnel and move south.", "A1"],
    },
    actions={
        "recall knowledge": {
            "DC": 20,
            "success": "piecing together the clues, you can guess that the creature "
            "stalking you is a Kobold, a cunning and opportunistic creature. The "
            "like to burrow in tunnels and are generally peaceful as long as you "
            "don't trespass in their territory. You know that as long as you can "
            "avoid it or convince it to go away, it will probably just ignore you.",
            "fail": "There aren't enough clues for you to piece together what kind "
            "of creature is stalking you."
        },
        "perception": {
            "DC": 26,
            "success": "You lay low and wait for a bit. You hone in on your senses and "
            "adjust to the darkness. The faint lights you saw flicker and form into the "
            "shadow of the creature. It appears to be a Kobold, minding its own business "
            "and looking for crevices to squeeze into.",
            "fail": ["You don't seem to notice anything.",
                     "trigger combat"]
        },
        "attacking": {
            "DC": 0,
            "success": ["Without hesitation, you draw your blade and prepare to strike "
                        "whatever it is that’s following you. With bated breath, "
                        "adrenaline courses through your veins as you wait.",
                        "trigger combat"]
        },
        "cast spell": {
            "DC": 0,
            "success": ["You channel your magical energies, preparing to unleash a "
                        "spell at your shadowed stalker.",
                        "trigger combat"]
        },
        "throw": {
            "DC": 27,
            "success": ["In a moment of quick thinking, you grab a trusted loose pebble "
                        "on the floor. You wait with bated breath as you wait for your "
                        "shadowed follower. A kobold steps out of the shadows, inspecting "
                        "the tunnel walls and unassuming. You hurl the loose rock and nail "
                        "it right at the kobold’s head. It’s a direct hit, knocking him at "
                        "the temple. With a teeter, the kobold rocks as it falls onto the "
                        "floor, completely incapacitated.",
                        "room cleared"],
            "fail": ["You grab a loose pebble from the floor. And wait with bated breath "
                     "as you wait for your shadowed follower. A kobold steps out of the "
                     "shadows, inspecting the tunnel walls and unassuming. You hurl the "
                     "pebble and it hits its mark. However, the force of impact was so "
                     "minimal that it simply directs the kobold to your location.",
                     "trigger combat"]
        },
        "stealth": {
            "DC": 26,
            "success": ["You move quickly and blend into the shadows. Hugging the tunnel "
                        "walls in the crevice of darkness. You hold your breath as you "
                        "watch the shadow of a kobold creep into sight. It appears to be "
                        "inspecting one of the tunnel walls. It grabs something from the "
                        "wall and then creeps back into the shadows, scurrying into a "
                        "tunnel in the floor. You let go of the wall. It doesn’t look "
                        "like it’s coming back. You see a tunnel up ahead to the north.",
                        "room cleared"],
            "fail": ["You move quickly and walk into the shadows. You hug the tunnel "
                     "walls as a kobold appears to creep into sight. You can’t get a "
                     "good look at it and what it’s doing. So you move closer into sight. "
                     "However, you snag a loose pebble under your foot as it bounces "
                     "clumsily and loudly towards the kobold. Alerted, it turns around "
                     "and looks straight at you.",
                     "trigger combat"]
        },
        "intimidate": {
            "DC": 26,
            "success": ["You wait for whatever it is following you through the tunnel. "
                        "You hold onto your weapon with great resolve and puff your "
                        "chest. From the shadows, you see a creature come out of the "
                        "shadows, a small kobold. You charge towards it with your weapon in hand, letting out a most ferocious roar. The kobolds eyes grow large as its heart leaps out. It falls to the floor and then quickly gets back up to run away. As you partly chase it, it scampered and squeezes into a hidden tunnel in the floor; one that is far too small for you to get into. It likely won’t be coming back out any time soon. You see up ahead a northern tunnel.",
                        "room cleared"],
            "fail": ["You wait for the creature to come out of the shadows, ready to scare it away with your might. A small kobold appears from the light, carrying a small weapon and some tools. You move towards it and yell at him. Confused, it looks at you with an angry look on its face. It sees your signs of aggression and is ready for combat.",
                     "trigger combat"]
        },
        "diplomacy": {
            "DC": 20,
            "success": ["You think the best way to get out of this is to reason your "
                        "way out of it. You gently call out at the shadow scampered "
                        "along the tunnel walls. You reason that you’re here peacefully "
                        "and simply wish to move through. The kobold scurries out of "
                        "the shadows, fearful at first, but quickly relieved. It looks "
                        "at you and tells you how it’s just here to check one of the walls "
                        "for the lady of the caves. Before you could ask anything else, "
                        "it does exactly as it says. Checking the wall and then "
                        "scampering away into a tunnel in the floor. It doesn’t look "
                        "like it’s coming back. You see a tunnel ahead that leads north.",
                        "room cleared"],
            "fail": ["You call out to the shadows, thinking reasoning may be better than "
                     "just fighting. You say that you do not wish to harm whatever he "
                     "is.\nA kobold scurries out of the shadows, but it looks at you "
                     "with fear. It looks at your gear and doesn’t seem to trust you "
                     "despite your words.",
                     "trigger combat"]
        },
        "perform": {
            "DC": 20,
            "success": ["You begin to play a tune, playing a beautiful progression of "
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
                        "room cleared"],
            "fail": ["You begin to play a tune, but it is completely discordant and out "
                     "of tune. A kobold runs out of the shadows mad and upset. It seems "
                     "to be completely irritated with your disharmonious tune ready to "
                     "stop the source.",
                     "trigger combat"]
        },
        "play dead": {
            "DC": 30,
            "success": ["You press yourself up against the tunnel wall, feigning death; "
                        "losing weight from your limbs and going limp. You don’t even "
                        "stir as you hear small scuffling from a creature in the distance. "
                        "You don’t know if has noticed you or not but seems to not care "
                        "or notice your presence. It seems to walk towards a tunnel wall "
                        "as it disappears into the ground. You wait a few minutes, until "
                        "you’re sure it won’t come back again. You get up and brush "
                        "yourself off. You see a northern tunnel up ahead.",
                        "room cleared"],
            "fail": ["You fall limply to the floor but fail to conceal yourself in a "
                     "convincing manner. You wait with your heart beating through your "
                     "chest as you hear faint footsteps in the distance. But then, the "
                     "footsteps grow even louder as it begins to approach closer. You "
                     "try not to move as you feel something small walk right next to you. "
                     "You can feel moist breath as it sniffs your ‘corpse’. It screeches "
                     "and you stir to life startled. Your cover is blown, and it has its "
                     "weapon at the ready.",
                     "trigger combat"]
        },
        "navigate": ["You walk through the room and move up ahead.", "trigger combat"],
    }
)

b2 = Room(
    name="Shadow",
    event="Combat",
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
    ###
    room_cleared=False,
    room_failed=False,
    trigger_hazard=False,
    hazard_name=None,
    trigger_combat=False,
    combat_name="shadow",
    description_cleared="The room is now empty, you may go either north or south.",
    description_failed="The room is now empty, you may go either north or south.",
    actions_cleared={
        "north": ["Continue through the tunnel and move north.", "C3"],
        "south": ["Continue through the tunnel and move south.", "A3"],
    },
    actions={
        "recall knowledge": {
            "DC": 20,
            "success": "You wrack you brain and recall the type of creature this is. "
            "It’s a Shadow, an undead creature made of darkness. They lurk in dark "
            "places and attack those who stray from the light. If you parlay with a "
            "shadow, you remember that you can keep them at bay with a strong light...",
            "fail": "You can’t seem to recall what kind of creature this is other than "
            "some kind of shadow."
        },
        "attacking": {
            "DC": 0,
            "success": ["You grip your weapon, prepared to strike the shadowed fiend.",
                        "trigger combat"],
        },
        "cast spell": {
            "DC": 20,
            "success": ["You think quickly on your feet. Thinking of the current spells "
                        "in your arsenal, you are reminded of one of the most common "
                        "cantrip spells… ‘Light’. You cast it as radiant light blooms "
                        "in the narrow corridor. The creature of darkness recoils in "
                        "the bright light. The shadows around you seem to scurry into "
                        "the depths of the cave. The flash-bomb you’ve magically created "
                        "seems to have deterred the shadow from making an enemy of you. "
                        "You may continue moving north.",
                        "room cleared"],
            "fail": ["You conjure magical energy around you, prepared to blast the shadowed fiend.",
                     "trigger combat"]
        },
        "perception": {
            "DC": 24,
            "success": ["You notice that the shadow is sulking in the darkest parts of "
                        "the room. As long as you fight him in the lightest parts, it "
                        "will at least give you a small advantage in combat.",
                        "attack roll bonus small"],
            "fail": ["The shadow is large and imposing, sending shivers coursing through "
                     "your body. You can’t tell anything peculiar about it that will "
                     "help you in combat.",
                     "trigger combat"]
        },
        "punch": {
            "DC": 0,
            "success": ["You throw a big punch at the fiend, but it seems to phase "
                        "right through it. The shadowy creature arches its back and "
                        "howls, sending shivers coursing through your body.",
                        "trigger combat"],
        },
        "throw": {
            "DC": 0,
            "success": ["You take a lose rock from the floor and toss it at the shadow. "
                        "It simply phases right through it. The shadowy creature lets "
                        "out a hiss resembling a laugh. It lurches forward at you with "
                        "its claws.",
                        "trigger combat"],
        },
        "detect magic": {
            "DC": 20,
            "success": ["You quickly decipher through your mind, studying the magic in "
                        "the room. You detect some sort of illusion spell throughout "
                        "the small corridor. Without moments hesitation, you counteract "
                        "the illusion. The darkness begins to dissipate around you as "
                        "the torches you’d become accustomed to seeing throughout this "
                        "dungeon relight. The bright light pours through the corridor as "
                        "the shadow reals in discomfort. It holds its claws to its eyes "
                        "disoriented by the change of scenery. It begins to dissipate "
                        "as the light tears through its body.",
                        "room cleared"],
            "fail": ["You try to detect if there’s any magic in the room. You get the "
                     "sense that some powerful magic is at work in the room. But you "
                     "can’t distinguish if it’s from the shadow itself or the corridor. "
                     "In your confusion, the shadow takes the opportunity to strike.",
                     "trigger combat"]
        },
        "stealth": {
            "DC": 32,
            "success": ["You grab your torch and put it up to its face, it recoils as "
                        "you use the instance to slip into a small crevice. The shadow "
                        "shakes its head in disbelief, losing sight of you. Now you "
                        "have the perfect opportunity to strike back at it with great force.",
                        "attack roll bonus big"],
            "fail": ["It shocking that you even thought you could slip away from an "
                     "actual shadow seeing as you were standing right in front of it. "
                     "It sees through your ruse quite clearly and readies its claws.",
                     "trigger combat"]
        },
        "intimidate": {
            "DC": 28,
            "success": ["The shadows begins to lurch out at you as you grab onto your "
                        "blade and unleash the deadliest insult to its face. It recoils "
                        "at your ferocity and shudders. Your display has granted you "
                        "the upper hand.",
                        "attack roll bonus small"],
            "fail": ["You muster up a pathetic roar at the shadow. It is unimpressed "
                     "as it lets out a hiss like laughter. Reading its claws, it "
                     "prepares for combat.",
                     "trigger combat"]
        },
        "play dead": {
            "DC": 31,
            "success": ["With the most impressive acting of your life, you clench your "
                        "chest and hold your breath. Feigning death as if you were "
                        "struck by the fear of fear itself. The shadow creeps over "
                        "your body confused at first. But then becomes most pleased "
                        "with itself, letting out a hiss resembling laughter. It "
                        "coaches back into the shadows and slips away.",
                        "room cleared"],
            "fail": ["You grab your chest and lean backwards. You let out a pathetic "
                     "groan as if you were keeling over. However, the shadow is not "
                     "very impressed with your lackluster performance. It lets out a "
                     "roar as it readies its claws.",
                     "trigger combat"]
        },
        "perform": {
            "DC": 0,
            "success": ["You perform a small song in the thick of the moment. The "
                        "shadow recoils with anger as the melody trickles within the "
                        "small corridor. It flails its claws over its face as if "
                        "shielding itself from the harmony of your tune.",
                        "attack roll bonus small"],
        },
        "throw": {
            "DC": 0,
            "success": ["An idea comes into your head. If this creature is made of "
                        "darkness, then the best way to counteract it is to use light. "
                        "You quickly take some cloth from inside your bag and light it "
                        "on fire with your torch. The flames grow readily as you toss "
                        "it on the floor. The light causes the corridor to feel "
                        "completely alight. The shadow recoils in agony, screeching "
                        "as it flails on the floor. As the light grows, the shadow seems "
                        "to dissipate and disappear.", "room cleared"],
        },
        "navigate": ["You try to walk ahead with the shadow looming over you. \n\n"
                     "He won't let you escape.",
                     "trigger combat"],
    }
)



# Access and use functions of the room
print(s3.get_description())
print(s3.actions_cleared["diplomacy"])


print(b2.actions["perception"])
# Check if the room is cleared
# print(a0.is_cleared())

# # Set the room as cleared
# a0.set_cleared(True)
# print(a0.is_cleared())

# # Perform an action and get the result
# action_result = a0.perform_action("perception")
# print(action_result["success"][0])

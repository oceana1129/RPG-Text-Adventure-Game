compendium_rooms = [
    # ENTRANCE WITH NO SECRET
    {
        "room": "A0",
        "event": "explore",
        "description": """You stand at the entrance of a dark cave. The ground rustles as the wind carries an uneasy tune. This may be your very last breath of fresh air for all you know. You grip your weapon and prepare for your journey ahead.""",
        "room_cleared": False,
        "room_cleared_description": """Continue north to the main entrance or examine the wall further east?""",
        "room_cleared_actions": [{
            "move": {
                "north": ["Continue through the entrance and move north.", "A1"],
                "east": ["Walk over and investigate the east wall.", "S1"],
            }
        }],
        "actions": [
            {
                "perception": {
                    "DC": 30,
                    "skill_success": ["""You notice some strange markings on the wall to the east. You walk up close to the wall with the markings. You swear these markings weren't here before.""", "room_cleared"],
                    "skill_fail": """You see nothing out of the ordinary. Steel your wits; it’s time to go in!""",
                }
            },
            {
                "move": {
                    "North": ["Continue and move north.", "A1"],
                    None: "You can't move that way."
                }
            }]
    },
    # ENTRANCE WITH POTENTIAL SECRET
    {
        "room": "S1",
        "event": "explore",
        "description": """Now that you've noticed the strange markings on the wall, you've noticed that there is a strange shimmer underneath. Perhaps there is something the runic markings are hiding on this wall?\nDo you simply ignore the markings and continue forward or investigate further?""",
        "room_cleared": False,
        "room_cleared_description": """You've uncovered the illusion behind the wall markings. Do you plan to move into this eastern wall or go north through the tunnel entrance.""",
        "room_cleared_actions": [{
            "move": {
                "north": ["Ignore the markings and continue to move north.", "A1"],
                "east": ["You continue to move east and go through eastern wall.", "S2"]
            },
        }],
        "actions": [
            {
                "perception": {
                    "DC": 0,
                    "skill_success": """You've already investigated the markings... Try something else instead."""
                }
            },
            {
                "detect magic": {
                    "DC": 25,
                    "skill_success": ["""You identify the carvings as a seal for some kind of illusion spell. You trace over the carvings and undo the magical seal. You can now proceed east.""", "room_cleared"],
                    "skill_fail": """The carvings are magical, but you aren't sure from which magic school they're from. Best to tread carefully."""
                }
            },
            {
                "throw": {
                    "DC": 0,
                    "skill_success": """You grab a rock and throw it at the wall. Congrats, you just threw a rock at a wall."""
                }
            },
            {
                "brute force": {
                    "DC": 0,
                    "skill_success": """You hit the wall, as your weapon phases through it. You try to walk forward but bounce off the wall. You wonder if there's another angle you can take or if you're just wasting your time."""
                }
            },
            {
                "cast spell": {
                    "DC": 0,
                    "skill_success": """You cast a spell at the wall. The carvings glow as they absorb your magic harmlessly. You wonder if there's another approach you can take or if you should even bother."""
                }
            },
            {
                "manipulate": {
                    "DC": 0,
                    "skill_success": ["""You touch the carvings and find your finger tracing along the symbols. They grow bright and dissipate. Soon the illusion of a wall begins to disappear. Now you can traverse into this unconventional opening.""", "room_cleared"]
                }
            },
            {
                "move": {
                    "North": ["Ignore the markings and continue to move north.", "A1"],
                    None: "You can't move that way."
                }
            }]
    },
    # SPIKE TRAP ROOM
    {
        "room": "A1",
        "event": "hazard",
        "description": """You walk along the corridor, and the tiles seem to have various patterns on the floor. A few tiles on the wall and floor are marked with patterns.\nYou can see further that there is a passage to the north and to the east.""",
        "room_cleared_description": """You've already been through this room, you may walk north or east.""",
        "room_cleared": False,
        "room_cleared_actions": [{
            "move": {
                "north": ["You continue to move north.", "B1"],
                "east": ["You continue to move east.", "A2"]
            }
        }],
        "actions": [
            {
                "perception": {
                    "DC": 20,
                    "skill_success": """A few of the tiles look odd. You instantly recognize it as a pressure plate trap.""",
                    "skill_fail": """Other than having a few inscriptions on the walls and floor, you don't notice anything odd.""",
                    "crit_fail": ["""While inspecting, you accidentally trigger one of the pressure plates.""",
                                  "trigger_hazard"]
                }
            },
            {
                "disable": {
                    "DC": 18,
                    "skill_success": ["""You safely disarm the trap with your Lockpick. Good thing you've been practicing. The tiles shift down harmlessly.""", "room_cleared"],
                    "skill_fail": ["""You trigger the trap, as arrows shoot across the room.""",
                                   "trigger_hazard"]
                }
            },
            {
                "jump": {
                    "DC": 24,
                    "skill_success": ["""With a running start, you leap over the tiles without triggering it.""", "room_cleared"],
                    "skill_fail": ["""You misjudge your jump, triggering the trap as arrows shoot across the room.""",
                                   "trigger_hazard"]
                }
            },
            {
                "throw": {
                    "DC": 22,
                    "skill_success": ["""You pick up a loose stone and toss it onto the tiles. You safely trigger the trap as arrows shoot across the room.""", "room_cleared"],
                    "skill_fail": ["""You throw an item onto the pressure plate, but it isn't heavy enough to activate it. You confidently walk over it and trigger the trap, as arrows shoot across the room.""",
                                   "trigger_hazard"]
                }
            },
            {
                "attacking": {
                    "DC": 22,
                    "skill_success": ["""With precision, you strike the pressure plate with your weapon, triggering the trap from a safe distance. Arrows fly across the room as you narrowly dodge them.""", "room_cleared"],
                    "skill_fail": ["""You attempt to hit the pressure plate from a safe distance. However, when you hit the plate, you were too close. You get caught in a flurry of arrows across the room.""",
                                   "trigger_hazard"]
                }
            },
            {
                "cast spell": {
                    "DC": 22,
                    "skill_success": ["""Using your wits, you cast a spell from a safe distance. You trigger the trap as arrows fly across the room.""", "room_cleared"],
                    "skill_fail": ["""Thinking you're clever, you cast a spell from a safe distance at the tiles. You didn't realize how weak your spell was as you walked across the tiles that triggered a flurry of arrows.""",
                                   "trigger_hazard"]
                }
            },
            {
                "move": {
                    "DC": 0,
                    "skill_success": "You can't move yet until you've cleared the room.",
                }
            }]
    },
    # GIANT RAT ROOM
    {
        "room": "A2",
        "event": "combat",
        "monster": "Giant Rat",
        "description": """You walk down the tunnel as the darkness grows deeper. You hear a scampering on the floor followed by sharp screeches. After being through many dark caves before, you instantly recognize the sounds. It's a Giant Rat. Think quickly.""",
        "room_cleared_description": """You've already been through this room, you may walk east or west.""",
        "room_cleared": False,
        "room_cleared_actions": [{
            "move": {
                "east": ["You continue to move east.", "A3"],
                "west": ["You continue to move west.", "A1"]
            }
        }],
        "actions": [
            {
                "perception": {
                    "DC": 20,
                    "skill_success": ["""You notice the Giant Rat has a limp on its back left paw; you can use this to your advantage in combat. [Gain +2 to attack rolls]""", "trigger_combat", "atk_roll_bonus_2"],
                    "skill_fail": """You don't notice anything peculiar about this rat, other than him being a giant rat."""
                }
            },
            {
                "stealth": {
                    "DC": 22,
                    "skill_success": ["""Like a shadow, you slink into the darkest crevices in the cavern, slowing your breath and obscuring your presence.\nWhen the rat comes near, you will be ready to attack with utmost precision [+2 to attack rolls]""", "atk_roll_bonus_2"],
                    "skill_fail": ["""You attempt to hide and loudly kick a loose rock. Its movement ricochets in the tunnel as the rat turns to face you, ready for combat.""", "trigger_combat"]
                }
            },
            {
                "animal handling": {
                    "DC": 24,
                    "skill_success": ["""Surprisingly, you manage to soothe the filthy creature's heart. Perhaps its old days of being a small rat resurface in its mind. It now acts very friendly and docile with you, deciding to befriend you. To show its gratitude, it uncovers a hidden treasure buried in the ground. You gain a torch, rope, and a letter.""", "room_cleared", "friendly"],
                    "skill_fail": ["""Your attempts to communicate or pet the rat fall flat, aggravating it further. The Giant Rat grows even more hostile. It bares its teeth and is ready for combat.""", "trigger_combat"]
                }
            },
            {
                "throw": {
                    "DC": 18,
                    "skill_success": ["""You hurl a loose pebble, distracting the Giant Rat momentarily and giving you an advantage in combat. [Gain +2 to attack rolls]""", "atk_roll_bonus_2"],
                    "skill_fail": ["""You throw a loose pebble attempting to distract the rat, instead you only draw attention to yourself. The rat turns towards you and bares its teeth ready for combat.""", "trigger_combat"]
                }
            },
            {
                "intimidate": {
                    "DC": 20,
                    "skill_success": ["""With an intimidating glare, you strike fear into the Giant Rat. It cowers in fear, unable to move [+4 attack]""", "atk_roll_bonus_4"],
                    "skill_fail": ["""The rat can't even tell you were trying to intimidate it. It lowers its stance, ready to attack.""", "trigger_combat"]
                }
            },
            {
                "play dead": {
                    "DC": 24,
                    "skill_success": ["""You collapse to the ground, feigning death. The rat comes over to sniff you, and once it assumes you're dead, it turns to leave. You have the opportunity to strike while its guard is down [+4 to attack]""", "atk_roll_bonus_4"],
                    "skill_fail": ["""You try to play dead, but it's not very convincing. The Giant Rat still thinks you're a threat and is ready to attack.""", "trigger_combat"]
                }
            },
            {
                "attacking": {
                    "DC": 0,
                    "skill_success": ["You raise your weapon, ready to attack", "trigger_combat"]
                }
            },
            {
                "cast spell": {
                    "DC": 0,
                    "skill_success": ["You steady your hands, ready to attack", "trigger_combat"]
                }
            },
            {
                "perform": {
                    "DC": 22,
                    "skill_success": ["""Your melody fills the cavern. The Giant Rat lowers its guard, completely enamored with your song. It seems friendly and no longer interested in attacking you. To show its gratitude, it uncovers a hidden treasure buried in the ground. You gain a torch, rope, and a letter.""", "room_cleared", "friendly"],
                    "skill_fail": ["""Your melody falls flat, and the Giant Rat, in its irritation, bares its teeth ready to fight you.""", "trigger_combat"]
                }
            },
            {
                "move": {
                    "DC": 0,
                    "skill_success": "You can't move yet until you've cleared the room.",
                }
            }]
    }
]


class CompendiumRoom:
    def __init__(self, room_data):
        self.room_id = room_data["room"]
        self.event = room_data["event"]
        self.description = room_data["description"]

        self.room_cleared = room_data.get("room_cleared", False)
        self.room_cleared_description = room_data.get(
            "room_cleared_description", None)
        self.room_cleared_actions = room_data.get("room_cleared_actions", [])
        self.actions = room_data.get("actions", [])

    def __str__(self):
        return f"Room ID: {self.room_id}\nEvent: {self.event}\nDescription: {self.description}\n"


compendium_rooms = [CompendiumRoom(room_data)
                    for room_data in compendium_rooms]

room_names_dict = {}

for index, room in enumerate(compendium_rooms):
    room_names_dict[room.room_id] = index


# print("")
# print("Entrance")
# print("Room ID:", compendium_rooms[0].room_id)
# print("Event:", compendium_rooms[0].event)
# print(compendium_rooms[0].description)
# print("Perception DC:", compendium_rooms[0].actions[0]["perception"]["DC"])
# print("Perception Skill Success:",
#       compendium_rooms[0].actions[0]["perception"]["skill_success"][0])
# print("Yes?:",
#       compendium_rooms[0].actions[0]["perception"]["skill_success"][1])
# print("Perception Skill Fail:",
#       compendium_rooms[0].actions[0]["perception"]["skill_fail"])
# print(room_names_dict)

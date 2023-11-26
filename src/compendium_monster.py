

compendium_monster = [
    {
        "id": 1,
        "name": "Giant Rat",
        "level": 1,
        "lore": [{"lore_dc": 11, "type": "wis"}],
        "attacks": [
            {
                "name": "Jaws",
                "atk_roll": 6,
                "dmg_roll": [1, 6],
                "atk_success": "The Giant Rat lunges out at you with a vicious bite, sinking its teeth into you.",
                "atk_fail": "The Giant Rat lunges out at you, missing. As it ferociously snaps at the air."
            }
        ],
        "loot": ["rope", "gold"]
    },
    {
        "id": 2,
        "name": "Kobold",
        "level": 1,
        "lore": [{"lore_dc": 13, "type": "int"}],
        "AC": 18,
        "HP": 16,
        "attacks": [
            {
                "name": "Shortsword",
                "atk_roll": 9,
                "dmg_roll": [1, 8],
                "atk_success": "The Kobold swings its shortsword with precision, landing a solid blow.",
                "atk_fail": "The Kobold's attack misses as it barely grazes your body."
            }
        ],
        "loot": [
            "Playing Cards",
            "25 gold",
            "Lockpick",
            "Torch"
        ]
    },
    {
        "id": 3,
        "name": "Shadow",
        "level": 4,
        "lore": [{"lore_dc": 17, "type": "Wisdom"}],
        "AC": 20,
        "HP": 30,
        "attacks": [
            {
                "name": "Shadow Hand",
                "atk_roll": 15,
                "dmg_roll": [2, 6, 3],
                "atk_success": "The Shadow swipes at you with its shadow hand. Tendrils phase through your skin as you take damage.",
                "atk_fail": "You shudder as the Shadow reaches out for you with its shadow hand. It overestimates and misses."
            }
        ],
        "loot": []
    },
    {
        "id": 4,
        "name": "Luminous Ooze",
        "level": 4,
        "lore": [{"lore_dc": 17, "type": "int"}],
        "AC": 11,
        "HP": 50,
        "attacks": [
            {
                "name": "Psuedopod",
                "stk_roll": 13,
                "dmg_roll": [2, 8, 5],
                "atk_success": "The ooze extends its pseudopod and strikes with blinding speed, dealing a devastating blow.",
                "atk_fail": "You successfully block the ooze's pseudopod."
            }
        ],
        "special_attacks": [
            [
                {
                    "name": "Light Up",
                    "description": "The ooze glows with blinding brightness. You try to resist the blinding light.",
                    "DC": 21,
                    "save": "fortitude",
                    "atk_success": "You are unaffected by the blinding light.",
                    "atk_fail": "You are frazzled and can't see properly. Take a -4 to your next attack roll."
                }
            ]
        ],
        "loot": ["5 gold"]
    },
    {
        "id": 5,
        "name": "Skeletal Mage",
        "level": 5,
        "lore": [{"lore_dc": 18, "type": "int"}],
        "AC": 16,
        "HP": 50,
        "attacks": [
            {
                "name": "Claw",
                "atk_roll": 11,
                "dmg_roll": [2, 8, 2],
                "atk_success": "The Skeletal Mage's bony claws strike and tear into your flesh. You wince in pain and take damage.",
                "atk_fail": "You avoid the Skeletal Mage's claws, avoiding harm."
            },
            {
                "name": "Ray of Frost",
                "atk_roll": 14,
                "dmg_roll": [3, 4, 4],
                "atk_success": "The Skeletal Mage's hands become enveloped in cold and it shoots you with an icy ray. You grit your teeth as you take cold damage.",
                "atk_fail": "The Skeletal Mage's hands become enveloped in cold and it shoots you, but you narrowly dodge out of the way."
            },
            {
                "name": "Burning Hands",
                "atk_roll": 14,
                "dmg_roll": [4, 6],
                "atk_success": "The Skeletal Mage unleashes a burst of searing flames that engulf you. You scream in agony as you take fire damage.",
                "atk_fail": "You swiftly move out of the way of the Skeletal Mage's fiery onslaught, with it only singeing a bit of hair."
            }
        ],
        "loot": ["20 gold", "Mana Potion Greater", "Healing Potion Minor", "Translation Book", "Letter"]
    },
    {
        "id": 6,
        "name": "Harpy Skeleton",
        "level": 5,
        "lore": [{"lore_dc": 18, "type": "wis"}],
        "AC": 16,
        "HP": 50,
        "attacks": [
            {
                "name": "Talon",
                "Attack Roll": 15,
                "Damage Roll": [2, 6, 7],
                "Hit Success": "The Harpy Skeleton's sharp talons dig into your flesh, as you wince in pain.",
                "Hit Fail": "You avoid the Harpy Skeleton's talons, avoiding harm."
            },
            {
                "name": "Club",
                "Attack Roll": 15,
                "Damage Roll": [1, 6, 7],
                "Hit Success": "The Skeleton Harpy strikes you with its club, delivering a solid blow.",
                "Hit Fail": "The Skeleton Harpy swings its club in the air and clumsily misses you."
            }],
        "special_attacks": [
            [
                {
                    "name": "Shriek",
                    "description": "The Harpy Skeleton emits an unearthly, bone-chilling scream.",
                    "DC": 24,
                    "save": "fortitude",
                    "damage": [4, 10],
                    "atk_success": "You are able to push through the disorientation and keep fighting.",
                    "atk_fail": "It pierces your ears causing sharp damage and disorienting you."
                }
            ]
        ],
    },
    {
        "id": 7,
        "name": "Frost Drake",
        "level": 7,
        "lore": [{"lore_dc": 21, "type": "int"}],
        "AC": 25,
        "HP": 110,
        "attacks": [
            {
                "name": "Fangs",
                "atk_roll": 17,
                "dmg_roll": [3, 10, 4],
                "atk_success": "The Frost Drake sinks its fangs into you, dealing a heavy blow.",
                "atk_fail": "The Frost Drake lunges forward with its fangs, but you manage to evade."
            },
            {
                "name": "Tail",
                "atk_roll": 17,
                "dmg_roll": [2, 12, 8],
                "atk_success": "The Frost Drake shifts its weight and lashes out at you with its tail, hitting you with great force.",
                "atk_fail": "The Frost Drake whips its tail through the air. You sidestep and avoid the blow."
            },
        ],
        "special_attacks": [
            [
                {
                    "name": "Frost Breath",
                    "description": "The Frost Drake breathes in a heavy breath, as swirling cold fills its lungs.",
                    "DC": 24,
                    "save": "fortitude",
                    "damage": [7, 6],
                    "atk_success": "You narrowly dodge the Frost Drake's icy frost breath by the skin of your teeth.",
                    "atk_fail": "The Frost Drake breathes out as a chilling frost engulfs you, freezing you down to your core as you take damage."
                }
            ]
        ],
        "loot": ["+150 gp", "Glacial Amulet", "Healing Potion Greater", "Mana Potion Greater"]
    },
    {
        "id": 8,
        "name": "Necromancer Mage",
        "level": 12,
        "lore": [{"lore_dc": 99, "type": "int"}],
        "AC": 32,
        "HP": 150,
        "attacks": [
            {
                "name": "Hundred Moth Caress Scythe",
                "atk_roll": 21,
                "dmg_roll": [4, 6, 5],
                "self_heal": [1, 6, 2],
                "atk_success": "The necromancer swings her scythe at you. A fluttering gust of hundreds of moths' wingbeats fills the air. You feel your life essence drain as her scythe seeps into your bones.",
                "atk_fail": "The necromancer swings her scythe at you. You count your prayers as you feel hundreds of moths' wingbeats slice through the air, missing you."
            },
            {
                "name": "Phantasmal Killer",
                "atk_roll": 21,
                "atk_success": "The necromancer points her scythe at you as an illusion of your worst fear materializes, instilling terror deep within your heart and pain within your soul.",
                "atk_fail": "The necromancer points her scythe at you, but her dark magic falters."
            }
        ],
        "special_attacks": [
            [
                {
                    "name": "Rip the Spirit",
                    "description": "The necromancer reaches her hand out to you and closes it into a fist.",
                    "DC": 30,
                    "save": "will",
                    "damage": [6, 6, 10],
                    "atk_success": "You feel a dark force attempt to tear your soul apart. You resist.",
                    "atk_fail": "You shudder as you feel an eerie force envelop around you. It attempts to rip your very soul from your body, causing immense pain."
                },
                {
                    "name": "Shackled Shadow Bind",
                    "description": "Dark tendrils emerge from the necromancer's scythe, as shadowy minions wrap around you.",
                    "DC": 29,
                    "save": "fortitude",
                    "damage": [3, 8, 7],
                    "atk_success": "You successfully break free from their grasp.",
                    "atk_fail": "The tendrils constrict and suffocat you, dealing substantial damage."
                }
            ]
        ],
        "loot": ["Hundred Moth Caress Scythe", "Necromancer Cloak", "Voidsworn Amulet (drain health from enemies and heal you)", "Book of Shadows", "Haunted Mirror (inspect to see necromancer's secrets)", "Crypt Key"]
    }

]


class Monster:
    def __init__(self, monster_data):
        self.id = monster_data["id"]
        self.name = monster_data["name"]
        self.level = monster_data["level"]
        self.lore = monster_data.get("lore", [])
        self.attacks = monster_data.get("attacks", [])
        self.loot = monster_data.get("loot", [])
        self.AC = monster_data.get("AC", None)
        self.HP = monster_data.get("HP", None)
        self.special_attacks = monster_data.get("special_attacks", [])

    def __str__(self):
        return f"Monster ID: {self.id}\nName: {self.name}\nLevel: {self.level}\n"


monsters = [Monster(monster_data) for monster_data in compendium_monster]

# Accessing attributes of the first monster
print("First Monster:")
print("Name:", monsters[0].name)
print("Level:", monsters[0].level)
print("Lore:", monsters[0].lore)
print("Attacks:", monsters[0].attacks)
print("Attacks 1:", monsters[0].attacks[0]["name"])
print("Loot:", monsters[0].loot)

"""
Create a base class for the monster
Class into class for attacks (also include what % of the time a specific move should be used)
Create defs for: take damage, heal, apply_condition, is alive
Create defs to determine which atk the monster used -> then deal damage or apply condition
Special attacks require a DC check, while normal attacks go against player AC
"""

import mechanics
import random


class Monster():
    def __init__(self, name, ac, max_hp, current_hp, level, lore_dc, lore_mod, loot, defeat_text, win_text, attack_list):
        """
        Initialize basic information for a monster
        """
        self.name = name
        self.ac = ac
        self.max_hp = max_hp
        self.level = level
        self.current_hp = current_hp
        self.lore_dc = lore_dc
        self.lore_mod = lore_mod
        self.loot = loot
        self.defeat_text = defeat_text
        self.win_text = win_text

        ### SPECIFIC MONSTER ATTACKS ###
        self.attack_list = attack_list

    def take_damage(self, damage):
        """
        Will make the monster take damage. Will display text whether it is
        near death or died.

        Args:
            damage (int): damage monster took
        """
        self.current_hp -= damage
        mechanics.print_text(mechanics.style_damage(
            self.name, damage, self.current_hp))
        if not self.is_alive():
            mechanics.print_text(
                f"\033[1m\033[38;5;241m{self.defeat_text}\n.\n.\033[0m")
        else:
            if self.current_hp <= (self.max_hp * .1):
                mechanics.print_text(f"{self.name} is looking worse for wear. "
                                     "One strike may be their last.")

    def heal(self, healing):
        """
        Will make the monster take healing. If healing is over their max_hp
        then set to their max_hp

        Args:
            healing (int): the number healed by the monster
        """
        self.current_hp += healing
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        mechanics.print_text(mechanics.style_heal(self.name, healing))

    def is_alive(self) -> bool:
        """
        Check if current enemy is still alive.

        Returns:
            is_alive (bool): whether the characters health exceeds 0
        """
        return self.current_hp > 0

    def event_type(self) -> str:
        """
        Returns the type of event the monster is.

        Returns:
            (str): returns the event type
        """
        return "combat"

    def get_name(self) -> str:
        """
        Gets the name of the monster.

        Returns:
            (str): the name of the monster
        """
        return self.name

    def select_move(self) -> str:
        """
        Determines the current moveset the monster has. It will randomly
        select which move will be returned based on the frequency that the
        attack should occur.

        Returns:
            (str): the selected move for the monster
        """
        move_dict = {}
        for move_name, attack in self.attack_list.items():
            move_dict[move_name] = attack
        if not move_dict:
            return None

        sorted_moves = sorted(
            move_dict.items(), key=lambda x: x[1].frequency, reverse=True)

        selected_move = None
        random_value = random.random()  # use rand to see if move was selected

        for move_name, attack in sorted_moves:
            if attack.frequency[0] <= random_value <= attack.frequency[1]:
                selected_move = (move_name, attack)
                break
        return selected_move


class Attacks(Monster):
    def __init__(self, name, frequency, atk_roll, dc, dc_type, apply_condition_first, apply_condition_second,
                 num_of_dice: int, dice_size: int, add_dmg, success_text, fail_text, self_heal_num_dice,
                 self_heal_dice_size, self_heal_mod) -> None:
        self.name = name
        self.frequency = frequency
        self.atk_roll = atk_roll
        self.dc = dc
        self.dc_type = dc_type
        self.apply_condition_first = apply_condition_first
        self.apply_condition_second = apply_condition_second
        self.num_of_dice = num_of_dice
        self.dice_size = dice_size
        self.add_dmg = add_dmg
        self.success_text = success_text
        self.fail_text = fail_text
        self.self_heal_num_dice = self_heal_num_dice
        self.self_heal_dice_size = self_heal_dice_size
        self.self_heal_mod = self_heal_mod

    def standard_damage_roll(self, monster, char_ac=24) -> int:
        """
        Based on a standard attack, determine the amount of damage inflicted.

        Args:
            monster (class): the base monster information
            char_ac (int): the ac of the player character

        Returns:
            damage (int): the amount of damage inflicted
        """
        roll = mechanics.calculate_enemy_attack_damage_dealt(
            self.num_of_dice, self.dice_size, self.add_dmg, self.atk_roll, char_ac)
        if self.hit_or_miss(roll):
            mechanics.print_text(self.success_text)
            mechanics.print_text(
                f"Using \033[1m{self.name}\033[0m, \033[1m{monster.name}\033[0m dealt "
                f"\033[1m{roll} damage\033[0m to you")
        else:
            mechanics.print_text(self.fail_text)
        return roll

    def saving_throw_damage_roll(self, monster, char_roll=21, nat_one=False, nat_twenty=False) -> int:
        """
        Based on a special attack, determine the amount of damage inflicted.

        Args:
            monster (class): the base monster information
            char_roll (int): the saving throw roll of the player character
            nat_one (bool): was the player roll a nat 1
            nat_twenty (bool): was the player roll a nat 20

        Returns:
            damage (int): the amount of damage inflicted
        """
        roll = mechanics.calculate_enemy_saving_throw_damage(
            self.num_of_dice, self.dice_size, self.add_dmg, self.atk_roll,
            self.dc, char_roll, nat_one, nat_twenty)
        if self.hit_or_miss(roll):
            mechanics.print_text(self.success_text)
            mechanics.print_text(
                f"Using \033[1m{self.name}\033[0m, \033[1m{monster.name}\033[0m dealt "
                f"\033[1m{roll} damage\033[0m to you")
        else:
            mechanics.print_text(self.fail_text)
        return roll

    def can_heal(self) -> bool:
        """
        Returns if the attack can also heal

        Return:
            can_heal (bool): if the attack can heal or not
        """
        return self.self_heal_dice_size > 0 or self.self_heal_mod > 0

    def apply_healing(self, monster):
        """
        determine the amount of health the monster healed up. Will prompt to heal them.

        Args:
            monster (class): the base monster information
        """
        healing = mechanics.roll_dice(
            self.self_heal_num_dice, self.self_heal_dice_size)
        healing = mechanics.calculate_damage_dealt(healing)
        monster.heal(healing)

    def deal_condition(self):
        """
        Determines if the attack inflicts a condition onto the player.

        Returns:
            conditions (dict): a list of conditions it inflicted
        """
        conditions = {"blinded": False, "dazzled": False, "doomed": False, "drained": False,
                      "fatigued": False, "fascinated": False, "flat_footed": False, "frightened": False, "prone": False}
        if self.apply_condition_first[0] in conditions:
            conditions[self.apply_condition_first[0]] = True
        if self.apply_condition_second[0] in conditions:
            conditions[self.apply_condition_second[0]] = True

        return conditions

    def hit_or_miss(self, damage=20) -> bool:
        """
        Determines if the attack hit or missed

        Args:
            damage (int): damage that the monster inflicted

        Returns:
            (bool): if the attack hit or missed
        """
        return damage != 0


test_monster = Monster(
    name="",
    ac=0,
    max_hp=0,
    current_hp=0,
    level=0,
    lore_dc=0,
    lore_mod="int",
    loot={},
    defeat_text="",
    win_text="",
    attack_list={
        "first": Attacks(
            name="",
            frequency=1,
            atk_roll=0,
            dc=0,
            dc_type=None,
            apply_condition_first=None,
            apply_condition_second=None,
            num_of_dice=0,
            dice_size=0,
            add_dmg=0,
            success_text="yes",
            fail_text="no",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        )
    }
)

monster_rat = Monster(
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
        "jaws": Attacks(
            name="jaws",
            frequency=1,
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
monster_kobold = Monster(
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
        "shortsword": Attacks(
            name="Shortsword",
            frequency=1,
            atk_roll=9,
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

monster_shadow = Monster(
    name="Shadow",
    ac=22,
    max_hp=35,
    current_hp=35,
    level=4,
    lore_dc=17,
    lore_mod="wis",
    loot={},
    defeat_text="The shadow shakes, falling to the floor and leaving behind a black ooze.",
    win_text="The Shadow shakes with glee as a shrill laughter escapes from it.",
    attack_list={
        "shadow claws": Attacks(
            name="Shadow Claws",
            frequency=[0, 0.7],
            atk_roll=15,
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
        "steal shadow": Attacks(
            name="Steal Shadow",
            frequency=[0.71, 1],
            atk_roll=0,
            dc=27,
            dc_type="reflex",
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=3,
            dice_size=4,
            add_dmg=6,
            success_text="The Shadow grasps a sliver of your shadow and steals it.",
            fail_text="You shudder as the Shadow reaches out for your shadow as you "
            "adeptly dodge it.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        )
    }
)

monster_drake = Monster(
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
    "by the pain you've inflected. It flaps its wings in a desperate big to keep "
    "itself up. And as the light in it's eyes dims, it slams to the floor in defeat.",
    win_text="The Frost Drake laughs in utter triamph, it walks over to "
    "it's mound of gold with a smile on it's face.",
    attack_list={
        "fangs": Attacks(
            name="Fangs",
            frequency=[0, 0.35],
            atk_roll=20,
            dc=0,
            dc_type=None,
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=3,
            dice_size=10,
            add_dmg=4,
            success_text="The Frost Drake sinks its fangs into you, dealing a heavy blow.",
            fail_text="The Frost Drake lunges forward with its fangs, but you manage to evade.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        ),
        "tail whip": Attacks(
            name="Tail Whip",
            frequency=[0.36, 0.79],
            atk_roll=21,
            dc=0,
            dc_type=None,
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=2,
            dice_size=12,
            add_dmg=8,
            success_text="The Frost Drake shifts its weight and lashes out at you with "
            "its heavy tail, hitting you with great force.",
            fail_text="The Frost Drake whips its tail through the air. You "
            "sidestep and avoid the blow.",
            self_heal_num_dice=0,
            self_heal_dice_size=0,
            self_heal_mod=0
        ),
        "frost breath": Attacks(
            name="Frost Breath",
            frequency=[0.8, 1],
            atk_roll=0,
            dc=32,
            dc_type="fortitude",
            apply_condition_first="",
            apply_condition_second="",
            num_of_dice=7,
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
        "HP": 20,
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
        "AC": 22,
        "HP": 35,
        "attacks": [
            {
                "name": "Shadow Hand",
                "atk_roll": 15,
                "dmg_roll": [2, 6, 4],
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
                "atk_roll": 13,
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
        "loot": ["20 gold", "Mana Potion Greater", "Healing Potion Minor", "Book"]
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
                "atk_roll": 23,
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

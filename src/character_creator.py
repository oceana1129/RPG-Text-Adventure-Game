"""
    Create the character that the player will  use.
"""
import mechanics


class Weapon:
    def __init__(self, name, typing, job, num_of_dice, damage_size, add_dmg, mana_cost=0, heals=False, cooldown_duration=False, cooldown_counter=False):
        """
        Initializes the attack or weapon used by the player character
        """
        self.name = name
        self.typing = typing
        self.job = job
        self.num_of_dice = num_of_dice
        self.damage_size = damage_size
        self.add_dmg = add_dmg
        self.mana_cost = mana_cost
        self.heals = heals
        self.cooldown_duration = cooldown_duration
        self.cooldown_counter = cooldown_counter

    def attempt(self) -> str:
        """
        Returns a message when player attempts to use this attack

        Returns:
            message (str): message when player uses this attack
        """
        return f"You attempt to use {self.name}."

    def you_hit(self) -> str:
        """
        Returns a message when player hits

        Returns:
            message (str): message when player hits
        """
        return "You hit."

    def you_missed(self) -> str:
        """
        Returns a message when player misses

        Returns:
            message (str): message when player misses
        """
        return "You missed the"

    def attack_roll(self) -> tuple:
        """
        Make an attack roll with the weapon.

        Returns:
            roll (tuple): A tuple with base roll[0], total roll[1], nat 1 bool[2], and nat 20 bool[3]
        """
        return mechanics.roll_attack_or_spell()

    def damage_roll(self, degree_of_success=1, enemy="monster") -> int:
        """
        Will determine the amount of damage the character inflicted onto
        the monster. Will display a success or fail message for hitting
        the monster.

        Args:
            degree_of_success (int): the degree of success from the hit
            enemy (str): the name of the monster

        Returns:
            damage (int): the amount of damage inflicted
        """
        modifer_based_on_success = {-1: 0, 0: 0, 1: 1, 2: 2}
        roll = mechanics.roll_dice(self.num_of_dice, self.damage_size)
        damage = mechanics.calculate_damage_dealt(roll, self.add_dmg)

        if degree_of_success == 2:
            mechanics.print_text("It's a crit hit! Damage Doubled")
        damage = damage * modifer_based_on_success[degree_of_success]
        if self.hit_or_miss(damage):
            mechanics.print_text(self.you_hit())
            mechanics.print_text(
                f"You used \033[1m{self.name}\033[0m and rolled "
                f"\033[1m{damage}\033[0m total damage.")
        else:
            mechanics.print_text(f"{self.you_missed()} {enemy}")

        return damage

    def consume_mana(self, character):
        """
        Have the player character consume mana from their mana pool.
        Will reduce their mana by mana_cost.

        Args:
            character (class): the current player character
        """
        if self.mana_cost > 0:
            if character.mp >= self.mana_cost:
                character.mp -= self.mana_cost
                mechanics.print_text(mechanics.style_mana(
                    self.mana_cost, character.mp))
            else:
                mechanics.print_text(mechanics.style_mana(
                    self.mana_cost, character.mp))

    def apply_healing(self, character):
        """
        If the attack applies healing, then it will heal the character.

        Args:
            character (class): the current player character
        """
        if self.heals:
            roll = mechanics.roll_dice(self.num_of_dice, self.damage_size)
            healing = mechanics.calculate_damage_dealt(roll, self.add_dmg)
            character.heal(healing)

    def start_cooldown(self):
        """
        Set the cooldown counter, for the attack, to the maximum duration
        """
        self.cooldown_counter = self.cooldown_duration
        print(
            f"Cooldown Counter has started for {self.name} for {self.cooldown_duration} rounds")

    def reduce_cooldown(self):
        """
        Reduce the cooldown counter by 1 (called at the start of each combat round).
        Used for the specific attack.
        """
        if self.cooldown_counter > 0:
            self.cooldown_counter -= 1
            print(
                f"{self.name} cooldown reduced by 1... {self.cooldown_counter}")

    def can_use(self, character) -> bool:
        """
        Check if the weapon can be used, either:
        cooldown counter is 0
        or mana cost is over or equal to current mana player has

        Args:
            character (class): current player character

        Returns:
            (bool): whether the player can use the action or not
        """
        #
        if self.cooldown_duration > 0:
            return self.cooldown_counter == 0
        if self.mana_cost > 0:
            return character.mp > self.mana_cost
        if self.cooldown_duration == 0:
            return True

    def hit_or_miss(self, damage=20) -> bool:
        """
        Returns if the attack hit or missed.

        Returns:
            (bool): if attack hit or missed
        """
        return damage != 0


class Character:
    # initialize saves
    perception = 3
    fortitude = 3
    reflex = 3
    will = 3

    def __init__(self, chosen_class):
        """
        Initialize the player character with basic information.
        """
        self.character_name = "player"
        self.alignment = ""
        self.level = chosen_class.lvl
        self.location = "A0"

        self.class_name = chosen_class.name
        self.class_main_ability = chosen_class.class_main_ability
        self.class_hitpoints = chosen_class.class_hp
        self.mp = chosen_class.class_mp
        self.melee = chosen_class.attacks["physical"]
        self.spellcaster = chosen_class.attacks["spell"]

        # initialize abilities
        self.str = chosen_class.abilities["str"]
        self.dex = chosen_class.abilities["dex"]
        self.con = chosen_class.abilities["con"]
        self.intell = chosen_class.abilities["intell"]
        self.wis = chosen_class.abilities["wis"]
        self.cha = chosen_class.abilities["cha"]

        # initialize saving throws
        self.perception = chosen_class.saves["perception"]
        self.fortitude = chosen_class.saves["fortitude"]
        self.reflex = chosen_class.saves["reflex"]
        self.will = chosen_class.saves["will"]
        self.ac = chosen_class.saves["ac"]

        # initialize max and current health
        self.max_health = 0
        self.current_health = 0

        # initialize combat actions
        self.actions = chosen_class.actions

        # initialize status conditions
        self.blinded = False
        self.dazzled = False
        self.doomed = False
        self.drained = False
        self.fatigued = False
        self.fascinated = False
        self.flat_footed = False
        self.frightened = False
        self.prone = False

        # bonuses applied during exploration
        self.atk_roll_bonus = 0

        # initialize inventory
        self.inventory = {}

        # calculations upon initializing
        self.calculate_max_health()

    def get_ability_mod(self, ability: str) -> int:
        """
        Get the appropirate ability modifier from the player character

        Args:
            ability (str): the name of the ability

        Returns:
            abilities (int): the modifier for the ability
        """
        abilities = {"str": self.str + 10, "dex": self.dex + 10, "con": self.con + 10,
                     "intell": self.intell + 10, "int": self.intell + 10, "wis": self.wis + 10, "cha": self.cha + 10,
                     "perception": self.perception, "fortitude": self.fortitude,
                     "reflex": self.reflex, "will": self.will}
        if ability in abilities:
            return abilities[ability]
        else:
            raise ValueError(f"Invalid ability: {ability}")

    def calculate_max_health(self) -> int:
        """
        Calculate the characters total max health using their class hitpoints, 
        their current level, and their number of constitution points.
        Also, sets current hit points to max.
        """
        self.max_health = (self.con + self.class_hitpoints) * self.level
        self.current_health = self.max_health

    def get_fighting_actions(self) -> list:
        """
        Get the list of actions the specific player character can use

        Returns:
            fighting_actions (list): the list of fighting actions
        """
        fighting_actions = []
        for action_name in self.actions:
            fighting_actions.append(action_name)
        return fighting_actions

    def character_death(self) -> str:
        """
        Display the character death text

        Returns:
            (str): character death text
        """
        return f"\033[38;5;196m\033[1mEverything goes dark... And you die\033[0m"

    def take_damage(self, damage: int):
        """
        Reduce characters current health by the damage amount inflicted.
        Will display the damage taken and their current health to the user.

        Args:
            damage (int): the amount of damage they took
        """
        self.current_health -= damage
        if not self.is_alive():
            mechanics.print_text(self.character_death())
        else:
            mechanics.print_text(mechanics.style_damage(
                self.character_name, damage, self.current_health))

    def heal(self, healing: int):
        """
        Increases characters current health by the healing amount received.
        Will also display the healing received to the user.

        Args:
            healing (int): the amount of healing a character recieved
        """
        self.current_health += healing
        if self.current_health > self.max_health:  # If healing exceeds current max, set to max
            self.current_health = self.max_health
        mechanics.print_text(mechanics.style_heal(
            self.character_name, healing))

    def restore_mana(self, healing):
        """
        Increases characters current health by the healing amount received.

        Args:
            healing (int): the amount of healing recieved
        """
        physical = ["str", "dex"]
        main_ability = self.class_main_ability
        if player.class_main_ability in physical:
            mechanics.print_text(
                "You can't restore mp since you're not a spellcaster")
        else:
            self.mp += healing
            if self.mp > 50:  # set to max if exceeds
                self.mp = 50
            mechanics.print_text(
                mechanics.style_restore_mana(healing, self.mp))

    # inventory management
    def add_item_to_inventory(self, item, quantity=1):
        """
        Add an item to the character's inventory.

        Args:
            item (str): The name of the item to add
            quantity (int): The quantity of the item to add (default is 1)
        """
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"Added {quantity} {item}(s) to your inventory.")

    def add_loot_to_inventory(self, loot):
        """
        Add loot items to the character's inventory.

        Args:
            loot (dict): contains loot items and their quantities
        """
        for item, quantity in loot.items():
            self.add_item_to_inventory(item, quantity)

    def remove_item_from_inventory(self, item, quantity=1):
        """
        Remove an item from the character's inventory.

        Args:
            item (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove (default is 1).
        """
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                print(f"Removed {quantity} {item}(s) from your inventory.")
                if self.inventory[item] == 0:
                    del self.inventory[item]
            else:
                print(f"You don't have enough {item}(s) in your inventory.")
        else:
            print(f"{item} is not in your inventory.")

    def view_inventory(self):
        """
        Display the contents of the character's inventory.
        """
        if not self.inventory:
            mechanics.print_text("Your inventory is empty.")
        else:
            print("Inventory:")
            for item, quantity in self.inventory.items():
                mechanics.print_text(f"- {item}: {quantity}")

    def use_potion(self, potion_name):
        """
        Allows the user to use a potion from their inventory.
        Depending on the type of potion will determine if the next
        function called is for healing or mana.

        Args:
            potion_name (str): name of the potion consumed
        """
        healing_type = {
            "healing potion lesser": [2, 8, 5],
            "healing potion moderate": [3, 8, 10],
            "healing potion greater": [6, 8, 20]
        }
        mana_type = {
            "mana potion lesser": [2, 8, 5],
            "mana potion moderate": [3, 8, 10]
        }
        if potion_name in self.inventory and self.inventory[potion_name] > 0:
            # Is potion in inventory and one is available?

            if potion_name in healing_type:
                item = healing_type[potion_name]
                rolls = mechanics.roll_dice(item[0], item[1])
                potion_healing = mechanics.calculate_damage_dealt(
                    rolls, item[2])
                self.heal(potion_healing)
            elif potion_name in mana_type:
                item = mana_type[potion_name]
                rolls = mechanics.roll_dice(item[0], item[1])
                potion_healing = mechanics.calculate_damage_dealt(
                    rolls, item[2])
                self.restore_mana(potion_healing)
            self.inventory[potion_name] -= 1
            mechanics.print_text(
                f"You used a {potion_name}")
        else:
            print(f"You don't have any {potion_name} in your inventory")

    # Condition management
    def apply_condition(self, condition):
        """
        Apply status conditions such as frightened, dazzled, etc by setting a bool to True

        Arguments:
            condition (str): the name of the status condition
        """
        if hasattr(self, condition):
            setattr(self, condition, True)

    def remove_condition(self, condition):
        """
        Remove status conditions such as frightened, dazzled, etc by setting a bool to False

        Arguments:
            condition (str): the name of the status condition
        """
        if hasattr(self, condition):
            setattr(self, condition, False)

    def current_conditions(self):
        """
        List out current conditions.
        """
        count = 0
        conditions = ["blinded", "dazzled", "doomed", "drained",
                      "fatigued", "fascinated", "flat_footed", "frightened", "prone"]
        for i in conditions:
            if getattr(self, i):
                count += 1
                mechanics.print_text(f"{i} is active")
        if count == 0:
            mechanics.print_text("No conditions are active")

    def reset_conditions(self):
        """
        Reset all of the conditions the player has.
        """
        self.blinded = False
        self.dazzled = False
        self.doomed = False
        self.drained = False
        self.fatigued = False
        self.fascinated = False
        self.flat_footed = False
        self.frightened = False
        self.prone = False

    def start_round_of_combat(self):
        """
        At the beginning of each round of combat, reduce cooldowns for all weapons
        """
        for action in self.actions.values():
            if action.cooldown_duration > 0:
                action.cooldown_counter = 0

    def apply_cleared_bonus(self, bonus="1 intell"):
        """
        If the room was cleared, and the user encountered a bonus
        then add the appropriate bonus to their stats.
        """
        bonus_parts = bonus.split()
        if len(bonus_parts) == 2:
            try:
                bonus_value = int(bonus_parts[0])
                bonus_attribute = bonus_parts[1]
                if hasattr(self, bonus_attribute):
                    # Apply the bonus directly to the specified attribute
                    setattr(self, bonus_attribute, getattr(
                        self, bonus_attribute) + bonus_value)
                    print(f"Applied +{bonus_value} to {bonus_attribute}")
                else:
                    print(f"Invalid attribute: {bonus_attribute}")
            except ValueError:
                print(f"Invalid bonus value: {bonus_parts[0]}")
        else:
            pass

    def apply_bonus(self, bonus):
        """
        Apply a bonus to the characters attack roll
        """
        if bonus > self.atk_roll_bonus:
            self.atk_roll_bonus = bonus
            print(f"Add +{bonus} to your attack rolls")

    def reset_attack_bonus(self):
        """
        Reset the characters attack bonus.
        """
        self.atk_roll_bonus = 0

    def is_alive(self) -> bool:
        """
        Check if current character is still alive.

        Returns:
            is_alive (bool): whether the characters health exceeds 0
        """
        return self.current_health > 0

    def attack_roll(self) -> tuple:
        """
        Have player make an attack roll... based on their class main ability

        Returns:
            roll (tuple): A tuple with base roll[0], total roll[1], nat 1 bool[2], and nat 20 bool[3].
        """
        physical = ["str", "dex"]
        spell = ["cha", "intell", "wis"]
        main_ability = self.class_main_ability
        ability = self.get_ability_mod(self.class_main_ability)
        if main_ability in physical:
            modifier = self.melee + self.atk_roll_bonus
        else:
            modifier = self.spellcaster + self.atk_roll_bonus
        roll = mechanics.roll_attack_or_spell(modifier)
        mechanics.print_text(
            f"Your \033[1mattack roll\033[0m was \033[1m{roll[1]}\033[0m")
        return roll

    def did_it_hit(self, roll, enemy_ac):
        """
        Determine if the attack hit the enemy.

        Args:
            roll (tuple): the roll and degree of success of the roll
            enemy_ac (int): the enemy armor class

        Returns:
            (int): integer representing degrees of success (-1=crit fail, 0= fail, 1=pass, 2=crit pass).
        """
        return mechanics.degree_of_success(enemy_ac, roll[1], roll[2], roll[3])


class Job:
    def __init__(self, name, lvl, abilities, saves, attacks, class_hp, class_mp, class_main_ability, actions):
        """
        Initialize the character class/job
        """
        self.name = name
        self.lvl = lvl
        self.abilities = abilities
        self.saves = saves
        self.attacks = attacks
        self.class_hp = class_hp
        self.class_mp = class_mp
        self.class_main_ability = class_main_ability
        self.actions = actions


class Fighter(Job):
    def __init__(self):
        abilities = {
            "str": 5,
            "dex": 3,
            "con": 4,
            "intell": 0,
            "wis": 2,
            "cha": 1
        }
        saves = {
            "perception": 10 + 2 + 6,
            "fortitude": 10 + 4 + 6,
            "reflex": 10 + 3 + 4,
            "will": 10 + 2 + 4,
            "ac": 10 + 12 + 6 + 1
        }
        attacks = {
            "physical": 21,
            "spell": 0
        }
        super().__init__(
            name="Fighter",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=10,
            class_mp=0,
            class_main_ability="str",
            actions={
                "punch": Weapon(
                    name="Punch",
                    typing="melee",
                    job="all",
                    num_of_dice=3,
                    damage_size=4,
                    add_dmg=0,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "greatsword": Weapon(
                    name="Greatsword",
                    typing="melee",
                    job="fighter",
                    num_of_dice=2,
                    damage_size=12,
                    add_dmg=7,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "sweeping blade": Weapon(
                    name="Sweeping Blade",
                    typing="melee",
                    job="fighter",
                    num_of_dice=4,
                    damage_size=10,
                    add_dmg=5,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=2,
                    cooldown_counter=False
                ),
                "dazing blow": Weapon(
                    name="Dazing Blow",
                    typing="melee",
                    job="fighter",
                    num_of_dice=5,
                    damage_size=12,
                    add_dmg=5,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=3,
                    cooldown_counter=False
                )}
        )


class Wizard(Job):
    def __init__(self):
        abilities = {
            "str": 0,
            "dex": 4,
            "con": 3,
            "intell": 5,
            "wis": 2,
            "cha": 1
        }
        saves = {
            "perception": 10 + 2 + 4,
            "fortitude": 10 + 3 + 4,
            "reflex": 10 + 4 + 4,
            "will": 10 + 2 + 2,
            "ac": 10 + 12 + 4 + 1
        }
        attacks = {
            "physical": 15,
            "spell": 20
        }
        super().__init__(
            name="Wizard",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=7,
            class_mp=50,
            class_main_ability="intell",
            actions={
                "punch": Weapon(
                    name="Punch",
                    typing="melee",
                    job="all",
                    num_of_dice=3,
                    damage_size=4,
                    add_dmg=0,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "electric arc": Weapon(
                    name="Electric Arc",
                    typing="spell",
                    job="wizard",
                    num_of_dice=3,
                    damage_size=4,
                    add_dmg=4,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "magic missile": Weapon(
                    name="Magic Missile",
                    typing="spell",
                    job="wizard",
                    num_of_dice=5,
                    damage_size=4,
                    add_dmg=5,
                    mana_cost=2,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "fireball": Weapon(
                    name="Fireball",
                    typing="spell",
                    job="wizard",
                    num_of_dice=8,
                    damage_size=6,
                    add_dmg=0,
                    mana_cost=3,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "elemental storm": Weapon(
                    name="Elemental Storm",
                    typing="spell",
                    job="wizard",
                    num_of_dice=12,
                    damage_size=6,
                    add_dmg=0,
                    mana_cost=5,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                )

            }
        )


class Bard(Job):
    def __init__(self):
        abilities = {
            "str": 0,
            "dex": 4,
            "con": 3,
            "intell": 1,
            "wis": 2,
            "cha": 5
        }
        saves = {
            "perception": 10 + 2 + 6,
            "fortitude": 10 + 3 + 6,
            "reflex": 10 + 4 + 4,
            "will": 10 + 2 + 6,
            "ac": 10 + 12 + 4 + 1
        }
        attacks = {
            "physical": 15,
            "spell": 20
        }
        super().__init__(
            name="Bard",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=8,
            class_mp=50,
            class_main_ability="cha",
            actions={
                "punch": Weapon(
                    name="Punch",
                    typing="melee",
                    job="all",
                    num_of_dice=3,
                    damage_size=4,
                    add_dmg=0,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "haunting hymm": Weapon(
                    name="Haunting Hymm",
                    typing="spell",
                    job="bard",
                    num_of_dice=4,
                    damage_size=6,
                    add_dmg=5,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "sooth": Weapon(
                    name="Sooth",
                    typing="spell",
                    job="bard",
                    num_of_dice=2,
                    damage_size=10,
                    add_dmg=8,
                    mana_cost=2,
                    heals=True,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "sound burst": Weapon(
                    name="Sound Burst",
                    typing="spell",
                    job="bard",
                    num_of_dice=3,
                    damage_size=10,
                    add_dmg=8,
                    mana_cost=3,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "painful vibrations": Weapon(
                    name="Painful Vibrations",
                    typing="spell",
                    job="bard",
                    num_of_dice=10,
                    damage_size=6,
                    add_dmg=2,
                    mana_cost=5,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),

            }
        )


class Rogue(Job):
    def __init__(self):
        abilities = {
            "str": 0,
            "dex": 5,
            "con": 4,
            "intell": 2,
            "wis": 1,
            "cha": 3
        }
        saves = {
            "perception": 10 + 2 + 4,
            "fortitude": 10 + 4 + 6,
            "reflex": 10 + 5 + 4,
            "will": 10 + 1 + 6,
            "ac": 10 + 12 + 5 + 1
        }
        attacks = {
            "physical": 21,
            "spell": 0
        }
        super().__init__(
            name="Rogue",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=8,
            class_mp=0,
            class_main_ability="dex",
            actions={
                "punch": Weapon(
                    name="Punch",
                    typing="melee",
                    job="all",
                    num_of_dice=3,
                    damage_size=4,
                    add_dmg=0,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "dagger": Weapon(
                    name="Dagger",
                    typing="melee",
                    job="rogue",
                    num_of_dice=5,
                    damage_size=4,
                    add_dmg=8,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=False,
                    cooldown_counter=False
                ),
                "sneak attack": Weapon(
                    name="Sneak Attack",
                    typing="melee",
                    job="rogue",
                    num_of_dice=8,
                    damage_size=4,
                    add_dmg=10,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=2,
                    cooldown_counter=0
                ),
                "backstab": Weapon(
                    name="Backstab",
                    typing="melee",
                    job="rogue",
                    num_of_dice=8,
                    damage_size=6,
                    add_dmg=12,
                    mana_cost=False,
                    heals=False,
                    cooldown_duration=3,
                    cooldown_counter=0
                ),

            }
        )


player = Character(Bard())

import random
import mechanics


class Animal:
    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")
        print("wow")


# inherit from Animal
class Dog(Animal):
    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)


# create an object of the subclass
labrador = Dog()
labrador.name = "Rohu"
# labrador.eat()
# labrador.display()

expertise = {
    "trained": 2,
    "expert": 4,
    "master": 6,
    "legendary": 8,
    "potency": 2
}


class Old_Character:
    #     # player specific details
    #     character_name = ""
    #     alignment = ""
    #     level = 1

    #     # initialize saves
    #     perception = 3
    #     fortitude = 3
    #     reflex = 3
    #     will = 3

    #     def __init__(self, class_name, class_main_ability,
    #                  class_hitpoints, melee, spellcaster, str, dex, con, intell, wis, cha):
    #         self.class_name = class_name
    #         self.class_main_ability = class_main_ability
    #         self.class_hitpoints = class_hitpoints
    #         self.melee = melee
    #         self.spellcaster = spellcaster

    #         # initialize abilities
    #         self.str = str
    #         self.dex = dex
    #         self.con = con
    #         self.intell = intell
    #         self.wis = wis
    #         self.cha = cha

    #         # initialize max and current health
    #         self.max_health = 0
    #         self.current_health = 0

    #         # initialize status conditions
    #         self.blinded = False
    #         self.dazzled = False
    #         self.doomed = False
    #         self.drained = False
    #         self.fatigued = False
    #         self.fascinated = False
    #         self.flat_footed = False
    #         self.frightened = False
    #         self.prone = False

    #         # calculations upon initializing
    #         self.calculate_max_health()

    #     def calculate_max_health(self) -> int:
    #         """
    #         Calculate the characters total max health using their class hitpoints,
    #         their current level, and their number of constitution points.
    #         Also, sets current hit points to max.
    #         """
    #         self.max_health = self.con + self.class_hitpoints * self.level
    #         self.current_health = self.max_health

    #     def take_damage(self, damage_amount):
    #         """
    #         Reduce characters current health by the damage amount inflicted.
    #         """
    #         self.current_health -= damage_amount
    #         if self.current_health <= 0:  # Check if the character is still alive
    #             self.current_health = 0
    #             print(f"{self.character_name} has been defeated!")

    #     def heal(self, healing):
    #         """
    #         Increases characters current health by the healing amount received.
    #         """
    #         self.current_health += healing
    #         if self.current_health > self.max_health:  # If healing exceeds current max, set to max
    #             self.current_health = self.max_health

    #     def apply_condition(self, condition):
    #         """
    #         Apply status conditions such as frightened, dazzled, etc by setting a bool to True

    #         Arguments:
    #             condition (str): the name of the status condition
    #         """
    #         if hasattr(self, condition):
    #             setattr(self, condition, True)

    #     def remove_condition(self, condition):
    #         """
    #         Remove status conditions such as frightened, dazzled, etc by setting a bool to False

    #         Arguments:
    #             condition (str): the name of the status condition
    #         """
    #         if hasattr(self, condition):
    #             setattr(self, condition, False)

    #     def is_alive(self) -> bool:
    #         """
    #         Check if current character is still alive.

    #         Returns:
    #             is_alive (bool): whether the characters health exceeds 0
    #         """
    #         return self.current_health > 0
    pass


class Character:
    # initialize saves
    perception = 3
    fortitude = 3
    reflex = 3
    will = 3

    def __init__(self, chosen_class):
        self.character_name = ""
        self.alignment = ""
        self.level = chosen_class.lvl

        self.class_name = chosen_class.name
        self.class_main_ability = chosen_class.class_main_ability
        self.class_hitpoints = chosen_class.class_hp
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

        # initialize max and current health
        self.max_health = 0
        self.current_health = 0

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

        # calculations upon initializing
        self.calculate_max_health()

    def calculate_max_health(self) -> int:
        """
        Calculate the characters total max health using their class hitpoints, 
        their current level, and their number of constitution points.
        Also, sets current hit points to max.
        """
        self.max_health = (self.con + self.class_hitpoints) * self.level
        self.current_health = self.max_health

    def take_damage(self, damage_amount):
        """
        Reduce characters current health by the damage amount inflicted.
        """
        self.current_health -= damage_amount
        if self.current_health <= 0:  # Check if the character is still alive
            self.current_health = 0
            print(f"{self.character_name} has been defeated!")

    def heal(self, healing):
        """
        Increases characters current health by the healing amount received.
        """
        self.current_health += healing
        if self.current_health > self.max_health:  # If healing exceeds current max, set to max
            self.current_health = self.max_health

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

    def is_alive(self) -> bool:
        """
        Check if current character is still alive.

        Returns:
            is_alive (bool): whether the characters health exceeds 0
        """
        return self.current_health > 0


class Job:
    def __init__(self, name, lvl, abilities, saves, attacks, class_hp, class_main_ability):
        self.name = name
        self.lvl = lvl
        self.abilities = abilities
        self.saves = saves
        self.attacks = attacks
        self.class_hp = class_hp
        self.class_main_ability = class_main_ability


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
            "will": 10 + 2 + 4
        }
        attacks = {
            "physical": 10 + 5 + 6 + 2,
            "spell": 0
        }
        super().__init__(
            name="Fighter",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=10,
            class_main_ability="str"
        )


chosen_class = Fighter()
character = Character(chosen_class)

print(character.current_health)
print(character.max_health)
print(character.con)
print(character.class_hitpoints)
print(character.level)
print(character.str)


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
            "will": 10 + 2 + 2
        }
        attacks = {
            "physical": 10 + 3,
            "spell": 10 + 5 + 4
        }
        super().__init__(
            name="Wizard",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=7
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
            "will": 10 + 2 + 6
        }
        attacks = {
            "physical": 10 + 3,
            "spell": 10 + 5 + 4
        }
        super().__init__(
            name="Bard",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=8
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
            "will": 10 + 1 + 6
        }
        attacks = {
            "physical": 10 + 5 + 6 + 2,
            "spell": 0
        }
        super().__init__(
            name="Rogue",
            lvl=10,
            abilities=abilities,
            saves=saves,
            attacks=attacks,
            class_hp=8
        )


class Weapon:
    def __init__(self, name, num_dice, dice_sides, dmg_modifier, phys_or_spell, strike_name, text_success, text_fail):
        self.name = name
        self.num_dice = num_dice
        self.dice_sides = dice_sides
        self.dmg_modifier = dmg_modifier
        self.phys_or_spell = phys_or_spell
        self.strike_name = strike_name
        self.text_success = text_success
        self.text_fail = text_fail

    def perform_strike(self, is_successful=True):
        # Perform a strike with the weapon
        if is_successful:
            return f"{self.strike_name} with {self.name} - {self.text_success}"
        else:
            return f"{self.strike_name} with {self.name} - {self.text_fail}"


# sword that rolls 2d8 for damage
sword = Weapon(
    name="Sword",
    num_dice=2,
    dice_sides=8,
    dmg_modifier=2,
    phys_or_spell="physical",
    strike_name="Slash",
    text_success="Hit the target!",
    text_fail="Missed the target."
)

import random


class Character:
    def __init__(self, name, alignment, level, class_hitpoints, strength, dexterity, constitution, intelligence, wisdom, charisma, main_ability):
        self.name = name
        self.alignment = alignment
        self.level = level
        self.class_hitpoints = class_hitpoints
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.main_ability = main_ability

        # Initialize other attributes as needed
        self.attack_modifier = 0
        self.spell_modifier = 0
        self.perception = 0
        self.initiative = 0
        self.fortitude = 0
        self.reflex = 0
        self.will = 0

    # Define methods for modifiers, hitpoints, and saving throws as needed
    # Example:
    def calculate_hit_points(self):
        self.hit_points = self.constitution + self.class_hitpoints * self.level

    def calculate_attack_modifier(self):
        # Calculate attack modifier based on attributes and equipment
        if self.name == "Fighter" or self.name == "Champion":
            self.attack_modifier = self.strength + 3
        elif self.name == "Ranger" or self.name == "Rogue":
            self.attack_modifier = self.dexterity + 3
        else:
            self.attack_modifier = 3

    def calculate_spell_modifier(self):
        # Calculate spell modifier based on attributes and spellcasting ability
        if self.name == "Bard" or self.name == "Champion":
            self.spell_modifier = self.charisma + 3
        if self.name == "Wizard":
            self.spell_modifier = self.intelligence + 3
        else:
            self.spell_modifier = 0

    def calculate_perception(self):
        if self.name == "Champion" or self.name == "Wizard":
            self.perception = self.wisdom + 3
        else:
            self.perception = self.wisdom + 5

    def calculate_fortitude(self):
        if self.name == "":
            self.fortitude = self.constitution + 3
        else:
            self.perception = self.wisdom + 5


# Create a Fighter character
fighter = Character(
    name="Fighter",
    alignment="Neutral",
    level=1,
    class_hitpoints=10,
    strength=4,
    dexterity=2,
    constitution=3,
    intelligence=0,
    wisdom=1,
    charisma=0,
    main_ability="Strength"
)


class Weapon:
    def __init__(self, name, num_dice, dice_sides, dmg_modifier, strike_name, text_success, text_fail):
        self.name = name
        self.num_dice = num_dice
        self.dice_sides = dice_sides
        self.dmg_modifier = dmg_modifier
        self.strike_name = strike_name
        self.text_success = text_success
        self.text_fail = text_fail

    def calculate_damage(self):
        # Roll dice to determine the damage
        total_damage = sum(random.randint(1, self.dice_sides)
                           for _ in range(self.num_dice))
        total_damage += self.dmg_modifier
        return total_damage

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
    strike_name="Slash",
    text_success="Hit the target!",
    text_fail="Missed the target."
)

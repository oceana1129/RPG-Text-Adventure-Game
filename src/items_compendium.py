class Create_Item:
    def __init__(self, name, description, consumeable, potion_type, event):
        """
        Initialize basic information for an item creation.
        """
        self.name = name
        self.description = description
        self.consumeable = consumeable
        self.potion_type = potion_type
        self.event = event

    def get_description(self) -> str:
        """
        Get description for the item.

        Returns:
            descrption (str): returns description of the item
        """
        return self.description


inventory_list = {
    "healing potion lesser": Create_Item(
        name="healing potion lesser",
        description="A potion that restores a small amount of health.",
        consumeable=True,
        potion_type="hp",
        event=False
    ),
    "healing potion moderate": Create_Item(
        name="healing potion moderate",
        description="A potion that restores a moderate amount of health.",
        consumeable=True,
        potion_type="hp",
        event=False
    ),
    "healing potion greater": Create_Item(
        name="healing potion greater",
        description="A potion that restores a large amount of health.",
        consumeable=True,
        potion_type="hp",
        event=False
    ),
    "mana potion lesser": Create_Item(
        name="mana potion lesser",
        description="A potion that restores a small amount of mana.",
        consumeable=True,
        potion_type="mp",
        event=False
    ),
    "mana potion moderate": Create_Item(
        name="mana potion moderate",
        description="A potion that restores a moderate amount of mana.",
        consumeable=True,
        potion_type="mp",
        event=False
    ),
    "amulet": Create_Item(
        name="amulet",
        description="A beautiful amulet granted to you by the Fey Queen, boosts your abilities.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "gold": Create_Item(
        name="gold",
        description="Gold pieces that can be used to buy more goodies later.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "rope": Create_Item(
        name="rope",
        description="Always useful to have more rope lying around.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "playing cards": Create_Item(
        name="playing cards",
        description="A deck used for party tricks and playing games with friends.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "letter": Create_Item(
        name="letter",
        description="A strange letter cold to the touch.",
        consumeable=False,
        potion_type=False,
        event="trigger lore"
    ),
    "diary": Create_Item(
        name="diary",
        description="Looks like a personal diary,  it's filled with various entries.",
        consumeable=False,
        potion_type=False,
        event="lore"
    ),
    "lockpick": Create_Item(
        name="lockpick",
        description="Good for unlocking doors and disabling traps.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "torch": Create_Item(
        name="torch",
        description="You already have one, but this is useful for lighting the way.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "shovel": Create_Item(
        name="shovel",
        description="A study shovel for digging.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "glacial ring": Create_Item(
        name="glacial ring",
        description="A magical ring with icy mist flowing inside it.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "hundred moth caress scythe": Create_Item(
        name="hundred moth caress scythe",
        description="The sctyhe used by necromancers. Made from a dull, gray wood of bone-like "
        "consistency, and when you slice with it, a fluttering gust of hundreds of "
        "moths' wingbeats fills the air.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "necromancer cloak": Create_Item(
        name="necromancer cloak",
        description="The swirling folds of this cloak appear to contain the void sky, "
        "with stars rotating hypnotically through its firmament shedding darkness "
        "around it in a short range.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "book of shadows": Create_Item(
        name="book of shadows",
        description="A mystical book filled with ancient and dark knowledge.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
    "haunted mirror": Create_Item(
        name="haunted mirror",
        description="",
        consumeable=False,
        potion_type=False,
        event="lore"
    ),
    "bone key": Create_Item(
        name="bone key",
        description="A grinning skull tops the bow of this macabre key.",
        consumeable=False,
        potion_type=False,
        event=False
    ),
}

# print(inventory_list["amulet"].name)
# item = inventory_list["amulet"]
# print(item.name)

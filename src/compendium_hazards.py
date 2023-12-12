import mechanics


class Hazard:
    def __init__(self, name, dc, saving_throw, description, skill_crit_success, skill_success, skill_fail, skill_crit_fail, damage_dice, damage_size, modifier):
        """
        Initialize the current hazard with basic information
        """
        self.name = name
        self.dc = dc
        self.saving_throw = saving_throw
        self.description = description
        self.skill_crit_success = skill_crit_success
        self.skill_success = skill_success
        self.skill_fail = skill_fail
        self.skill_crit_fail = skill_crit_fail
        self.damage_dice = damage_dice
        self.damage_size = damage_size
        self.modifier = modifier

    def get_name(self) -> str:
        """
        Returns the name of the current hazard

        Returns:
            (str): the name of the hazard
        """
        return self.name

    def calculate_damage(self, player_saving_throw_mod: int = 20) -> int:
        """
        Calculates the total damage a hazard dealt to the player

        Arguments:
            player_saving_throw_mod (str): what is the modifier the player uses 
            for this saving throw?

        Returns:
            total_damage (int): total damage with degree of success applied
        """
        # See if you pass or fail the hazard's DC
        mechanics.print_text(f"You encounted \033[1m{self.name}\033[0m, you must pass the "
                             f"\033[1mDC check of {self.dc}\033[0m")
        mechanics.press_enter_to_continue()
        player_results = mechanics.ability_save_and_text_result(
            player_saving_throw_mod, self.dc, self.skill_crit_success, self.skill_success, self.skill_fail, self.skill_crit_fail)
        mechanics.print_text(f"You rolled \033[1m{player_results[1]}\033[0m")
        # print(
        #     f"Degree of Success... {mechanics.print_degree_of_success_result(player_results[0])}")
        mechanics.print_text(f"{player_results[2]}")

        # Calculate total damage by trap as a total
        damage = mechanics.calculate_hazard_damage_dealt(
            self.damage_dice, self.damage_size, self.modifier, player_results[0])
        return damage

    def read_description(self) -> str:
        """
        Returns the description of the current hazard

        Returns:
            (str): the description of the hazard
        """
        return self.description

    def hazard_saving_throw(self) -> str:
        """
        Returns the saving throw of the current hazard

        Returns:
            (str): the saving throw of the hazard
        """
        return self.saving_throw

    def event_type(self) -> str:
        """
        Returns the type of event the hazard is

        Returns:
            (str): the type of event the hazard is
        """
        return "hazard"


hazard_tiles = Hazard(
    name="Tile Arrow Trap",
    dc=26,
    saving_throw="reflex",
    description="The tiles shift down as a mechanism is triggered. The walls surrounding "
    "you suddenly come to life, shifting and opening with a sinister creak. "
    "In an instant, a relentless flurry of arrows is unleashed, filling the "
    "narrow corridor with deadly projectiles",
    skill_crit_success="",
    skill_success="With remarkable agility, you gracefully evade the oncoming barrage "
    "of arrows. Your movements are like a carefully choreographed dance, and you "
    "emerge from the hail of projectiles completely unscathed, your heart pounding"
    " with adrenaline.",
    skill_fail="You valiantly attempt to dodge the relentless assault of arrows, "
    "but despite your efforts, some of the projectiles find their mark. The impact "
    "is painful, and you bear the brunt of the attack as you stagger through the "
    "other side, wounded but determined.",
    skill_crit_fail="In your desperate bid to avoid the arrows, you stumble and "
    "falter. The arrows seem to find you with uncanny accuracy, striking "
    "you with piercing force. \nYou endure the pain, as you finally make it through the storm.",
    damage_dice=2,
    damage_size=4,
    modifier=2
)

hazard_miasma = Hazard(
    name="Miasma Trap",
    dc=23,
    saving_throw="fortitude",
    description="The fog continues to grow becoming thick and dangerous. A thick and deadly miasma begins to seep through the air.",
    skill_crit_success="",
    skill_success="With a massive inhale of clean air, you hold your breath as you sprint "
    "across the room. The miasma barely effects you as you effortlessly walk through.",
    skill_fail="With a massive inhale, you steal yourself and walk across the room. Your "
    "lungs give out and you make your last stretch with some miasma filling them.",
    skill_crit_fail="You can’t properly prepare yourself as miasma completely fills "
    "up your lungs. Your find yourself coughing all the way through the corridor.",
    damage_dice=1,
    damage_size=6,
    modifier=5
)

hazard_door = Hazard(
    name="Locked Door Trap",
    dc=24,
    saving_throw="will",
    description="You burst through the door as you hear a strange humming noise "
    "coming from behind the door.",
    skill_crit_success="",
    skill_success="The strange noise from behind the door doesn’t even phase you. "
    "Sounding no more than an annoying buzz in your ears. You shake your head and "
    "continue to move ahead.",
    skill_fail="Your eyes widen as the strange noise from behind the door "
    "grows even louder. It sounds like shrill piercing screams that reverberate "
    "in your mind.",
    skill_crit_fail="You feel a sense of doom creep through your body. "
    "Behing the door, you feel the wailing of a thousand screams reverberate "
    "through your mind and body.",
    damage_dice=2,
    damage_size=6,
    modifier=3
)

hazard_mirror = Hazard(
    name="Soul Draining Mirror",
    dc=28,
    saving_throw="will",
    description="Before you stands a tall, ornate mirror framed in ancient pristine"
    " silver. It's surface is dark and foreboading. As you approach it, you can't "
    "help but feel an icy chill in the air. You see your reflection peer back at you.",
    skill_crit_success="You could swore you felt something emenating from the mirror. "
    "However, it seems like whatever dark magic was inside of it has fizzled out harmlessly.",
    skill_success="Your reflection begins to contort into a dark and shadowy figure. "
    "With great resolve, you avert your gaze and manage to break free from the "
    "spell. You feel a strange lingering unease, but are otherwise unharmed.",
    skill_fail="Your reflection begins to contort into a grotesque and shadowy figure. "
    "You feel locked in place, as the shadowy figure reaches out its hand for you. It "
    "grabs hold of your very essence as you begin to feel your strength waning.\nYou "
    "finally break free from its grip.",
    skill_crit_fail="The reflection in front of you contorts, billowing into a large "
    "shadowy form. It's haunting visage crumbles your willpower as you are face to "
    "face with overwhelming darkness. The shadowy figure pierces its hand into your "
    "sternum as your essence is violently torn from your body.\nYou hear the faintest "
    "rattling chuckle from the mirror as it lets go of you. Leaving you shuddering and empty.",
    damage_dice=5,
    damage_size=4,
    modifier=3
)

hazard_chest = Hazard(
    name="Dark Tendril Chest",
    dc=26,
    saving_throw="reflex",
    description="You catiously appeach the chest, noting it's intricate engravings "
    "etched into its cold metal surface. With bated breath, you reach for the latch "
    "and, with a faint click, the chest open... And other click.\nSuddenly, dark tendrils "
    "pour forth from within, lashing out at you.",
    skill_crit_success="",
    skill_success="Without a second thought, you manage to narrowly dodge each wave of "
    "tendrils that reach for you. You retreat from the chests grasp, shaken but unharmed.",
    skill_fail="You try to dodge the chilling dark tendrils. But despite your best "
    "efforts, you were mere seconds too late to escape from their grasp. They strike "
    "at you, sending sharp cold shivers of icy pain through your body.\nThe tendrils "
    "subside and you make it out with some cuts and scrapes.",
    skill_crit_fail="In a moment of sheer panick, you panic and freeze, completely "
    "unable to react as tendrils reach out from the chest and attack you. They lash "
    "out with a relentless fury and leave you with chilling cuts cause you to shiver in pain.",
    damage_dice=3,
    damage_size=6,
    modifier=0
)

hazard_beauty_of_a_god = Hazard(
    name="Beauty of a God",
    dc=32,
    saving_throw="will",
    description="",
    skill_crit_success="",
    skill_success="You keep your resolve as you muster the courage to keep moving forward. "
    "You get the feeling that you should act carefully from here on out. You’ve come "
    "this far.\n\nShould you keep moving forward or head back?",
    skill_fail="It feels like whatever uneasiness you had before is even ten thousand "
    "times more unnerving. You can't force yourself to keep moving forward. Whatever "
    "is up ahead can easily put a stop to your adventure. \n\n"
    "You can't stop the urge to turn tail and run away.",
    skill_crit_fail="",
    damage_dice=0,
    damage_size=0,
    modifier=10
)

hazard_instant_death = Hazard(
    name="Instant Death",
    dc=100,
    saving_throw="will",
    description="",
    skill_crit_success="",
    skill_success="",
    skill_fail="You can't feel anything over the overwhelming sense of pain and doom.",
    skill_crit_fail="Everything crumbles apart...",
    damage_dice=100,
    damage_size=2,
    modifier=50
)

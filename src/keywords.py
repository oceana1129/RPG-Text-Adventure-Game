"""
Keywords or messages used throughout the game
"""

action_keywords = {
    # menu stuff
    "play": ["start", "play", "play game", "start game", "boot", "boot game", "p1"],
    "help": ["help", "h3"],
    "about": ["about", "a2"],
    "restart": ["restart", "restart game", "reboot", "reboot game", "r4"],
    "quit": ["quit", "end", "quit game", "end game", "q5"],
    "yes": ["yes", "confirm", "accept", "affirmative", "indeed", "certainly",
            "absolutely", "sure", "okay", "positive", "roger", "aye", "correct"],
    "no": ["no", "cancel", "deny", "negative", "nah", "not really", "never",
           "nope", "decline", "deny", "reject", "disagree"],

    # character creation
    "fighter": ["fighter"],
    "wizard": ["wizard"],
    "bard": ["bard"],
    "rogue": ["rogue"],

    # out of combat and exploration
    "character status": [
        "check health", "examine status", "inspect character", "view stats",
        "analyze condition", "current status", "current health", "stats",
        "status", "health", "mana", "check mana"],
    "inventory": ["check inventory", "inventory", "item", "items", "look at inventory",
                  "check items"],

    # navigation
    "navigation": ["move", "go", "walk", "travel", "run", "move", "navigate", "traverse", "head"],
    "north": ["north", "up", "forward", "ahead"],
    "south": ["south", "down", "back", "backward", "behind"],
    "east": ["east", "right"],
    "west": ["west", "left"],

    # recall knowledge
    "recall knowledge": ["knowledge", "recall", "recall knowledge", "check", "learn",
                         "remember", "recall information", "think", "ponder", "contemplate",
                         "occult", "arcana", "society"],

    # basic interactions
    "interaction": ["pick up", "grab", "use", "interact", "maneuver", "handle"],
    "manipulate": ["touch", "trace", "reach", "handle", "feel", "caress", "manipulate", "tap"],

    # wisdom actions
    "perception": ["look", "observe", "inspect", "survey", "explore", "search", "investigate",
                   "gaze", "view", "examine", "scrutinize", "peer", "check", "assess",
                   "perception", "explore"],
    "animal handling": ["pet", "tame", "interact with animals", "speak with animals",
                        "befriend", "tame creatures", "communicate with beasts"],

    # physical stuff
    "attacking": ["attack", "swing", "hit", "combat", "chop", "smash",
                  "strike", "assail", "assault", "engage", "ready my"],
    "brute forcing": ["push", "shove", "break", "destroy", "hit",
                      "force", "power through", "overpower"],
    "punch": ["punch", "smack", "slap", "fist", "jab", "slug", "pummel"],

    # magic stuff
    "cast spell": ["cast spell", "cast a spell", "use magic", "invoke spell", "invoke a spell",
                   "enchant", "use cantrip", "ritual", "spell"],
    "detect magic": ["detect magic", "sense magic", "spot magical auras", "identify magic",
                     "see magic"],

    # dex actions
    "throw": ["throw", "toss", "hurl", "pitch", "launch", "fling"],
    "jump": ["jump", "glide", "leap", "vault", "leap", "hop", "bound", "spring"],
    "disable": ["disable", "disarm",
                "deactivate", "neutralize", "defuse"],
    "stealth": ["stealth", "hide", "sneak",
                "shadows", "sneak around", "conceal", "lurk"],

    # charisma actions
    "diplomacy": ["talk", "chat", "converse", "speak", "dialogue", "conversation", "diplomacy"],
    "intimidate": ["scare", "intimidate", "frighten", "scream", "yell", "glare", "impose",
                   "scare off", "threaten", "bully", "terrify"],
    "deception": ["deceive", "lie", "deceive", "fabricate", "mislead", "deception"],
    "play dead": ["play dead", "feint", "pretend to be dead",
                  "feign death", "pretend to be lifeless", "act deceased"],
    "charm": ["flirt", "seduce", "compliment",
              "charm", "woo", "allure", "captivate"],
    "perform": ["perform", "sing", "song", "instrument", "dance", "performance", "serenade", "balad", "lulluby",
                "give a performance", "showcase talent", "entertain", "play music"],

    # random actions based on the room
    "mask": ["cover", "mask", "cloth", "rag"],
    "light": ["torch", "light", "bright light", "shine"],

    # character attacks
    # fighter
    "greatsword": ["greatsword"],
    "sweeping blade": ["sweeping blade"],
    "dazing blow": ["dazing blow"],
    # rogue
    "dagger": ["dagger"],
    "sneak attack": ["sneak attack"],
    "backstab": ["backstab"],
    # bard
    "haunting hymm": ["haunting hymm"],
    "sooth": ["sooth"],
    "sound burst": ["sound burst"],
    "painful vibrations": ["painful vibrations"],
    # wizard
    "electric arc": ["electric arc"],
    "magic missile": ["magic missile"],
    "fireball": ["fireball"],
    "cone of cold": ["cone of cold"],

    # General actions later
    "consume": ["use", "eat", "drink"]
}

action_inventory = {
    "healing potion lesser": ["healing potion lesser", "hp lesser"],
    "healing potion moderate": ["healing potion moderate", "hp moderate"],
    "healing potion greater": ["healing potion greater", "hp greater"],
    "mana potion lesser": ["mana potion lesser", "mp lesser"],
    "mana potion moderate": ["mana potion moderate", "mp moderate"],
    "amulet": ["amulet", "necklace"],
    "gold": ["gold", "money", "gp", "gold pieces"],
    "rope": ["rope"],
    "playing cards": ["play cards", "playing deck", "playing card"],
    "letter": ["letter"],
    "diary": ["diary"],
    "lockpick": ["lockpick"],
    "torch": ["torch"],
    "shovel": ["shovel"],
    "glacial ring": ["glacial ring"],
    "hundred moth caress scythe": ["hundred moth caress scythe", "scythe", "moth scythe", "hundred moth"],
    "necromancer cloak": ["necromancer cloak", "cloak"],
    "book of shadows": ["book of shadows"],
    "haunted mirror": ["haunted mirror"],
    "bone key": ["bone key"]
}

text_title_screen = """
✦ .          ⁺      . ✦ .     ⁺           . ✦
           WELCOME TO THE TEXT RPG GAME
✦ .          ⁺      . ✦ .     ⁺           . ✦

        - PLAY
        - ABOUT
        - HELP
        - QUIT
"""

text_help_base = """
✦ .          ⁺      . ✦ .     ⁺           . ✦
                   HELP MENU
✦ .          ⁺      . ✦ .     ⁺           . ✦
To navigate use the following commands:
- north, east, west, south
- up, down, left, right
- (front/forward or back/backward)

To explore you may use the following commands (and many more):
- recall knowledge, perception
- interaction, manipulate
- animal handling
- attacking, brute forcing, punch
- cast spell, detect magic
- throw, jump
- disable, stealth
- diplomacy, intimidate, charm
- depeption, play dead
- perform


"""

text_about = "Hello, and welcome to the Text RPG game!\n"\
    "If you are new to the game, here is how it works...\n\n"\
    "You are an adventurer exploring a dungeon. You must explore your environment, "\
    "overcome obstacles, and surpass your enemies. When navigating through the dungeon, "\
    "remember, there are always multiple different ways to overcome various obstacles. "\
    "It is completely possible to go through a room without getting hurt. There are many "\
    "different actions you can take to approach a room such as stealth, intimidation, "\
    "brute force, or playing a song.\n"\
    "Explore and have fun.\n"\
    "Maybe you can discover potential secrets as you explore. "\
    "Note, exploration ends once you begin combat. You may only use specific class actions "\
    "during combat; and these actions vary depending on your chosen class.\n"\
    "If you need any more in depth explanations, type HELP at any time.\n\n"\
    "Good luck and have fun!"

text_demo_end = "You've made it to the end of the demo!\n"\
    "Congratulations!\n\n"\
    "There is more content to come for later updates of the game already planned out. I hope "\
    "you are interested in playing any future updates."\
    "If you'd like to play the demo again, then please type RESET.\n"\
    "Otherwise, type QUIT to end the game."

text_game_over_death = "✦ .          ⁺      . ✦ .     ⁺           . ✦\n"\
    "                   GAME OVER\n"\
    "✦ .          ⁺      . ✦ .     ⁺           . ✦\n\n"\
    "If you'd like to try again, type RESTART.\n"\
    "Otherwise you may QUIT the game.\n\n"

text_game_over = "\n\n"\
    "✦ .          ⁺      . ✦ .     ⁺           . ✦\n"\
    "                   GAME OVER\n"\
    "✦ .          ⁺      . ✦ .     ⁺           . ✦\n\n"\
    "If you'd like to try again, type RESTART.\n"\
    "Otherwise you may QUIT the game.\n\n"

text_quit = "Thanks for playing RPG TEXT ADVENTURE!\n\n"\
    "Copyright 2023 Oceana G"

text_error = "Please enter a valid command."

text_class_error = "Invalid class. Please choose from the available classes."

text_ask_name = "Welcome to the game!\nWhat is your character's name?"

text_select_class = """What is your character's class?
    CURRENT CLASSES:
      - FIGHTER
      - WIZARD
      - ROGUE
      - BARD
"""

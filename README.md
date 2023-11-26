# RPG-Text-Adventure-Game

Welcome to the Text RPG Adventure!
To create the game, we will need to do the following basic steps for set up

1.  Title Screen Start Up
    Will ask player for start, help, or quit

2.  Character Creator
    Will ask player for their adventurer's name, class, race, starting weapon, and alignment

    Name:
    // User input

    Class:
    // Fighter
    // Ranger
    // Bard
    // Wizard
    // MAYBE Champion
    // MAYBE Rogue

    Race:
    // Human + str
    // Elf + dex
    // Dwarf + con
    // Tiefling + cha

    Weapon:
    // Sword
    // Axe
    // Dagger
    // Bow
    // Shield
    // Staff

    Alignment:
    // Lawful Good
    // Neutral Good
    // Chaotic Good
    // Lawful Neutral
    // True Neutral
    // Chaotic Neutral
    // Lawful Evil
    // Neutral Evil
    // Chaotic Evi

    Specific stats for the character based on their choices
    Race and Alignment are flavor text only
    // may update later to let them effect certain text or encounters

3.  Create the Map for the player to explore
    ##########################################################
    ------------------ E1 E2
    ------------------ || ||
    ------------------ D1-D2-D3
    ------------------ || ||
    --------------- C1-C2-C3-C4-C5-C6
    ------------------ || || ||
    ----------------- B1-B2-B3
    ------------------ || || ||
    --------------- A1-A2-A3-A4-A5
    ------------------ ||
    -------------- Entrance -- S1 -- S2
    ##########################################################
    Each room has it's own event
    Types of Events:
    // Exploration
    // Combat
    // Hazard

        You can earn items after successfully completing an event
        Adventuring Gear:
        // Rope
        // Torch
        // Translation Book
        // Lockpick
        // Playing Cards
        // Mask
        // Shovel

        Consumeable:
        // Healing Potion Minor
        // Healing Potion Greater
        // Mana Potion Minor
        // Mana Potion Greater

    ##########################################################
    #######
    A0 - ENTRANCE
    // Event: Explore
    // Description: You stand at the entrance of a dark cave. The gross rustles as the wind carries an uneasy tune. This may be your very last breath of fresh air for all you know. You grip your [weapon ] and prepare for your journey ahead.

    // Available Actions:
    Look
    Crit Success: You spot some unusual carvings on the wall towards the east. Almost unconsciously lulled in, you trace the carvings and notice the wall underneath disappears. It appears that you've uncovered some kind of illusion spell.
    Success: You notice some strange markings on the wall to the east. You walk up close to the wall with the markings. You swear these markings weren't here before.
    Fail: You see nothing out of the ordinary. Steel your wits, it’s time to go in!
    Crit Fail: You step on a loose tile and stub your toe [take -1 damage]

    Detect Magic
    Success: You identify the carvings as a seal for some kind of illusion spell. If you trace over the carvings, you can undo the seal.
    Failure: The carvings are magical, but you aren't sure from which magic school they're from. Best to tread carefully.

    Throw Item
    You grab a rock and throw it at the wall. Congrats, you just threw a rock at a wall.

    Hit Wall
    You hit the wall, as your {weapon} phases through it. You try to walk forward but bounce off the wall. You wonder if there's another angle you can take or if you're just wasting your time.

    Cast Spell or Cantrip
    You cast a spell at the wall. The carvings glow as they absorb your magic harmlessly. You wonder if there's another approach you can take or if you should even bother.

    Touch or Trace Carvings
    You touch the carvings and find your finger tracing along the symbols. They grow bright and dissipate. Soon the illusion of a wall begins to disappear. Now you can traverse into this unconventional opening.

    Move
    -- North
    -- East (Secret)

SECRET S1
// Event: Explore
// Description: You walk through the hidden room. It seems to glow with an ethereal magic. Your mind begins to race with curiosity wondering what you might be at the end of this hall.
The passage seems to stretch almost endlessly as you lose track of time. It's been hours, maybe days until you reach an almost blindingly bright light at the end of the tunnel. You feel an ominous presence at the end of the hall. Like one of overwhelming strength and beauty. Before you can inspect further, you must fight against the urge to flee [will save].

    Save: Will
    DC: 30
    Success: You keep your resolve as you muster the courage to keep moving forward. You get the feeling that you should act carefully from here on out. You’ve come this far. Should you keep moving forward or head back?
    Fail: It feels like whatever uneasiness you had before is even ten thousand times more unnerving. You can't force yourself to keep moving forward. Whatever is up ahead can easily put a stop to your adventure. You turn tail and run away.
    You find yourself back at the entrance, out of breath and feeling more tired than before. You take a moment and rest before you walk into the main entrance.
    Move
    -- West
    -- East (Secret)

SECRET S2
// Event: Hazard
// Description: You decide to keep moving forward, despite your body's urges to flee and run. You walk closer to the bright light at the end of the tunnel before you get close enough to see what it is.
Within the glowing bright light, you see a beautiful Fey sitting on a throne. Small pixies flitter around her like moths to a flame. Her face is carved with intellect and power as it glows. Her eyes twinkle with either amusement or curiosity. What do you do?

    // Available Actions:
    Look
    Success: She seems to be rather intrigued by your presence. She doesn't appear to want to hurt you in any way. However, you still sense an unnerving amount of power emanating from her. It'd be best to stay on her good side.
    Fail: The bright light is too bright for your eyes. It's hard to discern anything peculiar about her.


    Knowledge or Recall Check
    Success: You recall how Fey came from the Feywilds. They are synonymous with the supernatural. They are often found near specific natural locations imbued with magic. Their nature can vary from playful and mischievous to outright selfish.
    This particular Fey is a Lampesperid Queen which rules over isolated regions soaked in light. They guard countless treasures and secrets, though, for those who approach them with respect, they're willing to part with knowledge or items.
    Failure: You can't recognize what kind of creature she is other than some kind of Fey or fairy.


    Talk
    Success: She is pleased and has a conversation with you. You share stories of your previous adventures and secrets you've uncovered before. In return, she warns you about the cave ahead filled with traps and monsters. She also gives you an amulet that will give you +5 to all damage rolls. As well as a Greater Potion of Healing. Bathed in a warm light, she summons you away.
    You find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.
    Fail: Although the Queen is normally one for good company, she finds your presence rather annoying. While you are mid-sentence, she waves her hand at you as you feel bathed in a warm light. Before your next breath, you find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.


    Intimidate
    Success: You somehow manage to intimidate the Fey Queen. She shivers in repulsion as she hastily gives you a Potion of Greater Healing and summons you away.
    You find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.
    Fail: You let out a pathetic roar or mumble under your breath. It's evident you were trying to intimidate the Fey Queen. No matter, she laughs in your face. And then a cheeky look creeps upon her face. She begins to move her hands around and whispers something in Fey's tongue. A warm light begins to envelop you as you feel your very being begin to burn. Everything around you seems to grow bigger as you shrink into the floor. Before you come to, you find yourself the size of a sprite with wings upon your back. And you feel an overwhelming urge to fly towards the queen and worship her for the rest of your life. Hope you like a life of eternal servitude!


    Play a Song or Serenade
    Success: You reach for your instrument and begin to play a soothing melody. The ethereal music fills the air, and the Fey Queen's eyes sparkle with delight. She leans in closer, entranced by your performance and humming to the tune. In appreciation for your beautiful serenade, she bestows upon you an amulet. [+5 bonus to all damage rolls].
    Fail: Your music falls flat, and the notes seem discordant in this otherworldly realm. The Fey Queen winces at the cacophony and abruptly waves her hand. You are bathed in a bright light and find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.


    Seduce or Flirt
    Success: Your charm and wit catch the Fey Queen off guard. She bursts into laughter, thoroughly entertained by your advances. In appreciation, she bestows upon you an amulet that enhances your prowess, granting you a +5 bonus to all damage rolls.
    Fail: Instead of being flattered, she becomes annoyed. Annoyance replaces her mirth as she promptly ushers you away. She waves her hand as you are bathed in a bright light.
    You find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.


    Attack or Cast Spell
    You ready an attack, immediately wary of her presence. The Fey Queen frowns and looks at you with disappointment. Before you can so much as think, she lifts her finger as you are enveloped in a white light. You feel your body begin to burn as each molecule of your being begins to erupt. And before you know it, you're dead.


    Reach Out or Touch
    You seem drawn to her... like a moth to a flame. And as you reach out your hand to touch the Fey Queen she begins to move her hands around and whispers something in Fey's tongue. A warm light begins to envelop you as you feel your very being begin to burn. Everything around you seems to grow bigger as you shrink into the floor. Before you come to, you find yourself the size of a sprite with wings upon your back. And you feel an overwhelming urge to fly towards the queen and worship her for the rest of your life. Hope you like a life of eternal servitude!


    Throw Item
    In a panic, you grab a rock on the floor and chuck it at the Fey Queen. She frowns in annoyance. One of the pixies catches the pebble in midair. With a flick of the wrist, the Fey Queen ushers you away as you are bathed in a glowing light. You find yourself at the entrance of the cave again. Why did you think that was a good idea?


    Move
    -- West


    A1
    // Event: Hazard
    // Description: You walk along the corridor, and the tiles seem to have various patterns on the floor. A few tiles on the wall and floor are marked with patterns.


    // Available Actions:
    Look
    Crit Success: A few of the tiles look odd. You instantly recognize it as a pressure plate trap.
    Success: You've seen something like this before. You think this room may be some kind of trigger trap.
    Fail: Other than having a few inscriptions, on the walls and floor, you don't notice anything odd.
    Crit Fail: While inspecting, you accidentally trigger one of the pressure plates [roll reflex].


    Disable
    Success: You safely disarm the trap with your Lockpick. Good thing you've been practicing. The tiles shift down harmlessly.
    Fail: You trigger the trap, as arrows shoot across the room [roll reflex].


    Jump over
    Success: With a running start, you leap over the tiles without triggering it.
    Fail: You misjudge your jump, triggering the trap as arrows shoot across the room [roll reflex].


    Throw Item or Trigger Trap
    Success: You pick up a loose stone and toss it onto the tiles. You safely trigger the trap as arrows shoot across the room.
    Fail: You throw an item onto the pressure plate, but it isn't heavy enough to activate it. You confidently walk over it and trigger the trap, as arrows shoot across the room [roll reflex].


    Hit Trap
    Success: With precision, you strike the pressure plate with your weapon, triggering the trap from a safe distance. Arrows fly across the room as you narrowly dodge them.
    Fail: You attempt to hit the pressure plate from a safe distance. However, when you hit the plate, you were too close. You get caught in a flurry of arrows across the room.


    Cast Spell or Cantrip
    Success: Using your wits, you cast a spell from a safe distance. You trigger the trap as arrows fly across the room.
    Fail: Thinking you're clever, you cast a spell from a safe distance at the tiles. You didn't realize how weak your spell was as you walked across the tiles that triggered a flurry of arrows [roll reflex].


    Move
    -- North
    -- East

A2
// Event: Combat
// Monster: Giant Rat
// Description: You walk down the tunnel as the darkness grows deeper. You hear a scampering on the floor followed by sharp screeches. After being through many dark caves before, you instantly recognize the sounds. It's a Giant Rat. Think quickly.

    // Actions (Before Combat):
    Inspect or Look
    Success: You notice the Giant Rat has a limp on its back left paw, you can use this to your advantage in combat. [Gain +2 to attack rolls]
    Fail: You don't notice anything peculiar about this rat, other than him being a giant rat.


    Hide or Sneak
    Success: Like a shadow, you slink into the darkest crevices in the cavern. Slowing your breath and obscuring your presence. When the rat comes near, you will be ready to attack with utmost precision [+1 to attack rolls and +4 to initiative]
    Fail: You attempt to hide and loudly kick a loose rock. Its movement ricochets in the tunnel as the rat turns to face you, ready for combat.


    Talk or Pet
    Success: Surprisingly, you manage to soothe the filthy creature's heart. Perhaps its old days of being a small rat resurface in its mind. It now acts very friendly and docile with you, deciding to befriend you. To show its gratitude, it uncovers a hidden treasure buried in the ground. You gain a torch, rope, and a letter.
    Fail: Your attempts to communicate or pet the rat fall flat, aggravating it further. The Giant Rat grows even more hostile. It bares its teeth and is ready for combat.


    Throw Item
    Success: You hurl a loose pebble, distracting the Giant Rat momentarily and giving you an advantage in combat. [Gain +2 to attack rolls]
    Fail: You throw a loose pebble attempting to distract the rat, instead you only draw attention to yourself. The rat turns towards you and bares its teeth ready for combat.


    Intimidate
    Success: With an intimidating glare, you strike fear into the Giant Rat. In cowers in fear, unable to move [+4 attack]
    Fail: The rat can't even tell you were trying to intimidate it. It lowers its stance, ready to attack.


    Play Dead
    Success: You collapse to the ground, feigning death. The rat comes over to sniff you, and once it assumes you're dead it turns to leave. You have the opportunity to strike while its guard is down [+4 to attack]
    Fail: You try to play dead, but it's not very convincing. The Giant Rat still thinks you're a threat and is ready to attack.


    Play Song or Lulluby or Serenade
    Success: Your melody fills the cavern. The Giant Rat lowers its guard, completely enamored with your song. It seems friendly and no longer interested in attacking you. To show its gratitude, it uncovers a hidden treasure buried in the ground. You gain a torch, rope, and a letter.
    Fail: Your melody falls flat and the Giant Rat, in its irritation, bares its teeth ready to fight you.


    // Enter Combat

4.  System/Mechanics
5.  Default Character/Weapon/Monster/Trap
    ---- MONSTERS----
    Level:
    Lore:
    AC:
    HP:
    // Attacks
    Name:
    Attack Roll:
    Damage Roll:
    Hit Success:
    Hit Fail:
    // Loot

---

    GIANT RAT
    Level: -1
    Lore: 11 (Wisdom)
    AC: 12
    HP: 8
    // Attacks
    Name: Jaws
    Attack Roll: +6
    Damage Roll: 1d6
    Hit Success: The Giant Rat lunges out at you with a vicious bite, sinking its teeth into you.
    Hit Fail: The Giant Rat lunges out at you, missing. As it ferociously snaps at the air.

    ***

    // Loot
    Rope
    2 gold

---

    KOBOLD
    Level: 1
    Lore: 13 (Intelligence)
    AC: 18
    HP: 16
    // Attacks
    Name: Shortsword
    Attack Roll: +9
    Damage Roll: 1d8
    Hit Success: The Kobold swings its shortsword with precision, landing a solid blow.
    Hit Fail: The Kobold's attack misses as it barely grazes your body.

    ***

    // Loot
    Playing Cards
    25 gold
    Lockpick
    Torch

---

    SHADOW
    Level: 4
    Lore: 17 (Wisdom)
    AC: 20
    HP: 30
    // Attacks
    Name: Shadow Hand
    Attack Roll: +15
    Damage Roll: 2d6+3
    Hit Success: The Shadow swipes at you with its shadow hand. Tendrils phase through your skin as you take damage.
    Hit Fail: You shudder as the Shadow reaches out for you with its shadow hand. It overestimates and misses.

    ***

    // Loot

---

    LUMINOUS OOZE
    Level: 4
    Lore: 17 (Intelligence)
    AC: 11
    HP: 50
    // Attacks
    Name: Psuedopod
    Attack Roll: +13
    Damage Roll: 2d8+5
    Hit Success: The ooze extends its pseudopod and strikes with blinding speed, dealing a devastating blow.
    Hit Fail: You successfully blocks the ooze's psuedopod.

    ***

    Name: Light Up
    Description: The ooze glows with blinding brightness. You try to resist the blinding light.
    DC: 21
    Save: Fortitude
    Successful Saving Throw: You are unaffected by the blinding light.
    Fail Saving Throw: You are frazzled and can't see properly. Take a -4 to your next attack roll.

    ***

    // Loot
    5 gold

---

    SKELETAL MAGE
    Level: 5
    Lore: 18 (Intelligence)
    AC: 16
    HP: 50
    // Attacks
    Name: Claw
    Attack Roll: +11
    Damage Roll: 2d8+2
    Hit Success: The Skeletal Mage's bony claws strike and tear into your flesh. You wince in pain and take damage.
    Hit Fail: You avoid the Skeletal Mage's claws, avoiding harm.

    ***
    Name: Ray of Frost
    Attack Roll: +14
    Damage Roll: 3d4+4 cold
    Hit Success: The Skeletal Mage's hands become envoloped in cold and it shoots you with an icy ray. You grit your teeth as you take cold damage.
    Hit Fail: The Skeletal Mage's hands become envoloped in cold and it shoots you, but you narrowly dodge out of the way.
    ***
    Name: Burning Hands
    Attack Roll: +14
    Damage Roll: 4d6 fire
    Hit Success: The Skeletal Mage unleashes a burst of searing flames that engulf you. You scream in agony as you take fire damage.
    Hit Fail: You swiftly move out of the way of the Skeletal Mage's fiery onslaught, with it only singing a bit of hair.

    ***

    // Loot
    20 gold
    Mana Potion Greater
    Healing Potion Minor
    Translation Book
    Letter

---

    HARPY SKELETON
    Level: 5
    Lore: 18 (Wisdom)
    AC: 16
    HP: 50
    // Attacks
    Name: Talon
    Attack Roll: +15
    Damage Roll: 2d6+7
    Hit Success: The Harpy Skeleton's sharp talons dig into your flesh, as you wince in pain.
    Hit Fail: You avoid the Harpy Skeleton's talons, avoiding harm.

    ***
    Name: Club
    Attack Roll: +15
    Damage Roll: 1d6+7
    Hit Success: The Skeleton Harpy strikes you with its club, delivering a solid blow.
    Hit Fail: The Skeleton Harpy swings its club in the air and clumsily misses you.
    ***
    Name: Shriek
    DC: 24
    Save: Fortitude
    Damage: 4d10
    Successful Saving Throw: The Harpy Skeleton emits an unearthly, bone-chilling scream. You are able to push through the disorientation and keep fighting.
    Fail Saving Throw: The Harpy Skeleton emits an unearthly, bone-chilling scream that pierces your ears causing sharp damage and disorienting you.

    ***
    10 gold
    Club
    Healing Potion Minor
    Mana Potion Minor

---

    FROST DRAKE
    Level: 7
    Lore: 21 (Intelligence)
    AC: 25
    HP: 110
    // Attacks
    Name: Fangs
    Attack Roll: +17
    Damage Roll: 2d12+8 + 1d6 cold
    Hit Success: The Frost Drake sinks its fangs into you, dealing a heavy blow.
    Hit Fail: The Frost Drake lunges forward with its fangs, but you manage to evade.

    ***

    Name: Tail
    Attack Roll: +17
    Damage Roll: 2d10+8
    Hit Success: The Frost Drake shifts it weight and lashes out at you with it's tail. Hitting you with great force.
    Hit Fail: The Frost Drake whips it's tail through the air. You sidestep and avoid the blow.

    ***

    Name: Frost Breath
    DC: 25
    Save: Reflex
    Damage Roll: 7d6 cold
    Successful Saving Throw: You narrowly dodge the dragons icy frost breath by the skin of your teeth.
    Fail Saving Throw: The Frost Drake breaths in a heavy breath, as swirling cold fills it's lungs. It breaths out as a chilling frost engulfs you, freezing you down to your core as you take damage.

    ***

    // Loot
    +150 gp
    Glacial Amulet (+4 damage resistance)
    Healing Potion Greater
    Mana Potion Greater

---

    NECROMANCER MAGE
    Level 12
    Lore: ???
    AC: 32
    HP: 150
    // Attacks
    Name: Hundred Moth Caress Scythe
    Attack Roll: +21
    Damage Roll: +4d6 +5
    Heal: 1d6 + 2
    Hit Success: The necromancer swings her scythe at you. A fluttering gust of hundreds of moths' wingbeats fills the air. You feel your life essence drain as her scythe seeps into your bones.
    Hit Fail: The necromancer swings her scythe at you. You count your prayers as you feel hundreds of moths' wingbeats slice through the air, missing you.

    ***

    Name: Rip the Spirit
    Damage Roll: +6d6 + 10
    Saving Throw: Will
    Successful Saving Throw: The necromancer reaches her hand out to you and closes it into a fist. You feel a dark force attempt to tear your soul apart. You resist.
    Fail Saving Throw: The necromancer reaches her hand out to you and closes it into a fist. You shudder as you feel an eerie force envelope around you. It attempts to rip your very soul from your body, causing emmense pain.

    ***

    Name: Phantasmal Killer
    Attack Roll: +21
    Damage Roll:
    Hit Success: The necromancer points her scythe at you as an illusion of your worst fear materializes, instilling terror deep within your heart and pain within your soul.
    Hit Fail: The necromancer points her scythe at you, but her dark magic falters.

    ***

    Name: Shakled Shadow Bind
    Damage Roll: 3d8 + 7
    Saving Throw: Fortitude
    Successful Saving Throw: The necromancer's shadowy minions sprout forth asdark tendrils attempt to ensnare you. But, you successfully break free from their grasp.
    Fail Saving Throw: Dark tendrils emerge from the necromancer's scythe, as shadowy minions wrap around you, constricting and suffocating you, dealing substantial damage.

    ***
    // Loot
    Hundred Moth Caress Scythe
    Necromancer Cloak
    Voidsworn Amulet (drain health from enemies and heal you)
    Book of Shadows
    Haunted Mirror (inspect to see necromancer's secrets)
    Crypt Key

6.

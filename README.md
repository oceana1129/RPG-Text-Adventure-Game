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
    Greatsword(FightingAction): # 9 - 20 - 31
    Sweeping_Blade(FightingAction): # 9 - 27 - 45
    Dazing_Blow(FightingAction): # 10 - 37.5 - 66

    // Rogue
    Dagger(FightingAction): # 13 - 20 - 28
    Sneak_Attack(FightingAction): # 20 - 30 - 40
    Backstab(FightingAction): # 20 - 40 - 56

    // Bard
    Haunting_Hymm(FightingAction): # 9 - 19 - 29
    Sooth(FightingAction): # 10 - 19 - 28
    Sound_Burst(FightingAction): # 11 - 24.5 - 38
    Painful_Vibrations(FightingAction): # 20 - 37 - 56

    // Wizard
    Electric_Arc(FightingAction): # 12 - 19.5 - 27
    Magic_Missile(FightingAction): # 30
    Fireball(FightingAction): # 12 - 28 - 44
    Cone_Of_Cold(FightingAction): # 22 - 42 - 62
    // MAYBE Champion
    // MAYBE Ranger

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

As you muster your courage to continue onward, the relentless urge to flee battles your determination. Each step takes you closer to the radiant light that beckons from the tunnel's end, its brilliance obscured by a dazzling glow.

Emerging within the incandescent brilliance, you behold a captivating sight—a magnificent Fey, regally seated upon an intricately adorned throne. Ethereal pixies, their luminescent wings shimmering like fireflies, dance around her in an enchanting ballet. Her visage, chiseled with an aura of wisdom and power, emits an iridescent luminescence.

Her eyes, two pools of sparkling enigma, betray traces of either amusement or an insatiable curiosity, their gaze fixed upon you. A palpable aura of enchantment envelops the throne room, drawing you deeper into her mesmerizing presence.

In this ethereal encounter, the question remains: What course of action will you choose to take?

    // Available Actions:
    Look
    DC: 25
    Success: She seems to be rather intrigued by your presence. She doesn't appear to want to hurt you in any way. However, you still sense an unnerving amount of power emanating from her. It'd be best to stay on her good side.
    Fail: The bright light is too bright for your eyes. It's hard to discern anything peculiar about her.


    Knowledge or Recall Check
    DC: 30
    Success: You recall how Fey came from the Feywilds. They are synonymous with the supernatural. They are often found near specific natural locations imbued with magic. Their nature can vary from playful and mischievous to outright selfish.
    This particular Fey is a Lampesperid Queen which rules over isolated regions soaked in light. They guard countless treasures and secrets, though, for those who approach them with respect, they're willing to part with knowledge or items.
    Failure: You can't recognize what kind of creature she is other than some kind of Fey or fairy.


    Talk
    DC: 27
    Success: She is pleased and has a conversation with you. You share stories of your previous adventures and secrets you've uncovered before. In return, she warns you about the cave ahead filled with traps and monsters. She also gives you an amulet that will give you +5 to all damage rolls. As well as a Greater Potion of Healing. Bathed in a warm light, she summons you away.
    You find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.
    Fail: Although the Queen is normally one for good company, she finds your presence rather annoying. While you are mid-sentence, she waves her hand at you as you feel bathed in a warm light. Before your next breath, you find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.


    Intimidate
    DC: 32
    Success: You somehow manage to intimidate the Fey Queen. She shivers in repulsion as she hastily gives you a Potion of Greater Healing and summons you away.
    You find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.
    Fail: You let out a pathetic roar or mumble under your breath. It's evident you were trying to intimidate the Fey Queen. No matter, she laughs in your face. And then a cheeky look creeps upon her face. She begins to move her hands around and whispers something in Fey's tongue. A warm light begins to envelop you as you feel your very being begin to burn. Everything around you seems to grow bigger as you shrink into the floor. Before you come to, you find yourself the size of a sprite with wings upon your back. And you feel an overwhelming urge to fly towards the queen and worship her for the rest of your life. Hope you like a life of eternal servitude!


    Play a Song or Serenade
    DC: 28
    Success: You reach for your instrument and begin to play a soothing melody. The ethereal music fills the air, and the Fey Queen's eyes sparkle with delight. She leans in closer, entranced by your performance and humming to the tune. In appreciation for your beautiful serenade, she bestows upon you an amulet. [+5 bonus to all damage rolls].
    Fail: Your music falls flat, and the notes seem discordant in this otherworldly realm. The Fey Queen winces at the cacophony and abruptly waves her hand. You are bathed in a bright light and find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.


    Seduce or Flirt
    DC: 31
    Success: Your charm and wit catch the Fey Queen off guard. She bursts into laughter, thoroughly entertained by your advances. In appreciation, she bestows upon you an amulet that enhances your prowess, granting you a +5 bonus to all damage rolls.
    Fail: Instead of being flattered, she becomes annoyed. Annoyance replaces her mirth as she promptly ushers you away. She waves her hand as you are bathed in a bright light.
    You find yourself back at the entrance of the cave. The eastern wall you came through appears to be missing.


    Attack or Cast Spell
    DC: 0
    You ready an attack, immediately wary of her presence. The Fey Queen frowns and looks at you with disappointment. Before you can so much as think, she lifts her finger as you are enveloped in a white light. You feel your body begin to burn as each molecule of your being begins to erupt. And before you know it, you're dead.


    Reach Out or Touch
    DC: 0
    You seem drawn to her... like a moth to a flame. And as you reach out your hand to touch the Fey Queen she begins to move her hands around and whispers something in Fey's tongue. A warm light begins to envelop you as you feel your very being begin to burn. Everything around you seems to grow bigger as you shrink into the floor. Before you come to, you find yourself the size of a sprite with wings upon your back. And you feel an overwhelming urge to fly towards the queen and worship her for the rest of your life. Hope you like a life of eternal servitude!


    Throw Item
    DC: 0
    In a panic, you grab a rock on the floor and chuck it at the Fey Queen. She frowns in annoyance. One of the pixies catches the pebble in midair. With a flick of the wrist, the Fey Queen ushers you away as you are bathed in a glowing light. You find yourself at the entrance of the cave again. Why did you think that was a good idea?


    Move
    -- West


    A1
    // Event: Hazard
    // Description: You walk along the corridor, and the tiles seem to have various patterns on the floor. A few tiles on the wall and floor are marked with patterns.


    As you cautiously step into the cave's entrance, an otherworldly stillness envelopes you. A hushed silence fills the air. The dim light filtering in from the outside barely penetrates the cavern's depths. What little light there is casts eeries shadows that dance along the rocky walls.

    Beneath your feet, you discover a tangled mosaic of peculiar tiles, each carved with intricate patterns emenating with energy. The air carries a faint hymm, daring you to venture further. Each step uncovering more about the secrets of this dungeon.

    As you move deeper along the corridor, your torchlight reveals the walls and floor adorned with these mysterious designs. The patterns intertwine and shift, as you're still unsure of their origin. Call it your sense of experience, paranoia begins to gnaw at you as you feel every step further may lead you to peril. There's something odd about these tiles.
    What would you like to do?

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
    Fail: You misjudge your jump, triggering the trap as arrows shoot across the room. [roll reflex].


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
// Description:  
 You walk down the tunnel as the darkness grows deeper. The narrow passage is damp, and the air feels heavy with moisture. The faint echoes of your footsteps bounce off the cold, stone walls. As you continue, you hear a scampering on the floor, followed by sharp screeches. After being through many dark caves before, you instantly recognize the sounds. It's a Giant Rat.

    You take a moment to assess the situation. The tunnel extends ahead, and you can't see the end of it. The rats could be coming from anywhere within the darkness. It steps sound even closer as you wait, till it nears closer in sight. Think quickly; your next steps could be crucial.

    // Actions (Before Combat):
    Inspect or Look
    Success: You notice the Giant Rat has a limp on its back left paw, you can use this to your advantage in combat. [Gain +2 to attack rolls]
    Fail: You don't notice anything peculiar about this rat, other than him being a giant rat.


    Hide or Sneak
    Success: Like a shadow, you slink into the darkest crevices in the cavern. Slowing your breath and obscuring your presence. When the rat comes near, you will be ready to attack with utmost precision [+2 to attack rolls]
    Fail: You attempt to hide and loudly kick a loose rock. Its movement ricochets in the tunnel as the rat turns to face you, ready for combat.


    Talk or Pet
    Success: Surprisingly, you manage to soothe the filthy creature's heart. Perhaps its old days of being a small rat resurface in its mind. It now acts very friendly and docile with you, deciding to befriend you. To show its gratitude, it uncovers a hidden treasure buried in the ground. [Loot: You gain a torch, rope, and a letter.]
    Fail: Your attempts to communicate or pet the rat fall flat, aggravating it further. The Giant Rat grows even more hostile. It bares its teeth and is ready for combat.


    Throw Item
    Success: You hurl a loose pebble, distracting the Giant Rat momentarily and giving you an advantage in combat. [Gain +2 to attack rolls]
    Fail: You throw a loose pebble attempting to distract the rat, instead you only draw attention to yourself. The rat turns towards you and bares its teeth ready for combat.


    Intimidate
    Success: With an intimidating glare, you strike fear into the Giant Rat. In cowers in fear, unable to move [+4 to attack rolls]
    Fail: The rat can't even tell you were trying to intimidate it. It lowers its stance, ready to attack.


    Play Dead
    Success: You collapse to the ground, feigning death. The rat comes over to sniff you, and once it assumes you're dead it turns to leave. You have the opportunity to strike while its guard is down [+4 to attack rolls]
    Fail: You try to play dead, but it's not very convincing. The Giant Rat still thinks you're a threat and is ready to attack.


    Play Song or Lulluby or Serenade
    Success: Your melody fills the cavern. The Giant Rat lowers its guard, completely enamored with your song. It seems friendly and no longer interested in attacking you. To show its gratitude, it uncovers a hidden treasure buried in the ground. [Loot: You gain a torch, rope, and a letter.]
    Fail: Your melody falls flat and the Giant Rat, in its irritation, bares its teeth ready to fight you.

    Attacking
    Without hesitation, you draw your weapon and prepare to strike. Adrenaline courses through your veins as you prepare for the upcoming battle.

    Cast Spell
    You focus your energy, drawing upon your magical powers. With a series of gestures the air around you crackles. You prepare to cast a spell for the upcoming battle.

A3
// Event: Hazard
// Hazard: Miasma
// Description:  
 You walk down the dimly lit tunnel as the darkness grows deeper. The silence envelops you. The walls, damp and uneven, seem to close in around you with every step. Strange, otherworldly markings and symbols are etched into the stone, their meaning lost to time. The air is heavy with an earthy scent, and the distant echoes of water dripping create an eerie backdrop.\n

    As you continue, a thick fog begins seeps through the air. It swirls through the tunnel as your breathing becomes labored. The dim light from your torch dances through the mist. As you move through, it doesn't seem to get any thinner, and is in fact becoming dangerously thick. You can see a passageway up ahead towards the north.\n\nWhat do you do?

    recall knowledge
    DC: 24
    success: You think back to previous adventures and books you've read. The thickening air and sickly hue... This is a miasma. If you don't protect yourself properly, then inhaling too much of this fog will cause lethal damage. You recognize that if you cover up your mouth in some way or create a clean pocket of air, then you'll likely make it through just fine.
    fail: You can't really think of anything that explains the fog in the air.

    mask
    DC: 0
    success: You think fast and create a makeshift mask out of some cloth. You're able to walk through the fog with little to no problem.
    room cleared

    attacking
    DC: 30
    success: A strange idea pops in your head. You take out your weapon and begin to spin it in the air rapidly. By spinning it around at such a fast speed, you are able to make a pocket of air around you. You are able to pass through the fog with little trouble.\nYou see a passage up north.
    room cleared
    fail: You have your weapon out, but there is nothing really to attack.
    trigger hazard

    perception:
    DC: 27
    success: You search your way through the fog and end up finding areas in the tunnel with a thin amount of fog. You are able to walk through the fog safely by utilizing this weakness.
    fail: You peer through the fog but you can't find anything that will help you.

    cast spell
    DC: 24
    success: You look around you and begin to chant a spell to yourself. Gesturing your arms you create a makeshift bubble around you. You are able to purify the air around you as you walk through the tunnel.
    room cleared
    fail: You think of various different spells in your arsenal. You think of any that could help in this situation.
    trigger hazard

    jump
    DC: 28
    success: With a running start, you aim towards the end of the corridor with a glorious vault. Tumbling through air, you land on your feet gracefully at the other end of the tunnel. You can now continue to move north.
    room cleared
    fail: With a running start, you vault through the corridor; trying to make it through the end. However, your jump ends short and you're still in the thick of the fog.
    trigger hazard

    disable
    DC: 29
    success: You peer all over the room, shining your light on the walls. You miraculously find a portion of the wall with some vents in it. You take out some items from your belt as you finagle with the vents. With a click, the vents stop pushing out air. The fog begins to thin and you can now make it through the other side at the north wall.
    fail: You peer all over the room, looking for a way to reduce the fog. You can't find anthing of note.
    trigger hazard

B1
// Event: Combat
// Enemy: Kobold
// Description: You cautiously walk through the corridor, dimly lit and long. The silence is disrupted by faint sounds of scuttling feet and muted chattering. You swivel your head around. Paranoia gnaws at your senses.\nYou strain your ears and listen more closely, trying to discern the noises. You get the feeling that you are not alone in this tunnel. You swear you could hear a faint chuckling from behind the walls.\nA sense of danger pricks your skin. From the corner of your eye, you catch a fleeting moment of a dim light, darting along the tunnel walls. Somethingn is following you, stalking you through the darkness.\n\nThink fast.

recall knowledge
DC: 20
success: Piecing together the clues, you can guess that the creature stalking you is a Kobold, a cunning and opportunistic creature. The like to burrow in tunnels and are generally peaceful as long as you don't trespass in their territory. You know that as long as you can avoid it or convince it to go away, it will probably just ignore you.
fail: There aren't enough clues for you to piece together what kind of creature is stalking you.

perception
DC: 26
success: You lay low and wait for a bit. You hone in on your senses and adjust to the darkness. The faint lights you saw flicker and form into the shadow of the creature. It appears to be a Kobold, minding its own business and looking for crevices to squeeze into.
fail:
trigger combat

attacking
DC: 0
success: Without hesitation, you draw your blade and prepare to strike whatever it is that’s following you. With bated breath, adrenaline courses through your veins as you wait.
trigger combat

cast spell
DC: 0
success: You channel your magical energies, preparing to unleash a spell at your shadowed stalker.
trigger combat

throw
DC: 27
success: In a moment of quick thinking, you grab a trusted loose pebble on the floor. You wait with bated breath as you wait for your shadowed follower. A kobold steps out of the shadows, inspecting the tunnel walls and unassuming. You hurl the loose rock and nail it right at the kobold’s head. It’s a direct hit, knocking him at the temple. With a teeter, the kobold rocks as it falls onto the floor, completely incapacitated.
room cleared
fail: You grab a loose pebble from the floor. And wait with bated breath as you wait for your shadowed follower. A kobold steps out of the shadows, inspecting the tunnel walls and unassuming. You hurl the pebble and it hits its mark. However, the force of impact was so minimal that it simply directs the kobold to your location.
trigger combat

stealth
DC: 26
success: You move quickly and blend into the shadows. Hugging the tunnel walls in the crevice of darkness. You hold your breath as you watch the shadow of a kobold creep into sight. It appears to be inspecting one of the tunnel walls. It grabs something from the wall and then creeps back into the shadows, scurrying into a tunnel in the floor. You let go of the wall. It doesn’t look like it’s coming back. You see a tunnel up ahead to the north.
room cleared
fail: You move quickly and walk into the shadows. You hug the tunnel walls as a kobold appears to creep into sight. You can’t get a good look at it and what it’s doing. So you move closer into sight. However, you snag a loose pebble under your foot as it bounces clumsily and loudly towards the kobold. Alerted, it turns around and looks straight at you.
trigger combat

diplomacy
DC: 28
success: You think the best way to get out of this is to reason your way out of it. You gently call out at the shadow scampered along the tunnel walls. You reason that you’re here peacefully and simply wish to move through. The kobold scurries out of the shadows, fearful at first, but quickly relieved. It looks at you and tells you how it’s just here to check one of the walls for the lady of the caves. Before you could ask anything else, it does exactly as it says. Checking the wall and then scampering away into a tunnel in the floor. It doesn’t look like it’s coming back. You see a tunnel ahead that leads north.
room cleared
fail: You call out to the shadows, thinking reasoning may be better than just fighting. You say that you do not wish to harm whatever he is.\nA kobold scurries out of the shadows, but it looks at you with fear. It looks at your gear and doesn’t seem to trust you despite your words.
trigger combat

perform
DC: 20
success: You begin to play a tune, playing a beautiful progression of cords. The sound is reminiscent of a warm winter day, filling the tunnel with a harmonious tune. From the shadows appears a kobold. It seems completely mesmerized and curious by what you’re doing. You pay no mind to it as it begins to sway with the tempo. It hums to itself as it walks over to the tunnel wall it was intending to work on. It taps the tunnel wall with inspiration carrying its steps. It turns around and waves at you goodbye as it disappears in a kobold sized tunnel in the floor. You don’t think it’ll be coming back any time soon. You see the northern tunnel up ahead.
room cleared
fail: You begin to play a tune, but it is completely discordant and out of tune. A kobold runs out of the shadows mad and upset. It seems to be completely irritated with your disharmonious tune ready to stop the source.
trigger combat

intimidate
DC: 24
success: You wait for whatever it is following you through the tunnel. You hold onto your weapon with great resolve and puff your chest. From the shadows, you see a creature come out of the shadows, a small kobold. You charge towards it with your weapon in hand, letting out a most ferocious roar. The kobolds eyes grow large as its heart leaps out. It falls to the floor and then quickly gets back up to run away. As you partly chase it, it scampered and squeezes into a hidden tunnel in the floor; one that is far too small for you to get into. It likely won’t be coming back out any time soon. You see up ahead a northern tunnel.
room cleared
fail: You wait for the creature to come out of the shadows, ready to scare it away with your might. A small kobold appears from the light, carrying a small weapon and some tools. You move towards it and yell at him. Confused, it looks at you with an angry look on its face. It sees your signs of aggression and is ready for combat.
trigger combat

play dead
DC: 30
success: You press yourself up against the tunnel wall, feigning death; losing weight from your limbs and going limp. You don’t even stir as you hear small scuffling from a creature in the distance. You don’t know if has noticed you or not but seems to not care or notice your presence. It seems to walk towards a tunnel wall as it disappears into the ground. You wait a few minutes, until you’re sure it won’t come back again. You get up and brush yourself off. You see a northern tunnel up ahead.
room cleared
fail: You fall limply to the floor but fail to conceal yourself in a convincing manner. You wait with your heart beating through your chest as you hear faint footsteps in the distance. But then, the footsteps grow even louder as it begins to approach closer. You try not to move as you feel something small walk right next to you. You can feel moist breath as it sniffs your ‘corpse’. It screeches and you stir to life startled. Your cover is blown, and it has its weapon at the ready.
trigger combat

B2
// Event: Combat
// Enemy: Shadow
// Description:
You find yourself walking further, and as you walk, the walls begin to narrow into a claustrophobic corridor. Dimly lit by the flickering light of your torch. You can see strange encryptions on the walls as you continue to walk. Each step brings you into an ever encroaching darkness.\nYou cautiously proceed as you feel the hair on your body begin to prickle. You exhale as your breath turns into frosty plumes. You begin to shiver as you begin to feel an unsettling presence looming. You turn with your torch in hand as the shadows around you begin to twist and distort. And from above you, the shadows begin to form dripping onto the cavern floor. A shapeless malevolent entity emerges from the tendrils of darkness on the floor. Made of pure darkness, its very presence seems to drain warmth and light from the surrounded. A cold shroud intensifies as the creature draws nearer.\n\nThink fast!

Recall knowledge
DC: 20
Success: You wrack you brain and recall the type of creature this is. It’s a Shadow, an undead creature made of darkness. They lurk in dark places and attack those who stray from the light. If you parlay with a shadow, you remember that you can keep them at bay with a strong light...
Fail: You can’t seem to recall what kind of creature this is other than some kind of shadow.

Attacking
DC: 0
Success: You grip your weapon, prepared to strike the shadowed fiend.
trigger combat

Cast spell
DC: 20
Success: You think quickly on your feet. Thinking of the current spells in your arsenal, you are reminded of one of the most common cantrip spells… ‘Light’. You cast it as radiant light blooms in the narrow corridor. The creature of darkness recoils in the bright light. The shadows around you seem to scurry into the depths of the cave. The flash-bomb you’ve magically created seems to have deterred the shadow from making an enemy of you. You may continue moving north.
Room cleared
Fail: You conjure magical energy around you, prepared to blast the shadowed fiend.
trigger combat

Perception
DC: 24
Success:
Attack roll small bonus
Fail: The shadow is large and imposing, sending shivers coursing through your body. You can’t tell anything peculiar about it that will help you in combat.
trigger combat

Punch
DC: 0
Success: You throw a big punch at the fiend, but it seems to phase right through it. The shadowy creature arches its back and howls, sending shivers coursing through your body.
trigger combat

Throw
DC: 0
Success: You take a lose rock from the floor and toss it at the shadow. It simply phases right through it. The shadowy creature lets out a hiss resembling a laugh. It lurches forward at you with its claws.
trigger combat

Detect magic
DC: 26
Success: You quickly decipher through your mind, studying the magic in the room. You detect some sort of illusion spell throughout the small corridor. Without moments hesitation, you counteract the illusion. The darkness begins to dissipate around you as the torches you’d become accustomed to seeing throughout this dungeon relight. The bright light pours through the corridor as the shadow reals in discomfort. It holds its claws to its eyes disoriented by the change of scenery. It begins to dissipate as the light tears through its body.
Room cleared
Fail: You try to detect if there’s any magic in the room. You get the sense that some powerful magic is at work in the room. But you can’t distinguish if it’s from the shadow itself or the corridor. In your confusion, the shadow takes the opportunity to strike.
trigger combat

Stealth
DC: 32
Success: You grab your torch and put it up to its face, it recoils as you use the instance to slip into a small crevice. The shadow shakes its head in disbelief, losing sight of you. Now you have the perfect opportunity to strike back at it with great force.
Attack roll big bonus’s
Fail: It shocking that you even thought you could slip away from an actual shadow seeing as you were standing right in front of it. It sees through your ruse quite clearly and readies its claws.
trigger combat

Intimidate
DC: 28
Success: The shadows begins to lurch out at you as you grab onto your blade and unleash the deadliest insult to its face. It recoils at your ferocity and shudders. Your display has granted you the upper hand.
Attack roll small bonus
Fail: You muster up a pathetic roar at the shadow. It is unimpressed as it lets out a hiss like laughter. Reading its claws, it prepares for combat.
trigger combat

Play dead
DC: 31
Success: With the most impressive acting of your life, you clench your chest and hold your breath. Feigning death as if you were struck by the fear of fear itself. The shadow creeps over your body confused at first. But then becomes most pleased with itself, letting out a hiss resembling laughter. It coaches back into the shadows and slips away.
Room cleared
Fail: You grab your chest and lean backwards. You let out a pathetic groan as if you were keeling over. However, the shadow is not very impressed with your lackluster performance. It lets out a roar as it readies its claws.
trigger combat

Perform
DC: 0
Success: You perform a small song in the thick of the moment. The shadow recoils with anger as the melody trickles within the small corridor. It flails its claws over its face as if shielding itself from the harmony of your tune.
Attack roll small bonus

Light, fire, torch
DC: 0
Success: An idea comes into your head. If this creature is made of darkness, then the best way to counteract it is to use light. You quickly take some cloth from inside your bag and light it on fire with your torch. The flames grow readily as you toss it on the floor. The light causes the corridor to feel completely alight. The shadow recoils in agony, screeching as it flails on the floor. As the light grows, the shadow seems to dissipate and disappear.
room cleared

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

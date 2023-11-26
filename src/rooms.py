# Below is the class for every single room in the game
import mechanics


class Room:
    event = None
    monsters = None
    description = ""
    completed_room = False

    class Actions:

        def determine_which_stat_to_roll():

            pass

        def interaction():
            pass

        def touch():
            pass

        def perception():
            pass  # roll stuff and determine if it's a pass or fail, then display text

        def animal():
            pass

        def attack():
            pass

        def brute_force():
            pass

        def spell():
            pass

        def detect_magic():
            pass

        def throw():
            pass

        def jump():
            pass

        def disable():
            pass

        def stealth():
            pass

        def talk():
            pass

        def intimidate():
            pass

        def deception():
            pass

        def play_dead():
            pass

        def seduce():
            pass

        def perform():
            pass


success = """You recall how Fey come from the Feywilds. They are synominous with the supernatural. They are often found near to specific nature locations imbued with magic. They're nature can vary between playful and mischevious to outright selfish.
    This particular Fey is a Lampesperid Queen which rules over isolated regions soaked in light. They guard countless treasures and secrets, though for those who approach them with respect, they're willing to part with knowledge or items."""
failure = """You can't recognize what kind of creature she is other than some kind of Fey or fairy."""

if __name__ == "__main__":
    pass

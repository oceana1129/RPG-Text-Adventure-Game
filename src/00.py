import create_room

room = create_room.Room(
    name="Entrance",
    event="Exploration",
    description="The demo has ended, you may type QUIT or RESTART.",
    room_cleared=False,
    room_failed=False,
    room_secret=False,
    trigger_event=False,
    trigger_name=False,
    description_cleared="",
    description_failed="",
    loot={},
    action_cleared={
        "": create_room.Action_Cleared(
            used=False,
            bonus="",
            text=""
        )
    },
    actions_cleared_navigation={
        "north": create_room.Action_Cleared_Navigation(
            navigation_text="",
            next_room=""
        )
    },
    actions_not_cleared={
        "": create_room.Action_Not_Cleared(
            used=False,
            DC=0,
            ability="int",
            bonus="",
            success_effect=False,
            success_bonus=False,
            fail_effect=False,
            success_text="",
            fail_text="",
        )
    },
    actions_not_cleared_navigation={
        "north": create_room.Action_Not_Cleared_Navigation(
            navigation_text=".",
            next_room="",
            trigger_event=""
        )
    }
)

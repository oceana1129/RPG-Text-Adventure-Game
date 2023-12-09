"""
Store all of the original values for rooms, events, and characters
"""
import character_creator
import a0
import s1
import s2
import s3
import a1
import a2
import a3
import b1
import b2

CHARACTER = character_creator.Character(character_creator.Bard())
CURRENT_ROOM = a0.room
CURRENT_EVENT = b2.event

DIRECTIONS = ["north", "south", "east", "west"]
ROOMS = {
    "entrance": a0.room,
    "s1": s1.room,
    "s2": s2.room,
    "s3": s3.room,
    "a1": a1.room,
    "a2": a2.room,
    "a3": a3.room,
    "b1": b1.room,
    "b2": b2.room,
}
EVENTS = {
    "entrance": None,
    "s1": None,
    "s2": s2.event,
    "s3": s3.event,
    "a1": a1.event,
    "a2": a2.event,
    "a3": a3.event,
    "b1": b1.event,
    "b2": b2.event,
}


def reset_game_state():
    global CHARACTER, CURRENT_ROOM, CURRENT_EVENT, DIRECTIONS, ROOMS, EVENTS
    CHARACTER = character_creator.Character(character_creator.Bard())
    CURRENT_ROOM = a0.room
    CURRENT_EVENT = b2.event
    DIRECTIONS = ["north", "south", "east", "west"]
    ROOMS = {
        "entrance": a0.room,
        "s1": s1.room,
        "s2": s2.room,
        "s3": s3.room,
        "a1": a1.room,
        "a2": a2.room,
        "a3": a3.room,
        "b1": b1.room,
        "b2": b2.room,
    }
    EVENTS = {
        "entrance": None,
        "s1": None,
        "s2": s2.event,
        "s3": s3.event,
        "a1": a1.event,
        "a2": a2.event,
        "a3": a3.event,
        "b1": b1.event,
        "b2": b2.event,
    }

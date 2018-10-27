from items import *

statue = Item("Statue",
    ItemType.FEATURE,
    "A Statue sits in the center of the park.",
    "A giant bronze statue of the city's founder. It's reflecting the sun's blinding light.",
    [
        Action(["view the statue", 
        "look at the statue"], 
        ActionType.DISPLAY, "A giant bronze statue of the city's founder. It's reflecting the sun's blinding light."),
        Action(["eat statue"], ActionType.DISPLAY, "Don't be silly - you can't eat that.")
    ]
)

lotto_ticket = Item("Lotto Ticket",
    ItemType.CRITICAL,
    "You see a Lotto Ticket on the ground.",
    "A Lotto Ticket with the numbers '23 57 12' on it.",
    [
        Action(["view the lotto ticket", 
        "look at the lotto ticket", 
        "view the lotto", 
        "look at the lotto", 
        "look at the ticket"], ActionType.DISPLAY, "A Lotto Ticket with the numbers '23 57 12' on it."),
        Action(["eat the lotto", 
        "eat the lotto ticket"], ActionType.DISPLAY, "There must be a better way to get fiber in your system."),
        Action(["take the lotto", 
        "pick up the lotto",
        "take the ticket",
        "pick up the ticket",
        "pick up the lotto ticket",
        "take the lotto ticket"], ActionType.ACTION, "The lotto ticket is in my inventory now.", ActionType.TAKE_ITEM)
    ]
)
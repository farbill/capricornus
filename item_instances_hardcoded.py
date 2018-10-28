
from items import *

statue = Item("Statue",
    ItemType.FEATURE,
    "A Statue sits in the center of the park.",
    "A giant bronze statue of the city's founder. It's reflecting the sun's blinding light.",
    [
        Action([
            "view statue",
            "view the statue",
            "look at statue",
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
        Action([
        "view lotto",
        "view lotto ticket",
        "view the lotto ticket",
        "look at lotto",
        "look at ticket",
        "look at lotto ticket",
        "look at the lotto ticket",
        "view the lotto",
        "look at the lotto",
        "look at the ticket"], ActionType.DISPLAY, "A Lotto Ticket with the numbers '23 57 12' on it."),
        Action([
        "eat the lotto",
        "eat the lotto ticket",
        "eat lotto",
        "eat ticket"], ActionType.DISPLAY, "There must be a better way to get fiber in your system."),
        Action([
        "take lotto",
        "take ticket",
        "take the lotto",
        "pick up the lotto",
        "take the ticket",
        "pick up the ticket",
        "pick up the lotto ticket",
        "take the lotto ticket"], ActionType.ACTION, "The lotto ticket is in my inventory now.", ActionType.TAKE_ITEM)
    ]
)

old_siver_coin =Item("Old silver coin",
    ItemType.NONCRITICAL,
    "There is a silver coin dropped on the steet.",
    "It's a tiny silver coin.  It has number 50 on the front side.",
    [
        Action([
        "look coin",
        "look at coin",
        "look at the coin",
        "see the coin",
        "check out the coin"], ActionType.DISPLAY, "It's a tiny silver coin.  It has number 50 on the front side."),
        Action(["eat the coin",
        "eat coin"], ActionType.DISPLAY, "Don't be silly - you will get sick!")
    ]
)

#LEGENDARY ITEMS
magic_sword = Item("Magic Sword",
    ItemType.LEGENDARY,
    "There is a sword stuck in the ground at the center of the town's square. ",
    "As I get closer, the sword starts glowing and making humming sound.",
    [
        Action([
        "view sword",
        "look at sword",
        "view the sword",
        "look at the sword",
        "inspect the sword"], ActionType.DISPLAY, "As I get closer, the sword starts glowing and making humming sound."),
        Action(["take the sword",
        "grab the sword",
        "take sword",
        "grab sword",
        "obtain the sword"], ActionType.ACTION, "You have obtained the magic sword!", ActionType.TAKE_LEGENDARY)
    ]
)

vision_orb = Item("Vision Orb",
    ItemType.LEGENDARY,
    "There is an orb glowing in blue in the spring!",
    "It's the legendary vision orb I was looking for!",
    [
        Action([
        "look at orb",
        "look at the orb",
        "see the orb",
        "check out the orb"], ActionType.DISPLAY, "It's the legendary vision orb I was looking for!"),
        Action([
        "take orb",
        "grab orb",
        "take the orb",
        "grab the orb",
        "acquire the orb",
        "pick up the orb"], ActionType.ACTION, "The vision orb is in my inventory now.", ActionType.TAKE_LEGENDARY)
    ]
)
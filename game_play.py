import gamestate
import gameaction


def game_play(ga: gameaction.GameAction):
    print("TEST PURPOSE: game_play triggered\n")

    # Done in main()
    # print("TEST PURPOSE: GameState class for a new game need to be instantiated")
    # print("TEST PURPOSE: GameAction classes need to be instantiated")

    print("TEST PURPOSE: Agent Dope class needs tobe instantiated")
    print("TEST PURPOSE: Dr. Crime class needs tobe instantiated")
    print("TEST PURPOSE: City class needs to be instantiated")
    print("TEST PURPOSE: District classes need to be instantiated")
    print("TEST PURPOSE: Item classes need to be instantiated")
    print("TEST PURPOSE: Puzzle classes need to be instantiated")


def load_game(ga: gameaction.GameAction) -> gameaction.GameAction:
    print("Load_game function called")
    print("- Call load game function in GameAction class to load into GameState")
    print("- return a loaded GameAction class obj")
    return ga
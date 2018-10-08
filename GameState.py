import json

INITIAL_NUMBER_OF_TURNS = 80
MAX_INVENTORY = 8


class GameState:
    # Initialize game state
    def __init__(self):
        self.turns_remaining = INITIAL_NUMBER_OF_TURNS
        self.current_location = "city_hall"
        self.current_inventory = []
        self.solved_puzzles = {}
        self.obtained_clues = {}

        # Legendary items
        self.vision_orb = False
        self.strength_orb = False
        self.vitality_orb = False
        self.magic_sword = False

    # Work in progress ...
    # def load_game_state(self, json_string):
    #     json_obj = json.loads(json_string)



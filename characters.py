from typing import List


class Character(object):
    def __init__(self,
                 short_description: str,
                 long_description: str):
        self._short_description = short_description
        self._long_description = long_description
        super().__init__()

    def short_description(self) -> str:
        return self._short_description

    def long_description(self) -> str:
        return self._long_description

    def __str__(self):
        return self._short_description


class AgentDope(Character):
    def __init__(self,
                 short_description: str,
                 long_description: str):
        # Mr. Dope starts with an empty set of items
        self._items = []
        super().__init__(short_description=short_description,
                         long_description=long_description)

    def add_item(self, item) -> None:
        self._items.append(item)

    def remove_item(self, remove_item) -> None:
        self._items = [item for item in self._items if remove_item != item]


class DrCrime(Character):
    def __init__(self,
                 short_description: str,
                 long_description: str,
                 puzzle,
                 dialogs: List):
        self._puzzle = puzzle
        self._dialogs = dialogs

        super().__init__(short_description=short_description,
                         long_description=long_description)


class NonPlayableCharacter(Character):
    def __init__(self,
                 short_description: str,
                 long_description: str,
                 puzzle,
                 dialogs: List):
        self._puzzle = puzzle
        self._dialogs = dialogs

        super().__init__(short_description=short_description,
                         long_description=long_description)



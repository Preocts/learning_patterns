from avgame.character import Character


class Troll(Character):
    def __init__(self) -> None:
        super().__init__()
        self.set_weapon("axe")

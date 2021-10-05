from avgame.character import Character


class King(Character):
    def __init__(self) -> None:
        super().__init__()
        self.set_weapon("bow")

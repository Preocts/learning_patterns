from avgame.character import Character


class Knight(Character):
    def __init__(self) -> None:
        super().__init__()
        self.set_weapon("sword")

from avgame.king import King
from avgame.knight import Knight
from avgame.queen import Queen
from avgame.troll import Troll


def main() -> int:
    queen = Queen()
    king = King()
    knight = Knight()
    troll = Troll()

    queen.fight()
    king.fight()
    knight.fight()
    troll.fight()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

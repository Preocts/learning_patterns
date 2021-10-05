from avgame.weapon.weaponbehavior import WeaponBehavior


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self) -> None:
        print("With speed, I fire an arrow into my target!")

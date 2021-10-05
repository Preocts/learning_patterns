from avgame.weapon.weaponbehavior import WeaponBehavior


class AxeBehavior(WeaponBehavior):
    def use_weapon(self) -> None:
        print("I swing down a might blow with my axe!")

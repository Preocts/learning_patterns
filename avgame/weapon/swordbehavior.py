from avgame.weapon.weaponbehavior import WeaponBehavior


class SwordBehavior(WeaponBehavior):
    def use_weapon(self) -> None:
        print("I swing my sword with expert skill!")

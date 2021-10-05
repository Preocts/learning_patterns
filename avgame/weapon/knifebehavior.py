from avgame.weapon.weaponbehavior import WeaponBehavior


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self) -> None:
        print("I stab with my knife, graceful and clean!")

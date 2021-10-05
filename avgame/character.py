from typing import Literal
from typing import Optional

from avgame.weapon.axebehavior import AxeBehavior
from avgame.weapon.bowandarrowbehavior import BowAndArrowBehavior
from avgame.weapon.knifebehavior import KnifeBehavior
from avgame.weapon.swordbehavior import SwordBehavior
from avgame.weapon.weaponbehavior import WeaponBehavior


class Character:
    weapon_behavior: Optional[WeaponBehavior] = None

    def set_weapon(self, weapon: Literal["sword", "axe", "knife", "bow"]) -> None:
        """Sets the weapon of choice"""
        choices = {
            "sword": SwordBehavior,
            "axe": AxeBehavior,
            "knife": KnifeBehavior,
            "bow": BowAndArrowBehavior,
        }
        choice = choices.get(weapon)
        if choice is not None:
            self.weapon_behavior = choice()

    def fight(self) -> None:
        """Uses the weapon_behavior of choice"""
        if self.weapon_behavior is None:
            print("I have no weapon to fight with!")
        else:
            self.weapon_behavior.use_weapon()

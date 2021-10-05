from abc import ABC


class WeaponBehavior(ABC):
    def use_weapon(self) -> None:
        """Override with weapon behavior"""
        raise NotImplementedError()

import pytest

from src.army.weapon import CombiRifle, NullWeapon, Weapon

class TestWeaponTestSuit:
    def test_a_weapon_has_a_modifier_based_on_range(self,):
        weapon = NullWeapon()

        assert weapon.modifier_at(0) == 0

    def test_a_combi_has_a_modifier_based_on_range(self,):
        weapon = CombiRifle()

        assert weapon.modifier_at(CombiRifle.GoodRange) == 3
        assert weapon.modifier_at(CombiRifle.MediumBadRange) == -3
        assert weapon.modifier_at(CombiRifle.BadRange) == -6

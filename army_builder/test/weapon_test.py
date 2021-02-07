from src.army.weapon import BallisticWeapon, CombiRifle, NullWeapon


class TestWeaponTestSuit:
    def test_a_weapon_has_a_modifier_based_on_range(self,):
        weapon = NullWeapon()

        assert weapon.modifier_at(0) == 0

    def test_a_ballistic_weapon_has_a_default_burst_of_one(self,):
        weapon = BallisticWeapon()

        assert weapon.burst == 1
    
    def test_a_combi_has_a_burst_of_three(self,):
        weapon = CombiRifle()

        assert weapon.burst == 3
    
    def test_a_combi_has_a_damage_of_13(self,):
        weapon = CombiRifle()

        assert weapon.damage == 13
    
    def test_a_combi_has_a_modifier_based_on_range(self,):
        weapon = CombiRifle()

        assert weapon.modifier_at(CombiRifle.GoodRange) == 3
        assert weapon.modifier_at(CombiRifle.MediumBadRange) == -3
        assert weapon.modifier_at(CombiRifle.BadRange) == -6

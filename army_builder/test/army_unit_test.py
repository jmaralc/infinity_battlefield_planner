import pytest

from src.army.armyunit import ArmyUnit
from src.army.weapon import CombiRifle

class ArmyUnitMotherObject:
    BasicUnitA = ArmyUnit()
    BasicUnitB = ArmyUnit()


class TestArmyUnitTestSuit:
    
    def test_a_new_unit_has_basic_profile_to_zero(self,):

        unit = ArmyUnitMotherObject.BasicUnitA

        assert unit.cc == 0
        assert unit.bs == 0
        assert unit.ph == 0
        assert unit.wip == 0
        assert unit.arm == 0
        assert unit.bts == 0
        assert unit.w == 0
        assert unit.ava == 0
        assert unit.points == 0
        assert unit.scw == 0

    def test_a_new_unit_can_be_initialized(self,):
        unit = ArmyUnit(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

        assert unit.cc == 1
        assert unit.bs == 1
        assert unit.ph == 1
        assert unit.wip == 1
        assert unit.arm == 1
        assert unit.bts == 1
        assert unit.w == 1
        assert unit.ava == 1
        assert unit.points == 1
        assert unit.scw == 1

    def test_a_vanilla_BS13_unit_with_no_mods_has_default_target_threshold_of_13(self,):
        unit = ArmyUnit(bs=13)

        assert unit.threshold_hit() == 13

    def test_a_vanilla_BS13_unit_with_combi_in_good_range_has_target_threshold_of_16(self,):
        unit = ArmyUnit(bs=13)
        unit.weapon = CombiRifle()

        assert unit.threshold_hit(CombiRifle.GoodRange) == 16
    
    def test_a_vanilla_BS13_unit_with_combi_in_medium_bad_range_has_target_threshold_of_10(self,):
        unit = ArmyUnit(bs=13)
        unit.weapon = CombiRifle()

        assert unit.threshold_hit(CombiRifle.MediumBadRange) == 10

    def test_a_vanilla_BS13_unit_with_combi_in_bad_range_has_target_threshold_of_7(self,):
        unit = ArmyUnit(bs=13)
        unit.weapon = CombiRifle()

        assert unit.threshold_hit(CombiRifle.BadRange) == 7


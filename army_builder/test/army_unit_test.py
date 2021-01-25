from src.army.armyunit import ArmyUnit, UnitBuilder
from src.army.weapon import CombiRifle
from src.army.cover import NoCover


class TestArmyUnitTestSuit:

    def test_a_new_unit_has_basic_profile_to_zero(self,):

        unit = UnitBuilder().build()

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

    def test_a_new_unit_has_no_cover(self,):
        unit = ArmyUnit()

        assert type(unit.cover) is NoCover

    def test_a_new_unit_has_no_skills(self,):
        unit = ArmyUnit()

        assert len(unit.skills) == 0

    def test_a_vanilla_BS13_unit_with_no_mods_has_default_target_threshold_of_13(self,):  # noqa
        unit = UnitBuilder().vanilla().ballistics(13).build()

        assert unit.threshold_to_hit() == 13

    def test_a_vanilla_BS13_unit_with_combi_in_good_range_has_target_threshold_of_16(self,):  # noqa
        unit = UnitBuilder().vanilla().ballistics(13).combi_rifle().build()

        assert unit.threshold_to_hit(CombiRifle.GoodRange) == 16

    def test_a_vanilla_BS13_unit_with_combi_in_medium_bad_range_has_target_threshold_of_10(self,):  # noqa
        unit = UnitBuilder().vanilla().ballistics(13).combi_rifle().build()

        assert unit.threshold_to_hit(CombiRifle.MediumBadRange) == 10

    def test_a_vanilla_BS13_unit_with_combi_in_bad_range_has_target_threshold_of_7(self,):  # noqa
        unit = UnitBuilder().vanilla().ballistics(13).combi_rifle().build()

        assert unit.threshold_to_hit(CombiRifle.BadRange) == 7

    def test_a_vanilla_BS13_unit_with_mimetism_minus3_has_a_shooter_penalty_of_minus3(self,):  # noqa
        unit = UnitBuilder().vanilla().ballistics(13).mimetism().build()

        assert unit.modifier_to_defend() == -3

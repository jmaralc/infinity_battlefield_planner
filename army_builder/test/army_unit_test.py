import pytest
from src.army.armyunit import ArmyUnit

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
        unit = ArmyUnit(1,1,1,1,1,1,1,1,1,1)

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

    def test_a_unit_with_no_weapon_has_probability_of_ballistic_skill_percentage(self,):

        unit = ArmyUnit(bs=13)
        assert unit.threshold_hit() == 13


def test_calculate_simple_result_probabilties_for_typical_unit_pair():
    
    encounter_context = {
        "unit1": ArmyUnit(bs=13),
        "unit2": ArmyUnitMotherObject.BasicUnitB,
        "distance" : 10,
    }

    result = compute_encounter(encounter_context)
    
    assert result["winning"] == 0.65
    assert result["both_death"] == 0
    assert result["losing"] == 0.35



def compute_encounter(context):
    unit1 = context["unit1"]
    unit2 = context["unit2"]
    distance = context["distance"]

    winning = unit1.threshold_hit()/20.0
    losing = 1 - winning
    return {
        "winning": winning,
        "both_death": 0,
        "losing": losing
    }

import pytest

from src.army.armyunit import ArmyUnit
from src.army.weapon import CombiRifle
from src.army.encounter import Encounter
class TestEncounterCalculator:

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_BS13_unit_with_null_weapon(self,):
        
        encounter = Encounter({
            "shooter": ArmyUnit(bs=13)
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.65

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_with_combi_in_good_range(self,):
        shooter = ArmyUnit(bs=13)
        shooter.weapon = CombiRifle()
        
        encounter = Encounter({
            "shooter": shooter,
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.8

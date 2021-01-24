import pytest

from src.army.armyunit import ArmyUnit
from src.army.weapon import CombiRifle
from src.army.encounter import Encounter
from src.army.cover import PartialCover

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

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_under_cover_with_combi_in_good_range(self,):
        shooter = ArmyUnit(bs=13)
        shooter.weapon = CombiRifle()
        
        target = ArmyUnit(bs=13)
        target.cover = PartialCover()

        encounter = Encounter({
            "shooter": shooter,
            "target": target,
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.65 
    
    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_with_mimetism_3minus_with_combi_in_good_range(self,):
        shooter = ArmyUnit(bs=13)
        shooter.weapon = CombiRifle()
        
        target = ArmyUnit(bs=13)
        target.skills.add(Mimetism(-3))

        encounter = Encounter({
            "shooter": shooter,
            "target": target,
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.65

    
    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_under_cover_with_mimetism_3minus_with_combi_in_good_range(self,):
        shooter = ArmyUnit(bs=13)
        shooter.weapon = CombiRifle()
        
        target = ArmyUnit(bs=13)
        target.skills.add(Mimetism(-3))
        target.cover = Cover.PartialCover

        encounter = Encounter({
            "shooter": shooter,
            "target": target,
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.35

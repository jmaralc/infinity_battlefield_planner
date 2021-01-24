import pytest

from src.army.armyunit import ArmyUnit, UnitBuilder
from src.army.weapon import CombiRifle
from src.army.encounter import Encounter
from src.army.cover import PartialCover
from src.army.skill import Mimetism


class TestEncounterCalculator:

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_with_null_weapon(self,):
        
        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).build(),
            "target": UnitBuilder().vanilla().build()
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.65

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_with_combi_in_good_range(self,):
        
        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).combi_rifle().build(),
            "target": UnitBuilder().vanilla().build(),
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.8

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_under_cover_with_combi_in_good_range(self,):

        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).combi_rifle().build(),
            "target": UnitBuilder().vanilla().partial_cover().build(),
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.65 
    
    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_with_mimetism_minus3_with_combi_in_good_range(self,):
        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).combi_rifle().build(),
            "target": UnitBuilder().vanilla().mimetism().build(),
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.65

    
    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_under_cover_with_mimetism_minus3_with_combi_in_good_range(self,):
        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).combi_rifle().build(),
            "target": UnitBuilder().vanilla().partial_cover().mimetism().build(),
            "distance": CombiRifle.GoodRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.5

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_under_cover_with_mimetism_minus3_with_combi_in_bad_range(self,):
        shooter = ArmyUnit(bs=13)
        shooter.weapon = CombiRifle()
        
        target = ArmyUnit(bs=13)
        target.skills.append(Mimetism(-3))
        target.cover = PartialCover()

        encounter = Encounter({
            "shooter": shooter,
            "target": target,
            "distance": CombiRifle.BadRange
        })
        
        result = encounter.compute()
        
        assert result["hit"] == 0.05
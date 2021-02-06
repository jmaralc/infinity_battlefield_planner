from src.army.armyunit import UnitBuilder
from src.army.weapon import CombiRifle
from src.army.encounter import Encounter

import pytest


class TestEncounterCalculator:
    
    @pytest.mark.skip
    def test_calculate_wound_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_with_combi(self):  # noqa
        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).build(),
            "target": UnitBuilder().vanilla().build(),
            "distance": 1
        })

        result = encounter.compute()

        assert result["no_wounds"] == 0.65
        assert result["one_wound"] == 0.65
        assert result["two_wounds"] == 0.65
    
    
    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_with_combi_with_saves_PH10(self):  # noqa
        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).combi_rifle().build(),
            "target": UnitBuilder().vanilla().build(),
            "distance": 1
        })

        result = encounter.compute_with_saves()

        print(result)
        # TODO: This should be checked i dont think im saving correctly
        #       Current assumption is 0.65 (BS13 + 3 COMBI = 16/20) to hit x 0.4 to save (DM13 - 1ARM - 0 COVER = 8/20)
        assert result["hit"] == 0.26
        

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_with_null_weapon(self):  # noqa

        encounter = Encounter({
            "shooter": UnitBuilder().vanilla().ballistics(13).build(),
            "target": UnitBuilder().vanilla().armor(1).build(),
            "distance": None
        })

        result = encounter.compute()

        assert result["hit"] == 0.65

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_with_combi_in_good_range(self,):  # noqa

        encounter = Encounter({
            "shooter": (
                UnitBuilder()
                .vanilla()
                .ballistics(13)
                .combi_rifle()
                .build()
            ),
            "target": UnitBuilder().vanilla().build(),
            "distance": CombiRifle.GoodRange
        })

        result = encounter.compute()

        assert result["hit"] == 0.8

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_vanilla_unit_under_cover_with_combi_in_good_range(self,): # noqa

        encounter = Encounter({
            "shooter": (
                UnitBuilder()
                .vanilla()
                .ballistics(13)
                .combi_rifle()
                .build()
            ),
            "target": UnitBuilder().vanilla().partial_cover().build(),
            "distance": CombiRifle.GoodRange
        })

        result = encounter.compute()

        assert result["hit"] == 0.65

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_with_mimetism_minus3_with_combi_in_good_range(self,):  # noqa
        encounter = Encounter({
            "shooter": (
                UnitBuilder()
                .vanilla()
                .ballistics(13)
                .combi_rifle()
                .build()
            ),
            "target": UnitBuilder().vanilla().mimetism().build(),
            "distance": CombiRifle.GoodRange
        })

        result = encounter.compute()

        assert result["hit"] == 0.65

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_under_cover_with_mimetism_minus3_with_combi_in_good_range(self):  # noqa
        encounter = Encounter({
            "shooter": (
                UnitBuilder()
                .vanilla()
                .ballistics(13)
                .combi_rifle()
                .build()
            ),
            "target": (
                UnitBuilder()
                .vanilla()
                .partial_cover()
                .mimetism()
                .build()
            ),
            "distance": CombiRifle.GoodRange
        })

        result = encounter.compute()

        assert result["hit"] == 0.5

    def test_calculate_hit_probabilities_for_one_shot_of_vanilla_BS13_unit_targeting_unit_under_cover_with_mimetism_minus3_with_combi_in_bad_range(self,):  # noqa
        encounter = Encounter({
            "shooter": (
                UnitBuilder()
                .vanilla()
                .ballistics(13)
                .combi_rifle()
                .build()
            ),
            "target": (
                UnitBuilder()
                .vanilla()
                .partial_cover()
                .mimetism()
                .build()
            ),
            "distance": CombiRifle.BadRange
        })

        result = encounter.compute()

        assert result["hit"] == 0.05

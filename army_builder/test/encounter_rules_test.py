from src.army.armyunit import UnitBuilder
from src.army.attack import AttackHitsRule
import pytest


class TestEncounterRules:

    def test_rule_returns_an_outcome(self,):
        rule = AttackHitsRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().build(),
            "shooter_rolls": (10),
            "target": UnitBuilder().build(),
            "target_rolls": (1),
            "distance": 1
        })

        assert outcome is not None

    def test_rule_throws_exception_it_doenst_have_needed_params(self,):
        with pytest.raises(Exception):
            rule = AttackHitsRule()
            rule.resolve()


class TestEncounterAttackHitRules:

    def test_attack_hit_rule_returns_true_if_hit(self,):
        rule = AttackHitsRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (10),
            "target": UnitBuilder().build(),
            "target_rolls": (1),
            "distance": 1
        })

        assert outcome["hits"] is True

    def test_attack_hit_rule_returns_false_if_roll_missess_hit_threshold(self,):  # noqa
        rule = AttackHitsRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().combi_rifle().build(),
            "shooter_rolls": (20),
            "target": UnitBuilder().build(),
            "target_rolls": (1),
            "distance": 1
        })

        assert outcome["hits"] is False
    
    @pytest.mark.skip
    def test_attack_hit_rule_returns_false_if_roll_under_threshold_but_enemy_saves_it(self,):  # noqa
        rule = AttackHitsRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().combi_rifle().build(),
            "shooter_rolls": (10),
            "target": UnitBuilder().build(),
            "target_rolls": (21),
            "distance": 1
        })

        assert outcome["hits"] is False
    
    @pytest.mark.skip
    def test_attack_hit_rule_returns_false_if_roll_under_threshold_but_enemy_shoots_and_cancels_it(self,):  # noqa
        pass

    @pytest.mark.skip
    def test_attack_hit_rule_returns_wounded_if_enemy_roll_hits(self,):  # noqa
        pass
    
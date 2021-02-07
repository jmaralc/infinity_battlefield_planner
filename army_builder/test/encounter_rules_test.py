from src.army.armyunit import UnitBuilder
from src.army.attack import UncontestedAttackRule, UncontestedToHitRule, ToSaveRule
import pytest


class TestEncounterRules:

    def test_rule_returns_an_outcome(self,):
        rule = ToSaveRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().build(),
            "shooter_rolls": (10,),
            "target": UnitBuilder().build(),
            "target_rolls": (1,),
            "distance": 1
        })

        assert outcome is not None

    def test_rule_throws_exception_it_doenst_have_needed_params(self,):
        with pytest.raises(Exception):
            rule = UncontestedToHitRule()
            rule.resolve()

class TestUncontestedToHitRules:
     
    def test_attack_hit_rule_returns_true_if_hit(self,):
        rule = UncontestedToHitRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (10,),
            "target": UnitBuilder().build(),
            "distance": 1
        })

        assert outcome["shooter_hits"] is True

    def test_attack_hit_rule_returns_true_if_at_least_one_hit(self,):
        rule = UncontestedToHitRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (10, 20),
            "target": UnitBuilder().build(),
            "distance": 1
        })

        assert outcome["shooter_hits"] is True

    def test_attack_hit_rule_returns_criticals_count_if_hit_is_critical(self,):
        rule = UncontestedToHitRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (16, 16),
            "target": UnitBuilder().physical(20).build(),
            "distance": 1
        })

        assert outcome["criticals_count"] == 2
    
    def test_attack_hit_rule_returns_false_if_roll_missess_hit_threshold(self,):  # noqa
        rule = UncontestedToHitRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (20,),
            "target": UnitBuilder().build(),
            "distance": 1
        })

        assert outcome["shooter_hits"] is False

    

class TestToSaveRules:
    def test_attack_save_rule_returns_true_if_saves(self,):
        rule = ToSaveRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (10,),
            "target": UnitBuilder().armor(1).build(),
            "target_rolls": (13,),
            "distance": 1
        })

        assert outcome["saves"] is True
        assert outcome["saves_count"] == 1

    def test_attack_save_rule_returns_false_if_fails(self,):
        rule = ToSaveRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (10,),
            "target": UnitBuilder().armor(1).build(),
            "target_rolls": (12,),
            "distance": 1
        })

        assert outcome["saves"] is False
        assert outcome["saves_count"] == 0


class TestEncounterUncontestedAttackRules:
    def test_attack_hit_rule_returns_false_if_roll_under_threshold_but_enemy_saves_it(self,):  # noqa
        rule = UncontestedAttackRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (10,),
            "target": UnitBuilder().build(),
            "target_rolls": (21,),
            "distance": 1
        })

        assert outcome["shooter_hits"] is False

    def test_attack_hit_rule_returns_true_if_at_least_one_roll_doesnt_save(self,):  # noqa
        rule = UncontestedAttackRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().ballistics(13).combi_rifle().build(),
            "shooter_rolls": (10, 10),
            "target": UnitBuilder().build(),
            "target_rolls": (21, 1),
            "distance": 1
        })

        assert outcome["shooter_hits"] is True
        assert outcome["hits_count"] == 1

class TestEncounterContestedAttackRules:
    
    @pytest.mark.skip
    def test_attack_hit_rule_returns_false_if_roll_under_threshold_but_enemy_shoots_and_cancels_it(self,):  # noqa
        pass

    @pytest.mark.skip
    def test_attack_hit_rule_returns_shooter_wounded_if_enemy_roll_hits(self,):  # noqa
        pass
    
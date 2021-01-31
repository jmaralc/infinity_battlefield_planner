from src.army.armyunit import UnitBuilder
import pytest


class Rule:
    def __init__(self, needed_context_keys=[]):
        self.__needed_context_keys = needed_context_keys

    def apply(self, context={}):
        self.__check_context_keys(context)
        return True

    def __check_context_keys(self, context):
        keys = []
        
        for key in self.__needed_context_keys:
            if key not in context:
                keys.append(keys)
    
        if len(keys) > 0:         
            message = "The following context keys are missing {}".format(keys)
            raise Exception(message)


class AttackHitsRule(Rule):
    def __init__(self):
        super().__init__(["shooter", "shooter_rolls", "target", "target_rolls"])
    
    def apply(self, context={}):
        super().apply(context)
        # Do some magic here
        return {"hits": False}
        

class TestEncounterRules:

    def test_rule_returns_an_outcome(self,):
        rule = AttackHitsRule()

        outcome = rule.apply({
            "shooter": UnitBuilder().build(),
            "shooter_rolls": (10),
            "target": UnitBuilder().build,
            "target_rolls": (1)
        })

        assert outcome is not None

    def test_rule_throws_exception_it_doenst_have_needed_params(self,):
        with pytest.raises(Exception) as e_info:
            rule = AttackHitsRule()
            rule.apply()


class TestEncounterAttackHitRules:

    def test_attack_hit_rule_returns_true_if_hit(self,):
        rule = AttackHitsRule()

        outcome = rule.apply({
            "shooter": UnitBuilder().combi_rifle().build(),
            "shooter_rolls": (10),
            "target": UnitBuilder().build,
            "target_rolls": (1)
        })

        assert outcome["hits"] is True
    
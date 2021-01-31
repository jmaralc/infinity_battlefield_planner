from src.army.armyunit import UnitBuilder
import pytest


class Rule:
    def __init__(self, needed_context_keys=[]):
        self.__needed_context_keys = needed_context_keys

    def resolve(self, context={}):
        self.__check_context_keys(context)
        return True

    def __check_context_keys(self, context):
        keys = []
        
        for key in self.__needed_context_keys:
            if key not in context:
                keys.append(keys)
    
        if len(keys) > 0:         
            message = "The following context keys are missing {0!s}".format(keys)
            raise Exception(message)


class AttackHitsRule(Rule):
    def __init__(self):
        super().__init__(["shooter", "shooter_rolls", "target", "target_rolls", "distance"])
    
    def resolve(self, context={}):
        super().resolve(context)
        
        hits = True

        shooter = context["shooter"]
        target = context["target"]
        distance = context["distance"]
        
        s_threshold = shooter.threshold_to_hit(distance)
        s_rolls = context["target_rolls"]
        
        t_threshold = target.threshold_to_save()
        t_rolls = target.threshold_to_save()
        
        if s_rolls > s_threshold:  # Make it work with multiple rolls
            hits = False
        else:
            hits = True
            if t_rolls > t_threshold:  # Make it work with multiple rolls
                hits = False 
            

        return {"hits": hits}
        

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
        with pytest.raises(Exception) as e_info:
            rule = AttackHitsRule()
            rule.resolve()


class TestEncounterAttackHitRules:

    def test_attack_hit_rule_returns_true_if_hit(self,):
        rule = AttackHitsRule()

        outcome = rule.resolve({
            "shooter": UnitBuilder().combi_rifle().build(),
            "shooter_rolls": (10),
            "target": UnitBuilder().build(),
            "target_rolls": (1),
            "distance": 1
        })

        assert outcome["hits"] is True

    @pytest.mark.skip
    def test_attack_hit_rule_returns_false_if_roll_missess_hit_threshold(self,):  # noqa
        pass
    
    @pytest.mark.skip
    def test_attack_hit_rule_returns_false_if_roll_under_threshold_but_enemy_roll_cancels_it(self,):  # noqa
        pass
    
    @pytest.mark.skip
    def test_attack_hit_rule_returns_wounded_if_enemy_roll_hits(self,):  # noqa
        pass
    
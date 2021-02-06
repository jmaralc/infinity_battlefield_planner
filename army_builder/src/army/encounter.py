from src.army.attack import AttackHitsRule, UncontestedToHitRule
from src.army.dice import DiceRoller


class Encounter():

    def __init__(self, context):
        self.context = context

    def compute(self):
        encounter_outcome = {"shooter_hits": 0}
        total_hits = 0

        attack_rule = UncontestedToHitRule()
        dice_roller = DiceRoller()
        rolls = dice_roller.all_rolls()

        for roll in rolls:
            context = self.context.copy()
            context["shooter_rolls"] = roll
            rule_outcome = attack_rule.resolve(context)
            if rule_outcome["hits"] is True:
                total_hits += 1
        encounter_outcome["shooter_hits"] = total_hits / len(rolls)

        return encounter_outcome

    def compute_with_saves(self):
        encounter_outcome = {"hit": 0}
        total_hits = 0

        attack_rule = AttackHitsRule()
        
        shooter_rolls = DiceRoller().all_rolls()
        target_rolls = DiceRoller().all_rolls()
        
        total_rolls = len(shooter_rolls) * len(target_rolls)
        
        for s_roll in shooter_rolls:
            context = self.context.copy()
            context["shooter_rolls"] = s_roll
            
            for t_roll in target_rolls:
                context["target_rolls"] = t_roll
                rule_outcome = attack_rule.resolve(context)
                if rule_outcome["hits"] is True:
                    total_hits += 1
        
        encounter_outcome["shooter_hits"] = total_hits / total_rolls
        encounter_outcome["shooter_misses"] = 1 - encounter_outcome["shooter_hits"]

        return encounter_outcome
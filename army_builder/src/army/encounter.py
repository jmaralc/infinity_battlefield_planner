from src.army.attack import UncontestedAttackRule, UncontestedToHitRule
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
            if rule_outcome["shooter_hits"] is True:
                total_hits += 1
        encounter_outcome["shooter_hits"] = total_hits / len(rolls)

        return encounter_outcome

    def compute_with_saves(self):
        encounter_outcome = {}
        total_hits = 0
        total_outcomes = 0

        attack_rule = UncontestedAttackRule()

        shooter = self.context["shooter"]
        weapon = shooter.weapon
        shooter_rolls = DiceRoller(weapon.burst).all_rolls()

        target_rolls_collection = [[(0,)]*20]
        for save_numbers in range(1, weapon.burst + 1):
            target_rolls_collection.append(
                DiceRoller(save_numbers).all_rolls()
            )
 
        for s_roll in shooter_rolls:
            context = self.context.copy()
            context["shooter_rolls"] = s_roll
            hit_outcome = attack_rule.resolve_hit(context)
            hits_count = hit_outcome["hits_count"]

            for t_roll in target_rolls_collection[hits_count]:
                context["target_rolls"] = t_roll
                rule_outcome = attack_rule.resolve(context)
                total_outcomes += 1
                if rule_outcome["shooter_hits"] is True:
                    total_hits += 1

        encounter_outcome["shooter_hits"] = total_hits / total_outcomes
        encounter_outcome["shooter_misses"] = 1 - encounter_outcome["shooter_hits"]

        return encounter_outcome

from src.army.attack import AttackHitsRule
from src.army.dice import DiceRoller


class Encounter():

    def __init__(self, context):
        self.context = context

    def __compute(self):
        shooter = self.context["shooter"]
        target = self.context["target"]
        distance = self.context.get("distance")

        s_threshold = shooter.threshold_to_hit(distance)
        t_threshold = target.modifier_to_defend()
        hit = (s_threshold + t_threshold) / 20.0

        return {"hit": hit}

    def compute(self):
        encounter_outcome = {"hit": 0}
        total_hits = 0

        attack_rule = AttackHitsRule()
        dice_roller = DiceRoller()
        rolls = dice_roller.all_rolls()

        for roll in dice_roller.all_rolls():
            context = self.context.copy()
            context["shooter_rolls"] = roll
            context["target_rolls"] = 1  # For now pay no attention to this
            rule_outcome = attack_rule.resolve(context)
            if rule_outcome["hits"] is True:
                total_hits += 1
        encounter_outcome["hit"] = total_hits / len(rolls)

        return encounter_outcome

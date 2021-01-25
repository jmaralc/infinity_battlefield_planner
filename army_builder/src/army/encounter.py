class Encounter():

    def __init__(self, context):
        self.context = context

    def compute(self):
        shooter = self.context["shooter"]
        target = self.context["target"]
        distance = self.context.get("distance")

        s_threshold = shooter.threshold_to_hit(distance)
        t_threshold = target.modifier_to_defend()
        hit = (s_threshold + t_threshold) / 20.0

        return {"hit": hit}

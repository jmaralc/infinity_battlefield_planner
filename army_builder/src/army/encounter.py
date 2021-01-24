class Encounter():

    def __init__(self, context):
        self.context = context

    def compute(self):
        shooter  = self.context["shooter"]
        distance = self.context.get("distance")

        hit         = shooter.threshold_to_hit(distance) /20.0

        return {
            "hit": hit,
        }

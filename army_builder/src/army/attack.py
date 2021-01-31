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
        
        shooter = context["shooter"]
        target = context["target"]
        distance = context["distance"]
        
        s_threshold = shooter.threshold_to_hit(distance) + target.modifier_to_defend()
        s_rolls = context["shooter_rolls"]     
        
        hits = (s_rolls <= s_threshold)  # Make it work for multiple rolls
        criticals = 0
        if s_rolls == s_threshold:
            criticals += 1            

        return {"hits": hits, "criticals": criticals}

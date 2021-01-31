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
        super().resolve(context)  # TODO: Did not find how to call __check from here
        
        shooter = context["shooter"]
        target = context["target"]
        distance = context["distance"]
        
        s_threshold = shooter.threshold_to_hit(distance) + target.modifier_to_defend()
        s_rolls = context["shooter_rolls"]     
        
        hits_count = 0
        hits = False
        for roll in s_rolls:
            if roll <= s_threshold:
                hits_count += 1
                hits = True
        
        criticals_count = 0
        for roll in s_rolls:
            if roll == s_threshold:
                criticals_count += 1

        return {"hits": hits, "criticals_count": criticals_count}


class SavesHitRule(Rule):
    def __init__(self):
        super().__init__(["target", "target_rolls"])
    
    def resolve(self, context={}):
        super().resolve(context)
       
        target = context["target"]
        t_rolls = context["target_rolls"]     
        t_threshold = target.threshold_to_save()

        saves_count = 0
        saves = False
        for roll in t_rolls:
            if roll > t_threshold:
                saves_count += 1
                saves = True

        return {"saves": saves, "saves_count": saves_count}
class Cover:
    def __init__(self, modifier):
        self.modifier = modifier

    def modifier_to_hit(self):
        return self.modifier


class NoCover(Cover):
    def __init__(self):
        super().__init__(0)

    
class PartialCover(Cover):
    def __init__(self):
        super().__init__(-3)

class Skill:
    def __init__(self, modifier):
        self.modifier = modifier

    def modifier_to_hit(self):
        return self.modifier


class Mimetism(Skill):
    def __init__(self, modifier=-3):
        super().__init__(-3)

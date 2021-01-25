class Weapon:
    def __init__(self):
        pass

    def modifier_at(self, range):
        pass


class NullWeapon(Weapon):
    def modifier_at(self, range):
        return 0


class CombiRifle(Weapon):
    GoodRange = 16
    MediumBadRange = 32
    BadRange = 48

    def modifier_at(self, range):
        result = 0
        if range <= self.GoodRange:
            result = 3
        elif range <= self.MediumBadRange:
            result = -3
        elif range <= self.BadRange:
            result = -6

        return result

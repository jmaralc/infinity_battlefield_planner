class Weapon:
    def __init__(self, damage=0):
        self.damage = damage

    def modifier_at(self, range):
        pass


class NullWeapon(Weapon):
    def modifier_at(self, range):
        return 0


class BallisticWeapon(Weapon):
    def __init__(self, damage=0, burst=1):
        self.damage = damage
        self.burst = burst


class CombiRifle(BallisticWeapon):
    GoodRange = 16
    MediumBadRange = 32
    BadRange = 48

    def __init__(self):
        super().__init__(damage=13, burst=3)

    def modifier_at(self, range):
        result = 0
        if range <= self.GoodRange:
            result = 3
        elif range <= self.MediumBadRange:
            result = -3
        elif range <= self.BadRange:
            result = -6

        return result

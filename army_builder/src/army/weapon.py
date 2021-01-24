class Weapon:
    def __init__(self):
        pass

    def modifier_at(self, range):
        pass

class NullWeapon(Weapon):
    def modifier_at(self, range):
        return  0
    
class CombiRifle(Weapon):
    GoodRange       = 16
    MediumBadRange  = 32
    BadRange        = 48
    
    def modifier_at(self, range):
        if range <= self.GoodRange:
            return  3
        if range <= self.MediumBadRange:
            return -3
        if range <= self.BadRange:
            return -6
        return -20
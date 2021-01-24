
from src.army.weapon import NullWeapon

class ArmyUnit:

    def __init__(
        self, cc=0, bs=0, ph=0, wip=0, arm=0, bts=0, w=0, ava=0, points=0, scw=0
    ):
        self.cc = cc
        self.bs = bs
        self.ph = ph
        self.wip = wip
        self.arm = arm
        self.bts = bts
        self.w = w
        self.ava = ava
        self.points = points
        self.scw = scw
        self.weapon = NullWeapon()
        self.skills = []

    def threshold_to_hit(self, range=0):
        return self.bs + self.weapon.modifier_at(range)

    def modifier_to_defend(self):
        if len(self.skills) > 0:
            return self.skills[0].modifier_to_hit()
        return 0
    


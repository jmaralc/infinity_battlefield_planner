
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

    def threshold_hit(self, range=0):
        return self.bs + self.weapon.modifier_at(range)


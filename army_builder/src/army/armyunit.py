
from src.army.weapon import NullWeapon, CombiRifle
from src.army.cover import NoCover, PartialCover
from src.army.skill import Mimetism


class ArmyUnit:

    def __init__(
        self,
        cc=0, bs=0, ph=0, wip=0, arm=0, bts=0, w=0, ava=0, points=0, scw=0
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
        self.skills = set()
        self.cover = NoCover()

    def threshold_to_hit(self, range=0):
        return self.bs + self.weapon.modifier_at(range)
    
    def threshold_to_save(self):
        return 20  # For now... always fail, most likely will have to change

    def modifier_to_defend(self):
        modifier = 0
        for skill in self.skills:  # make this work with non defensive skills
            modifier += skill.modifier_to_hit()
        modifier += self.cover.modifier_to_hit()
        return modifier


class UnitBuilder:
    def __init__(self):
        self.unit = ArmyUnit()

    def vanilla(self):
        self.unit = ArmyUnit(
            cc=10,
            bs=10,
            ph=10,
            wip=10,
            arm=1,
            bts=1,
            w=1,
            ava=1,
            points=10,
            scw=0
        )
        return self

    def ballistics(self, profile=10):
        self.unit.bs = profile
        return self

    def mimetism(self, modifier=-3):
        self.unit.skills.add(Mimetism(modifier))
        return self

    def no_cover(self):
        self.unit.cover = NoCover()
        return self

    def partial_cover(self):
        self.unit.cover = PartialCover()
        return self

    def combi_rifle(self):
        self.unit.weapon = CombiRifle()
        return self

    def build(self):
        return self.unit

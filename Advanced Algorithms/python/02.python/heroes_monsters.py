import random as rd

class DiceSix:
    def __init__(self) -> None:
        pass

    @staticmethod
    def throw(dices, faces, isInit):
        values = []
        for _ in range(0, dices):
            values.append(rd.randint(1, faces))
        if isInit:
            values.remove(min(values))
        return sum(values)

class Personnage:
    def __init__(self):
        self._end = DiceSix.throw(dices=4, faces=6, isInit=1)
        self._forc = DiceSix.throw(dices=4, faces=6, isInit=1)
        self._pv = self._end + self.modifier(self._end)
        self._maxpv = self._pv
        print(f"Endurance: {self._end}, Force: {self._forc}, PV: {self._pv}")

    @property
    def end(self):
        return self._end

    @property
    def forc(self):
        return self._forc

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, value):
        self._pv = value

    def modifier(self, value):
        if value < 5:
            return -1
        elif value < 10:
            return 0
        elif value < 15:
            return 1
        else:
            return 2

    def hit(self, target):
        damage = DiceSix.throw(dices=1, faces=4, isInit=0) + self.modifier(self.forc)
        target.pv -= damage
        print(f"Damage: {damage} -> Target PV: {target.pv}")
        if target.pv <= 0:
            print("Target is dead")
            target.pv = 0

class Hero(Personnage):
    def __init__(self, h_type):
        super().__init__()
        if h_type not in ["Human", "Dwarf"]:
            raise ValueError("Hero should be a Human or a Dwarf")
        self.h_type = h_type
        if self.h_type == "Human":
            self._forc += 1
            self._end += 1
        else:
            self._end += 2
        self._pv = self._end + self.modifier(self._end)
        print(f"Hero Type: {self.h_type}, Endurance: {self._end}, Force: {self._forc}, PV: {self._pv}")

class Monster(Personnage):
    def __init__(self, m_type):
        super().__init__()
        if m_type not in ["Wolf", "Orc", "Dragonet"]:
            raise ValueError("Monster should be a Wolf, Orc, or Dragonet")
        self.m_type = m_type
        self.gold = DiceSix.throw(dices=1, faces=6, isInit=0) if m_type in ["Orc", "Dragonet"] else 0
        self.leather = DiceSix.throw(dices=1, faces=4, isInit=0) if m_type in ["Wolf", "Dragonet"] else 0
        if m_type == "Orc":
            self._forc += 1
        elif m_type == "Dragonet":
            self._end += 1
            self._pv = self._end + self.modifier(self._end)
        print(f"Monster Type: {self.m_type}, Endurance: {self._end}, Force: {self._forc}, PV: {self._pv}, Gold: {self.gold}, Leather: {self.leather}")

def main():
    hero = Hero("Human")
    monsters = [Monster("Wolf"), Monster("Orc"), Monster("Dragonet")]
    
    while hero.pv > 0 and len(monsters) > 0:
        target = monsters.pop(0)
        while target.pv > 0 and hero.pv > 0:
            hero.hit(target)
            if target.pv > 0:
                target.hit(hero)
        if hero.pv > 0:
            print(f"Hero looted: {target.gold} gold, {target.leather} leather")
            hero._pv = hero._maxpv
    
    if hero.pv > 0:
        print("Hero wins!")
    else:
        print("Hero is dead. Game over.")

if __name__ == "__main__":
    main()

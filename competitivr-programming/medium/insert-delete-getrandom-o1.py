import random
class RandomizedSet:
    def __init__(self):
        self.j = set()
        self.l = []
        self.discarded = set()
    def insert(self, val: int) -> bool:
        if val not in self.j:
            self.j.add(val)
            if val in self.discarded:
                self.discarded.remove(val)
                return True
            self.l.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if val  in self.j:
            self.j.remove(val)
            self.discarded.add(val)
            return True
        return False
    def getRandom(self) -> int:
        v = random.choice(self.l)
        while v in self.discarded:
            v = random.choice(self.l)
        return v
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
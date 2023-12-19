from collections import defaultdict
class ATM:

    def __init__(self):
        self.notes = defaultdict(int)
        self.mx = [500,200,100,50,20]
    def deposit(self, banknotesCount: List[int]) -> None:
        for x in range(5):
            self.notes[self.mx[4-x]] += banknotesCount[x]
    def withdraw(self, amount: int) -> List[int]:
        v = 0
        outs = [0]*5
        while v < 5:
            if self.notes[self.mx[v]] < 1:
                v += 1
                continue
            elif self.mx[v] > amount:
                v += 1
                continue
            needed = amount//self.mx[v]
            if needed < self.notes[self.mx[v]]:
                self.notes[self.mx[v]] -= needed
                outs[4-v] = needed
                amount -= needed*self.mx[v]
            else:
                outs[4-v] = self.notes[self.mx[v]]
                amount -= self.notes[self.mx[v]]*self.mx[v]
                self.notes[self.mx[v]] = 0
            v += 1
            if amount == 0:
                return outs
        if amount != 0:
            for x in range(5):
                self.notes[self.mx[4-x]] += outs[x]
            return [-1]
        return outs


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
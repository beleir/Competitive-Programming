from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.d = defaultdict(int)
        self.fr = defaultdict(set)
    def add(self, number: int) -> None:
        self.fr[self.d[number]].discard(number)
        self.fr[self.d[number]+1].add(number)
        self.d[number] += 1
    def deleteOne(self, number: int) -> None:
        if self.d[number] > 0:
            self.fr[self.d[number]].discard(number)
            self.d[number] -= 1
            self.fr[self.d[number]].add(number)
    def hasFrequency(self, frequency: int) -> bool:
        return len(self.fr[frequency]) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
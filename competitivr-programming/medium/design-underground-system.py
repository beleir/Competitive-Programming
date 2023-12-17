from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.users = defaultdict(list)
        self.station = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id]=[stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.station[(self.users[id][0], stationName)].append(t-self.users[id][1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.station[(startStation, endStation)])/len(self.station[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
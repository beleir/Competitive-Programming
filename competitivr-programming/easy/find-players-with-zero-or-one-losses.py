from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        gamers = {}
        z = set()
        for i in matches:
            if i[0] not in gamers:
                gamers[i[0]] = [0,0]
            if i[1] not in gamers:
                gamers[i[1]] = [0,0]
            gamers[i[0]][0] += 1
            gamers[i[1]][1] += 1
        outs = [[],[]]
        for x in gamers:
            if gamers[x][1] == 0 and gamers[x][0] > 0:
                outs[0].append(x)
            if gamers[x][1] == 1:
                outs[1].append(x)
        outs[0].sort()
        outs[1].sort()
        return outs
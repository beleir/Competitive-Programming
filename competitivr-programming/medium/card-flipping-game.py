from collections import defaultdict
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ups = defaultdict(list)
        down = defaultdict(list)
        for x in range(len(fronts)):
            ups[fronts[x]].append(x)
        for y in range(len(backs)):
            down[backs[y]].append(y)
            
        ms = 10**9
        
        for i in range(len(fronts)):
            if backs[i] >= ms:
                continue
            if fronts[i]!=backs[i]:
                broken = False
                for v in down[backs[i]]:
                    if fronts[v] == backs[i]:
                        broken = True
                        break
                if not broken:
                    ms = backs[i]
        for i in range(len(fronts)):
            if fronts[i] >= ms:
                continue
            if fronts[i]!=backs[i]:
                broken = False
                for v in ups[fronts[i]]:
                    if backs[v] == fronts[i]:
                        broken = True
                        break
                if not broken:
                    ms = fronts[i]
        if ms == 10**9:
            return 0
        return ms
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        j= []
        for i in paths:
            j.append(list(i.split(" ")))
        for x in j:
            for s in range(1,len(x)):
                v = x[s].index("(")
                r = x[s].index(")")
                d[x[s][v+1:r]].append(x[0]+"/"+x[s][:v])
        outs = []
        for cv in d:
            if len(d[cv]) > 1:
                outs.append(d[cv])
        return outs
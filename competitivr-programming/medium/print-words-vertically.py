class Solution:
    def printVertically(self, s: str) -> List[str]:
        outs = []
        v = list(s.split())
        maxs = 0
        for x in v:
            if len(x) > maxs:
                maxs = len(x)
        for xn in range(len(v)):
            v[xn] += " "*(maxs - len(v[xn]))
        for vf in range(len(v[0])):
            j = ""
            for fv in range(len(v)):
                j += v[fv][vf]
            outs.append(j.rstrip())
            j = ""
        return outs
                    
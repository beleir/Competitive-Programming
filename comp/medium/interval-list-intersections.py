class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        outs = []

        i,j = 0,0
        while i < len(f) and j < len(s):
            fi = max(f[i][0],s[j][0])
            si = min(f[i][1], s[j][1])

            if fi<=si:
                outs.append([fi,si])
            if f[i][1] <= s[j][1]:
                i += 1
                continue
            j+=1
        return outs
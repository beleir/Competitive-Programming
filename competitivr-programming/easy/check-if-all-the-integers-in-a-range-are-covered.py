class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        v = sorted(ranges,key = lambda x: x[0])
        i = 0
        while left <= right:
            broken = False
            print(i, v,left)
            while i < len(v):
                print(v[i][0],v[i][1]+1)
                if left in range(v[i][0],v[i][1]+1):
                    left = v[i][1]
                    i += 1
                    broken = True
                    break
                i += 1
            if not broken:
                return False
            left += 1
        return True
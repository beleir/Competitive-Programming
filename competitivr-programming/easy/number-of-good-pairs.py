from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        r = defaultdict(int)
        for i in nums:
            r[i] += 1
        sumy = 0
        for x in r:
            if r[x]>1:
                v = int(((r[x]-1)/2)*(r[x]))
                sumy += v
        return sumy
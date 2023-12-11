from collections import defaultdict
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        j = defaultdict(list)
        rc = defaultdict(int)
        for x in range(len(operations)):
            j[operations[x][0]].append([operations[x][1],x])
        def dfs(n,p):
            if n not in j:
                return n
            for g in j[n]:
                if g[1] > p:
                    return dfs(g[0],g[1])
            return n
        for jc in j:
            rc[jc] = dfs(j[jc][0][0],j[jc][0][1])
        for z in range(len(nums)):
            if nums[z] in rc:
                nums[z] = rc[nums[z]]
        return nums
        
class Solution:
    def reductionOperations(self, nums) -> int:
        nums.sort()
        p = []
        moves = 0
        i = 0
        while i < len(nums):
            j = i + 1
            ct = 1
            while j < len(nums) and nums[i] == nums[j]:
                ct += 1
                j += 1
            p.append([nums[i],ct])
            i = j
        for s in range(len(p)):
            moves += s*p[s][1]
        return moves
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == len(nums):
            return sum(nums)/k
        starting_pt = nums[:k]
        maxs = sum(starting_pt)
        real = maxs
        i = k
        while i < len(nums):
            maxs -= nums[i-k]
            maxs += nums[i]
            if maxs > real:
                real = maxs
            i += 1
        
        return real/k
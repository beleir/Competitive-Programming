class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        i,j = 0, len(nums)-1
        nums.sort()
        while i < j:
            if nums[i]+nums[j] == k:
                ops += 1
                i += 1
                j -= 1
            elif nums[i]+nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
        return ops
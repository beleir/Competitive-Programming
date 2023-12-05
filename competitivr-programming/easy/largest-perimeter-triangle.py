class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if i+2 >= len(nums):
                continue
            if nums[i] + nums[i+1] <= nums[i+2] or nums[i] + nums[i+2] <= nums[i+1] or nums[i+2] + nums[i+1] <= nums[i]:
                continue
            if nums[i] == 0 or nums[i+1]==0 or nums[i+2]==0:
                continue
            else:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
        
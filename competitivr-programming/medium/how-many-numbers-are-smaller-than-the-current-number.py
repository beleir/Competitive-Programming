class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numbers_lower = 0
        outed = []
        for i in nums:
            for k in range(len(nums)):
                if i > nums[k]:
                    numbers_lower += 1
            outed.append(numbers_lower)
            numbers_lower = 0
        return outed
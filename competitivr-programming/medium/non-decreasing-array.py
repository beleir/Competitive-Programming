class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ct = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if i != 0:
                    if nums[i-1] > nums[i+1] and (i+1!= len(nums)-1 and nums[i+2]<nums[i]):
                        return False
                ct +=1
            if ct > 1:
                return False
        return True
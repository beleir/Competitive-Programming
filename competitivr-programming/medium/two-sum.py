class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target_acquired = False
        List = []
        size = len(nums)
        sum = 0
        for i in range(size):
            for j in range(size):
                if j != i:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        List.append(i)
                        List.append(j)
                        return List
                

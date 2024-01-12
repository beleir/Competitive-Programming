class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        mins = float('inf')
        nums.sort()
        for i in range(len(nums)):

            k = i+1
            j = len(nums)-1

            while k < j:
                
                s = nums[i]+nums[j]+nums[k]
                if abs(target-s) < abs(target-mins):
                    mins = s
                if s == target:
                    return target
                elif s < target:
                    k += 1
                else:
                    j-=1
        return mins
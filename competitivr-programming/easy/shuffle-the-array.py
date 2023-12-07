class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = len(nums)//2
        def helper(n,v,l):
            if n >= len(nums):
                return []
            elif n%2:
                return [nums[r+v]] + helper(n+1,v+1,l)
            else:
                return [nums[l]] + helper(n+1,v,l+1)
        return helper(0,0,0)
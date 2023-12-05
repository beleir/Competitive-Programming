class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons = 0
        curr = 0
        for i in nums:
            if i == 0:
                if curr > cons:
                    cons = curr
                curr = 0
            else:
                curr += 1
        if curr > cons:
            cons = curr
        return cons
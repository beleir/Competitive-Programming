class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers)-1
        sv = 0
        while l < r:
            sv = numbers[l]+numbers[r]
            if sv > target:
                r -= 1
            elif sv < target:
                l += 1
            else:
                return [l+1,r+1]
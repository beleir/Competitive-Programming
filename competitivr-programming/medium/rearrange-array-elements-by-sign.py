class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = 0
        p = []
        n = []
        vs = []
        for i in nums:
            if i >= 0:
                p.append(i)
            else:
                n.append(i)
        for j in range(len(nums)):
            if j % 2==0:
                nums[j] = p[r]
                r += 1
            else:
                nums[j] = n[l]
                l += 1
        return nums
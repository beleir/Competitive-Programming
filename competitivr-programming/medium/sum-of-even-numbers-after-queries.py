class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        outs = []
        sqsum = 0
        for i in nums:
            if not i%2:
                sqsum += i
        for x in queries:
            if not nums[x[1]] % 2:
                sqsum -= nums[x[1]]
            nums[x[1]] += x[0]
            if not (nums[x[1]]) % 2:
                sqsum += (nums[x[1]])
            outs.append(sqsum)
        return outs
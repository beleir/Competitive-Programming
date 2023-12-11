from collections import deque
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        j = []
        less = deque()
        higher = deque()
        equal = deque()
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                higher.append(i)
        while len(less) != 0:
            j.append(less.popleft())
        while len(equal) != 0:
            j.append(equal.popleft())
        while len(higher) != 0:
            j.append(higher.popleft())
        return j
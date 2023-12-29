from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        j = defaultdict(int)
        r = defaultdict(int)
        for i in nums1:
            j[i] += 1
        for x in nums2:
            r[x] += 1
        out = []
        for v in j:
            if j[v] <= r[v]:
                for dv in range(j[v]):
                    out.append(v)
            else:
                for fv in range(r[v]):
                    out.append(v)
        return out
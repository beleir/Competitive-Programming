class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ks = {}
        for i in range(len(arr2)):
            ks[arr2[i]] = [i]
        added = []
        for j in range(len(arr1)):
            if arr1[j] not in ks:
                added.append(arr1[j])
                continue
            ks[arr1[j]].append(arr1[j])
        s = []
        for x in ks:
            s.append(ks[x])
        s.sort()
        v = []
        for cv in s:
            v += cv[1:]
        added.sort()
        v += added
        return v

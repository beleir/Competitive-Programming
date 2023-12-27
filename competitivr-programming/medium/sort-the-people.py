class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        f = {}

        for i in range(len(names)):
            f[heights[i]] = names[i]
        heights.sort(reverse=True)
        v = []
        for x in heights:
            v.append(f[x])
        return v
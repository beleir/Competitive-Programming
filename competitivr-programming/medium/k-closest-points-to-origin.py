class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        cd = []
        size = len(points)
        closest = []
        for i in range(size):
            heappush(cd,(points[i][0] ** 2 + points[i][1] ** 2, points[i]))
        for i in range(k):
            closest.append(heappop(cd)[1])
        return closest
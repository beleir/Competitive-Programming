class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ccw = 0
        cw = 0
        n = len(distance)
        i = start
        while i != destination:
            if (i-1) < 0:
                i = n
            ccw += distance[(i-1)%n]
            i -= 1
        x = start
        while x != destination:
            cw += distance[(x)%n]
            x = ((x+1)%n)
        return min(ccw,cw)
            
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = 0
        steps = 0
        amt = 0
        for i in range(len(plants)):
            curr += plants[i]
            if i == len(plants)-1:
                steps += 1
                continue
            if curr + plants[i+1] > capacity:
                steps += 2*(i+1)
                curr = 0
            steps += 1
        return steps
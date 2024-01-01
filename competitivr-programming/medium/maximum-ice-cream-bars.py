import math
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        p = [0]*(max(costs)+1)

        for i in costs:
            p[i] += 1
        paid = 0
        bought = 0
        for i in range(len(p)):
            paid += p[i]*i
            bought += p[i]
            if paid >= coins:
                if paid == coins:
                    return bought
                v = paid - coins
                rs = math.ceil(v/i)
                return bought - rs
        return bought
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = (num-3)/3
        if int(x) == x:
            return [int(x),int(x+1),int(x+2)]
        return []
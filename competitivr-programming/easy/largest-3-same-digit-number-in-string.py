class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num)<3:
            return ""
        maxs = 0
        rv = ""
        for i in range(len(num)):
            if num[i]*3 == num[i:i+3] and maxs <= int(num[i]*3):
                rv = num[i]*3
                maxs = int(rv)
        return rv
class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num)-1

        while i >= 0 and not int(num[i])%2:
            i -= 1
        if i < 0:
            return ""
        return num[:i+1]
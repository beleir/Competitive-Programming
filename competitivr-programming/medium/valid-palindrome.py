from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        A = deque()
        B = []
        s = s.lower()
        for i in s:
            if i == " " or not i.isalpha():
                if i.isnumeric():
                    B.append(i)
                continue
            B.append(i)
        for j in B:
            A.append(j)
        c = 0
        while A.__len__():
            k = A.pop()
            if k != B[c]:
                return False
            c += 1
        return True
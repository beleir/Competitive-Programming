class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        size = len(s)
        for i in range(size):
            if i == size - 1:
                result += romans[s[i]]
            else:
                if romans[s[i]] >= romans[s[i + 1]]:
                    result += romans[s[i]]
                else:
                    result -= romans[s[i]]

        return result
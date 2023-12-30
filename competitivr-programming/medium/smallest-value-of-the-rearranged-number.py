class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 0:
            p = str(num)
            v = list(p[1:].strip())
            v.sort(reverse = True)
            out = ""
            zeros = 0
            for i in v:
                if out == "" and i == "0":
                    zeros += 1
                elif zeros > 0:
                    out += "0"*zeros
                    out += i
                    zeros = 0
                else:
                    out += i 
            return -int(out)
        else:
            p = str(num)
            v = list(p.strip())
            v.sort()
            out = ""
            zeros = 0
            for i in v:
                if out == "" and i == "0":
                    zeros += 1
                elif zeros > 0:
                    out += i
                    out += "0"*zeros
                    zeros = 0
                else:
                    out += i
            return int(out)
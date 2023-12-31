class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numbers = {"0":0,"1":1,
                    "2":2,"3":3,
                    "4":4,"5":5,
                    "6":6,"7":7,
                    "8":8,"9":9}
        nu1 = 0
        nu2 = 0
        for i in range(len(num1)):
            nu1 += numbers[num1[i]] * (10**(len(num1)-1-i))
        for j in range(len(num2)):
            nu2 += numbers[num2[j]] * (10**(len(num2)-1-j))
        return str(nu1 * nu2) 
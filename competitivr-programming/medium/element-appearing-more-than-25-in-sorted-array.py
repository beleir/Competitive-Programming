class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        j = int(len(arr)*0.25)
        ct = 1
        v = arr[0]
        for i in range(1,len(arr)):
            if ct > j:
                return arr[i-1]
            if v == arr[i]:
                ct+=1
                continue
            else:
                ct = 1
                v = arr[i]
        return v
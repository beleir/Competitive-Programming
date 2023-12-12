class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        v = [0]*len(boxes)
        for i in range(len(boxes)):
            k = 0
            for j in range(i-1,-1,-1):
                if boxes[j]=="1":
                    k += abs(i-j)
            for f in range(i+1,len(boxes)):
                if boxes[f]=="1":
                    k += abs(i-f)

            v[i] = k
        return v
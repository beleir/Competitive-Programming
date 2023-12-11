class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        arr.sort()
        j = len(arr)//3
        ct = 1
        v = arr[0]
        r = set()
        outs = []
        for i in range(1,len(arr)):
            if ct > j:
                if arr[i-1] not in r:
                    outs.append(arr[i-1])
                    r.add(arr[i-1])
                ct = 1
            if v == arr[i]:
                ct += 1
                continue
            else:
                ct = 1
                v = arr[i]
        if ct > j and arr[len(arr)-1] not in r:
            outs.append(arr[len(arr)-1])
        return outs
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        outs = []
        p = 0
        while p < len(arr):
            v = max(arr[:len(arr)-p])
            pn = arr.index(v)
            outs.append(pn+1)
            vs = 0 
            while vs < ((pn+1)//2):
                arr[vs],arr[pn-vs] = arr[pn-vs], arr[vs]
                vs += 1
            if arr == sorted(arr):
                break
            outs.append(len(arr)-p)
            pr = 0
            while pr < ((len(arr)-p)//2):
                arr[pr],arr[len(arr)-1-p-pr] = arr[len(arr)-1-p-pr], arr[pr]
                pr += 1
            p += 1
        return outs
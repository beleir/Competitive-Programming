class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        decreased = 0
        flag = False
        increased = 1
        for i in range(len(arr)-1):
            if i == 0 and arr[i] > arr[i+1]:
                return False
            if arr[i] == arr[i+1]:
                return False
            if arr[i] > arr[i+1] and flag == True:
                decreased += 1
                flag = False
            if arr[i] < arr[i+1]:
                if decreased > 0:
                    return False
                flag = True
        if decreased != 1:
            return False
        return True
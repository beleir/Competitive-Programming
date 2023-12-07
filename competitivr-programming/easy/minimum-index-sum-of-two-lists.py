class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s = set(list2)
        mins = 10**9
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i+j < mins:
                        outs = []
                        mins = i+j
                        outs.append(list1[i])
                    elif i+j == mins:
                        outs.append(list1[i])
        return outs
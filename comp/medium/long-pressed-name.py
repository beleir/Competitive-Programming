class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        original = ""
        k = 0
        i = 0
        while i < len(typed):
            if i == 0:
                if name[0]!=typed[0]:
                    return False
                original += typed[0]
                i +=1
                continue
            if original == name:
                if typed[i] != original[-1]:
                    return False
                i += 1
                continue
            if len(original)<len(name) and typed[i]==name[len(original)]:
                original += typed[i]
                i += 1
                continue
            else:
                k = i
                while k < len(typed) and typed[k]==original[-1]:
                    k+=1
                i = k
                if i< len(typed) and len(original)< len(name) and typed[i] != name[len(original)]:
                    return False
                if i<len(typed):
                    original += typed[i]
            i += 1
        if original != name:
            return False
        return True
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        chk = {}
        out = 0
        for i in range(len(strs)):
            for x in range(len(strs[0])):
                
                if x not in chk:
                    chk[x] = [strs[i][x]]
                elif chk[x][-1] == "ct":
                    continue
                else:
                    if chk[x][-1] != "ct" and ord(chk[x][-1]) > ord(strs[i][x]):
                            out += 1
                            chk[x].append("ct")
                    else:
                        chk[x].append(strs[i][x])
        return out
          
    
            
                     
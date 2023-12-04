class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        i = 0
        while i < len(command):
            if command[i] == "(" and command[i+1]==")":
                s += "o"
                i += 2
                continue
            elif command[i] == "(" and command[i+1]=="a":
                s += "al"
                i += 4
                continue
            s += "G"
            i += 1
        return s
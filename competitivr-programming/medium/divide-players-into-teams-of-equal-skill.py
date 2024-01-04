class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = skill[0] + skill[-1]
        pro = -1
        for i in range(len(skill)//2):
            if i == 0:
                pro = skill[0] * skill[-1]
            elif n == (skill[i] + skill[-1-i]):
                n =  skill[i] + skill[-1-i]
                pro += skill[i] * skill[-1-i]
            else:
                return -1
        return pro
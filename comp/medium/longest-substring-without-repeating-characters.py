class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        starting,leader = 0,0
        longest = 0
        while leader < len(s):
            if leader == len(s)-1 and (s[leader] not in d or d[s[leader]]<starting):
                longest = max(longest, leader-starting+1)
                leader += 1
            elif s[leader] in d and d[s[leader]] >= starting:
                longest = max(longest, leader-starting)
                starting = d[s[leader]]+1
            else:
                d[s[leader]] = leader
                leader += 1
        return longest
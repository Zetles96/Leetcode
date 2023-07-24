# https://leetcode.com/problems/valid-anagram/
# Algo: Hash Table

# Too slow
# but manages to pass the test and should use less space than the solution below
# class Solution:
# def isAnagram(self, s: str, t: str) -> bool:
#     if sorted(s) == sorted(t):
#         return True
#     else:
#         return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = {}, {}
        for n in range(len(s)):
            s_map[s[n]] = s_map.get(s[n], 0) + 1
            t_map[t[n]] = t_map.get(t[n], 0) + 1
        for c in s_map:
            if c not in t_map or s_map[c] != t_map[c]:
                return False
        return True

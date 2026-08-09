class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map1={}
        char_map2={}
        for i in range(len(s)):
            char_map1[s[i]]= 1 + char_map1.get(s[i], 0)
            char_map2[t[i]]= 1 + char_map2.get(t[i], 0)

        return char_map2==char_map1
                    
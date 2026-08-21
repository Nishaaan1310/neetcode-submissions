class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        length=0
        letter_map={}
        while i< len(s) and j < len(s):
            if s[j] in letter_map:
                length= max(length, j-i)
                if i <= letter_map[s[j]]:
                    i = letter_map[s[j]] + 1
            letter_map[s[j]]=j
            j += 1
        return max(length, j-i) 
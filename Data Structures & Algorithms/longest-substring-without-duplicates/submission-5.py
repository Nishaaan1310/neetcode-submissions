class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        length=0
        letter_map={}
        for j in range(len(s)):
            if s[j] in letter_map:
                i = max(letter_map[s[j]] + 1, i)
            letter_map[s[j]] = j
            length = max(length, j-i + 1)
        return length
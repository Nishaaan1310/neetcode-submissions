class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        max_freq=0
        freq_map={}
        max_length = 0
        for j in range(len(s)):
            freq_map[s[j]] = freq_map.get(s[j], 0) + 1
            max_freq = max(max_freq, freq_map[s[j]])
            window = j - i + 1
            if (window - max_freq)>k:
                freq_map[s[i]] = freq_map.get(s[i], 0) - 1
                i += 1
            max_length = max(max_length, j-i+1)
        return max_length


        
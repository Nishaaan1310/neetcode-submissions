class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        count_1 = {}
        for char in t:
            count_1[char] = count_1.get(char, 0) + 1

        required = len(count_1)
        match = 0
        window = {}
        i = 0

        output_len = float('inf')
        start = 0
        
        for j in range(len(s)):
            window[s[j]] = window.get(s[j], 0) + 1

            if s[j] in count_1 and count_1[s[j]] == window[s[j]]:
                match += 1

            while required == match:
                if output_len > (j-i+1):
                    start = i
                    output_len = j-i+1

                window[s[i]] -= 1
                if s[i] in count_1 and count_1[s[i]] > window[s[i]]:
                    match -= 1

                i += 1

        return s[start : start + output_len] if output_len != float('inf') else ""


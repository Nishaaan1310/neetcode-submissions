class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""

        if len(t) > len(s):
            return output

        count_1 = {}
        for char in t:
            count_1[char] = count_1.get(char, 0) + 1

        required = len(count_1)
        match = 0
        window = {}
        i = 0

        for j in range(len(s)):
            window[s[j]] = window.get(s[j], 0) + 1

            if s[j] in count_1 and count_1[s[j]] == window[s[j]]:
                match += 1

            while required == match:
                if len(output) == 0 or len(output) > (j-i+1):
                    output = s[i : j+1]

                window[s[i]] -= 1
                if s[i] in count_1 and count_1[s[i]] > window[s[i]]:
                    match -= 1

                i += 1

        return output



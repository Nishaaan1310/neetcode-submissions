class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map1={}
        char_map2={}
        for char in s:
            if char in char_map1:
                count=char_map1[char]
                char_map1[char]=count+1
            else:
                char_map1[char]=1
        for char in t:
            if char in char_map2:
                count=char_map2[char]
                char_map2[char]=count+1
            else:
                char_map2[char]=1

        return char_map2==char_map1
                    
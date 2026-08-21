class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count= [0] * 26
        s2_count = [0] * 26
        if len(s1)> len(s2):
            return False

        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            s1_count[index]+= 1

        i = 0
        j = 0
        for j in range(len(s2)):
            index = ord(s2[j]) - ord('a')
            if j< len(s1):
                s2_count[index]+= 1

            else:
                index_left = ord(s2[i]) - ord('a')
                s2_count[index_left]-= 1
                s2_count[index]+= 1
                i += 1

            if s1_count == s2_count:
                return True

        return False


        
                


        
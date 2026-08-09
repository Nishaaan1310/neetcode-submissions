class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                if length<count:
                    length=count
            else:
                count=0
        return length

        
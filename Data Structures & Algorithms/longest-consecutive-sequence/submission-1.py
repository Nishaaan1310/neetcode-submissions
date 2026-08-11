class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        Max_length=0
        for num in set_nums:
            if num-1 not in set_nums:
                length=1
                while (num+length) in set_nums:
                    length+=1
                if Max_length<length:
                    Max_length=length

        return Max_length
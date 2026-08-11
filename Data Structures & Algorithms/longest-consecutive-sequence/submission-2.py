class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        Max_length=0
        for num in set_nums:
            if num-1 not in set_nums:
                value=num
                while value in set_nums:
                    value=value+1
                Max_length=max(Max_length, value-num)

        return Max_length
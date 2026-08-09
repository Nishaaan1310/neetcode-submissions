class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map=set()
        n=len(nums)
        for num in nums:
            if num in num_map:
                return True
            else:
                num_map.add(num)
        return False
            
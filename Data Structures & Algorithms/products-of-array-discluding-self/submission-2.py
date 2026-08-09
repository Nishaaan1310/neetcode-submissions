class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        solution=[1]*n
        left=1
        for i in range (n):
                solution[i]=left
                left*=nums[i]
        right=1
        for i in range (n-1,-1,-1):
                solution[i] *= right
                right*=nums[i]
        return solution
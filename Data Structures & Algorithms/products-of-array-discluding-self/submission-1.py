class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_product=[1] * n
        right_product=[1] * n
        left=1
        for i in range (0,n):
                left_product[i]=left
                left*=nums[i]
        right=1
        for i in range (n-1,-1,-1):
                right_product[i]= right
                right*=nums[i]
        
        solution=[x*y for x,y in zip(left_product,right_product)]
        return solution







        
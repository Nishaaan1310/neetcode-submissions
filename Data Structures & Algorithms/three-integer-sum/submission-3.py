class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        sol=[]
        for i in range (n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                value=nums[i]+nums[left]+nums[right]
                if value==0:
                    sol.append([nums[i],nums[left],nums[right]])
                    right-=1
                    left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif value>0:
                    right-=1
                else:
                    left+=1
        return sol



        
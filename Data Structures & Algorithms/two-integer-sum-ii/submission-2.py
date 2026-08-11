class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        while left<right:
            value=numbers[left]+numbers[right]
            if value==target:
                return [left+1,right+1]
            elif value>target:
                right-=1
            elif value<target:
                left+=1
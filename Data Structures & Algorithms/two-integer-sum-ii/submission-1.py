class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        seen={}
        for i in range(n):
            diff=target-numbers[i]
            if diff in seen:
                return [seen[diff],i+1]
            else:
                seen[numbers[i]]=i+1